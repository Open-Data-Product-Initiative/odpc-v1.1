# ODPC Policy

The `Policy` object defines a reusable governance, compliance, security, or quality policy in an ODPC catalog. It aligns with the ODPG `Policy` node type.

## Mandatory attributes and options

```yml
policy:
  id: POL-001
  name:
    en: Mobility Data Retention Policy
  description:
    en: Policy governing retention of mobility data.
```

| Attribute | Type | Required | Description |
| --- | --- | ---: | --- |
| `policy` | object | ✓ | Top-level ODPC Policy object. |
| `id` | string | ✓ | Stable policy identifier. |
| `name` | language-tagged string | ✓ | Human-readable policy name. |
| `description` | language-tagged string | ✓ | Policy discovery description. |
| `$ref` | string |  | Authoritative policy definition. |
| `tags` | array of strings |  | Discovery and filtering labels. |

Relationships between policies and other objects belong in [ODPG](https://opendataproducts.org/odpg-v1.0/).
