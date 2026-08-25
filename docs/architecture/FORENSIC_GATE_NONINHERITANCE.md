# Forensic Gate Non-Inheritance

## Canonical rule

There is **ONE FORENSIC FSM**. Database admission gates are not separate forensic systems. They are sequential gates inside the same forensic admission chain.

```text
DB_EXISTENCE
    -> DB_BINDING
    -> SECRET_RESOLUTION
    -> DB_TLS_ADMISSION
    -> NETWORK_ORIGIN_PROOF
    -> DB_ROUND_TRIP
    -> PROMOTION
```

## Meaning of each gate

- `DB_EXISTENCE`: proves the target database resource exists and is available.
- `DB_BINDING`: proves the service has the required binding reference (`DATABASE_URL`) without exposing the credential.
- `SECRET_RESOLUTION`: proves the binding resolves through the approved secret-management boundary.
- `DB_TLS_ADMISSION`: proves the connection policy is PostgreSQL + an admitted TLS mode.
- `NETWORK_ORIGIN_PROOF`: proves the actual connection originates from the authorized runtime boundary.
- `DB_ROUND_TRIP`: proves a compact non-source-data envelope can be written, read back, and SHA-256 verified.
- `PROMOTION`: authorizes the durable evidence sink only after all upstream predicates have fresh admissible evidence.

## Non-inheritance

A PASS is always local to its own gate.

```text
DB_EXISTS = PASS
    != DB_BINDING = PASS

DB_BINDING = PASS
    != TLS = PASS

TLS = PASS
    != NETWORK_ORIGIN = PASS

NETWORK_ORIGIN = PASS
    != ROUND_TRIP = PASS

ROUND_TRIP = PASS
    -> eligible for PROMOTION
```

No gate may synthesize, infer, or inherit another gate's PASS.

## Why this is mandatory

A database can exist while the service has no credential binding. A binding can exist while TLS is inadmissible. TLS can be valid while the connection does not originate from the authorized runtime. A valid connection can exist while durable write/read integrity remains unproven.

Therefore the following equivalence is forbidden:

```text
RESOURCE EXISTS == SERVICE AUTHORIZED == ROUND-TRIP PROVEN
```

They are distinct predicates with distinct evidence.

## Evidence discipline

Every gate owns:

1. its evidence;
2. its timestamp/freshness;
3. its allocation/runtime identity when applicable;
4. its reason-coded DENY/HOLD state;
5. its promotion decision.

Historical evidence is immutable history only. It cannot be silently reused as fresh promotion evidence.

## Security analogy

The house analogy is literal in architecture:

```text
corridor key
    +
room key
    +
inner latch / host approval for protected rooms
    +
room-specific evidence
```

Having the corridor key never grants the room key. Having the room key never grants an inner-latched protected room. Passing one gate never grants the next gate.

## Successor Bot instruction

If a successor sees a PASS for any gate, it must ask:

> "PASS của gate nào, evidence nào, allocation/runtime nào, timestamp nào, và gate kế tiếp đã tự chứng minh chưa?"

Never answer that question by inheritance or inference.

## Current project consequence

S1 remains the only admitted data-admission room. S2-S7 remain locked until S1's own evidence is complete. Current N175 remains HOLD because its previously recorded triple-worker receipt is bound to a stale allocation and cannot be inherited by the current allocation.
