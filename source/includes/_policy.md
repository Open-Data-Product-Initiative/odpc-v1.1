# ODPC Policy

The `Policy` object defines a reusable governance, compliance, security, or quality policy in an ODPC catalog. It aligns with the ODPG `Policy` node type. Policy rules, targets, duties, and governed objects belong in the authoritative policy definition and ODPG.

## Mandatory attributes and options

```yml
node:
  kind: policy
  id: POL-001
  name:
    en: Mobility Data Retention Policy
  description:
    en: Policy governing retention of mobility data.
```

| Attribute | Type | Required | Description |
| --- | --- | ---: | --- |
| `node` | object | ✓ | Top-level standalone node wrapper. |
| `kind` | string | ✓ | `policy`. |
| `id` | string | ✓ | Stable policy identifier. |
| `name` | language-tagged string | ✓ | Human-readable policy name. |
| `description` | language-tagged string | ✓ | Policy discovery description. |

## Optional attributes and options

```yml
node:
  kind: policy
  id: POL-001
  name:
    en: Mobility Data Retention Policy
  description:
    en: Policy governing retention of mobility data.
  type: retention
  effectiveFrom: "2026-01-01"
  effectiveTo: "2028-12-31"
  enforcement: automated
  owner:
    organization: Example Transport Authority
    team: Data Governance
    role: Policy Owner
  status: active
  $ref: https://example.org/policies/mobility-data-retention
  tags: [retention, governance]
```

| Attribute | Type | Options | Description |
| --- | --- | --- | --- |
| `type` | string | `access`, `privacy`, `security`, `retention`, `quality`, `usage`, `compliance` | Primary policy concern. |
| `effectiveFrom` | date | optional | Date from which the policy applies. |
| `effectiveTo` | date | optional | Date after which the policy no longer applies. |
| `enforcement` | string | `manual`, `automated`, `mixed` | How the policy is enforced. |
| `owner` | object | optional | Accountable organization, team, and role. |
| `status` | string | `draft`, `active`, `deprecated`, `retired` | Catalog lifecycle status. |
| `$ref` | string | optional | Authoritative policy definition. |
| `tags` | array of strings | optional | Discovery and filtering labels. |
