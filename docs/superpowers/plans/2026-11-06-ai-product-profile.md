# ODPC v1.1 AI Product Profile Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add a versioned ODPC v1.1 catalog schema and normative `AIProduct` profile with validated examples, documentation, and unchanged v1.0 artifacts.

**Architecture:** The existing root artifact set remains the v1.0 compatibility baseline. A v1.1 schema tree supplies a catalog schema and a standalone AI Product Profile, both canonical in YAML and generated as JSON. A v1.1 `ProductReference` identifies an AI product; the existing `Agent` node continues to describe a cataloged component, and ODPG continues to own portfolio relationships.

**Tech Stack:** YAML, JSON Schema draft 2020-12, Python 3, PyYAML, jsonschema, unittest, Middleman Markdown.

---

### Task 1: Define the v1.1 contract in failing tests

**Files:**
- Create: `tests/test_v1_1_ai_product_profile.py`
- Modify: `tests/test_agent_scripts.py`

- [ ] **Step 1: Write direct schema tests before schemas or fixtures exist.**

```python
def test_yaml_and_json_ai_product_examples_are_equivalent_and_valid():
    schema = load_yaml(V11_SCHEMA_DIR / "ai-product.yaml")
    validator = jsonschema.Draft202012Validator(schema)
    for stem in AI_PROFILE_STEMS:
        yaml_document = load_yaml(V11_EXAMPLES / f"{stem}.yaml")
        json_document = json.loads((V11_EXAMPLES / f"{stem}.json").read_text(encoding="utf-8"))
        self.assertEqual(yaml_document, json_document)
        self.assertEqual(list(validator.iter_errors(yaml_document)), [])

def test_ai_catalog_reference_requires_the_odpc_v1_1_profile_contract():
    catalog = load_yaml(V11_EXAMPLES / "catalog-ai-products.yaml")
    validator = jsonschema.Draft202012Validator(load_yaml(V11_SCHEMA_DIR / "odpc.yaml"))
    self.assertEqual(list(validator.iter_errors(catalog)), [])
    del catalog["catalog"]["nodes"][0]["node"]["productModel"]["schema"]
    self.assertNotEqual(list(validator.iter_errors(catalog)), [])
```

- [ ] **Step 2: Add negative boundaries and v1.0 regression assertions.**

```python
def test_profile_requires_purpose_and_component_references_require_a_standard():
    document = load_yaml(V11_EXAMPLES / "agentic-procurement-review.yaml")
    validator = jsonschema.Draft202012Validator(load_yaml(V11_SCHEMA_DIR / "ai-product.yaml"))
    del document["aiProduct"]["purpose"]
    self.assertNotEqual(list(validator.iter_errors(document)), [])

def test_v1_0_schema_identity_is_unchanged():
    schema = load_yaml(ROOT / "source" / "schema" / "odpc.yaml")
    self.assertEqual(schema["$id"], "https://opendataproducts.org/odpc-v1.0/schema/odpc.yaml")
    self.assertEqual(schema["properties"]["version"]["pattern"], "^1\\.0$")
```

- [ ] **Step 3: Run the red test.**

Run: `PYTHONDONTWRITEBYTECODE=1 python3 -m unittest tests.test_v1_1_ai_product_profile -v`

Expected: FAIL because the v1.1 schema and example paths do not exist.

- [ ] **Step 4: Add failing CLI tests.**

```python
def test_validate_ai_product_accepts_v1_1_yaml(self):
    result = run_script("scripts/validate_ai_product.py", "source/v1.1/examples/rag-knowledge-assistant.yaml")
    self.assertEqual(result.returncode, 0, result.stderr + result.stdout)
    self.assertIn("valid AI Product", result.stdout)

def test_check_v1_1_artifacts_passes(self):
    result = run_script("scripts/check_v1_1_artifacts.py")
    self.assertEqual(result.returncode, 0, result.stderr + result.stdout)
```

- [ ] **Step 5: Run the red CLI tests and commit the test contract.**

Run: `PYTHONDONTWRITEBYTECODE=1 python3 -m unittest tests.test_agent_scripts.AgentScriptsTest.test_validate_ai_product_accepts_v1_1_yaml tests.test_agent_scripts.AgentScriptsTest.test_check_v1_1_artifacts_passes -v`

Expected: FAIL because both scripts are absent.

```bash
git add tests/test_v1_1_ai_product_profile.py tests/test_agent_scripts.py
git commit -m "test: define ODPC v1.1 AI profile contract"
```

### Task 2: Create canonical YAML schemas and derived JSON schemas

**Files:**
- Create: `source/schema/v1.1/odpc.yaml`
- Create: `source/schema/v1.1/ai-product.yaml`
- Create: `source/schema/v1.1/odpc.json`
- Create: `source/schema/v1.1/ai-product.json`
- Modify: `scripts/odpc_paths.py`
- Modify: `scripts/generate_catalog_artifacts.py`

- [ ] **Step 1: Copy the v1.0 catalog schema into the versioned v1.1 location and only change its root version identity plus ProductReference.**

