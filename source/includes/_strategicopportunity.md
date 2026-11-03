# ODPC StrategicOpportunity

The `StrategicOpportunity` object defines a reusable declared or inferred strategic opportunity in an ODPC catalog. It aligns with the ODPG `StrategicOpportunity` node type. Supporting signals, affected capabilities, objectives, and product relationships belong in ODPG.

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

## Optional attributes and options

| Attribute | Type | Options | Description |
| --- | --- | --- | --- |
| `type` | string | `growth`, `efficiency`, `risk`, `compliance`, `innovation`, `customer` | Primary value or change theme. |
| `stage` | string | `identified`, `assessed`, `prioritized`, `pursuing`, `realized`, `declined` | Decision and realization stage. |
| `confidence` | string | `low`, `medium`, `high` | Confidence in the opportunity assessment. |
| `impact` | object | optional | Expected value and urgency. |
| `impact.valuePotential` | string | `low`, `medium`, `high`, `critical` | Estimated value potential. |
| `impact.urgency` | string | `low`, `medium`, `high`, `critical` | Estimated urgency. |
| `timeHorizon` | string | `nearTerm`, `mediumTerm`, `longTerm` | Expected horizon for realizing value. |
| `owner` | object | optional | Accountable organization, team, and role. |
| `status` | string | `draft`, `active`, `deprecated`, `retired` | Catalog lifecycle status, distinct from opportunity `stage`. |
| `$ref` | string | optional | Authoritative opportunity definition. |
| `tags` | array of strings | optional | Discovery and filtering labels. |
