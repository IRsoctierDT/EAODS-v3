"""Validate cross-artifact traceability against the STD-0001/STD-0002 registries.

Checks, in order:
1. Every identifier-shaped token cited in docs/ or architecture/ uses a prefix
   registered in standards/vocabulary/object-identifiers.yaml.
2. Every relationship edge in standards/graph/relationships.yaml uses a
   registered edge type and endpoints that exist somewhere in the repository.

Exit code 0 on success, 1 with a failure report otherwise.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

import yaml

REGISTRY = Path("standards/vocabulary/object-identifiers.yaml")
TERMS = Path("standards/vocabulary/canonical-terms.yaml")
GRAPH = Path("standards/graph/relationships.yaml")
SCAN_ROOTS = (Path("docs"), Path("architecture"))

# Identifier-shaped token: registered-or-not, so unregistered prefixes are caught.
CANDIDATE = re.compile(r"\b([A-Z][A-Z0-9]*(?:-[A-Z0-9]+)*)-(\d{4,6})\b")


def load_yaml(path: Path) -> dict:
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def main() -> int:
    failures: list[str] = []

    registry = load_yaml(REGISTRY)
    prefixes = {p["prefix"] for p in registry["prefixes"]}

    # --- 1. Scan artifacts for cited identifiers ---------------------------
    cited: set[str] = set()
    for root in SCAN_ROOTS:
        for md in sorted(root.rglob("*.md")):
            for match in CANDIDATE.finditer(md.read_text(encoding="utf-8")):
                prefix, digits = match.group(1), match.group(2)
                identifier = f"{prefix}-{digits}"
                if prefix not in prefixes:
                    failures.append(
                        f"{md}: identifier '{identifier}' uses unregistered prefix '{prefix}'"
                    )
                else:
                    cited.add(identifier)

    # Terms registered but never cited are fine; terms cited must exist.
    terms = load_yaml(TERMS)
    known: set[str] = {t["id"] for t in terms["terms"]}
    known |= cited

    # --- 2. Validate the relationship graph --------------------------------
    graph = load_yaml(GRAPH)
    edge_types = set(graph["edge_types"])

    for edge in graph["edges"]:
        subject, edge_type, obj = edge["subject"], edge["type"], edge["object"]
        if edge_type not in edge_types:
            failures.append(f"graph: edge type '{edge_type}' is not registered")
        for endpoint in (subject, obj):
            endpoint_prefix = endpoint.rsplit("-", 1)[0]
            if endpoint_prefix not in prefixes:
                failures.append(
                    f"graph: endpoint '{endpoint}' uses unregistered prefix '{endpoint_prefix}'"
                )
            elif endpoint not in known:
                failures.append(
                    f"graph: endpoint '{endpoint}' is not cited in any artifact or registry"
                )

    if failures:
        print("Traceability validation failed:")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print(
        f"Traceability validated: {len(cited)} cited identifiers, "
        f"{len(graph['edges'])} graph edges, {len(prefixes)} registered prefixes."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
