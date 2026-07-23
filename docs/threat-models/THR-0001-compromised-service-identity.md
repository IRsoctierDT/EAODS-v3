# THR-0001 — Compromised Service Identity

**Owner:** Enterprise Cyber Command · **Status:** Approved · **Source:** EAODS v17.3 Volume 8/11, PAT-0001

## Scope & assets

Service-to-service authentication across the platform: credentials issued by the identity authority, the issuance service itself, and every protected service that trusts its verdicts.

## Trust boundary

A caller's presented identity versus its actual identity. Everything downstream of a successful verification inherits this boundary's integrity.

## Threat actors

External attacker with a stolen credential; compromised workload attempting lateral movement; malicious or defective internal automation reusing another service's identity.

## Threat scenarios

1. **Credential theft and replay.** A leaked credential is replayed against protected services to inherit the victim's scopes.
2. **Scope escalation.** A workload requests or accumulates scopes beyond its role specification and uses the surplus.
3. **Identity authority compromise.** The issuer itself is subverted, making every downstream verification unreliable.
4. **Revocation lag.** A revoked credential remains honored by services that cache verification results.

## Mitigations

| Scenario | Mitigation | Implemented by |
|---|---|---|
| Theft & replay | Short-lived credentials; per-call verification; fail closed | EAODS-CTRL-000184 · PAT-0001 |
| Scope escalation | Allow-listed scopes per role; delegation off by default | PAT-0001 · Volume 11 Identity domain |
| Issuer compromise | Issuer is Tier 1: recovery via governed orchestration; issuance anomalies feed assurance | PAT-0004 · RUN-0001 · PAT-0003 |
| Revocation lag | Central revocation checked on verification; no long-lived verification caches | PAT-0001 · EAODS-CTRL-000184 |

## Residual risk

A credential is valid between issuance and theft-detection for its full (short) lifetime; lifetime tuning trades availability against exposure. Issuer compromise remains the highest-impact scenario and justifies its Tier 1 classification and independent assurance monitoring.

## Assurance hooks

Issuance volume, verification failure rates, and revocation latency are emitted as evidence (PAT-0003); anomalies trigger RUN-0003 with immediate Enterprise Cyber Command escalation.
