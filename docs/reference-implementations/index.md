# Reference Implementations

Reference implementations demonstrate that EAODS objects — controls, patterns, threat mitigations — are buildable, not aspirational. Each entry lives in its own repository, is anchored to the EAODS object model by stable identifiers, and declares which objects it realizes and which threats it mitigates.

A reference implementation is the ADR-0002 **Build** pillar made concrete: the traceability chain runs from constitutional authority through control and pattern down to running code, and back up through evidence.

## Implementation index

| Implementation | Repository | Realizes | Mitigates |
|---|---|---|---|
| IANUA Agent Trust Broker (ATB) | `agent-trust-broker` — `docs/IANUA-ATB-v0.1-Identity-and-Policy-Broker.md` | PAT-0001 · EAODS-CTRL-000184 | THR-0001 · THR-0002 |

## IANUA Agent Trust Broker

The ATB is the identity-issuance and Zero-Trust policy-enforcement service for the IANUA agent fleet: every privileged agent action requires a verifiable, short-lived, scoped identity and a per-action allow/deny/escalate decision, recorded in a hash-chained audit log.

It is the reference realization of:

- **PAT-0001 Zero Trust Service Identity** — mint/verify/rotate/revoke lifecycle, allow-listed scopes, delegation off by default, fail-closed verification on every call.
- **EAODS-CTRL-000184 Service Identity Verification** — the control's `implementation_guidance` and `evidence_requirement` are implemented directly: short-lived scoped credentials, per-call verification, issuance and decision logs emitted as assurance evidence (PAT-0003).

And the mitigation architecture for:

- **THR-0001 Compromised Service Identity** — bounded credential lifetime, central revocation, least-privilege scopes.
- **THR-0002 LLM Instruction Injection** — model output is treated as data, never authorization; out-of-scope requests fail closed and escalate to a human gate; every escalation is a logged security event.

## Contributing a reference implementation

1. Anchor the design document to the EAODS object model: state what it realizes, mitigates, and evidences — by stable identifier.
2. Keep the implementation's own governance (charter, review gates, quality checks) in its repository; EAODS records the relationship, not the code.
3. Add the entry here and the corresponding edges to the knowledge graph when the implementation reaches a reviewable state.
4. Pass documentation validation and the human review gate (Enterprise Architecture Review Board).
