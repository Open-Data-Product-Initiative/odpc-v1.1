# ODPC Dataset

The `Dataset` object defines a reusable dataset resource in an ODPC catalog. It aligns with the ODPG `Dataset` node type and does not replace a full dataset specification. APIs that expose the dataset are separate `API` nodes connected through ODPG.

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

## Optional attributes and options

| Attribute | Type | Options | Description |
| --- | --- | --- | --- |
| `version` | string | optional | Version of this dataset definition or release. |
| `frequency` | string | `realTime`, `hourly`, `daily`, `weekly`, `monthly`, `quarterly`, `annual`, `irregular`, `static` | Expected update cadence. |
| `classification` | string | `public`, `internal`, `confidential`, `restricted` | Sensitivity classification of the dataset content. |
| `access` | string | `open`, `authenticated`, `restricted` | How a consumer may obtain the dataset. |
| `owner` | object | optional | Accountable organization, team, and role. |
| `status` | string | `draft`, `active`, `deprecated`, `retired` | Catalog lifecycle status. |
| `$ref` | string | optional | Authoritative dataset definition. |
| `tags` | array of strings | optional | Discovery and filtering labels. |
