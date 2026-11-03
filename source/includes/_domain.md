# ODPC Domain

The `Domain` object defines a reusable business, organizational, data, or technical domain in an ODPC catalog. It aligns with the ODPG `Domain` node type. Domain hierarchy and connections to other catalog objects belong in [ODPG](https://opendataproducts.org/odpg-v1.0/).

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

## Optional attributes and options

```yml
node:
  kind: domain
  id: DOM-001
  name:
    en: Urban Mobility
  description:
    en: Business and operational domain for city transportation services.
  type: business
  owner:
    organization: Example Transport Authority
    team: Urban Mobility
    role: Domain Owner
  status: active
  $ref: https://example.org/domains/urban-mobility
  tags: [mobility, transport]
```

| Attribute | Type | Options | Description |
| --- | --- | --- | --- |
| `type` | string | `business`, `organizational`, `data`, `technical` | Nature of the domain. |
| `owner` | object | optional | Accountable organization, team, and role. |
| `status` | string | `draft`, `active`, `deprecated`, `retired` | Catalog lifecycle status. |
| `$ref` | string | optional | Authoritative domain definition. |
| `tags` | array of strings | optional | Discovery and filtering labels. |
