---
title: EAODS Canonical Historical Mapping Matrix
document_id: EAODS-MIG-MAP-001
version: 1.0.0-reconstructed
status: active
reconstructed: true
---

# EAODS Canonical Historical Mapping Matrix

| Historical source/concept | Canonical destination | Pillar | Mapping rule | Conflict disposition |
|---|---|---|---|---|
| v17.0 cyber defense/resilience | Control catalog and threat-model library | Govern / Design | Decompose into controls, threats, relationships | Volume 10 constraints and canonical IDs prevail |
| v17.1 reference architecture | Architecture pattern library | Design | Preserve rationale and interfaces | Material conflict requires EARB/ADR |
| v17.2 operations/executive playbook | Runbooks and governance procedures | Operate / Govern | Separate procedure from policy and authority | Current operating model prevails |
| v17.3 implementation guidance | Reference implementations | Build / Operate | Link implementation to controls and evidence | Implementation cannot redefine architecture |
| Volumes 1–7 | Unit-specific volume destinations | All | Migrate recovered text only | Missing text remains exceptioned |
| Volume 9 | Resilience, HA, and DR | Design / Operate | Preserve integration and verify traceability | Volume 10 governs operations |
| Volume 10 | EPOC, SRE, operational engineering | Operate | Governing interpretation | Deviation requires ADR/EARB |
| Volume 11 | Control catalog and compliance | Govern / Design | Preserve canonical control IDs | Canonical taxonomy prevails |
| Python agent sources | Agent handbooks and `agents.yaml` | Build / Operate | Map only with content evidence | Filename alone is insufficient |
| Enterprise Orchestrator Handbook | Agent governance and trust boundaries | Govern / Operate / Build | Map duties to roles, controls, and human gates | Least privilege and human review mandatory |
| Executive Control Tower v4.6 | Decision rights and executive observability | Govern / Operate | Metadata now; content only when recovered | Do not infer metrics or controls |
| Metrics Standard v4.7 | Evidence and metrics schemas | Govern / Operate | Require owners, source authority, reproducibility | Reject unowned/unverifiable measures |
| July 6 Volume 10 plan | Volume 10 coverage/provenance | Operate / Govern | Coverage checklist, not canonical substitute | Approved Volume 10 text prevails |
| Proposed Volume 11 AI Governance Runtime | Future AI-governance runtime artifacts | Govern / Build | Historical proposed title only | Cannot overwrite canonical Volume 11 |
| Proposed Volumes 12–13 | Future roadmap concepts | Govern / Design / Operate | Preserve without assigning current status | No inferred numbering/completion |

## Required deprecated-name crosswalk

Each recovered source must add a row containing:

| Original name/ID | Canonical name/ID | Relationship | Authority | Effective date | Review state |
|---|---|---|---|---|---|

Permitted relationships are `renamed-to`, `replaced-by`, `split-into`, `merged-into`, `implements`, `governed-by`, and `superseded-by`.
