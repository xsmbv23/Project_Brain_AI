# CONSORTIUM AUTHORITY BOUNDARY AMENDMENT

## Purpose

Close an architectural ambiguity discovered during forensic review of the multi-worker model.

The Consortium is an execution/deliberation plane below Brain. It is not a second Forensic FSM and does not own canonical forensic state.

## Canonical invariants added

1. ONE_FORENSIC_AUTHORITY — Brain is the sole owner of canonical forensic state.
2. CONSORTIUM_HAS_NO_PROMOTION_AUTHORITY — deliberation cannot open a forensic gate.
3. CONSENSUS_IS_NOT_EVIDENCE — worker agreement cannot prove Reality.
4. WORKER_RESULT_IS_NOT_FORENSIC_PASS — execution success remains local worker evidence.
5. CURRENT_TOPOLOGY_IS_NOT_IMMUTABLE_DOCTRINE — Bot count and worker topology are implementation details.

Additional boundaries:

- no second Consortium FSM;
- no worker promotion state machine;
- no PASS inheritance;
- each forensic gate owns its own evidence;
- stale worker allocation/lease evidence cannot promote current state;
- worker memory is not evidence;
- evidence is not canonical state;
- state is not doctrine;
- Quant Engine results become admissible only through their own local evidence gate.

## Memory hierarchy

```text
CANONICAL_STATE
      ↓
EVIDENCE_HISTORY
      ↓
TASK_TRACE
      ↓
WORKER_MEMORY
      ↓
EPHEMERAL_CONTEXT
```

These layers are intentionally non-interchangeable.

## Architectural consequence

Do not create a separate `Forensic_Bot_Consortium` FSM merely because worker coordination grows. If a future Consortium repository is created, it must contain execution/deliberation contracts only and explicitly reference the Brain authority contract. It must not become a competing canonical state authority.

## Current E2E impact

This amendment does not promote S1 and does not alter the current foundation gate outcome. Existing state remains governed by the canonical S1 reconciliation action and its evidence requirements.

Current promotion remains:

```text
DENY
```

Layer 1 remains locked.
