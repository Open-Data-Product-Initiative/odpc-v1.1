# ODPG-aligned placeholders

ODPC defines minimal top-level placeholders for eight ODPG core node types that do not yet have a richer ODPC object model. They make those resources discoverable in a catalog without claiming to define their full semantics.

Use these placeholders for identity, a short description, optional source reference, and local extensions. Use the referenced source for detailed metadata, and use [ODPG](https://opendataproducts.org/odpg-v1.0/) for relationships, traversal, and graph reasoning.

| Catalog collection | ODPG node type |
| --- | --- |
| `domains` | `Domain` |
| `datasets` | `Dataset` |
| `apis` | `API` |
| `policies` | `Policy` |
| `workflows` | `Workflow` |
| `agents` | `Agent` |
| `capabilities` | `Capability` |
| `strategicOpportunities` | `StrategicOpportunity` |

Every placeholder uses the same minimal shape.

| Attribute | Type | Required | Description |
| --- | --- | ---: | --- |
| `id` | string | ✓ | Stable identifier within the catalog. |
| `name` | language-tagged string | ✓ | Human-readable name. |
| `description` | language-tagged string | ✓ | Short discovery description. |
| `$ref` | string |  | Optional path or URI to the authoritative source record. |
| `tags` | array of strings |  | Optional discovery labels. |
| `x-*` | any |  | Local implementation-specific metadata. |

These are placeholders, not a substitute for API descriptions, policy definitions, workflow specifications, agent cards, or capability models. Do not add relationship fields to them; model connections in ODPG.
