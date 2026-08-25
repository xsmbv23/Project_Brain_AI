# FOUR-BOT CONSORTIUM V1

## Purpose

Define the architecture boundary for a possible separate project that coordinates four AI bots around the existing XSMB Forensic Quant system.

This document is intentionally a DESIGN CONTRACT, not a permission to open any locked layer.

## 1. Existing authority is preserved

The existing system already establishes:

- Brain = Governance / Control Plane
- Quant Engine = Calculation / Replay / Feature / EV
- XSMB sources = Reality Observation
- ChatGPT = communication / analysis / code only

The four-bot consortium must NOT replace Brain authority and must NOT create a second forensic FSM.

## 2. Evidence from current repository

The repository currently contains explicit Bot-1, Bot-2 and Bot-3 work:

- Bot-1 work includes Brain governance/state and worker orchestration.
- Bot-2 work is associated with Quant-side admission/audit and the handoff to Quant.
- Bot-3 work codifies the forensic admission chain.
- A backup branch explicitly references `bot1-bot2-bot3-bot4`, and a feature branch named `feat/multi-bot-deliberation-governance` exists.

However, the exact canonical role definition of Bot-4 is NOT sufficiently proven by the currently inspected durable documents. Therefore Bot-4's role must NOT be invented in this contract. It must be recovered from the canonical Bot-4 artifact/branch before implementation.

This is a deliberate Forensic UNKNOWN, not a failure.

## 3. Recommended separate project

YES: the four-bot collaboration layer should be a separate repository/project.

It should be a coordination/control substrate, not another Brain.

Suggested conceptual name:

`Forensic_Bot_Consortium`

The exact repository name remains UNDECIDED until explicitly chosen. Do not create a repository under an invented name.

## 4. Boundary

```text
                 PROJECT_BRAIN_AI
                ┌──────────────────┐
                │ FORENSIC BRAIN   │
                │ authority        │
                │ state            │
                │ admission        │
                │ promotion/deny   │
                └────────┬─────────┘
                         │ governed envelopes only
                         ▼
          ┌─────────────────────────────┐
          │ FOUR-BOT CONSORTIUM         │
          │ orchestration only          │
          │                             │
          │  BOT-1 ─┐                   │
          │  BOT-2 ─┼─► HANDOFF BUS     │
          │  BOT-3 ─┤                   │
          │  BOT-4 ─┘                   │
          │                             │
          │ scoped memory               │
          │ task leases                 │
          │ deliberation                │
          │ receipts                    │
          └──────────────┬──────────────┘
                         │
               structured outputs only
                         ▼
                ┌─────────────────┐
                │ DATA / QUANT /  │
                │ AUDIT COMPONENTS│
                └─────────────────┘
```

The consortium may coordinate. It may not silently mutate Brain state.

## 5. Four bots are workers/roles, not four authorities

Each bot receives:

- agent_id
- role_id
- task_id
- parent_action_id
- current_state_sha
- allowed_capabilities
- allowed_corridors
- allowed_rooms
- input evidence references
- deadline / lease
- expected output schema

Each bot returns a structured handoff envelope.

A bot does NOT return a new canonical state by itself.

## 6. Shared state rule

There must be one canonical state writer: Brain.

Workers may read scoped state and submit observations/proposals/results.

Workers must NOT concurrently rewrite canonical state.

This follows the safest supervisor-mediated pattern for small specialist counts: canonical state is owned by the supervisor/authority while workers remain scoped clients. External multi-agent guidance likewise recommends durable external state, scoped handoffs, context compaction, and explicit security trimming rather than one ever-growing shared context. 

## 7. Communication security

The existing corridor/room model applies to bot-to-bot communication:

```text
BOT A
  │
  ▼
CORRIDOR ADMISSION
  │ corridor_key
  ▼
ROOM ADMISSION
  │ room_key
  ▼
CAPABILITY CHECK
  │
  ▼
MESSAGE ENVELOPE
  │
  ▼
BOT B
```

Protected rooms additionally require the inner-latch/owner-release mechanism.

There is NO master key.

Correct corridor != correct room.
Correct room != permission to mutate.
Permission to read != permission to write.
Permission to write a proposal != authority to promote.

## 8. Handoff envelope

Minimum conceptual fields:

```text
message_id
trace_id
parent_action_id
sender_agent_id
sender_role_id
receiver_agent_id
receiver_role_id
source_state_sha
input_evidence_sha[]
requested_capability
corridor_id
room_id
capability_grant_id
nonce
created_at
expires_at
payload_sha
payload
result_type
result_status
result_evidence_sha[]
```

Credentials, secrets, raw database URLs and bulk source data do not belong in a handoff envelope.

## 9. Deliberation is not authority

If the four bots disagree:

