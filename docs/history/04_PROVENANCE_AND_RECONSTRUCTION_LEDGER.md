---
title: EAODS Provenance and Reconstruction Ledger
document_id: EAODS-PROV-LED-001
version: 1.0.0-reconstructed
status: active
reconstructed: true
---

# EAODS Provenance and Reconstruction Ledger

| ID | Assertion | Basis | Confidence | Limitation |
|---|---|---:|---:|---|
| REC-001 | Release lineage spans v17.0–v17.3 | Canonical project record | 100% | Historical corpora not all present |
| REC-002 | v17.3 references Volumes 1–11 | Roadmap/project evidence | 100% | Volumes 1–7 filenames/bodies absent |
| REC-003 | Volume 10 is the architectural north star | Explicit user and project decision | 100% | Must remain encoded in canonical governance |
| REC-004 | Volume 10 is v17.3.9-alpha and extends Volumes 1–9 | Recovered project record | 100% | Full artifact is outside current workspace |
| REC-005 | Volume 11 is v17.3.10-alpha and extends Volumes 1–10 | Recovered project record | 100% | Full artifact is outside current workspace |
| REC-006 | Ten named Python sources were requested as YAML-front-mattered Markdown conversions | Direct July 6 transcript | 100% | Bodies and outputs absent |
| REC-007 | Early Enterprise Edition reportedly contained 29 files | Conversation evidence | 90% | Manifest/archive absent |
| REC-008 | v3.2.0-alpha reportedly included release/map/roadmap/registry/workflow artifacts | Conversation evidence | 90% | Tag, commit, and bodies absent |
| REC-009 | July 6 Volume 10 plan included SRE, NOC/SOC/AIOC, incident command, telemetry, reliability, AI assistance, and human gates | Direct transcript | 100% | Planning scope is not proof of final coverage |
| REC-010 | July 6 Volumes 11–13 taxonomy conflicts with later canonical Volume 11 | Direct transcript plus later record | 100% | Requires explicit supersession, not renumbering |
| REC-011 | PR #10 was intended to complete Volume 9 integration and establish ADR-0002 | Direct transcript and later project record | 100% | Transcript includes obsolete failed attempt |
| REC-012 | v4.6, v4.7, and Orchestrator Handbook existed as drafts | Dated conversation/email records | 90% | Full bodies absent |
| REC-013 | PR #19 made `docs/governance/ROADMAP.md` authoritative | Verified project record | 100% | Repository path must be used as current authority |

## Conflict register

| ID | Conflict | Resolution |
|---|---|---|
| CON-001 | “Volume 11 — Enterprise AI Governance Runtime” versus canonical Volume 11 control catalog | Preserve the former as superseded planning taxonomy; do not renumber canonical content |
| CON-002 | Historical intent versus current implementation status | Mark intent as planned until repository evidence verifies completion |
| CON-003 | Reconstructed artifact versus recovered original | Preserve both; label reconstruction and link the original by checksum |

## Reconstruction declaration

This ledger records what is known, how it is known, and what remains unknown. A confidence score applies only to the stated assertion; it does not elevate an unavailable document body into recovered content.
