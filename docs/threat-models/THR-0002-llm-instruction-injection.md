# THR-0002 — LLM Instruction Injection

**Owner:** Enterprise Cyber Command · **Status:** Approved · **Source:** EAODS v17.3 Volume 11 (Automation domain — governed AI execution)

## Scope & assets

AI-assisted operations across the Automation Fabric: agent workloads that read untrusted content (logs, tickets, documents, external data) and can request privileged actions (tool calls, data retrieval, workflow execution).

## Trust boundary

Model-generated output versus authorized instruction. Content an agent *reads* and actions an agent may *take* are different trust domains; the boundary is crossed the moment model output influences a privileged action.

## Threat actors

External attacker planting instructions in content the platform will ingest (log entries, submitted documents, web content); insider seeding poisoned knowledge-base material; compromised upstream data source.

## Threat scenarios

1. **Direct injection.** Ingested content contains instructions the agent treats as commands, steering it to misuse its own authorized scopes.
2. **Privilege escalation via injection.** Injected content induces the agent to request actions beyond its scopes — exfiltration, destructive operations, or invoking other agents.
3. **Knowledge poisoning.** Malicious material enters the retrieval corpus and biases future agent outputs and decisions.
4. **Cross-agent laundering.** A low-privilege agent's poisoned output becomes a higher-privilege agent's trusted input.

## Mitigations

| Scenario | Mitigation | Implemented by |
|---|---|---|
| Direct injection | LLM output treated as data, never authorization; every action re-authorized against the agent's scopes | Volume 11 Automation domain · PAT-0001 |
| Escalation attempts | Least-privilege scopes make out-of-scope requests fail closed; human gates on irreversible actions | PAT-0001 · Volume 10 operational governance |
| Knowledge poisoning | Governed corpus intake with provenance; deviations handled as compliance findings | RUN-0003 · PAT-0003 |
| Cross-agent laundering | Per-agent identity and scope checks on every agent-to-agent invocation | EAODS-CTRL-000184 · PAT-0001 |

## Residual risk

Injection that steers an agent *within* its authorized scopes (subtly wrong analysis, biased summaries) is not blocked by authorization and must be caught by human review of consequential outputs and by assurance-side anomaly detection. This is the standing residual and the reason production decisions remain under human governance.

## Assurance hooks

Out-of-scope action requests are high-signal security telemetry: each one is emitted as evidence (PAT-0003) and evaluated under RUN-0003, with Enterprise Cyber Command escalation on any escalation-pattern recurrence.
