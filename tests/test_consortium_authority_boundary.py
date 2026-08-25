import json
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]


class ConsortiumAuthorityBoundaryTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.contract = json.loads((ROOT / "contracts/consortium_authority_boundary_v1.json").read_text())

    def test_single_forensic_authority(self):
        self.assertEqual(self.contract["authority_model"]["forensic_authority_count"], 1)
        self.assertEqual(self.contract["authority_model"]["authority_owner"], "BRAIN")

    def test_consortium_cannot_promote(self):
        self.assertFalse(self.contract["authority_model"]["consortium_promotion_authority"])
        self.assertFalse(self.contract["authority_model"]["consortium_forensic_state_authority"])

    def test_topology_is_not_doctrine(self):
        self.assertFalse(self.contract["topology_policy"]["worker_count_is_doctrine"])

    def test_forensic_vocabulary_is_not_worker_vocabulary(self):
        forbidden = set(self.contract["forbidden_worker_state_semantics"])
        self.assertIn("FORENSIC_PASS", forbidden)
        self.assertIn("FORENSIC_PROMOTION", forbidden)
        self.assertIn("CANONICAL_TRUTH", forbidden)
        self.assertIn("GATE_OPEN", forbidden)

    def test_memory_layers_do_not_collapse(self):
        self.assertFalse(self.contract["memory_policy"]["ephemeral_context_is_evidence"])
        self.assertFalse(self.contract["memory_policy"]["worker_memory_is_evidence"])
        self.assertFalse(self.contract["memory_policy"]["evidence_is_state"])
        self.assertFalse(self.contract["memory_policy"]["state_is_doctrine"])


if __name__ == "__main__":
    unittest.main()
