---
title: ODPC v1.1 AI Product Profile
---

# ODPC v1.1 AI Product Profile

`AIProduct` is a normative ODPC v1.1 product-definition profile and `aiProduct` is a first-class top-level catalog node. Both describe business identity, capabilities, governance, evaluation, operations, and references to implementation components. They do not define a new OAPS or ODPC-AI specification.

An AI product is listed in an ODPC catalog through `ProductReference` with `productCategory: ai_product`. Its `productModel.schema` identifies the validation structure; `productModel.$ref` identifies the actual AI product document. `type` remains available for finer product classification.

The profile does not replace the existing `Agent` catalog object. An agent is a component or actor; an AI product is the accountable business product. Use `implementationReferences` for agent cards, models, services, workflows, tools, and evaluations described by their own standards. Do not embed prompts, model weights, credentials, arbitrary agent configuration, or runtime orchestration.

ODPC describes objects and product metadata. ODPG describes portfolio relationships among business objectives, use cases, data products, AI products, and agents. Technical implementation references are not ODPG relationship edges.

See `/v1.1/examples/` for predictive, RAG, agentic, and hybrid product examples, and validate with `/schema/v1.1/ai-product.yaml`.
