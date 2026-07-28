from __future__ import annotations

import shutil
import tempfile
import unittest
from pathlib import Path

from tools.bos_validate import compute_revision, universe_descriptor, validate_space


ROOT = Path(__file__).resolve().parents[1]


class BOSValidatorCountervectors(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        for name in ("atoms", "spec", "schemas", "reviews", "raw"):
            source = ROOT / name
            if source.exists():
                shutil.copytree(source, self.root / name)

    def tearDown(self) -> None:
        self.temp.cleanup()

    def codes(self) -> set[str]:
        return {finding.code for finding in validate_space(self.root)}

    def mutate(self, relative: str, old: str, new: str) -> None:
        path = self.root / relative
        text = path.read_text()
        self.assertIn(old, text)
        path.write_text(text.replace(old, new, 1))

    def test_clean_graph_passes(self) -> None:
        self.assertEqual(validate_space(self.root), [])

    def test_unknown_field_fails_schema(self) -> None:
        self.mutate(
            "atoms/risk/meta-recursion.bos.md",
            "relations: []\n",
            "unknown_power: true\nrelations: []\n",
        )
        self.assertIn("SCHEMA", self.codes())

    def test_duplicate_id_fails(self) -> None:
        source = self.root / "atoms/risk/meta-recursion.bos.md"
        shutil.copy2(source, source.with_name("duplicate.bos.md"))
        self.assertIn("DUPLICATE_ID", self.codes())

    def test_unresolved_reference_fails(self) -> None:
        self.mutate(
            "atoms/proposal/v0-bounded-scope.bos.md",
            "bos:risk:meta-recursion",
            "bos:risk:missing",
        )
        self.assertIn("UNRESOLVED", self.codes())

    def test_wrong_status_axis_fails(self) -> None:
        self.mutate(
            "atoms/risk/meta-recursion.bos.md",
            "maturity: bos:status:maturity:research",
            "maturity: bos:status:governance:proposed",
        )
        self.assertIn("STATUS_AXIS", self.codes())

    def test_embedded_semantic_predicate_fails(self) -> None:
        self.mutate(
            "atoms/claim/experience-is-trajectory.bos.md",
            "relations: []",
            "relations:\n  - predicate: motivates\n    object: bos:requirement:model-trajectory",
        )
        self.assertIn("SCHEMA", self.codes())

    def test_dirty_cut_fails(self) -> None:
        self.mutate(
            "atoms/context-cut/bos-0001-rev1.bos.md",
            "dirty: false",
            "dirty: true",
        )
        self.assertIn("SCHEMA", self.codes())

    def test_embedded_secret_fails(self) -> None:
        self.mutate(
            "atoms/risk/meta-recursion.bos.md",
            "classification: public",
            "classification: secret",
        )
        self.assertIn("SCHEMA", self.codes())

    def test_read_set_alias_fails(self) -> None:
        self.mutate(
            "atoms/trajectory/kimi-bos-0001-rev1-review.bos.md",
            "supplied_set:",
            "read_set:",
        )
        self.assertIn("SCHEMA", self.codes())

    def test_vehicle_duplicate_membership_fails(self) -> None:
        self.mutate(
            "spec/BOS-0001-core.bos.md",
            "relations:\n  - predicate: derived_from",
            "relations:\n  - predicate: contains\n    object: bos:risk:meta-recursion\n  - predicate: derived_from",
        )
        self.assertIn("RELATION_DOMAIN", self.codes())

    def test_evidence_digest_mismatch_fails(self) -> None:
        path = self.root / "reviews/2026-07-kimi-bos-0001-rev1.md"
        path.write_text(path.read_text() + "tampered\n")
        self.assertIn("EVIDENCE_DIGEST", self.codes())

    def test_invalid_revision_fails(self) -> None:
        self.mutate(
            "atoms/risk/meta-recursion.bos.md",
            "relations: []\n",
            'revision: "sha256:' + ("0" * 64) + '"\nrelations: []\n',
        )
        self.assertIn("REVISION", self.codes())

    def test_exact_revision_passes(self) -> None:
        path = self.root / "atoms/risk/meta-recursion.bos.md"
        text = path.read_text()
        text = text.replace(
            "relations: []\n",
            'revision: "sha256:' + ("0" * 64) + '"\nrelations: []\n',
            1,
        )
        digest = compute_revision(text.encode())
        path.write_text(text.replace("0" * 64, digest, 1))
        self.assertNotIn("REVISION", self.codes())

    def test_body_revision_lookalike_is_ignored(self) -> None:
        path = self.root / "atoms/risk/meta-recursion.bos.md"
        text = path.read_text()
        text = text.replace(
            "relations: []\n",
            'revision: "sha256:' + ("0" * 64) + '"\nrelations: []\n',
            1,
        )
        text = text.rstrip("\n") + '\n\n```yaml\nrevision: "sha256:' + ("f" * 64) + '"\n```\n'
        digest = compute_revision(text.encode())
        path.write_text(text.replace("0" * 64, digest, 1))
        self.assertNotIn("REVISION", self.codes())

    def test_crlf_atom_fails(self) -> None:
        path = self.root / "atoms/risk/meta-recursion.bos.md"
        path.write_bytes(path.read_bytes().replace(b"\n", b"\r\n"))
        self.assertIn("BYTES", self.codes())

    def test_competing_superseders_fail(self) -> None:
        for relative in (
            "atoms/risk/meta-recursion.bos.md",
            "atoms/risk/ontology-explosion.bos.md",
        ):
            self.mutate(
                relative,
                "relations: []",
                "relations:\n"
                "  - predicate: supersedes\n"
                "    object: bos:risk:false-replay",
            )
        self.assertIn("SUPERSESSION_CONFLICT", self.codes())

    def test_expired_reason_cannot_support_decision(self) -> None:
        self.mutate(
            "atoms/hypothesis/agent-decision-evidence-commercial-wedge.bos.md",
            'valid_until: "2026-10-28T00:00:00Z"',
            'valid_until: "2026-07-27T00:00:00Z"',
        )
        path = self.root / "atoms/decision/expired-reason.bos.md"
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(
            """---
id: bos:decision:expired-reason
schema: bos.atom@v0.2
kind: decision
states:
  governance: bos:status:governance:proposed
  maturity: bos:status:maturity:research
title: Expired reason decision fixture
created_at: "2026-07-28T00:00:00Z"
created_by:
  - bos:actor:human:s0fractal
scope: [bos]
disclosure:
  classification: public
  payload_mode: embedded
  retention: review
relations: []
payload:
  question: "May an expired claim authorize a current decision?"
  choice: "No"
  reasons:
    - bos:hypothesis:agent-decision-evidence-commercial-wedge
  authority: bos:actor:human:s0fractal
  context_cut: bos:context_cut:bos-0001-rev1
---

# Expired reason fixture
"""
        )
        self.assertIn("EXPIRED_REASON", self.codes())

    def test_commitment_mode_requires_named_private_nonce_scheme(self) -> None:
        self.mutate(
            "atoms/status/lifecycle-recorded.bos.md",
            """disclosure:
  classification: public
  payload_mode: embedded
  retention: indefinite
""",
            """disclosure:
  classification: secret
  payload_mode: commitment
  retention: indefinite
  commitment: "sha256:aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
  private_locator: "private://meta-recursion"
  encryption: "age"
""",
        )
        self.assertIn("SCHEMA", self.codes())
        self.mutate(
            "atoms/status/lifecycle-recorded.bos.md",
            '  commitment: "sha256:',
            "  commitment_scheme: sha256-private-nonce-payload-v1\n"
            '  commitment: "sha256:',
        )
        self.assertNotIn("SCHEMA", self.codes())

    def test_universe_digest_changes_with_input_bytes(self) -> None:
        before_entries, before_digest = universe_descriptor(self.root)
        path = self.root / "atoms/risk/meta-recursion.bos.md"
        path.write_text(path.read_text().replace("Meta-recursion", "Meta recursion", 1))
        after_entries, after_digest = universe_descriptor(self.root)
        self.assertEqual(len(before_entries), len(after_entries))
        self.assertNotEqual(before_digest, after_digest)

    def test_duplicate_yaml_key_fails(self) -> None:
        self.mutate(
            "atoms/risk/meta-recursion.bos.md",
            "scope: [bos, process]\n",
            "scope: [bos, process]\nscope: [bos]\n",
        )
        self.assertIn("BYTES", self.codes())

if __name__ == "__main__":
    unittest.main()
