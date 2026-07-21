from __future__ import annotations

from pathlib import Path
import sys
import yaml

REQUIRED_FIELDS = {
    "title",
    "version",
    "owner",
    "suite",
    "status",
    "classification",
    "purpose",
    "architecture_domain",
    "review_cycle",
}

SEARCH_ROOTS = (Path("docs/frameworks"), Path("frameworks"))


def parse_front_matter(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        raise ValueError("missing YAML front matter")
    _, front_matter, _ = text.split("---", 2)
    data = yaml.safe_load(front_matter)
    if not isinstance(data, dict):
        raise ValueError("front matter is not a mapping")
    return data


def main() -> int:
    failures: list[str] = []
    files: set[Path] = set()

    for root in SEARCH_ROOTS:
        if root.exists():
            files.update(root.rglob("*.md"))

    for path in sorted(files):
        try:
            metadata = parse_front_matter(path)
            missing = sorted(REQUIRED_FIELDS - metadata.keys())
            if missing:
                failures.append(f"{path}: missing {', '.join(missing)}")
        except Exception as exc:
            failures.append(f"{path}: {exc}")

    if failures:
        print("Front matter validation failed:")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print(f"Validated front matter for {len(files)} framework documents.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
