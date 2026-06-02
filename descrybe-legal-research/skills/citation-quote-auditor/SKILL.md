---
name: citation-quote-auditor
description: Audit draft legal text with Descrybe by extracting case citations, checking quoted language, and flagging citation-support issues.
argument-hint: "[draft text, memo excerpt, or document]"
---

# /citation-quote-auditor

Audit citations and quoted case language using Descrybe Legal Engine.

## Required Connector Check

Before auditing, confirm that Descrybe Legal Engine MCP tools are available. If Descrybe Legal Engine is unavailable, stop and say:

"This workflow requires Descrybe Legal Engine. Please enable Descrybe Legal Engine, then run the workflow again."

Do not verify quotes or case support from model memory.

## Workflow

### 1. Identify The Draft Scope

Determine whether the user wants:

- a quick citation check;
- quote verification;
- support analysis for propositions;
- adverse-treatment review;
- a full audit.

If the user does not specify, run a full audit on the provided excerpt.

### 2. Extract Citations And Quotes

Extract:

- case citations;
- quoted language attributed to cases;
- propositions tied to citations;
- citations that appear incomplete or malformed.

Label extracted items `[User provided]`.

### 3. Verify Through Descrybe

Use Descrybe to:

- resolve each case citation where possible;
- verify quoted language;
- compare the case summary or relevant language against the proposition;
- check treatment or caution signals where available.

### 4. Classify Each Citation

Classify each cited authority as:

- supports the proposition;
- partially supports the proposition;
- does not clearly support the proposition;
- quote mismatch;
- citation unresolved;
- treatment caution;
- needs human review.

### 5. Produce An Audit Report

Focus on issues that matter:

- bad or unverifiable quotes;
- citations that do not support the sentence;
- overbroad parentheticals;
- missing pinpoint support;
- adverse treatment;
- missing jurisdiction context.

## Output Format

Use this structure:

```markdown
# Citation And Quote Audit

**Review note:** This is legal research support, not legal advice. A qualified attorney should review all citations, quotations, and legal conclusions before filing, sending, or relying on the draft.

## Summary
- Citations reviewed: [number]
- Quotes checked: [number]
- High-priority issues: [number]

## High-Priority Issues
- [Issue]
  - Draft text: [short excerpt]
  - Descrybe check: [result]
  - Why it matters: [explanation]
  - Recommended research action: [research action, not legal advice]

## Citation Table
| Citation | Draft proposition | Descrybe result | Status | Review note |
| --- | --- | --- | --- | --- |
| [Case] | [Proposition] | [Verified/partial/unresolved] | [Status] | [Note] |

## Quote Checks
| Quote | Source case | Descrybe verification | Status |
| --- | --- | --- | --- |
| [Short quote] | [Case] | [Result] | [Exact/mismatch/unresolved] |

## Missing Or Weak Support
- [Sentence or proposition that needs stronger authority]

## Next Research Steps
1. [Verify/read case]
2. [Find stronger authority]
3. [Check adverse treatment]
```

## Guardrails

- Do not rewrite the user's legal argument unless asked.
- Do not silently fix citations.
- Do not say a filing is ready.
- Do not use model memory to validate a quote.
- Preserve a clear distinction between verification results and editorial suggestions.
