from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "source"
SCHEMA_YAML = SOURCE / "schema" / "odpc.yaml"
SCHEMA_JSON = SOURCE / "schema" / "odpc.json"
SCHEMA_V11_DIR = SOURCE / "schema" / "v1.1"
V11_ODPC_SCHEMA_YAML = SCHEMA_V11_DIR / "odpc.yaml"
V11_ODPC_SCHEMA_JSON = SCHEMA_V11_DIR / "odpc.json"
AI_PRODUCT_SCHEMA_YAML = SCHEMA_V11_DIR / "ai-product.yaml"
AI_PRODUCT_SCHEMA_JSON = SCHEMA_V11_DIR / "ai-product.json"
V11_EXAMPLES_DIR = SOURCE / "v1.1" / "examples"
CATALOG_DIR = SOURCE / "catalog"
OBJECTS_JSONL = CATALOG_DIR / "objects.jsonl"
LLMS_TXT = SOURCE / "llms.txt"
EXAMPLES_DIR = CATALOG_DIR / "examples"
TEMPLATES_DIR = CATALOG_DIR / "templates"
DEFAULT_CATALOG_HTML_TEMPLATE = TEMPLATES_DIR / "catalog.html"
