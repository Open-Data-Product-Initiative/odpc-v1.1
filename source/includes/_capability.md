# ODPC Capability

The `Capability` object defines a reusable business, data, technical, or AI capability in an ODPC catalog. It aligns with the ODPG `Capability` node type. Capability decomposition and relationships to enabling assets belong in ODPG.

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

## Optional attributes and options

```yml
node:
  kind: capability
  id: CAP-001
  name:
    en: Traffic Demand Forecasting
  description:
    en: Capability to forecast traffic demand from historical and current signals.
  type: ai
  maturity: emerging
  owner:
    organization: Example Transport Authority
    team: Urban Analytics
    role: Capability Owner
  status: active
  $ref: https://example.org/capabilities/traffic-demand-forecasting
  tags: [forecasting, mobility]
```

| Attribute | Type | Options | Description |
| --- | --- | --- | --- |
| `type` | string | `business`, `data`, `technical`, `ai` | Nature of the capability. |
| `maturity` | string | `planned`, `emerging`, `established`, `retiring` | Current maturity of the capability. |
| `owner` | object | optional | Accountable organization, team, and role. |
| `status` | string | `draft`, `active`, `deprecated`, `retired` | Catalog lifecycle status. |
| `$ref` | string | optional | Authoritative capability definition. |
| `tags` | array of strings | optional | Discovery and filtering labels. |
