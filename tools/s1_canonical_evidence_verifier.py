"""Machine-checkable S1 evidence verifier.

This verifier consumes only compact acquisition metadata from Quant_Engine.
It never loads raw lottery payloads into Brain, never fabricates missing dates,
and never promotes data. Every predicate has its own evidence and PASS does
not inherit across gates.
"""
from __future__ import annotations

import hashlib
import json
from datetime import date, timedelta
from pathlib import PurePosixPath
from urllib.request import Request, urlopen

SOURCE = "xsmbv23/Quant_Engine"
STATUS_URL = "https://raw.githubusercontent.com/xsmbv23/Quant_Engine/main/data_buffer/acquisition_status.jsonl"
WINDOW_DAYS = 10


def _get(url: str) -> bytes:
    req = Request(url, headers={"User-Agent": "Project-Brain-AI-S1-Verifier/1.0"})
    with urlopen(req, timeout=20) as response:
        return response.read()


def load_records(raw: bytes) -> list[dict]:
    records: list[dict] = []
    for line in raw.decode("utf-8").splitlines():
        if not line.strip():
            continue
        value = json.loads(line)
        if not isinstance(value, dict):
            raise ValueError("non-object acquisition record")
        records.append(value)
    return records


def _contiguous_run(days: list[date]) -> int:
    ordered = sorted(set(days))
    if not ordered:
        return 0
    best = current = 1
    for a, b in zip(ordered, ordered[1:]):
        if b == a + timedelta(days=1):
            current += 1
            best = max(best, current)
        else:
            current = 1
    return best


def verify(records: list[dict], *, window_days: int = WINDOW_DAYS) -> dict:
    dates = []
    conflicts = 0
    raw_hash_missing = 0
    source_ok = True
    http_ok = True
    partial_count = 0

    seen_by_date: dict[str, set[str]] = {}
    for r in records:
        d = str(r.get("business_date", ""))
        try:
            dates.append(date.fromisoformat(d))
        except ValueError:
            conflicts += 1
        if r.get("source_id") != "ketqua16.net":
            source_ok = False
        if r.get("http_status") != 200:
            http_ok = False
        digest = str(r.get("raw_bytes_sha256", ""))
        if len(digest) != 64:
            raw_hash_missing += 1
        if r.get("status") == "PARTIAL":
            partial_count += 1
        seen_by_date.setdefault(d, set()).add(digest)

    # Multiple raw captures for one business date are not automatically a
    # conflict: the raw hashes must simply remain distinguishable and immutable.
    duplicate_date_captures = {d: len(hashes) for d, hashes in seen_by_date.items() if len(hashes) > 1}
    unique_days = sorted(set(dates))
    observed_days = len(unique_days)
    coverage_ratio = min(1.0, observed_days / window_days)
    contiguous_days = _contiguous_run(unique_days)

    predicates = {
        "source_provenance": source_ok,
        "http_200": http_ok,
        "raw_hash_present": raw_hash_missing == 0 and bool(records),
        "consecutive_real_date_coverage": contiguous_days >= window_days,
        "coverage_ratio_1_0": coverage_ratio == 1.0,
        "zero_unresolved_conflicts": conflicts == 0,
        "fresh_real_admission_receipt": False,
        "frozen_canonical_sha256": False,
        "canonical_dataset_admitted": False,
    }

    status = "PASS" if all(predicates.values()) else "HOLD"
    return {
        "schema": "brain-s1-canonical-evidence-verifier/v1",
        "source": SOURCE,
        "source_id": "ketqua16.net",
        "window_days": window_days,
        "records": len(records),
        "observed_days": observed_days,
        "dates": [d.isoformat() for d in unique_days],
        "contiguous_days": contiguous_days,
        "coverage_ratio": coverage_ratio,
        "partial_records": partial_count,
        "duplicate_date_captures": duplicate_date_captures,
        "predicates": predicates,
        "status": status,
        "promotion": "DENY",
        "raw_status_sha256": hashlib.sha256(json.dumps(records, sort_keys=True).encode()).hexdigest(),
        "forensic_rule": "PASS_IS_LOCAL;NO_PASS_INHERITANCE;UNKNOWN_IS_NOT_PASS",
    }


def main() -> int:
    raw = _get(STATUS_URL)
    report = verify(load_records(raw))
    print(json.dumps(report, ensure_ascii=False, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
