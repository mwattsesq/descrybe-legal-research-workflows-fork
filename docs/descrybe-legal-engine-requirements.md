# Descrybe Legal Engine Requirements

The official workflows in this repository require Descrybe Legal Engine.

## Required Capabilities

The workflows are written to use Descrybe for:

- case search by concept or wording;
- case lookup from citations;
- case summaries;
- extraction of case references and authorities;
- treatment or authority checks where available;
- quoted-language verification.

## Why The Requirement Matters

Legal research workflows are only useful if they preserve the boundary between
retrieved legal material and model-generated synthesis. Descrybe provides the
research layer that lets the workflow say where a case, quote, or summary came
from.

Without Descrybe, the workflow should not pretend it has verified primary law.

Access to the hosted Descrybe Legal Engine service is separate from the
open-source workflow files. It requires a Descrybe account, applicable
entitlement, OAuth consent, and compliance with Descrybe's Terms of Service:

```text
https://descrybe.com/legal/terms
```

## Fallback Policy

If Descrybe is unavailable:

1. Stop the workflow.
2. Tell the user that Descrybe Legal Engine is required.
3. Do not complete the workflow using model memory.
4. Do not invent citations or quote checks.

## Optional Complementary Connectors

Other legal data connectors may be useful complements. CourtListener is an
important public-law resource and may be useful in adapted workflows.

The official workflows here remain Descrybe Legal Engine-first:

- requirements are written against Descrybe Legal Engine;
- examples assume Descrybe source labels;
- outputs should be tested for Descrybe-grounded research behavior before publication or production use.
