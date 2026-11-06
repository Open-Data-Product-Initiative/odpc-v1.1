# ODPC v1.1 AI Product Profile Design

## Purpose

ODPC v1.1 adds a normative, machine-readable `AIProduct` profile. It describes an AI product as a governed business product without prescribing models, prompts, agents, runtime orchestration, or deployment technology.

The profile is part of ODPC v1.1. It is not a new specification named OAPS or ODPC-AI.

## Versioning and compatibility

The existing `source/schema/odpc.yaml`, `source/schema/odpc.json`, current examples, and their checks remain the ODPC v1.0 compatibility baseline. New v1.1 material lives in versioned directories and uses v1.1 schema identifiers and version constraints.

The v1.1 catalog schema extends `ProductReference` without changing the meaning of its existing `type` field:

- `productCategory` is optional and initially permits `data_product` and `ai_product`.
- `type` remains available for finer classifications.
- `productModel` requires `standard`, `version`, `format`, and `$ref`; it may contain `profile` and `schema`.
- `format` preserves existing values and supports YAML and JSON.
- For `productCategory: ai_product` referencing the ODPC v1.1 `AIProduct` profile, `standard: ODPC`, `version: "1.1"`, `profile: AIProduct`, and `schema` are required. The schema must identify the AI Product Profile validation schema.
- `$ref` always identifies the product-definition instance. `schema` identifies the structure used to validate that instance.

Existing data-product references remain flexible: their `standard` values are not narrowed, and `schema` stays optional unless the ODPC AI Product rule applies.

## AIProduct profile boundary

`AIProduct` is a standalone product-definition document:

```yaml
schema: https://opendataproducts.org/odpc-v1.1/schema/ai-product.yaml
version: "1.1"
kind: AIProduct
aiProduct: {}
```

It is referenced from a catalog through `ProductReference`; it is not a new top-level ODPC catalog node. The existing `Agent` catalog object remains a component-level object and may be independently cataloged. It does not become an AI product and does not replace the profile.

ODPG remains responsible for explicit portfolio relationships among products, use cases, business objectives, and agents. Implementation references are technical references, not portfolio relationship edges.

## AIProduct definition

`aiProduct` is the authoritative business product definition and contains:

- **Identity and business context:** `productID`, `productVersion`, language-tagged `name`, `description`, and `purpose`; optional `valueProposition`; existing ODPC `owner`; and one primary `productType` from `predictive`, `generative`, `rag`, `agentic`, `hybrid`, or `other`.
- **Capabilities:** optional descriptions of stable capability identifiers, names, descriptions, intended users, expected inputs and outputs, and operational limitations. Capabilities do not contain agent execution logic.
- **Governance:** autonomy level, human oversight, approval requirements for consequential actions, risk classification, policy/compliance references, and known limitations. Product autonomy does not assert the authority of any individual agent.
- **Evaluation:** measurable requirements with metric identifier and name, measurement method, target value, unit, evaluation status, and optional evidence reference. Evaluation requirements are distinct from observed results and support quantitative or qualitative methods.
- **Operations:** optional lifecycle, availability, monitoring, operational ownership, support/incident handling, and cost or resource expectations. Deployment configuration is excluded.
- **Implementation references:** optional component references with `role`, `standard`, `version`, `format`, optional `schema`, and `$ref`. Roles are `model`, `agent`, `agent_card`, `workflow`, `tool`, `service`, `evaluation`, and `other`.

The profile does not embed arbitrary agent configuration, model weights, prompts, or runtime orchestration.

## Published artifacts and examples

The versioned v1.1 release supplies canonical YAML schemas and derived JSON schemas for both the catalog and AI Product Profile. It also supplies:

- four realistic YAML AI Product examples: predictive demand forecasting, RAG knowledge assistant, agentic procurement review assistant, and hybrid decision-support product;
- matching JSON examples produced or verified from the YAML representation;
- a v1.1 catalog example that references an AI Product profile and has matching `productID` and `productVersion` values;
- reference documentation and `llms.txt` guidance explaining correct modeling and non-goals;
- generated/retrieval artifact entries that expose `AIProduct` as a product-definition profile, not a catalog-node kind.

## Validation and regression strategy

Tests first establish that v1.1 accepts valid product references and all profile examples, then that it rejects:

- an AI product reference missing a profile schema;
- an AI product reference with a non-ODPC standard, incorrect version, or wrong profile name;
- a profile with a non-`AIProduct` kind or missing required business identity fields;
- implementation references missing their required technical identity fields;
- catalog/profile identifier or version mismatches.

Regression tests retain evidence that v1.0 schema ids, version patterns, fixtures, generated JSON, and checks remain unchanged. Artifact generation confirms every JSON schema remains an exact rendering of its canonical YAML source.
