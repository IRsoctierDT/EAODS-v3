# RUN-0001 — Service Recovery Execution

**Owner:** Enterprise Platform Operations Center · **Status:** Approved · **Source:** EAODS v17.3 Volume 9, PAT-0004

## Trigger

A Tier 1 platform service (per its `RES-` resilience record) fails or degrades beyond its availability target.

## Preconditions

- The service holds a current resilience record with defined RTO/RPO and recovery classification.
- Dependency maps for the service are synchronized (Volume 9 dependency modeling).
- The resilience control plane is reachable.

## Procedure

1. Confirm detection and classify impact (service, dependencies, data exposure).
2. **Human approval gate — recovery authority authorizes entry into recovery.**
3. Execute the orchestrated recovery sequence from the resilience control plane, in dependency order.
4. Validate integrity at each step before proceeding; halt and reassess on any validation failure.
5. Measure elapsed recovery against the service's RTO and data loss against its RPO.
6. **Human approval gate — operational owner approves business resumption.**
7. Resume service and close the recovery window.

## Validation

- All integrity checks passed in sequence order.
- RTO/RPO objectives met or the miss documented with cause.
- Dependent services report healthy post-resumption.

## Escalation

- Validation failure or projected RTO breach → recovery authority + Business Continuity Program.
- Suspected cyber cause → Enterprise Cyber Command before further recovery steps.

## Evidence

Recovery timeline, per-step validation results, and RTO/RPO attainment are emitted to Continuous Assurance (PAT-0003) before the incident record closes.

## Related objects

RES-00163 · PAT-0004 · TERM-0004 Continuous Assurance
