from __future__ import annotations

import shutil
import tempfile
import unittest
from pathlib import Path

from tools.bos_validate import compute_revision, validate_space


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

    def test_duplicate_yaml_key_fails(self) -> None:
        self.mutate(
            "atoms/risk/meta-recursion.bos.md",
            "scope: [bos, process]\n",
            "scope: [bos, process]\nscope: [bos]\n",
        )
        self.assertIn("BYTES", self.codes())

if __name__ == "__main__":
    unittest.main()
