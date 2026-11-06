#!/usr/bin/env python
import argparse
import json
import sys
from pathlib import Path

import yaml

from odpc_paths import AI_PRODUCT_SCHEMA_YAML
from validate_catalog import NoDatesSafeLoader


def load_data(path):
    with path.open(encoding="utf-8") as handle:
        return json.load(handle) if path.suffix.lower() == ".json" else yaml.load(handle, Loader=NoDatesSafeLoader)


def main(argv=None):
    parser = argparse.ArgumentParser(description="Validate an ODPC v1.1 AI Product YAML or JSON document.")
    parser.add_argument("document")
    parser.add_argument("--schema", default=str(AI_PRODUCT_SCHEMA_YAML))
    args = parser.parse_args(argv)
    try:
        import jsonschema
    except ModuleNotFoundError:
        print("Missing dependency: jsonschema.", file=sys.stderr)
        return 2
    try:
        document_path, schema_path = Path(args.document), Path(args.schema)
        schema = load_data(schema_path)
        jsonschema.Draft202012Validator.check_schema(schema)
        errors = sorted(jsonschema.Draft202012Validator(schema).iter_errors(load_data(document_path)), key=lambda error: list(error.path))
    except (FileNotFoundError, json.JSONDecodeError, yaml.YAMLError, jsonschema.SchemaError) as exc:
        print(str(exc), file=sys.stderr)
        return 1
    if errors:
        print(f"{document_path}: invalid AI Product", file=sys.stderr)
        for error in errors:
            location = ".".join(str(part) for part in error.path) or "<root>"
            print(f"- {location}: {error.message}", file=sys.stderr)
        return 1
    print(f"{document_path}: valid AI Product")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
