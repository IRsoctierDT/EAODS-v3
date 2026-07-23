---
title: EAODS Unified Historical Corpus
document_id: EAODS-HIST-ROOT-001
version: 1.0.0-reconstructed
status: controlled-working-baseline
classification: internal
owner: Ivan Rozenblad
reconstruction_date: 2026-07-23
reconstructed: true
governing_architecture: Volume 10
canonical_roadmap: docs/governance/ROADMAP.md
---

# EAODS Unified Historical Corpus

This package consolidates the presently recoverable EAODS history into one controlled body of work. It joins conversation evidence, retained artifacts, repository facts, version lineage, migration controls, and reconstruction boundaries without representing unavailable originals as recovered.

## Governing order

When sources conflict, apply the following precedence:

1. Current approved EAODS repository artifacts and ADRs.
2. Volume 10 as the architectural north star.
3. Canonical v17.3 terminology, identifiers, and Volume 11 control catalog.
4. Complete retained historical artifacts.
5. Direct dated conversation evidence.
6. Corroborated summaries and roadmap references.
7. Unresolved references, which remain exceptions and are never silently completed.

## Corpus map

| File | Function |
|---|---|
| `00_MASTER_CORPUS.md` | Unified narrative, lineage, recovered architecture, and current reconstruction state |
| `01_SOURCE_INVENTORY.md` | Authoritative inventory of every presently known source or source class |
| `02_MIGRATION_MANIFEST.md` | Source-to-target migration dispositions and acceptance gates |
| `03_CANONICAL_MAPPING_MATRIX.md` | Crosswalk from historical concepts into the governed EAODS model |
| `04_PROVENANCE_AND_RECONSTRUCTION_LEDGER.md` | Evidence grades, reconstructed assertions, conflicts, and limitations |
| `05_EXCEPTION_QUEUE.md` | Missing sources, accountable owners, review dates, and closure conditions |
| `06_VOLUME_10_NORTH_STAR_CHARTER.md` | Binding interpretation rules derived from the recovered Volume 10 record |
| `07_HISTORICAL_ARTIFACT_RECORDS.md` | Reconstructed records for known historical packages, drafts, agents, and roadmap concepts |

## Package integrity

Source package: `EAODS_Unified_Historical_Corpus_1.0.0-reconstructed.tar.gz`
`sha256: a8b9da1eedac3159e99ffbc4dec2e995eb818ec8cd3d1e2066b1504517ccb6a2`
(checksum registered per the controlled migration rule; the archive itself is
retained outside the repository — its contents are these files.)

## Integrity notice

Every file in this package is reconstructed. The package is an authoritative migration-control baseline, not a substitute for missing original binaries. Recovered originals must be checksummed, registered, and linked without erasing this reconstruction history.

## Completion boundary

The corpus consolidates everything presently evidenced. It does **not** manufacture the unrecovered bodies of v17.0–v17.2, Volumes 1–7, the ten Python sources, or the three later draft artifacts. Those units are registered and controlled in the exception queue until recovered or formally superseded.
