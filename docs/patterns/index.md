# Architecture Pattern Library

The pattern library captures approved, reusable architecture patterns extracted from the EAODS framework volumes. Each pattern is a governed object under STD-0001: it carries a stable `PAT-` identifier, traces to the volume that defines its authority, and names the controls it satisfies.

Patterns are normative once approved: new designs that face a problem covered by an approved pattern shall either apply the pattern or record a justified exception per Volume 11 architecture exception governance.

## Pattern index

| ID | Pattern | Source authority | Primary domain |
|---|---|---|---|
| [PAT-0001](PAT-0001-zero-trust-service-identity.md) | Zero Trust Service Identity | Volume 8, Volume 11 (EAODS-CTRL-000184) | Identity and trust |
| [PAT-0002](PAT-0002-error-budget-gated-delivery.md) | Error-Budget-Gated Delivery | Volume 10 | Operations |
| [PAT-0003](PAT-0003-continuous-assurance-evidence-pipeline.md) | Continuous Assurance Evidence Pipeline | Volumes 9–11 | Assurance |
| [PAT-0004](PAT-0004-governed-recovery-orchestration.md) | Governed Recovery Orchestration | Volume 9 | Resilience |

## Pattern entry structure

Every pattern documents: **Context · Problem · Solution · Structure (diagram) · Consequences · Governing controls · Related objects**. Pattern IDs are minted from the object identifier registry and are never reused.

## Contributing a pattern

1. Confirm the pattern is demonstrated in at least one framework volume or approved implementation.
2. Mint the next `PAT-` identifier from the registry sequence.
3. Author the entry using the structure above.
4. Pass documentation validation and the human review gate (Enterprise Architecture Review Board).
