#!/usr/bin/env python
import json
import sys

import yaml

from odpc_paths import AI_PRODUCT_SCHEMA_JSON, AI_PRODUCT_SCHEMA_YAML, V11_EXAMPLES_DIR, V11_ODPC_SCHEMA_JSON, V11_ODPC_SCHEMA_YAML


def load_yaml(path):
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def check_pair(yaml_path, json_path):
    assert yaml_path.is_file() and json_path.is_file(), f"missing {yaml_path} or {json_path}"
    assert load_yaml(yaml_path) == json.loads(json_path.read_text(encoding="utf-8")), f"{json_path} is stale"


def main():
    try:
        check_pair(V11_ODPC_SCHEMA_YAML, V11_ODPC_SCHEMA_JSON)
        check_pair(AI_PRODUCT_SCHEMA_YAML, AI_PRODUCT_SCHEMA_JSON)
        catalog_schema = load_yaml(V11_ODPC_SCHEMA_YAML)
        profile_schema = load_yaml(AI_PRODUCT_SCHEMA_YAML)
        assert catalog_schema["properties"]["version"]["const"] == "1.1"
        assert profile_schema["properties"]["kind"]["const"] == "AIProduct"
        product_reference = catalog_schema["$defs"]["ProductReference"]
        assert product_reference["properties"]["productCategory"]["enum"] == ["data_product", "ai_product"]
        for path in sorted(V11_EXAMPLES_DIR.glob("*.yaml")):
            check_pair(path, path.with_suffix(".json"))
        catalog = load_yaml(V11_EXAMPLES_DIR / "catalog-ai-products.yaml")
        profile = load_yaml(V11_EXAMPLES_DIR / "agentic-procurement-review.yaml")
        reference = catalog["catalog"]["nodes"][0]["node"]
        assert reference["productID"] == profile["aiProduct"]["productID"]
        assert reference["productVersion"] == profile["aiProduct"]["productVersion"]
        llms = (V11_EXAMPLES_DIR.parents[1] / "llms.txt").read_text(encoding="utf-8")
        for fragment in ["/schema/v1.1/odpc.yaml", "/schema/v1.1/ai-product.yaml", "ODPG", "implementationReferences"]:
            assert fragment in llms, f"llms.txt missing {fragment}"
    except Exception as exc:
        print(f"FAIL {exc}", file=sys.stderr)
        return 1
    print("OK: ODPC v1.1 AI Product artifacts are consistent.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
