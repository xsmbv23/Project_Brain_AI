# CONSORTIUM AUTHORITY BOUNDARY V1

## Canonical decision

The Consortium is **not** a second Forensic system and is **not** a second FSM.

It is a governed execution/deliberation plane below Brain.

```text
                         BRAIN
                 SINGLE FORENSIC AUTHORITY
                         |
                 GOVERNED WORK DISPATCH
                         |
          +--------------+--------------+
          |              |              |
       WORKER A       WORKER B       WORKER C ...
          |              |              |
          +--------------+--------------+
                         |
                 STRUCTURED RECEIPTS
                         |
                         v
                       BRAIN
                    LOCAL GATE
                         |
                  STATE TRANSITION
```

## Five immutable boundaries

1. **ONE FORENSIC AUTHORITY** — Brain owns canonical forensic state.
2. **CONSORTIUM HAS NO PROMOTION AUTHORITY** — deliberation cannot open a forensic gate.
3. **CONSENSUS IS NOT EVIDENCE** — four agreeing workers do not make reality true.
4. **WORKER RESULT IS NOT FORENSIC PASS** — worker success is execution evidence only.
5. **CURRENT TOPOLOGY IS NOT IMMUTABLE DOCTRINE** — Bot count and worker arrangement may evolve without changing the authority doctrine.

Additional invariants:

- no PASS inheritance;
- local gate evidence is owned by the gate;
- a worker cannot approve its own unreviewed material claim;
- minority/challenge positions remain durable records;
- stale leases and stale allocation evidence cannot promote a current action;
- cross-repo execution never changes canonical truth directly.

## State vocabulary

Workers may have execution states such as:

`TASK_PENDING`, `TASK_RUNNING`, `RESULT_SUCCESS`, `RESULT_FAILURE`, `RESULT_UNKNOWN`, `RESULT_HOLD`, `RESULT_CONFLICT`, `RETRY`, `STALE`, `RETIRED`.

The following vocabulary is forbidden for worker/consortium state because it can be confused with forensic authority:

- `FORENSIC_PASS`
- `FORENSIC_PROMOTION`
- `CANONICAL_TRUTH`
- `GATE_OPEN`

Only the Brain admission layer may express those semantics.

## Topology is replaceable

A current deployment may contain Bot1/Bot2/Bot3/Bot4. That is an implementation topology, not immutable doctrine.

Doctrine is instead:

```text
ONE AUTHORITY
ONE FORENSIC FSM
SCOPED WORKERS
IMMUTABLE HANDOFFS
LOCAL EVIDENCE OWNERSHIP
NO PASS INHERITANCE
```

A future Bot5 or a removed Bot3 must not require a rewrite of the Forensic DNA merely because worker topology changed.

## Quant boundary

Consortium may ask Quant Engine to perform:

`QUESTION -> HYPOTHESIS -> TEST -> REPLAY -> BACKTEST -> ANALYSIS`

But:

```text
CONSORTIUM CONSENSUS
        !=
EDGE

QUANT RESULT
        !=
FORENSIC PASS
```

The Quant Engine produces deterministic calculation/research results. Admission into Reality or promotion remains governed by the relevant local evidence gate.

## Memory hierarchy

```text
CANONICAL_STATE
      |
EVIDENCE_HISTORY
      |
TASK_TRACE
      |
WORKER_MEMORY
      |
EPHEMERAL_CONTEXT
```

The following distinctions are mandatory:

```text
EPHEMERAL_CONTEXT != EVIDENCE
WORKER_MEMORY    != EVIDENCE
EVIDENCE         != STATE
STATE            != DOCTRINE
```

Worker memory can explain what a worker previously considered. It cannot prove what Reality is.

## Successor transmission

A successor bot must reconstruct authority from persistent artifacts, not conversation memory:

1. `state/current_state.json`
2. `state/next_action.json`
3. latest action record referenced by the current successor chain
4. relevant contract
5. relevant evidence/receipt references
6. reconciliation records when present

A chat statement such as “the consortium agreed” is never sufficient to promote a gate.

## Anti-proliferation rule

Do not create a new Consortium FSM, a worker forensic FSM, or a separate promotion state machine.

If orchestration needs state, use execution/task state and receipts. The only canonical forensic transitions remain inside the existing Brain admission chain.
