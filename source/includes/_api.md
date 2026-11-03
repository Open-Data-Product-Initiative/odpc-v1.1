# ODPC API

The `API` object defines a reusable service interface in an ODPC catalog. It aligns with the ODPG `API` node type and should point to an authoritative API definition when one exists. Operations, schemas, authentication details, and service-to-dataset relationships remain in that definition or ODPG.

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

## Optional attributes and options

```yml
node:
  kind: api
  id: API-001
  name:
    en: Traffic Conditions API
  description:
    en: Service interface for current traffic conditions.
  type: rest
  version: "1.4.0"
  endpoint: https://api.example.org/traffic/v1
  access: authenticated
  owner:
    organization: Example Transport Authority
    team: Digital Services
    role: API Owner
  status: active
  $ref: https://example.org/apis/traffic-conditions/openapi.yaml
  tags: [traffic, conditions]
```

| Attribute | Type | Options | Description |
| --- | --- | --- | --- |
| `type` | string | `rest`, `graphql`, `grpc`, `event`, `other` | Interface style. |
| `version` | string | optional | Version of the exposed API contract. |
| `endpoint` | URI | optional | Base endpoint for the live service. |
| `access` | string | `open`, `authenticated`, `restricted` | Access expectation, not a detailed security contract. |
| `owner` | object | optional | Accountable organization, team, and role. |
| `status` | string | `draft`, `active`, `deprecated`, `retired` | Catalog lifecycle status. |
| `$ref` | string | optional | Authoritative API definition, such as OpenAPI or AsyncAPI. |
| `tags` | array of strings | optional | Discovery and filtering labels. |
