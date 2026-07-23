# RUN-0003 — Compliance Deviation Response

**Owner:** Engineering Governance · **Status:** Approved · **Source:** EAODS v17.3 Volume 11, PAT-0003

## Trigger

Continuous compliance monitoring detects a material deviation: configuration drift, a failed control validation, an architecture deviation, or a policy violation against a registered control.

## Preconditions

- The affected control exists in the reference control catalog with a defined `evidence_requirement`.
- The implicated service has a current ownership record identifying its assurance owner.

## Procedure

1. Correlate the deviation to its control (`EAODS-CTRL-` ID) and implicated service (`SVC-` ID).
2. Classify severity: does the deviation disable a Preventive control or expose a trust boundary?
3. For trust-boundary exposure → **escalate immediately to Enterprise Cyber Command** and treat as a potential security event, not only a compliance finding.
4. Open a corrective engineering workflow assigned to the service's engineering owner.
5. Verify whether an approved architecture exception covers the deviation; if expired, trigger the Volume 11 mandatory exception review.
6. Remediate: restore conforming state or process a new exception with compensating controls.
7. **Human approval gate — assurance owner confirms the control validates clean.**
8. Close the deviation with root cause recorded in engineering-debt analytics.

## Validation

- Control re-validation passes under the same conditions that detected the deviation.
- No sibling services share the same deviating configuration (sweep before close).

## Escalation

- Preventive-control failure on a Tier 1 service → Enterprise Cyber Command + executive sponsor.
- Deviation recurrence after closure → architecture review (the fix was cosmetic, not structural).

## Evidence

Detection record, severity classification, corrective workflow reference, re-validation result, and closure decision are emitted to Continuous Assurance (PAT-0003).

## Related objects

EAODS-CTRL-000184 · PAT-0003 · TERM-0004 Continuous Assurance · Volume 11 exception governance
