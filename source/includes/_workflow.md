# ODPC Workflow

The `Workflow` object defines a reusable business or technical workflow in an ODPC catalog. It aligns with the ODPG `Workflow` node type.

## Mandatory attributes and options

```yml
node:
  kind: workflow
  id: WF-001
  name:
    en: Incident Response Workflow
  description:
    en: Operational workflow for responding to major traffic incidents.
```

| Attribute | Type | Required | Description |
| --- | --- | ---: | --- |
| `node` | object | ✓ | Top-level standalone node wrapper. |
| `kind` | string | ✓ | `workflow`. |
| `id` | string | ✓ | Stable workflow identifier. |
| `name` | language-tagged string | ✓ | Human-readable workflow name. |
| `description` | language-tagged string | ✓ | Workflow discovery description. |
| `$ref` | string |  | Authoritative workflow definition. |
| `tags` | array of strings |  | Discovery and filtering labels. |

Relationships between workflows and other objects belong in [ODPG](https://opendataproducts.org/odpg-v1.0/).
