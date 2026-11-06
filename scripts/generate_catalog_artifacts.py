#!/usr/bin/env python
import argparse
import json
import sys

import yaml

from odpc_paths import (
    AI_PRODUCT_SCHEMA_JSON,
    AI_PRODUCT_SCHEMA_YAML,
    SCHEMA_JSON,
    SCHEMA_YAML,
    V11_EXAMPLES_DIR,
    V11_ODPC_SCHEMA_JSON,
    V11_ODPC_SCHEMA_YAML,
)


SCHEMA_ARTIFACTS = (
    (SCHEMA_YAML, SCHEMA_JSON),
    (V11_ODPC_SCHEMA_YAML, V11_ODPC_SCHEMA_JSON),
    (AI_PRODUCT_SCHEMA_YAML, AI_PRODUCT_SCHEMA_JSON),
)


def load_yaml(path):
    with path.open(encoding="utf-8") as handle:
        return yaml.safe_load(handle)


def render_json(path):
    return json.dumps(load_yaml(path), indent=2) + "\n"


def artifact_pairs():
    yield from SCHEMA_ARTIFACTS
    if V11_EXAMPLES_DIR.exists():
        for yaml_path in sorted(V11_EXAMPLES_DIR.glob("*.yaml")):
            yield yaml_path, yaml_path.with_suffix(".json")


def main(argv=None):
    parser = argparse.ArgumentParser(
        description="Generate derived ODPC catalog artifacts from canonical sources.",
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="Check whether generated artifacts are up to date without writing files.",
    )
    args = parser.parse_args(argv)

    stale = []
    for source_path, target_path in artifact_pairs():
        expected = render_json(source_path)
        current = target_path.read_text(encoding="utf-8") if target_path.exists() else ""
        if current != expected:
            stale.append((source_path, target_path, expected))

    if args.check and stale:
        for _, target_path, _ in stale:
            print(f"{target_path}: out of date. Run `python scripts/generate_catalog_artifacts.py`.", file=sys.stderr)
        return 1
    if args.check:
        print("OK: catalog artifacts are up to date.")
        return 0

    for _, target_path, expected in stale:
        target_path.write_text(expected, encoding="utf-8")
        print(f"Generated {target_path.relative_to(target_path.parents[2])}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
