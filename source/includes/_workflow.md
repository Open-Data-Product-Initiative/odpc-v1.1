# ODPC Workflow

The `Workflow` object defines a reusable business or technical workflow in an ODPC catalog. It aligns with the ODPG `Workflow` node type. Workflow steps, participants, dependencies, and input/output relationships remain in the authoritative workflow definition and ODPG.

## Mandatory attributes and options

```yml
node:
  kind: workflow
  id: WF-001
  name:
    en: Incident Response Workflow
  description:
    en: Operational workflow for responding to major traffic incidents.
```

| Attribute | Type | Required | Description |
| --- | --- | ---: | --- |
| `node` | object | ✓ | Top-level standalone node wrapper. |
| `kind` | string | ✓ | `workflow`. |
| `id` | string | ✓ | Stable workflow identifier. |
| `name` | language-tagged string | ✓ | Human-readable workflow name. |
| `description` | language-tagged string | ✓ | Workflow discovery description. |

## Optional attributes and options

| Attribute | Type | Options | Description |
| --- | --- | --- | --- |
| `type` | string | `business`, `operational`, `data`, `automation` | Primary workflow purpose. |
| `trigger` | string | `manual`, `schedule`, `event`, `api` | How the workflow starts. |
| `version` | string | optional | Version of the workflow definition. |
| `owner` | object | optional | Accountable organization, team, and role. |
| `status` | string | `draft`, `active`, `deprecated`, `retired` | Catalog lifecycle status. |
| `$ref` | string | optional | Authoritative workflow definition, such as BPMN or an orchestration definition. |
| `tags` | array of strings | optional | Discovery and filtering labels. |
