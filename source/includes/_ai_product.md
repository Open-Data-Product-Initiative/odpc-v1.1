# ODPC AIProduct

The `AIProduct` object defines an accountable AI product as a first-class Top-level ODPC object in a catalog. It is distinct from `Agent`: an agent is a component or actor, while an AI product owns the business purpose, governance, evaluation, operations, and implementation references for the product as a whole.

Use `AIProduct` for predictive, generative, RAG, agentic, hybrid, and other AI products. Use ODPG for relationships between the product, business objectives, use cases, data products, and agents. Use external specifications for detailed model, Agent Card, workflow, tool, service, and evaluation definitions.

## Mandatory attributes and options

```yml
node:
  kind: aiProduct
  id: AI-001
  productID: procurement-review-assistant
  productVersion: "1.0.0"
  name:
    en: Procurement Review Assistant
  description:
    en: Prepares procurement review material for accountable human decision makers.
  purpose:
    en: Reduce review preparation effort without delegating approval authority.
  owner:
    organization: Example Authority
    team: Procurement
    role: AI Product Owner
  productType: agentic
  governance:
    autonomyLevel: supervised
    humanOversight: required
    consequentialActionApproval: required
    riskClassification: high
  evaluation:
    - id: EVIDENCE-COVERAGE
      name: Evidence coverage
```

| Attribute | Type | Required | Description |
| --- | --- | ---: | --- |
| `node.kind` | string | ✓ | `aiProduct`. |
| `id` | string | ✓ | Stable ODPC catalog object identifier. |
| `productID` / `productVersion` | string | ✓ | Stable identity and version of the AI product. |
| `name`, `description`, `purpose` | language-tagged string | ✓ | Business identity and purpose. |
| `owner` | object | ✓ | Accountable organization, team, and role. |
| `productType` | string | ✓ | `predictive`, `generative`, `rag`, `agentic`, `hybrid`, or `other`. |
| `governance` | object | ✓ | Product autonomy, human oversight, consequential-action approval, and risk. |
| `evaluation` | array | ✓ | Measurable evaluation requirements, not observed results. |

## Optional attributes and implementation references

```yml
node:
  kind: aiProduct
  id: AI-001
  productID: procurement-review-assistant
  productVersion: "1.0.0"
  name: {en: Procurement Review Assistant}
  description: {en: Prepares procurement review material.}
  purpose: {en: Support accountable procurement review.}
  owner: {organization: Example Authority, team: Procurement, role: AI Product Owner}
  productType: agentic
  governance: {autonomyLevel: supervised, humanOversight: required, consequentialActionApproval: required, riskClassification: high}
  evaluation: [{id: EVIDENCE-COVERAGE, name: Evidence coverage}]
  capabilities:
    - id: CAP-PROCUREMENT-REVIEW
      name: {en: Procurement review preparation}
      description: {en: Identifies evidence gaps for analyst review.}
  operations:
    lifecycleStatus: pilot
  implementationReferences:
    - role: agent_card
      standard: A2A Agent Card
      version: "0.3"
      format: json
      $ref: ./components/procurement-agent-card.json
```

`implementationReferences` identify externally governed technical components. `schema` identifies a referenced content structure and `$ref` identifies the referenced content instance. Do not embed prompts, credentials, model weights, arbitrary agent configuration, deployment configuration, runtime orchestration, or ODPG relationships in `AIProduct`.
