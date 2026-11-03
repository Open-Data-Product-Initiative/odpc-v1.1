# ODPC Domain

The `Domain` object defines a reusable business, organizational, technical, or data domain in an ODPC catalog. It aligns with the ODPG `Domain` node type.

## Mandatory attributes and options

```yml
node:
  kind: domain
  id: DOM-001
  name:
    en: Urban Mobility
  description:
    en: Business and operational domain for city transportation services.
```

| Attribute | Type | Required | Description |
| --- | --- | ---: | --- |
| `node` | object | ✓ | Top-level standalone node wrapper. |
| `kind` | string | ✓ | `domain`. |
| `id` | string | ✓ | Stable domain identifier. |
| `name` | language-tagged string | ✓ | Human-readable domain name. |
| `description` | language-tagged string | ✓ | Domain purpose and scope. |
| `$ref` | string |  | Authoritative domain definition. |
| `tags` | array of strings |  | Discovery and filtering labels. |

Relationships between domains and other objects belong in [ODPG](https://opendataproducts.org/odpg-v1.0/).