```yaml
$id: https://opendataproducts.org/odpc-v1.1/schema/odpc.yaml
properties:
  schema: {const: https://opendataproducts.org/odpc-v1.1/schema/odpc.yaml}
  version: {pattern: ^1\\.1$}
$defs:
  ProductModel:
    required: [standard, version, format, "$ref"]
    properties:
      standard: {type: string, minLength: 1}
      version: {type: string, minLength: 1}
      profile: {type: string, minLength: 1}
      format: {type: string, enum: [yaml, json, html, markdown, api, other]}
      schema: {$ref: "#/$defs/Reference"}
      "$ref": {$ref: "#/$defs/Reference"}
  ProductReference:
    properties:
      productCategory: {type: string, enum: [data_product, ai_product]}
```

Add an `allOf` conditional: `productCategory: ai_product` requires `standard: ODPC`, `version: "1.1"`, `profile: AIProduct`, and non-empty `schema`; other product references retain flexible standards and optional schema.

- [ ] **Step 2: Define the standalone AI Product Profile.**

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
$id: https://opendataproducts.org/odpc-v1.1/schema/ai-product.yaml
type: object
additionalProperties: false
required: [schema, version, kind, aiProduct]
properties:
  schema: {const: https://opendataproducts.org/odpc-v1.1/schema/ai-product.yaml}
  version: {const: "1.1"}
  kind: {const: AIProduct}
  aiProduct: {$ref: "#/$defs/AIProduct"}
```

`AIProduct` requires `productID`, `productVersion`, language-tagged `name`, `description`, `purpose`, `owner`, and one `productType` from `predictive`, `generative`, `rag`, `agentic`, `hybrid`, and `other`. Define optional capabilities; governance with autonomy, human oversight, consequential approval, risk, policy references, and limitations; evaluation requirements; operations; and `implementationReferences` with role, standard, version, format, optional schema, and `$ref`. Permit `x-*` extension fields but omit prompts, runtime configuration, weights, deployment config, and graph edges.

- [ ] **Step 3: Generalize JSON generation from a canonical list.**

```python
SCHEMA_ARTIFACTS = (
    (SCHEMA_YAML, SCHEMA_JSON),
    (V11_ODPC_SCHEMA_YAML, V11_ODPC_SCHEMA_JSON),
    (AI_PRODUCT_SCHEMA_YAML, AI_PRODUCT_SCHEMA_JSON),
)
for source_path, target_path in SCHEMA_ARTIFACTS:
    expected = json.dumps(yaml.safe_load(source_path.read_text(encoding="utf-8")), indent=2) + "\n"
```

- [ ] **Step 4: Generate JSON artifacts and run the partial test suite.**

Run: `PYTHONDONTWRITEBYTECODE=1 python3 scripts/generate_catalog_artifacts.py && PYTHONDONTWRITEBYTECODE=1 python3 -m unittest tests.test_v1_1_ai_product_profile -v`

Expected: JSON schemas are created; tests still fail only because fixtures are absent.

- [ ] **Step 5: Commit schemas and generation support.**

```bash
git add source/schema/v1.1 scripts/odpc_paths.py scripts/generate_catalog_artifacts.py
git commit -m "feat: add ODPC v1.1 AI Product schemas"
```

### Task 3: Add complete YAML and JSON profile and catalog examples

**Files:**
- Create: `source/v1.1/examples/predictive-demand-forecast.{yaml,json}`
- Create: `source/v1.1/examples/rag-knowledge-assistant.{yaml,json}`
- Create: `source/v1.1/examples/agentic-procurement-review.{yaml,json}`
- Create: `source/v1.1/examples/hybrid-decision-support.{yaml,json}`
- Create: `source/v1.1/examples/catalog-ai-products.{yaml,json}`

- [ ] **Step 1: Create the four profiles.**

All profiles use the same standalone envelope. The predictive profile demonstrates measurable forecasting evaluation. The RAG profile demonstrates qualitative and retrieval-grounding evaluation. The agentic procurement-review profile requires human approval for consequential recommendations and references an external agent card. The hybrid profile combines prediction, generation, and human decision support with multiple implementation-reference roles.

- [ ] **Step 2: Create an AI product catalog reference with matching identity.**

```yaml
schema: https://opendataproducts.org/odpc-v1.1/schema/odpc.yaml
version: "1.1"
kind: Catalog
catalog:
  metadata:
    id: CAT-AI-001
    name: {en: AI Product Portfolio}
    description: {en: A catalog with AI product references.}
  nodes:
    - node:
        kind: productReference
        id: AI-PR-001
        productID: procurement-review-assistant
        productVersion: "1.0.0"
        name: {en: Procurement Review Assistant}
        description: {en: An agentic application that prepares procurement reviews for human approval.}
        productCategory: ai_product
        productModel:
          standard: ODPC
          version: "1.1"
          profile: AIProduct
          format: yaml
          schema: ./schema/ai-product.yaml
          $ref: ./agentic-procurement-review.yaml
```

- [ ] **Step 3: Serialize each YAML fixture to canonical JSON and execute the direct tests.**

Run: `PYTHONDONTWRITEBYTECODE=1 python3 -m unittest tests.test_v1_1_ai_product_profile -v`

Expected: PASS for profile validity, YAML/JSON equivalence, AI-reference validation, negative cases, and the v1.0 regression assertions.

- [ ] **Step 4: Commit the example set.**

```bash
git add source/v1.1/examples tests/test_v1_1_ai_product_profile.py
git commit -m "docs: add ODPC v1.1 AI Product examples"
```

### Task 4: Add reusable validation and v1.1 consistency checks

**Files:**
- Create: `scripts/validate_ai_product.py`
- Create: `scripts/check_v1_1_artifacts.py`
- Modify: `tests/test_agent_scripts.py`

- [ ] **Step 1: Implement the profile validator by mirroring the existing safe YAML/JSON loader.**

```python
parser.add_argument("document", help="Path to an AI Product YAML or JSON document")
parser.add_argument("--schema", default=str(AI_PRODUCT_SCHEMA_YAML))
validator = jsonschema.Draft202012Validator(load_schema(schema_path))
errors = sorted(validator.iter_errors(load_data(document_path)), key=lambda error: list(error.path))
print(f"{document_path}: valid AI Product")
```

- [ ] **Step 2: Implement the artifact checker.**

Assert v1.1 root IDs/version constraints, exact YAML-to-JSON rendering, the AI `ProductReference` conditional, five YAML/JSON fixture pairs, catalog/profile ID and version agreement, every requested product type, and documentation guidance that distinguishes product profiles, agents, ODPG relationships, and external component standards.

- [ ] **Step 3: Run the previously red CLI tests and generation freshness.**

Run: `PYTHONDONTWRITEBYTECODE=1 python3 -m unittest tests.test_agent_scripts.AgentScriptsTest.test_validate_ai_product_accepts_v1_1_yaml tests.test_agent_scripts.AgentScriptsTest.test_check_v1_1_artifacts_passes -v && PYTHONDONTWRITEBYTECODE=1 python3 scripts/generate_catalog_artifacts.py --check`

Expected: all commands exit 0.

- [ ] **Step 4: Commit the validation tooling.**

```bash
git add scripts/validate_ai_product.py scripts/check_v1_1_artifacts.py tests/test_agent_scripts.py
git commit -m "feat: validate ODPC v1.1 AI Product artifacts"
```

### Task 5: Publish versioned specification and agent guidance

**Files:**
- Create: `source/v1.1/index.html.md`
- Modify: `source/llms.txt`
- Modify: `scripts/check_v1_1_artifacts.py`

- [ ] **Step 1: Write the v1.1 guide.**

Explain the profile envelope, every section and controlled vocabulary, the exact `ProductReference` example, `schema` versus `$ref`, and implementation-reference roles. State normative non-goals: no ODPC-AI/OAPS standard, no AI catalog-node kind, no embedded agent/model runtime definition, and no ODPG relationships in ODPC.

- [ ] **Step 2: Add v1.1 resource selection to `llms.txt`.**

Direct agents to `/schema/v1.1/odpc.yaml`, `/schema/v1.1/ai-product.yaml`, and `/v1.1/examples/`; direct catalog linking through `ProductReference`; direct portfolio relationships to ODPG; and direct component definitions to external technical standards.

- [ ] **Step 3: Verify documentation artifacts and commit.**

Run: `PYTHONDONTWRITEBYTECODE=1 python3 scripts/check_v1_1_artifacts.py`

Expected: `OK: ODPC v1.1 AI Product artifacts are consistent.`

```bash
git add source/v1.1/index.html.md source/llms.txt scripts/check_v1_1_artifacts.py
git commit -m "docs: publish ODPC v1.1 AI Product guidance"
```

### Task 6: Verify the complete release change

**Files:**
- Verify: all files above

- [ ] **Step 1: Run the complete Python suite.**

Run: `PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s tests -v`

Expected: all v1.0 and v1.1 tests pass.

- [ ] **Step 2: Run independent consistency checks.**

Run: `PYTHONDONTWRITEBYTECODE=1 python3 scripts/check_agent_artifacts.py && PYTHONDONTWRITEBYTECODE=1 python3 scripts/check_v1_1_artifacts.py && PYTHONDONTWRITEBYTECODE=1 python3 scripts/generate_catalog_artifacts.py --check`

Expected: all three commands exit 0.

- [ ] **Step 3: Validate every versioned YAML and JSON example.**

Run: `for path in source/v1.1/examples/*.{yaml,json}; do case "$path" in *catalog*) python3 scripts/validate_catalog.py "$path" --schema source/schema/v1.1/odpc.yaml ;; *) python3 scripts/validate_ai_product.py "$path" ;; esac; done`

Expected: every profile reports `valid AI Product`; every catalog reports `valid ODPC catalog`.

- [ ] **Step 4: Build the static documentation.**

Run: `bundle exec middleman build`

Expected: exit 0 and renders the versioned guide under `build/v1.1/`.

- [ ] **Step 5: Inspect scope before publication.**

Run: `git status --short && git diff --check && git log --oneline origin/main..HEAD`

Expected: only v1.1 schemas, examples, validators, guidance, and tests are changed.

- [ ] **Step 6: Push only with user authorization.**

Run: `git push origin HEAD`
