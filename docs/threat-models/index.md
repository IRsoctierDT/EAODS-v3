# Threat-Model Library

The threat-model library holds governed threat analyses for the EAODS platform's core trust boundaries. Each entry is an object under STD-0001: it carries a stable `THR-` identifier, names the assets and boundaries in scope, and maps every mitigation to the control, pattern, or runbook that implements it — by stable ID.

Threat models are defensive artifacts: they exist so that controls are placed where attacks actually land, and so Continuous Assurance can verify that each identified threat has a living, validated mitigation. They contain no offensive tooling or exploitation procedures (per SECURITY.md and the lawful-lab scope of this repository).

## Threat-model index

| ID | Threat model | Primary boundary | Source authority |
|---|---|---|---|
| [THR-0001](THR-0001-compromised-service-identity.md) | Compromised Service Identity | Service-to-service trust | Volume 8/11, PAT-0001 |
| [THR-0002](THR-0002-llm-instruction-injection.md) | LLM Instruction Injection | Model output to privileged action | Volume 11 (Automation domain) |
| [THR-0003](THR-0003-assurance-evidence-tampering.md) | Assurance Evidence Tampering | Operations to assurance reporting | Volumes 9–11, PAT-0003 |

## Entry structure

Every threat model documents: **Scope & assets · Trust boundary · Threat actors · Threat scenarios · Mitigations (mapped by ID) · Residual risk · Assurance hooks**. Scenarios state what the attacker achieves and how the platform resists — not how to reproduce the attack.

## Contributing a threat model

1. Identify the trust boundary and the framework volume that governs it.
2. Mint the next `THR-` identifier from the registry sequence.
3. Map every mitigation to an existing control (`EAODS-CTRL-`), pattern (`PAT-`), or runbook (`RUN-`); a threat with no mapped mitigation is a finding, not a footnote — open a corrective workflow.
4. Pass documentation validation and the human review gate (Enterprise Cyber Command).
