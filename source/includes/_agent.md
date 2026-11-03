# ODPC Agent

The `Agent` object defines a reusable AI, automation, human, or organizational actor in an ODPC catalog. It aligns with the ODPG `Agent` node type. Interfaces, credentials, skills, tools, prompts, and run-time settings remain in the authoritative agent definition.

## Mandatory attributes and options

```yml
node:
  kind: agent
  id: AGENT-001
  name:
    en: Mobility Planning Assistant
  description:
    en: Automation actor that prepares planning recommendations.
```

| Attribute | Type | Required | Description |
| --- | --- | ---: | --- |
| `node` | object | ✓ | Top-level standalone node wrapper. |
| `kind` | string | ✓ | `agent`. |
| `id` | string | ✓ | Stable agent identifier. |
| `name` | language-tagged string | ✓ | Human-readable agent name. |
| `description` | language-tagged string | ✓ | Agent discovery description. |

## Optional attributes and options

```yml
node:
  kind: agent
  id: AGENT-001
  name:
    en: Mobility Planning Assistant
  description:
    en: Automation actor that prepares planning recommendations.
  type: ai
  version: "0.8.0"
  autonomy: supervised
  owner:
    organization: Example Transport Authority
    team: Urban Analytics
    role: Agent Owner
  status: active
  $ref: https://example.org/agents/mobility-planning-assistant
  tags: [planning, recommendations]
```

| Attribute | Type | Options | Description |
| --- | --- | --- | --- |
| `type` | string | `ai`, `automation`, `human`, `organization` | Nature of the acting entity. |
| `version` | string | optional | Version of the agent definition or implementation. |
| `autonomy` | string | `assistive`, `supervised`, `autonomous` | Degree to which the agent may act without human approval. |
| `owner` | object | optional | Accountable organization, team, and role. |
| `status` | string | `draft`, `active`, `deprecated`, `retired` | Catalog lifecycle status. |
| `$ref` | string | optional | Authoritative agent definition, such as an Agent Card. |
| `tags` | array of strings | optional | Discovery and filtering labels. |
