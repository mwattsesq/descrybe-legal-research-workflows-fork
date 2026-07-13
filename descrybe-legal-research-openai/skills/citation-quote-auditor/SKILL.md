---
name: citation-quote-auditor
description: Audit draft legal text with Descrybe for citations, quotes, and support.
argument-hint: "[draft text, memo excerpt, or document]"
---

# Citation And Quote Auditor

Audit citations and quoted case language using Descrybe Legal Engine.

## Required Connector Check

Before auditing, confirm that Descrybe Legal Engine MCP tools are available.
If Descrybe Legal Engine is unavailable, stop and say:

"This workflow requires Descrybe Legal Engine. Please enable Descrybe Legal
Engine, then run the workflow again."

Do not verify quotes or case support from model memory.

## Workflow

1. Identify whether the user wants a quick citation check, quote verification,
   support analysis, adverse-treatment review, or a full audit.
2. If the user does not specify, run a full audit on the provided excerpt.
3. Extract case citations, quoted language, propositions tied to citations, and
   incomplete or malformed citations. Label extracted items `[User provided]`.
4. Run `extract_case_references` with `resolve: true` when available. If that
   tool is unavailable, extract citations manually and resolve each one with
   `find_case_from_reference`.
5. For unresolved, short-form, or ambiguous references, call
   `find_case_from_reference` with nearby draft text as `context_text` and
   quoted language as `quote_hint` when available.
6. Preserve the Descrybe `case_id` for resolved cases. Do not pass reporter
   citations, docket numbers, CourtListener IDs, or opinion IDs to known-case
   tools that require a Descrybe `case_id`.
7. For each quote attributed to a resolved case, call `verify_quote`. If the
   quote is too long or no match is found, retry once with a shorter exact
   excerpt of about 8-25 words and report both attempts.
8. Compare each draft proposition against `get_case_details`,
   `get_case_passages`, summaries, or treatment fields returned by Descrybe.
9. Call `check_case_status` for important resolved cases. Use
   `find_cases_that_cite` when the user requested adverse-treatment review or
   Descrybe returns caution signals.
10. Classify each citation as supporting, partially supporting, not clearly
    supporting, quote mismatch, unresolved, treatment caution, or needs human
    review.
11. Group issues by severity and focus on what matters for human review.

## Severity And Edge Cases

- High: material quote mismatch; cited case resolves to the wrong authority; key
  proposition is unsupported; unresolved citation is central to the draft; or
  treatment signals could materially affect reliance.
- Medium: partial support; overbroad parenthetical; ambiguous short cite;
  missing pinpoint support; unclear jurisdiction or procedural posture.
- Low: minor citation-form issue, redundant citation, or low-stakes uncertainty.
- Assess multiple citations in one sentence separately.
- Resolve short cites, "id.", and "supra" references using nearby context.
- Report quote accuracy and proposition support separately; an exact quote may
  still fail to support the proposition.

## Output Format

Use this structure:

```markdown
# Citation And Quote Audit

**Review note:** This is legal research support, not legal advice. A qualified
attorney should review all citations, quotations, and legal conclusions before
filing, sending, or relying on the draft.

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
- Preserve a clear distinction between verification results and editorial
  suggestions.
