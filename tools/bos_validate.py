#!/usr/bin/env python3
"""Validate the active BOS-0001 atom graph.

This validator covers the implemented mechanical subset of V0/V1/V3. It does
not claim semantic truth, global completeness, adoption, or historical Git
membership beyond the active checkout.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Any, Iterable
from urllib.parse import unquote

import yaml
from jsonschema import Draft202012Validator, FormatChecker


SCHEMA_PATHS = {
    "bos.atom@v0.2": Path("schemas/bos-atom-v0.2.schema.json"),
    "bos.atom@v0.3": Path("schemas/bos-atom-v0.3.schema.json"),
}
ID_RE = re.compile(r"^bos:[a-z][a-z0-9_-]*(?::[a-z0-9][a-z0-9._-]*)+$")
ACTOR_RE = re.compile(r"^bos:actor:(human|model|service):[a-z0-9][a-z0-9._-]*$")
REVISION_LINE_RE = re.compile(
    rb'(?m)^revision: "sha256:([0-9a-f]{64})"$'
)
MARKDOWN_LINK_RE = re.compile(r"\[[^\]]*\]\(([^)]+)\)")


class UniqueKeyLoader(yaml.SafeLoader):
    """YAML loader that rejects duplicate mapping keys."""


def _construct_mapping(
    loader: UniqueKeyLoader, node: yaml.MappingNode, deep: bool = False
) -> dict[str, Any]:
    mapping: dict[str, Any] = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node, deep=deep)
        if key in mapping:
            raise ValueError(f"duplicate YAML key: {key!r}")
        mapping[key] = loader.construct_object(value_node, deep=deep)
    return mapping


UniqueKeyLoader.add_constructor(
    yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, _construct_mapping
)


@dataclass(frozen=True, order=True)
class Finding:
    path: str
    code: str
    message: str

    def render(self) -> str:
        return f"ERR {self.code} {self.path}: {self.message}"


@dataclass
class Record:
    path: Path
    raw: bytes
    frontmatter: dict[str, Any]
    body: str

    @property
    def ident(self) -> str:
        value = self.frontmatter.get("id")
        return value if isinstance(value, str) else "<invalid-id>"

    @property
    def kind(self) -> str:
        value = self.frontmatter.get("kind")
        return value if isinstance(value, str) else "<invalid-kind>"


def _frontmatter_bytes(raw: bytes) -> tuple[bytes, bytes]:
    if raw.startswith(b"\xef\xbb\xbf"):
        raise ValueError("UTF-8 BOM is forbidden")
    raw.decode("utf-8", errors="strict")
    if b"\r" in raw:
        raise ValueError("CR/CRLF is forbidden; atom files use LF")
    if not raw.endswith(b"\n") or raw.endswith(b"\n\n"):
        raise ValueError("file must end in exactly one LF")
    if not raw.startswith(b"---\n"):
        raise ValueError("frontmatter must begin at byte 0 with ---")
    marker = raw.find(b"\n---\n", 4)
    if marker < 0:
        raise ValueError("frontmatter closing marker is missing")
    return raw[4:marker], raw[marker + 5 :]


def load_record(path: Path) -> Record:
    raw = path.read_bytes()
    frontmatter_raw, body_raw = _frontmatter_bytes(raw)
    decoded = yaml.load(frontmatter_raw.decode("utf-8"), Loader=UniqueKeyLoader)
    if not isinstance(decoded, dict):
        raise ValueError("frontmatter must decode to an object")
    return Record(
        path=path,
        raw=raw,
        frontmatter=decoded,
        body=body_raw.decode("utf-8"),
    )


def compute_revision(raw: bytes) -> str:
    frontmatter_raw, _ = _frontmatter_bytes(raw)
    matches = list(REVISION_LINE_RE.finditer(frontmatter_raw))
    if len(matches) != 1:
        raise ValueError(
            "adopted revision requires exactly one frontmatter revision line"
        )
    match = matches[0]
    digest_start = 4 + match.start(1)
    digest_end = 4 + match.end(1)
    normalized = raw[:digest_start] + (b"0" * 64) + raw[digest_end:]
    return hashlib.sha256(normalized).hexdigest()


def active_atom_paths(root: Path) -> list[Path]:
    return sorted((root / "atoms").rglob("*.bos.md")) + sorted(
        (root / "spec").rglob("*.bos.md")
    )


def universe_descriptor(root: Path) -> tuple[list[dict[str, str]], str]:
    root = root.resolve()
    paths = set(active_atom_paths(root))
    paths.update(root / relative for relative in SCHEMA_PATHS.values())
    for path in active_atom_paths(root):
        try:
            record = load_record(path)
        except Exception:
            continue
        if record.kind != "evidence":
            continue
        locator = record.frontmatter.get("payload", {}).get("locator")
        if not isinstance(locator, str) or locator.startswith(("http://", "https://")):
            continue
        evidence_path = (root / locator).resolve()
        if evidence_path.is_file() and evidence_path.is_relative_to(root):
            paths.add(evidence_path)
    entries = [
        {
            "path": str(path.relative_to(root)),
            "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
        }
        for path in sorted(paths)
    ]
    encoded = json.dumps(
        entries, ensure_ascii=True, separators=(",", ":"), sort_keys=True
    ).encode()
    return entries, hashlib.sha256(encoded).hexdigest()


def _timestamp(value: Any) -> datetime | None:
    if not isinstance(value, str):
        return None
    try:
        return datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        return None


def _add(
    findings: list[Finding], root: Path, path: Path, code: str, message: str
) -> None:
    try:
        shown = str(path.relative_to(root))
    except ValueError:
        shown = str(path)
    findings.append(Finding(shown, code, message))


def _refs(record: Record) -> Iterable[tuple[str, str]]:
    data = record.frontmatter
    for index, actor in enumerate(data.get("created_by", [])):
        yield f"created_by[{index}]", actor
    for axis, target in data.get("states", {}).items():
        yield f"states.{axis}", target
    for index, relation in enumerate(data.get("relations", [])):
        if not isinstance(relation, dict):
            continue
        yield f"relations[{index}].object", relation.get("object")
        if relation.get("context") is not None:
            yield f"relations[{index}].context", relation.get("context")

    payload = data.get("payload", {})
    if not isinstance(payload, dict):
        return

    list_fields_by_kind = {
        "claim": ("evidence",),
        "hypothesis": ("evidence",),
        "risk": ("evidence",),
        "proposal": ("reasons",),
        "decision": ("reasons",),
        "outcome": ("evidence",),
        "context_cut": ("sources",),
        "trajectory": ("supplied_set", "produced"),
        "relation_claim": ("evidence",),
        "vehicle": ("includes",),
        "status": ("transitions_to",),
    }
    scalar_fields_by_kind = {
        "decision": ("authority", "context_cut"),
        "adoption": ("subject", "authority", "context_cut"),
        "action": ("target", "authority"),
        "trajectory": (
            "actor",
            "context_cut",
            "output_evidence",
            "selected_action",
            "receipt",
        ),
        "relation_claim": ("subject", "object", "observed_in"),
        "countervector": ("target",),
    }
    for field in list_fields_by_kind.get(record.kind, ()):
        for index, target in enumerate(payload.get(field, [])):
            yield f"payload.{field}[{index}]", target
    for field in scalar_fields_by_kind.get(record.kind, ()):
        target = payload.get(field)
        if target is not None:
            yield f"payload.{field}", target
    if record.kind == "context_cut":
        for index, repo in enumerate(payload.get("repositories", [])):
            if isinstance(repo, dict):
                yield f"payload.repositories[{index}].asset", repo.get("asset")


STRUCTURAL_DOMAINS: dict[str, set[str]] = {
    "contains": {"asset"},
    "depends_on": {"asset", "proposal", "action", "vehicle"},
    "supersedes": {
        "actor",
        "asset",
        "claim",
        "hypothesis",
        "risk",
        "requirement",
        "evidence",
        "proposal",
        "decision",
        "adoption",
        "action",
        "outcome",
        "context_cut",
        "trajectory",
        "relation_claim",
        "countervector",
        "principle",
        "goal",
        "vehicle",
        "status",
    },
    "derived_from": {
        "actor",
        "asset",
        "claim",
        "hypothesis",
        "risk",
        "requirement",
        "evidence",
        "proposal",
        "decision",
        "adoption",
        "action",
        "outcome",
        "context_cut",
        "trajectory",
        "relation_claim",
        "countervector",
        "principle",
        "goal",
        "vehicle",
        "status",
    },
    "targets": {"proposal", "action", "countervector"},
    "produces": {"trajectory", "action"},
    "observes": {"evidence", "context_cut", "trajectory"},
    "changes": {"action", "outcome"},
    "implements": {"asset", "action"},
    "governed_by": {"asset", "decision", "adoption", "action"},
    "binds": {"adoption", "decision", "action", "evidence"},
}


SEMANTIC_DOMAIN_RANGE: dict[str, tuple[set[str], set[str]]] = {
    "supports": (
        {"evidence", "claim", "hypothesis", "relation_claim"},
        {"claim", "hypothesis", "risk", "requirement", "relation_claim"},
    ),
    "refutes": (
        {"evidence", "claim", "hypothesis", "relation_claim"},
        {"claim", "hypothesis", "risk", "requirement", "relation_claim"},
    ),
    "mitigates": (
        {"requirement", "proposal", "decision", "action", "asset"},
        {"risk"},
    ),
    "motivates": (
        {"claim", "hypothesis", "risk", "principle", "evidence"},
        {"requirement", "proposal", "decision", "action", "goal"},
    ),
    "enables": (
        {"asset", "requirement", "decision", "adoption"},
        {"asset", "action", "goal"},
    ),
    "conflicts_with": (
        {"claim", "hypothesis", "risk", "requirement", "proposal", "decision"},
        {"claim", "hypothesis", "risk", "requirement", "proposal", "decision"},
    ),
    "addresses": (
        {"asset", "proposal", "decision", "action"},
        {"risk", "requirement", "goal"},
    ),
    "predicts": (
        {"claim", "hypothesis", "relation_claim"},
        {"outcome"},
    ),
    "constrains": (
        {"principle", "requirement", "decision"},
        {"proposal", "decision", "action", "goal"},
    ),
    "equivalent_to": (
        {
            "claim",
            "hypothesis",
            "risk",
            "requirement",
            "proposal",
            "decision",
            "asset",
        },
        {
            "claim",
            "hypothesis",
            "risk",
            "requirement",
            "proposal",
            "decision",
            "asset",
        },
    ),
}


def validate_space(root: Path) -> list[Finding]:
    root = root.resolve()
    findings: list[Finding] = []
    schema_validators: dict[str, Draft202012Validator] = {}
    for tag, relative in SCHEMA_PATHS.items():
        schema_path = root / relative
        try:
            schema = json.loads(schema_path.read_text(encoding="utf-8"))
            schema_validators[tag] = Draft202012Validator(
                schema, format_checker=FormatChecker()
            )
        except Exception as exc:
            _add(findings, root, schema_path, "SCHEMA", str(exc))
    if findings:
        return sorted(findings)

    records: dict[str, Record] = {}
    for path in active_atom_paths(root):
        try:
            record = load_record(path)
        except Exception as exc:
            _add(findings, root, path, "BYTES", str(exc))
            continue
        tag = record.frontmatter.get("schema")
        schema_validator = schema_validators.get(tag)
        if schema_validator is None:
            _add(findings, root, path, "SCHEMA_TAG", "unsupported schema tag")
        else:
            for error in schema_validator.iter_errors(record.frontmatter):
                location = (
                    ".".join(str(part) for part in error.absolute_path) or "<root>"
                )
                _add(
                    findings, root, path, "SCHEMA", f"{location}: {error.message}"
                )
        if record.ident in records:
            _add(
                findings,
                root,
                path,
                "DUPLICATE_ID",
                f"{record.ident} also appears in {records[record.ident].path}",
            )
        else:
            records[record.ident] = record
        declared_revision = record.frontmatter.get("revision")
        if declared_revision is not None:
            try:
                computed = compute_revision(record.raw)
                if declared_revision != f"sha256:{computed}":
                    _add(
                        findings,
                        root,
                        path,
                        "REVISION",
                        f"declared {declared_revision}, computed sha256:{computed}",
                    )
            except Exception as exc:
                _add(findings, root, path, "REVISION", str(exc))

    for record in records.values():
        for location, target in _refs(record):
            if not isinstance(target, str) or not ID_RE.fullmatch(target):
                _add(
                    findings,
                    root,
                    record.path,
                    "REF_SHAPE",
                    f"{location} is not a BOS ID: {target!r}",
                )
                continue
            if target not in records:
                _add(
                    findings,
                    root,
                    record.path,
                    "UNRESOLVED",
                    f"{location} -> {target}",
                )

        for actor in record.frontmatter.get("created_by", []):
            target = records.get(actor)
            if not ACTOR_RE.fullmatch(actor) or (
                target is not None and target.kind != "actor"
            ):
                _add(
                    findings,
                    root,
                    record.path,
                    "ACTOR",
                    f"created_by target is not an actor: {actor}",
                )

        for axis, target_id in record.frontmatter.get("states", {}).items():
            target = records.get(target_id)
            if target is None:
                continue
            target_axis = target.frontmatter.get("payload", {}).get("axis")
            if target.kind != "status" or target_axis != axis:
                _add(
                    findings,
                    root,
                    record.path,
                    "STATUS_AXIS",
                    f"{axis} points to {target_id} with axis {target_axis!r}",
                )

        for relation in record.frontmatter.get("relations", []):
            if not isinstance(relation, dict):
                continue
            predicate = relation.get("predicate")
            allowed = STRUCTURAL_DOMAINS.get(predicate)
            if allowed is not None and record.kind not in allowed:
                _add(
                    findings,
                    root,
                    record.path,
                    "RELATION_DOMAIN",
                    f"{predicate} is not structural for kind {record.kind}",
                )
            if record.kind == "vehicle" and predicate == "contains":
                _add(
                    findings,
                    root,
                    record.path,
                    "VEHICLE_MEMBERSHIP",
                    "vehicle membership lives only in payload.includes",
                )
            if predicate == "supersedes":
                target = records.get(relation.get("object"))
                if target is not None and target.kind != record.kind:
                    _add(
                        findings,
                        root,
                        record.path,
                        "SUPERSEDES_KIND",
                        f"{record.kind} supersedes {target.kind}",
                    )

        if record.kind == "relation_claim":
            payload = record.frontmatter["payload"]
            predicate = payload["predicate"]
            pair = SEMANTIC_DOMAIN_RANGE.get(predicate)
            subject = records.get(payload["subject"])
            obj = records.get(payload["object"])
            if pair is not None and subject is not None and subject.kind not in pair[0]:
                _add(
                    findings,
                    root,
                    record.path,
                    "SEMANTIC_DOMAIN",
                    f"{predicate} subject kind {subject.kind} is invalid",
                )
            if pair is not None and obj is not None and obj.kind not in pair[1]:
                _add(
                    findings,
                    root,
                    record.path,
                    "SEMANTIC_RANGE",
                    f"{predicate} object kind {obj.kind} is invalid",
                )

        if record.kind == "context_cut":
            for repo in record.frontmatter["payload"]["repositories"]:
                target = records.get(repo["asset"])
                if target is not None and (
                    target.kind != "asset"
                    or target.frontmatter["payload"]["asset_kind"] != "repository"
                ):
                    _add(
                        findings,
                        root,
                        record.path,
                        "CUT_ASSET",
                        f"{repo['asset']} is not a repository asset",
                    )

        if record.kind == "trajectory":
            actor_id = record.frontmatter["payload"]["actor"]
            actor = records.get(actor_id)
            if actor is not None and actor.kind != "actor":
                _add(
                    findings,
                    root,
                    record.path,
                    "TRAJECTORY_ACTOR",
                    f"{actor_id} is not an actor",
                )

        if record.kind == "adoption":
            payload = record.frontmatter["payload"]
            authority = records.get(payload["authority"])
            subject = records.get(payload["subject"])
            context = records.get(payload["context_cut"])
            if payload["mode"] == "genesis-human" and (
                authority is None
                or authority.kind != "actor"
                or authority.frontmatter["payload"]["actor_class"] != "human"
            ):
                _add(
                    findings,
                    root,
                    record.path,
                    "GENESIS_AUTHORITY",
                    "genesis-human adoption requires a human actor",
                )
            if subject is not None and subject.frontmatter.get("revision") != payload[
                "subject_revision"
            ]:
                _add(
                    findings,
                    root,
                    record.path,
                    "ADOPTION_REVISION",
                    "subject_revision does not match the subject atom",
                )
            if context is not None and context.kind != "context_cut":
                _add(
                    findings,
                    root,
                    record.path,
                    "ADOPTION_CONTEXT",
                    "adoption context_cut does not resolve to a context cut",
                )

        if record.kind == "decision":
            authority = records.get(record.frontmatter["payload"]["authority"])
            context = records.get(record.frontmatter["payload"]["context_cut"])
            if authority is not None and authority.kind not in {
                "actor",
                "adoption",
                "evidence",
            }:
                _add(
                    findings,
                    root,
                    record.path,
                    "DECISION_AUTHORITY",
                    f"decision authority has kind {authority.kind}",
                )
            if context is not None and context.kind != "context_cut":
                _add(
                    findings,
                    root,
                    record.path,
                    "DECISION_CONTEXT",
                    "decision context_cut does not resolve to a context cut",
                )
            decision_created = _timestamp(record.frontmatter.get("created_at"))
            for reason_id in record.frontmatter["payload"]["reasons"]:
                reason = records.get(reason_id)
                if reason is None:
                    continue
                valid_until = reason.frontmatter.get("payload", {}).get("valid_until")
                if valid_until is None:
                    continue
                expires = _timestamp(valid_until)
                if (
                    decision_created is not None
                    and expires is not None
                    and decision_created > expires
                ):
                    _add(
                        findings,
                        root,
                        record.path,
                        "EXPIRED_REASON",
                        f"decision cites {reason_id} after {valid_until}",
                    )

        if record.kind == "action":
            authority = records.get(record.frontmatter["payload"]["authority"])
            if authority is not None and authority.kind not in {
                "decision",
                "adoption",
            }:
                _add(
                    findings,
                    root,
                    record.path,
                    "ACTION_AUTHORITY",
                    f"action authority has kind {authority.kind}",
                )

        if record.kind == "evidence":
            payload = record.frontmatter["payload"]
            locator = payload["locator"]
            digest = payload.get("digest")
            local = root / locator
            if digest is not None and not locator.startswith(("http://", "https://")):
                if not local.is_file():
                    _add(
                        findings,
                        root,
                        record.path,
                        "EVIDENCE_LOCATOR",
                        f"local evidence is missing: {locator}",
                    )
                else:
                    actual = hashlib.sha256(local.read_bytes()).hexdigest()
                    if digest != f"sha256:{actual}":
                        _add(
                            findings,
                            root,
                            record.path,
                            "EVIDENCE_DIGEST",
                            f"{locator} digest mismatch",
                        )

        for match in MARKDOWN_LINK_RE.finditer(record.body):
            link = match.group(1)
            if link.startswith(("http://", "https://", "#")):
                continue
            target = (record.path.parent / unquote(link.split("#", 1)[0])).resolve()
            if not target.exists():
                _add(
                    findings,
                    root,
                    record.path,
                    "BODY_LINK",
                    f"broken local link: {link}",
                )

    superseders: dict[str, list[Record]] = {}
    for record in records.values():
        for relation in record.frontmatter.get("relations", []):
            if isinstance(relation, dict) and relation.get("predicate") == "supersedes":
                target = relation.get("object")
                if isinstance(target, str):
                    superseders.setdefault(target, []).append(record)
    for target, successors in superseders.items():
        if len(successors) > 1:
            names = ", ".join(sorted(record.ident for record in successors))
            for record in successors:
                _add(
                    findings,
                    root,
                    record.path,
                    "SUPERSESSION_CONFLICT",
                    f"{target} has competing successors: {names}",
                )

    if "bos:vehicle:bos-0001" not in records:
        _add(
            findings,
            root,
            root / "spec/BOS-0001-core.bos.md",
            "MANIFEST",
            "bos:vehicle:bos-0001 is missing",
        )

    return sorted(findings)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path.cwd())
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args(argv)
    findings = validate_space(args.root)
    if args.json:
        universe, universe_sha256 = universe_descriptor(args.root)
        print(
            json.dumps(
                {
                    "report": "bos.validate@v0",
                    "verdict_scope": "active-checkout-diagnostic",
                    "cut": None,
                    "universe": universe,
                    "universe_sha256": universe_sha256,
                    "ok": not findings,
                    "errors": len(findings),
                    "findings": [
                        {
                            "path": item.path,
                            "code": item.code,
                            "message": item.message,
                        }
                        for item in findings
                    ],
                },
                ensure_ascii=True,
                separators=(",", ":"),
                sort_keys=True,
            )
        )
    else:
        for finding in findings:
            print(finding.render())
        if not findings:
            print("BOS-VALIDATE: ALL PASS")
    return 1 if findings else 0


if __name__ == "__main__":
    raise SystemExit(main())
