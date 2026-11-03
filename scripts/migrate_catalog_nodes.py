#!/usr/bin/env python
"""Migrate a collection-based ODPC catalog to the canonical nodes[] form."""

import argparse
from pathlib import Path

import yaml


LEGACY_COLLECTIONS = (
    ("productReferences", "productReference"),
    ("useCases", "useCase"),
    ("businessObjectives", "businessObjective"),
    ("signals", "signal"),
    ("domains", "domain"),
    ("datasets", "dataset"),
    ("apis", "api"),
    ("policies", "policy"),
    ("workflows", "workflow"),
    ("agents", "agent"),
    ("capabilities", "capability"),
    ("strategicOpportunities", "strategicOpportunity"),
)


def migrate(document):
    if not isinstance(document, dict) or not isinstance(document.get("catalog"), dict):
        raise ValueError("Expected an ODPC document with a catalog object.")

    catalog = document["catalog"]
    if "nodes" in catalog:
        existing_nodes = catalog["nodes"]
        if not isinstance(existing_nodes, list):
            raise ValueError("catalog.nodes must be an array when present.")
        if all(isinstance(entry, dict) and isinstance(entry.get("node"), dict) for entry in existing_nodes):
            return document, 0
        if not all(isinstance(entry, dict) for entry in existing_nodes):
            raise ValueError("catalog.nodes entries must be objects.")
        catalog["nodes"] = [{"node": entry} for entry in existing_nodes]
        return document, len(existing_nodes)

    nodes = []
    for collection, kind in LEGACY_COLLECTIONS:
        items = catalog.pop(collection, [])
        if items is None:
            continue
        if not isinstance(items, list):
            raise ValueError(f"catalog.{collection} must be an array.")
        for item in items:
            if not isinstance(item, dict):
                raise ValueError(f"catalog.{collection} entries must be objects.")
            nodes.append({"node": {**item, "kind": kind}})
    catalog["nodes"] = nodes
    return document, len(nodes)


def main(argv=None):
    parser = argparse.ArgumentParser(description="Migrate an ODPC catalog to catalog.nodes[].")
    parser.add_argument("input", help="Legacy ODPC YAML catalog")
    parser.add_argument("--output", "-o", required=True, help="Migrated YAML output path")
    args = parser.parse_args(argv)

    input_path = Path(args.input)
    output_path = Path(args.output)
    try:
        document = yaml.safe_load(input_path.read_text(encoding="utf-8"))
        migrated, count = migrate(document)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(yaml.safe_dump(migrated, sort_keys=False, allow_unicode=False), encoding="utf-8")
    except (OSError, ValueError, yaml.YAMLError) as exc:
        print(f"Migration failed: {exc}")
        return 1

    print(f"Migrated {count} catalog item(s) to {output_path}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
