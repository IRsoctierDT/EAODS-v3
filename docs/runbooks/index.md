# Operational Runbook Library

The runbook library holds governed, executable operational procedures for the EAODS platform. Each runbook is an object under STD-0001: it carries a stable `RUN-` identifier, names its trigger and escalation path, and states the evidence it must emit to Continuous Assurance.

Runbooks operationalize the framework volumes: Volume 10 defines *who* operates the platform (the Enterprise Platform Operations Center); runbooks define *exactly what is done* when a defined condition occurs. A condition covered by an approved runbook shall be handled by that runbook or the deviation recorded.

## Runbook index

| ID | Runbook | Trigger | Source authority |
|---|---|---|---|
| [RUN-0001](RUN-0001-service-recovery-execution.md) | Service Recovery Execution | Tier 1 service failure | Volume 9, PAT-0004 |
| [RUN-0002](RUN-0002-error-budget-exhaustion-response.md) | Error Budget Exhaustion Response | Service error budget reaches zero | Volume 10, PAT-0002 |
| [RUN-0003](RUN-0003-compliance-deviation-response.md) | Compliance Deviation Response | Continuous compliance detects material deviation | Volume 11, PAT-0003 |

## Runbook entry structure

Every runbook documents: **Trigger · Preconditions · Procedure · Validation · Escalation · Evidence · Related objects**. Steps are numbered, idempotent where possible, and every human approval point is explicit.

## Contributing a runbook

1. Confirm the operational condition and its owning authority (Volume 10 service ownership).
2. Mint the next `RUN-` identifier from the registry sequence.
3. Author the entry using the structure above; every irreversible step must name its approval authority.
4. Pass documentation validation and the human review gate (Enterprise Platform Operations Center).
