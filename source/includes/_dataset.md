# ODPC Dataset

The `Dataset` object defines a reusable dataset resource in an ODPC catalog. It aligns with the ODPG `Dataset` node type and does not replace a full dataset specification.

## Mandatory attributes and options

```yml
node:
  kind: dataset
  id: DS-001
  name:
    en: Traffic Sensor Observations
  description:
    en: Time-stamped observations from roadside traffic sensors.
```

| Attribute | Type | Required | Description |
| --- | --- | ---: | --- |
| `node` | object | ✓ | Top-level standalone node wrapper. |
| `kind` | string | ✓ | `dataset`. |
| `id` | string | ✓ | Stable dataset identifier. |
| `name` | language-tagged string | ✓ | Human-readable dataset name. |
| `description` | language-tagged string | ✓ | Dataset discovery description. |
| `$ref` | string |  | Authoritative dataset definition. |
| `tags` | array of strings |  | Discovery and filtering labels. |

Relationships between datasets and other objects belong in [ODPG](https://opendataproducts.org/odpg-v1.0/).
