import json
import unittest
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "source"


def load_yaml(path):
    with path.open(encoding="utf-8") as handle:
        return yaml.safe_load(handle)


def assert_lang_string(value):
    assert isinstance(value, dict)
    assert isinstance(value.get("en"), str)
    assert value["en"].strip()


def assert_named_object(value, prefix):
    assert isinstance(value.get("id"), str)
    assert value["id"].startswith(prefix)
    assert_lang_string(value.get("name"))
    assert_lang_string(value.get("description"))


class AgentArtifactsTest(unittest.TestCase):
    def test_schema_uses_catalog_root_instead_of_product_root(self):
        schema = load_yaml(SOURCE / "schema" / "odpc.yaml")
        json_schema = json.loads((SOURCE / "schema" / "odpc.json").read_text(encoding="utf-8"))

        self.assertEqual(schema["required"], ["schema", "version", "kind", "catalog"])
        self.assertEqual(list(schema["properties"]), ["schema", "version", "kind", "catalog"])
        self.assertEqual(schema["properties"]["kind"]["const"], "Catalog")
        self.assertIn("catalog", schema["properties"])
        self.assertNotIn("product", schema["properties"])
        self.assertEqual(json_schema["required"], schema["required"])
        self.assertEqual(list(json_schema["properties"]), ["schema", "version", "kind", "catalog"])
        self.assertEqual(json_schema["properties"]["kind"]["const"], "Catalog")
        self.assertIn("catalog", json_schema["properties"])
        self.assertNotIn("product", json_schema["properties"])

        catalog_ref = schema["properties"]["catalog"]["$ref"].split("/")[-1]
        catalog = schema["$defs"][catalog_ref]
        self.assertEqual(catalog["required"], ["metadata", "nodes"])
        self.assertIn("metadata", catalog["properties"])
        self.assertIn("nodes", catalog["properties"])
        self.assertNotIn("meta", catalog["properties"])
        metadata_ref = catalog["properties"]["metadata"]["$ref"].split("/")[-1]
        metadata = schema["$defs"][metadata_ref]
        self.assertEqual(metadata["required"], ["id", "name", "description"])
        self.assertIn("tags", metadata["properties"])
        self.assertNotIn("tags", catalog["properties"])
        graph_reference = schema["$defs"]["GraphReference"]
        self.assertEqual(graph_reference["required"], ["standard", "version", "$ref"])
        self.assertIn("$ref", graph_reference["properties"])
        self.assertNotIn("uri", graph_reference["properties"])
        self.assertEqual(list(catalog["properties"]), ["metadata", "nodes"])
        self.assertIn("Node", schema["$defs"])

    def test_examples_cover_minimal_full_and_each_core_object(self):
        expected = [
            "minimal.yaml",
            "full.yaml",
            "product-reference.yaml",
            "use-case.yaml",
            "business-objective-with-kpis.yaml",
            "signal.yaml",
            "domain.yaml",
            "dataset.yaml",
            "api.yaml",
            "policy.yaml",
            "workflow.yaml",
            "agent.yaml",
            "capability.yaml",
            "strategic-opportunity.yaml",
        ]

        for filename in expected:
            self.assertTrue((SOURCE / "catalog" / "examples" / filename).is_file())

        minimal = load_yaml(SOURCE / "catalog" / "examples" / "minimal.yaml")
        self.assertEqual(minimal["schema"], "https://opendataproducts.org/odpc-v1.0/schema/odpc.yaml")
        self.assertEqual(minimal["version"], "1.0")
        self.assertEqual(minimal["kind"], "Catalog")
        assert_named_object(minimal["catalog"]["metadata"], "CAT-")
        self.assertNotIn("meta", minimal["catalog"])

        full = load_yaml(SOURCE / "catalog" / "examples" / "full.yaml")
        self.assertEqual(full["kind"], "Catalog")
        catalog = full["catalog"]
        assert_named_object(catalog["metadata"], "CAT-")
        self.assertIn("tags", catalog["metadata"])
        self.assertNotIn("meta", catalog)
        self.assertNotIn("tags", catalog)
        self.assertIn("$ref", catalog["metadata"]["graph"])
        self.assertNotIn("uri", catalog["metadata"]["graph"])
        nodes = {item["kind"]: item for item in catalog["nodes"]}
        assert_named_object(nodes["productReference"], "DP-")
        assert_named_object(nodes["useCase"], "UC-")
        assert_named_object(nodes["businessObjective"], "BO-")
        assert_named_object(nodes["signal"], "SIG-")

        product_reference = load_yaml(SOURCE / "catalog" / "examples" / "product-reference.yaml")["node"]
        self.assertEqual(product_reference["kind"], "productReference")
        assert_named_object(product_reference, "DP-")
        self.assertEqual(product_reference["productModel"]["standard"], "ODPS")
        self.assertIn("$ref", product_reference["productModel"])
        self.assertNotIn("uri", product_reference["productModel"])

    def test_product_model_uses_ref_for_odps_aligned_file_or_url_links(self):
        schema = load_yaml(SOURCE / "schema" / "odpc.yaml")
        product_model = schema["$defs"]["ProductModel"]

        self.assertEqual(product_model["required"], ["standard", "version", "format", "$ref"])
        self.assertIn("$ref", product_model["properties"])
        self.assertNotIn("uri", product_model["properties"])
        self.assertEqual(product_model["properties"]["$ref"]["$ref"], "#/$defs/Reference")
        self.assertEqual(schema["$defs"]["Reference"]["type"], "string")

        use_case = load_yaml(SOURCE / "catalog" / "examples" / "use-case.yaml")["node"]
        self.assertEqual(use_case["kind"], "useCase")
        assert_named_object(use_case, "UC-")
        self.assertTrue(use_case["dataNeeds"]["items"])

        objective = load_yaml(SOURCE / "catalog" / "examples" / "business-objective-with-kpis.yaml")["node"]
        self.assertEqual(objective["kind"], "businessObjective")
        assert_named_object(objective, "BO-")
        self.assertTrue(objective["kpis"][0]["id"].startswith("KPI-"))

        signal = load_yaml(SOURCE / "catalog" / "examples" / "signal.yaml")["node"]
        self.assertEqual(signal["kind"], "signal")
        assert_named_object(signal, "SIG-")
        self.assertIn(signal["source"]["origin"], {"internal", "external", "mixed"})

    def test_retrieval_jsonl_is_parseable_and_referenced(self):
        jsonl_path = SOURCE / "catalog" / "objects.jsonl"
        self.assertTrue(jsonl_path.is_file())

        records = [
            json.loads(line)
            for line in jsonl_path.read_text(encoding="utf-8").splitlines()
            if line.strip()
        ]

        ids = {record["id"] for record in records}
        self.assertEqual(
            ids,
            {
                "Catalog",
                "ProductReference",
                "UseCase",
                "BusinessObjective",
                "KPI",
                "Signal",
                "Domain",
                "Dataset",
                "API",
                "Policy",
                "Workflow",
                "Agent",
                "Capability",
                "StrategicOpportunity",
            },
        )

        for record in records:
            self.assertTrue(record["definition"])
            self.assertIsInstance(record["requiredFields"], list)
            self.assertTrue(record["doUseFor"])
            self.assertTrue(record["doNotUseFor"])

        llms = (SOURCE / "llms.txt").read_text(encoding="utf-8")
        self.assertIn("/catalog/objects.jsonl", llms)

    def test_odpg_core_objects_have_independent_top_level_examples(self):
        expected = {
            "domain.yaml": ("domain", "DOM-"),
            "dataset.yaml": ("dataset", "DS-"),
            "api.yaml": ("api", "API-"),
            "policy.yaml": ("policy", "POL-"),
            "workflow.yaml": ("workflow", "WF-"),
            "agent.yaml": ("agent", "AGENT-"),
            "capability.yaml": ("capability", "CAP-"),
            "strategic-opportunity.yaml": ("strategicOpportunity", "SO-"),
        }
        for filename, (object_name, prefix) in expected.items():
            item = load_yaml(SOURCE / "catalog" / "examples" / filename)["node"]
            self.assertEqual(item["kind"], object_name)
            assert_named_object(item, prefix)
            self.assertIn("$ref", item)

    def test_new_odpg_nodes_have_small_discovery_metadata_profiles(self):
        schema = load_yaml(SOURCE / "schema" / "odpc.yaml")
        common = {"owner", "status", "$ref", "tags"}
        expected = {
            "Domain": {"type"},
            "Dataset": {"version", "frequency", "classification", "access"},
            "API": {"type", "version", "endpoint", "access"},
            "Policy": {"type", "effectiveFrom", "effectiveTo", "enforcement"},
            "Workflow": {"type", "trigger", "version"},
            "Agent": {"type", "version", "autonomy"},
            "Capability": {"type", "maturity"},
            "StrategicOpportunity": {"type", "stage", "confidence", "impact", "timeHorizon"},
        }
        examples = {
            "Domain": "domain.yaml",
            "Dataset": "dataset.yaml",
            "API": "api.yaml",
            "Policy": "policy.yaml",
            "Workflow": "workflow.yaml",
            "Agent": "agent.yaml",
            "Capability": "capability.yaml",
            "StrategicOpportunity": "strategic-opportunity.yaml",
        }

        self.assertEqual(
            schema["$defs"]["LifecycleStatus"]["enum"],
            ["draft", "active", "deprecated", "retired"],
        )
        self.assertEqual(schema["$defs"]["TagList"]["items"]["type"], "string")
        self.assertEqual(schema["$defs"]["Priority"]["enum"], ["low", "medium", "high", "critical"])
        self.assertEqual(
            schema["$defs"]["WorkItemStatus"]["enum"],
            ["draft", "active", "paused", "completed", "retired"],
        )

        for definition, fields in expected.items():
            properties = schema["$defs"][definition]["properties"]
            self.assertTrue(common.issubset(properties), definition)
            self.assertTrue(fields.issubset(properties), definition)

            example = load_yaml(SOURCE / "catalog" / "examples" / examples[definition])["node"]
            for field in fields | common:
                self.assertIn(field, example, f"{definition} example missing {field}")


if __name__ == "__main__":
    unittest.main()
