import copy
import json
import unittest
from pathlib import Path

import jsonschema
import yaml


ROOT = Path(__file__).resolve().parents[1]
V11_SCHEMA_DIR = ROOT / "source" / "schema" / "v1.1"
V11_EXAMPLES = ROOT / "source" / "v1.1" / "examples"
AI_PROFILE_STEMS = (
    "predictive-demand-forecast",
    "rag-knowledge-assistant",
    "agentic-procurement-review",
    "hybrid-decision-support",
)


def load_yaml(path):
    with path.open(encoding="utf-8") as handle:
        return yaml.safe_load(handle)


class AIProductProfileTest(unittest.TestCase):
    def test_yaml_and_json_ai_product_examples_are_equivalent_and_valid(self):
        schema = load_yaml(V11_SCHEMA_DIR / "ai-product.yaml")
        validator = jsonschema.Draft202012Validator(schema)

        for stem in AI_PROFILE_STEMS:
            yaml_document = load_yaml(V11_EXAMPLES / f"{stem}.yaml")
            json_document = json.loads((V11_EXAMPLES / f"{stem}.json").read_text(encoding="utf-8"))
            self.assertEqual(yaml_document, json_document)
            self.assertEqual(list(validator.iter_errors(yaml_document)), [])

    def test_ai_catalog_reference_requires_the_odpc_v1_1_profile_contract(self):
        catalog_schema = load_yaml(V11_SCHEMA_DIR / "odpc.yaml")
        catalog = load_yaml(V11_EXAMPLES / "catalog-ai-products.yaml")
        validator = jsonschema.Draft202012Validator(catalog_schema)

        self.assertEqual(list(validator.iter_errors(catalog)), [])
        reference = next(
            entry["node"]
            for entry in catalog["catalog"]["nodes"]
            if entry["node"]["kind"] == "productReference"
        )
        self.assertEqual(reference["productCategory"], "ai_product")
        self.assertEqual(reference["productModel"]["standard"], "ODPC")
        self.assertEqual(reference["productModel"]["version"], "1.1")
        self.assertEqual(reference["productModel"]["profile"], "AIProduct")

        for field in ("schema", "profile"):
            invalid_catalog = copy.deepcopy(catalog)
            invalid_reference = next(
                entry["node"]
                for entry in invalid_catalog["catalog"]["nodes"]
                if entry["node"]["kind"] == "productReference"
            )
            del invalid_reference["productModel"][field]
            self.assertNotEqual(list(validator.iter_errors(invalid_catalog)), [])

        invalid_catalog = copy.deepcopy(catalog)
        invalid_reference = next(
            entry["node"]
            for entry in invalid_catalog["catalog"]["nodes"]
            if entry["node"]["kind"] == "productReference"
        )
        invalid_reference["productModel"]["standard"] = "OASF"
        self.assertNotEqual(list(validator.iter_errors(invalid_catalog)), [])

    def test_data_product_references_keep_flexible_standard_and_optional_schema(self):
        catalog_schema = load_yaml(V11_SCHEMA_DIR / "odpc.yaml")
        catalog = load_yaml(V11_EXAMPLES / "catalog-ai-products.yaml")
        reference = next(
            entry["node"]
            for entry in catalog["catalog"]["nodes"]
            if entry["node"]["kind"] == "productReference"
        )
        reference["productCategory"] = "data_product"
        reference["productModel"] = {
            "standard": "Internal Product Definition",
            "version": "2026.11",
            "format": "yaml",
            "$ref": "./internal-product.yaml",
        }
        self.assertEqual(list(jsonschema.Draft202012Validator(catalog_schema).iter_errors(catalog)), [])

    def test_profile_requires_business_identity_and_excludes_runtime_configuration(self):
        document = load_yaml(V11_EXAMPLES / "agentic-procurement-review.yaml")
        validator = jsonschema.Draft202012Validator(load_yaml(V11_SCHEMA_DIR / "ai-product.yaml"))

        invalid_document = copy.deepcopy(document)
        del invalid_document["aiProduct"]["purpose"]
        self.assertNotEqual(list(validator.iter_errors(invalid_document)), [])

        invalid_document = copy.deepcopy(document)
        invalid_document["aiProduct"]["runtimeConfiguration"] = {"systemPrompt": "never publish"}
        self.assertNotEqual(list(validator.iter_errors(invalid_document)), [])

    def test_implementation_references_require_external_component_identity(self):
        document = load_yaml(V11_EXAMPLES / "rag-knowledge-assistant.yaml")
        validator = jsonschema.Draft202012Validator(load_yaml(V11_SCHEMA_DIR / "ai-product.yaml"))

        invalid_document = copy.deepcopy(document)
        del invalid_document["aiProduct"]["implementationReferences"][0]["standard"]
        self.assertNotEqual(list(validator.iter_errors(invalid_document)), [])

    def test_catalog_and_profile_identity_agree(self):
        catalog = load_yaml(V11_EXAMPLES / "catalog-ai-products.yaml")
        profile = load_yaml(V11_EXAMPLES / "agentic-procurement-review.yaml")
        reference = next(
            entry["node"]
            for entry in catalog["catalog"]["nodes"]
            if entry["node"]["kind"] == "productReference"
        )

        self.assertEqual(reference["productID"], profile["aiProduct"]["productID"])
        self.assertEqual(reference["productVersion"], profile["aiProduct"]["productVersion"])

    def test_ai_product_is_a_top_level_catalog_node(self):
        catalog = load_yaml(V11_EXAMPLES / "catalog-ai-products.yaml")
        validator = jsonschema.Draft202012Validator(load_yaml(V11_SCHEMA_DIR / "odpc.yaml"))
        nodes = [entry["node"] for entry in catalog["catalog"]["nodes"]]
        ai_product = next(node for node in nodes if node["kind"] == "aiProduct")

        self.assertEqual(ai_product["productID"], "procurement-review-assistant")
        self.assertEqual(ai_product["productVersion"], "1.0.0")
        self.assertEqual(list(validator.iter_errors(catalog)), [])

    def test_generated_json_schemas_match_their_canonical_yaml(self):
        for stem in ("odpc", "ai-product"):
            self.assertEqual(
                load_yaml(V11_SCHEMA_DIR / f"{stem}.yaml"),
                json.loads((V11_SCHEMA_DIR / f"{stem}.json").read_text(encoding="utf-8")),
            )

    def test_v1_0_schema_identity_and_fixtures_remain_unchanged(self):
        schema = load_yaml(ROOT / "source" / "schema" / "odpc.yaml")
        minimal = load_yaml(ROOT / "source" / "catalog" / "examples" / "minimal.yaml")

        self.assertEqual(schema["$id"], "https://opendataproducts.org/odpc-v1.0/schema/odpc.yaml")
        self.assertEqual(schema["properties"]["version"]["pattern"], "^1\\.0$")
        self.assertEqual(minimal["version"], "1.0")


if __name__ == "__main__":
    unittest.main()
