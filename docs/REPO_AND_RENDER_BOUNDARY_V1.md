# Repo / Render Consolidation Map V1

## Canonical repositories

### 1. `xsmbv23/Project_Brain_AI`
Control plane: governance, canonical state, admission, worker allocation/reconciliation, orchestration adapters and forensic probes.

### 2. `xsmbv23/Quant_Engine`
Quantitative/data plane: collectors, temporal foundation, reconciliation, canonical dataset, features, research, edge, models, EV, backtest/replay and quantitative ledger.

### 3. `xsmbv23/xsmb-quant`
Product/application plane: user-facing product and thin adapters to admitted Quant Engine outputs.

No new fourth repository should be created for a worker or probe unless a hard deployment/security boundary requires it.

## Render service target map

| Current service | Target role | Status |
|---|---|---|
| `brain-worker-orchestrator-v4` | Project Brain worker orchestrator | CANONICAL CANDIDATE |
| `brain-bot2-worker-v2` | Project Brain BOT2 worker | CANONICAL CANDIDATE |
| `brain-bot3-worker` | Project Brain BOT3 worker | CANONICAL CANDIDATE |
| `brain-bot4-worker-v2` | Project Brain BOT4 worker | CANONICAL CANDIDATE |
| `source-independence-probe` | forensic probe | CANONICAL CANDIDATE |
| `brain-reality-probe` | reality/data probe | CANONICAL CANDIDATE |
| `quant-engine` | Quant Engine API | CANONICAL CANDIDATE |
| `bot2-headless-worker` | Quant Engine BOT2 runtime | LEGACY / DUPLICATE CANDIDATE |
| `quant-bot2-worker` | Quant Engine BOT2 runtime | LEGACY / DUPLICATE CANDIDATE |
| `brain-worker-orchestrator` | Project Brain orchestrator | LEGACY / DUPLICATE CANDIDATE |
| `brain-bot4-worker` | Project Brain BOT4 worker | LEGACY / DUPLICATE CANDIDATE |
| `project-brain-ai` | Project Brain API | LEGACY NAMING / REVIEW |
| `xsmb-quant` | Product | CANONICAL CANDIDATE |

## Safety rule

A legacy Render service is not deleted merely because a newer service exists. Before retirement, prove:

1. no workflow deploys to it;
2. no code/contract references its URL/service identity;
3. no active allocation depends on it;
4. its replacement has passed health/contract tests;
5. its evidence/receipt history is preserved;
6. the retirement is recorded in an append-only migration record.

## Desired end state

Project Brain: one canonical orchestrator + one worker service per active worker identity + only required forensic/reality probes.

Quant Engine: one canonical API/runtime + one canonical BOT2 headless runtime.

XSMB Quant: one canonical product service.

Duplicate services are retired only after the above proof chain.
