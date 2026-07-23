# RUN-0002 — Error Budget Exhaustion Response

**Owner:** Enterprise Platform Operations Center · **Status:** Approved · **Source:** EAODS v17.3 Volume 10, PAT-0002

## Trigger

A production service's error budget (per its SLO evaluation) reaches zero within the measurement window.

## Preconditions

- The service carries a canonical service ownership record with `error_budget_policy: Enforced`.
- SLI telemetry for the window is trusted (no known measurement defect).

## Procedure

1. Confirm exhaustion is real: rule out SLI measurement error before gating.
2. Activate the change gate: block further production changes for the service except reliability fixes.
3. Notify the service's engineering owner, operational owner, and executive sponsor.
4. Convene engineering review; identify the dominant budget-consuming failure modes.
5. Prioritize and execute reliability work targeting those failure modes.
6. Monitor SLO recovery; the gate remains until budget headroom is restored and the review signs off.
7. **Human approval gate — engineering review formally lifts the gate.**
8. Record the exhaustion cause and remediation in operational analytics (recurrence tracking).

## Validation

- Gate was applied within the policy window and no non-reliability change bypassed it.
- Post-remediation SLO trend shows restored headroom.

## Escalation

- Repeated exhaustion (recurrence within two windows) → Volume 10 operational governance review of the SLO and the service architecture.
- Gate bypass attempt → operational governance; record as a policy violation.

## Evidence

Exhaustion timestamp, gate activation/lift times, review decision, and remediation summary are emitted to Continuous Assurance (PAT-0003).

## Related objects

SVC-00387 · PAT-0002 · TERM-0003 EPOC · TERM-0009 Error budget
