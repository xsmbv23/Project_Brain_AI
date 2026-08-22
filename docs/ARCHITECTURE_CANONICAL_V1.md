# Project Brain AI — Canonical Architecture V1

## Purpose

This repository is the control/governance plane. It owns canonical state, next-action authority, forensic admission, worker allocation/reconciliation, and cross-plane coordination.

It does not own Quant Engine calculations and must not duplicate Quant Engine business logic.

## Canonical planes

1. `governance/` — authority, policy, role, session/bootstrap context.
2. `state/` — canonical current state and next action.
3. `contracts/` — machine-readable invariants and admission contracts.
4. `coordination/` — worker registry, allocation, leases, reconciliation, handoff.
5. `orchestration/` — thin execution adapters; no canonical-state authority.
6. `tools/` — probes/collectors; evidence producers only.
7. `tests/` — contract, forensic, orchestration and regression tests.
8. `workflows/` / `.github/workflows/` — CI and operational verification only.
9. `docs/` — human-readable architecture and runbooks; never a competing state store.
10. `state/receipts/` — append-only evidence/receipts when the repository currently uses repository-backed receipts.

## Authority rules

- BOT1 owns canonical governance/state/promotion authority.
- BOT2 is the Quant/Data adversarial peer and may challenge evidence; it does not promote canonical state.
- BOT3/BOT4 are worker identities and execution/evidence producers.
- Deliberation, worker receipts, runtime observations and proposals are not automatically canonical forensic truth.
- No PASS inheritance across allocations, deployments or sessions.
- Conflicts are preserved and escalated; history is append-only.

## Core mission boundary

The system exists to enable a defensible pipeline:

`real data -> canonical dataset -> causal features -> research -> real edge -> probability -> cost/payout -> multi-level EV -> OOS/robustness -> P&L/ROI -> controlled action`

Forensic/admission protects this pipeline; it is not the business outcome itself.

## Resource boundary

Render services must map one-to-one to canonical runtime roles. Duplicate services for the same role are deprecated unless a contract explicitly requires blue/green or migration overlap.

## Memory boundary

Workers must use bounded/streaming processing. No bulk historical load into RAM. On a 512 MB Render plan, design against a conservative memory guard and release per-day/page state before advancing.

## Migration rule

This document defines the target boundary. Existing files are not deleted merely because they are legacy. Every move/removal must first have a dependency audit, replacement path, and passing regression checks.
