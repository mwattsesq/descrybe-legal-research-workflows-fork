---
name: authority-finder
description: Find and organize Descrybe case-law authority for a legal proposition.
argument-hint: "[legal proposition, jurisdiction, and factual context]"
---

# Authority Finder

Find and organize case-law authority using Descrybe Legal Engine.

## Required Connector Check

Before searching, confirm that Descrybe Legal Engine MCP tools are available.
If Descrybe Legal Engine is unavailable, stop and say:

"This workflow requires Descrybe Legal Engine. Please enable Descrybe Legal
Engine, then run the workflow again."

Do not rely on model memory for case citations.

## Workflow

1. Restate the proposition in a researchable form.
2. Identify jurisdiction, doctrine, relevant facts, procedural posture, and
   whether the user wants support, adverse authority, or both.
3. Ask up to three clarifying questions if needed.
4. If the proposition is framed as a specific legal issue, doctrine, or rule,
   start with `search_cases_by_concept` using `search_focus: "legal_issue"`.
   If the tool rejects or does not support `search_focus`, rerun the same search
   as an ordinary concept search and note the fallback.
5. Run Descrybe searches for the proposition in the user's words, key terms of
   art, likely opposing formulations, narrower fact variants, and broader
   doctrine-level variants.
6. Unless the user asks for supporting authority only, run at least one search
   designed to surface limiting, distinguishing, or adverse cases. If the user
   asks for supporting authority only, say that the result is not a full
   adverse-authority review.
7. Classify useful cases as supporting, limiting, distinguishing, adverse,
   background, or not useful.
8. Use Descrybe summaries, treatment signals, and available authority data to
   avoid overstating a case.

## Confidence Rubric

- High: Descrybe resolves the case, the court/jurisdiction fit the requested
  scope, the case directly supports or rejects the narrow proposition, and no
  visible treatment signal undermines the use described.
- Medium: the case is relevant but depends on factual fit, procedural posture,
  court level, dated authority, or treatment that should be reviewed before
  reliance.
- Low: the result is summary-only, jurisdiction is uncertain, the match is
  indirect, treatment is unclear, or Descrybe did not resolve enough detail to
  characterize the case safely.

## Output Format

Use this structure:

```markdown
# Authority Finder: [Proposition]

**Review note:** This is legal research support, not legal advice. Case law should be reviewed by a qualified attorney before use.

## Proposition
[Restated proposition.]

## Jurisdiction And Search Scope
[Jurisdiction, court level, date limits, assumptions.]

## Descrybe Searches Run
- [Search/concept] - [why it was run]

## Supporting Authority
- [Case] [Descrybe]
  - Supports: [narrow proposition]
  - Why it matters: [short explanation]
  - Caution: [treatment, factual distinction, or none found]
  - Confidence: [high/medium/low]

## Limiting Or Distinguishing Authority
- [Case] [Descrybe]
  - Limits/distinguishes: [point]
  - Why it matters: [short explanation]
  - Confidence: [high/medium/low]

## Adverse Authority
- [Case] [Descrybe]
  - Cuts against: [point]
  - Why it matters: [short explanation]
  - Confidence: [high/medium/low]

## Research Gaps
- [Thin area, missing jurisdiction, outdated result, treatment uncertainty]

## Recommended Next Searches
1. [Search]
2. [Search]
3. [Search]
```

## Guardrails

- Do not call a case controlling unless Descrybe results and jurisdiction
  support that label.
- Do not hide adverse authority.
- Do not convert a research conclusion into advice about what the user should
  do.
- If the authority is thin, say so plainly.
