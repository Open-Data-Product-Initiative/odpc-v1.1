# ODPC StrategicOpportunity

The `StrategicOpportunity` object defines a reusable declared or inferred strategic opportunity in an ODPC catalog. It aligns with the ODPG `StrategicOpportunity` node type.

## Mandatory attributes and options

```yml
node:
  kind: strategicOpportunity
  id: SO-001
  name:
    en: Event-aware Mobility Planning
  description:
    en: Opportunity to improve mobility planning using event demand signals.
```

| Attribute | Type | Required | Description |
| --- | --- | ---: | --- |
| `node` | object | ✓ | Top-level standalone node wrapper. |
| `kind` | string | ✓ | `strategicOpportunity`. |
| `id` | string | ✓ | Stable opportunity identifier. |
| `name` | language-tagged string | ✓ | Human-readable opportunity name. |
| `description` | language-tagged string | ✓ | Opportunity discovery description. |
| `$ref` | string |  | Authoritative opportunity definition. |
| `tags` | array of strings |  | Discovery and filtering labels. |

Relationships between strategic opportunities and other objects belong in [ODPG](https://opendataproducts.org/odpg-v1.0/).
