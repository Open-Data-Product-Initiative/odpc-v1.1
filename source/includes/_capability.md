# ODPC Capability

The `Capability` object defines a reusable business or technical capability in an ODPC catalog. It aligns with the ODPG `Capability` node type.

## Mandatory attributes and options

```yml
node:
  kind: capability
  id: CAP-001
  name:
    en: Traffic Demand Forecasting
  description:
    en: Capability to forecast traffic demand from historical and current signals.
```

| Attribute | Type | Required | Description |
| --- | --- | ---: | --- |
| `node` | object | ✓ | Top-level standalone node wrapper. |
| `kind` | string | ✓ | `capability`. |
| `id` | string | ✓ | Stable capability identifier. |
| `name` | language-tagged string | ✓ | Human-readable capability name. |
| `description` | language-tagged string | ✓ | Capability discovery description. |
| `$ref` | string |  | Authoritative capability definition. |
| `tags` | array of strings |  | Discovery and filtering labels. |

Relationships between capabilities and other objects belong in [ODPG](https://opendataproducts.org/odpg-v1.0/).
