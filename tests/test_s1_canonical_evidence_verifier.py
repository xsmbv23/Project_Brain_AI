import unittest
from datetime import date

from tools.s1_canonical_evidence_verifier import verify


class S1VerifierTests(unittest.TestCase):
    def _records(self):
        return [
            {
                "business_date": d.isoformat(),
                "http_status": 200,
                "raw_bytes_sha256": f"{i + 1:064x}",
                "source_id": "ketqua16.net",
                "status": "PARTIAL",
            }
            for i, d in enumerate([date(2026, 8, 17), date(2026, 8, 18), date(2026, 8, 19)])
        ]

    def test_partial_short_window_holds(self):
        report = verify(self._records(), window_days=10)
        self.assertEqual(report["status"], "HOLD")
        self.assertEqual(report["promotion"], "DENY")
        self.assertFalse(report["predicates"]["consecutive_real_date_coverage"])
        self.assertFalse(report["predicates"]["coverage_ratio_1_0"])
        self.assertFalse(report["predicates"]["fresh_real_admission_receipt"])
        self.assertFalse(report["predicates"]["frozen_canonical_sha256"])

    def test_unknown_source_is_not_pass(self):
        rows = self._records()
        rows[0]["source_id"] = "unknown.invalid"
        report = verify(rows, window_days=3)
        self.assertEqual(report["status"], "HOLD")
        self.assertFalse(report["predicates"]["source_provenance"])
        self.assertEqual(report["promotion"], "DENY")


if __name__ == "__main__":
    unittest.main()
