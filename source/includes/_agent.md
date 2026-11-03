# ODPC Agent

The `Agent` object defines a reusable AI agent or automation actor in an ODPC catalog. It aligns with the ODPG `Agent` node type.

## Mandatory attributes and options

```yml
node:
  kind: agent
  id: AGENT-001
  name:
    en: Mobility Planning Assistant
  description:
    en: Automation actor that prepares planning recommendations.
```

| Attribute | Type | Required | Description |
| --- | --- | ---: | --- |
| `node` | object | ✓ | Top-level standalone node wrapper. |
| `kind` | string | ✓ | `agent`. |
| `id` | string | ✓ | Stable agent identifier. |
| `name` | language-tagged string | ✓ | Human-readable agent name. |
| `description` | language-tagged string | ✓ | Agent discovery description. |
| `$ref` | string |  | Authoritative agent definition. |
| `tags` | array of strings |  | Discovery and filtering labels. |

Relationships between agents and other objects belong in [ODPG](https://opendataproducts.org/odpg-v1.0/).
