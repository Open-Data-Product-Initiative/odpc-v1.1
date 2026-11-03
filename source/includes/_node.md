# ODPC Node

Every catalog item is an ODPC `node`. The `kind` attribute selects its object schema, so catalog tools can read one `catalog.nodes` array rather than separate type-specific collections.

```yml
node:
  kind: productReference
  id: DP-001
  productID: urbanpulse-events
  productVersion: "1.0.0"
  name:
    en: UrbanPulse Events Data Product
  description:
    en: Data product providing event information for urban analytics and citizen services.
  productModel:
    standard: ODPS
    version: "4.1"
    format: yaml
    $ref: ./odps.yaml
```

| `kind` value | Object schema |
| --- | --- |
| `productReference` | ProductReference |
| `useCase` | UseCase |
| `businessObjective` | BusinessObjective |
| `signal` | Signal |
| `domain` | Domain |
| `dataset` | Dataset |
| `api` | API |
| `policy` | Policy |
| `workflow` | Workflow |
| `agent` | Agent |
| `capability` | Capability |
| `strategicOpportunity` | StrategicOpportunity |

Standalone catalog-item files use a root `node` object. Inside a full catalog, use the same object directly in `catalog.nodes` without the extra root wrapper.

## Shared metadata for new ODPG-aligned nodes

The `domain`, `dataset`, `api`, `policy`, `workflow`, `agent`, `capability`, and `strategicOpportunity` nodes may use the following common optional attributes. They describe the node itself; links to other nodes belong in ODPG edges.

| Attribute | Type | Description |
| --- | --- | --- |
| `owner` | object | Accountable organization, team, and role. |
| `owner.organization` | string | Accountable organization. |
| `owner.team` | string | Accountable team. |
| `owner.role` | string | Accountable role. |
| `status` | string | Catalog lifecycle: `draft`, `active`, `deprecated`, or `retired`. |
| `$ref` | string | Authoritative external definition. |
| `tags` | array of strings | Search and filtering labels. |