```text
BOT-1 ─┐
BOT-2 ─┼─► DELIBERATION RECORD ─► BRAIN
BOT-3 ─┤
BOT-4 ─┘
```

The result is a deliberation record.

It is NOT automatically:

- Evidence
- State
- Edge
- EV
- Promotion

The Brain decides admission/promotion according to its existing contracts.

## 10. Orchestration pattern

Do NOT use a permanent unrestricted swarm.

Use a bounded hybrid:

```text
INTAKE
  ↓
BRAIN AUTHORIZATION
  ↓
TASK DECOMPOSITION
  ↓
┌──────────┬──────────┬──────────┐
│ worker A │ worker B │ worker C │  ...
└────┬─────┴────┬─────┴────┬─────┘
     │           │          │
     └───────────┴──────────┘
                 ↓
          RESULT VALIDATION
                 ↓
          DELIBERATION (only if needed)
                 ↓
             BRAIN GATE
                 ↓
           STATE / DENY / PROMOTE
```

Use sequential flow where ordering is causal/deterministic. Use parallel workers only where tasks are independent. Bounded fan-out, depth limits, timeouts and fallback behavior are mandatory. Multi-agent orchestration adds coordination cost and failure modes, so complexity must be justified by genuine specialization/security boundaries.

## 11. Memory architecture

Do not create one giant shared conversation memory.

Use four levels:

```text
L0  CANONICAL BRAIN STATE
L1  TASK / TRACE MEMORY
L2  AGENT-SCOPED WORK MEMORY
L3  EPHEMERAL MODEL CONTEXT
```

Only L0 is authority.

L1/L2 can contain intermediate work.

L3 disappears after the task unless explicitly committed as evidence/history through the correct gate.

Large outputs should be referenced by hash/object ID rather than copied between every agent. This protects both context size and Render memory.

## 12. Render/OOM rule

The consortium must be designed as a bounded dispatcher, not four continuously resident heavy agents on one 512 MB Render Free service.

Preferred model:

```text
Brain/dispatcher
      │
      ├── short task A → worker invocation → compact receipt
      ├── short task B → worker invocation → compact receipt
      ├── short task C → worker invocation → compact receipt
      └── short task D → worker invocation → compact receipt
```

No bulk source dataset is loaded into Brain.

No four-agent full-context fan-out.

No unbounded recursion.

No unbounded parallelism.

No giant in-memory result aggregation.

## 13. What belongs in the future consortium repository

```text
consortium/
├── agents/
│   ├── bot1/
│   ├── bot2/
│   ├── bot3/
│   └── bot4/
├── contracts/
│   ├── handoff.schema.json
│   ├── task.schema.json
│   ├── capability.schema.json
│   └── deliberation.schema.json
├── corridors/
├── rooms/
├── memory/
├── dispatcher/
├── receipts/
├── state/
├── tests/
└── docs/
```

The future repository must depend on Brain contracts, not redefine them.

## 14. Critical unknown

Bot-4 identity/role is unresolved.

Therefore:

```text
BOT4_ROLE = UNKNOWN
BOT4_CAPABILITIES = DENY
BOT4_ROOMS = DENY
BOT4_MUTATION = DENY
```

until canonical Bot-4 documentation is recovered.

## 15. Promotion rule

The consortium can recommend.

Only Brain can promote.

```text
WORKER PASS
   ≠
BRAIN PASS

DELIBERATION CONSENSUS
   ≠
EVIDENCE

MULTI-BOT AGREEMENT
   ≠
TRUTH

QUANT RESULT
   ≠
PROMOTION
```

## 16. Research basis

The design is consistent with current production multi-agent guidance: use the lowest orchestration complexity that reliably works; use specialized agents only when specialization/security/context boundaries justify them; persist shared state externally; compact context between agents; security-trim each agent; and apply explicit timeouts/fallbacks. Microsoft and AWS both emphasize these boundaries and warn against unnecessary multi-agent complexity. 

## 17. Status

```text
FOUR_BOT_CONSORTIUM_DESIGN = DESIGN_ONLY
BRAIN_AUTHORITY             = PRESERVED
BOT1_ROLE                   = PROVEN
BOT2_ROLE                   = PROVEN
BOT3_ROLE                   = PROVEN
BOT4_ROLE                   = UNKNOWN
SEPARATE_REPO               = RECOMMENDED
SEPARATE_REPO_CREATED       = NO
IMPLEMENTATION              = LOCKED
LAYER_1                     = LOCKED
STAIRCASE                   = LOCKED
PROMOTION                   = DENY
```

## 18. Successor instruction

Do not infer Bot-4.

Do not create a second Brain.

Do not create a second Forensic FSM.

Do not let four bots share mutable canonical state.

Do not use chat history as memory authority.

Recover Bot-4's canonical role first. Then create the separate consortium repository and implement only the orchestration boundary.
