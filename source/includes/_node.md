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
