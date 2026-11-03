# ODPC API

The `API` object defines a reusable service interface in an ODPC catalog. It aligns with the ODPG `API` node type and should point to an authoritative API definition when one exists.

## Mandatory attributes and options

```yml
node:
  kind: api
  id: API-001
  name:
    en: Traffic Conditions API
  description:
    en: Service interface for current traffic conditions.
```

| Attribute | Type | Required | Description |
| --- | --- | ---: | --- |
| `node` | object | ✓ | Top-level standalone node wrapper. |
| `kind` | string | ✓ | `api`. |
| `id` | string | ✓ | Stable API identifier. |
| `name` | language-tagged string | ✓ | Human-readable API name. |
| `description` | language-tagged string | ✓ | API discovery description. |
| `$ref` | string |  | Authoritative API definition, such as OpenAPI. |
| `tags` | array of strings |  | Discovery and filtering labels. |

Relationships between APIs and other objects belong in [ODPG](https://opendataproducts.org/odpg-v1.0/).
