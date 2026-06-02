---
name: authority-finder
description: Find and organize Descrybe case-law authority for a legal proposition, including supporting, limiting, distinguishing, and adverse cases.
argument-hint: "[legal proposition, jurisdiction, and factual context]"
---

# /authority-finder

Find and organize case-law authority using Descrybe Legal Engine.

## Required Connector Check

Before searching, confirm that Descrybe Legal Engine MCP tools are available. If Descrybe Legal Engine is unavailable, stop and say:

"This workflow requires Descrybe Legal Engine. Please enable Descrybe Legal Engine, then run the workflow again."

Do not rely on model memory for case citations.

## Workflow

### 1. Parse The Proposition

Restate the proposition in a researchable form.

Identify:

- jurisdiction;
- legal doctrine;
- relevant facts;
- procedural posture;
- whether the user wants supporting authority, adverse authority, or both.

If needed, ask up to three clarifying questions.

### 2. Search With Descrybe

If the proposition is framed as a specific legal issue, doctrine, or rule, start with Descrybe's case concept search using `search_focus: "legal_issue"`. Use ordinary concept searches for narrower fact-specific variants, opposing formulations, and broader doctrine-level checks.

Run Descrybe searches for:

- the proposition in the user's words;
- key terms of art;
- likely opposing formulations;
- narrower fact-specific variants;
- broader doctrine-level variants.

### 3. Classify Results

Classify each useful case as:

- supporting;
- limiting;
- distinguishing;
- adverse;
- background;
- not useful.

Use Descrybe summaries, treatment signals, and available authority data to avoid overstating a case.

### 4. Return A Balanced Authority Map

For each important case, include:

- case name and citation or Descrybe case identifier;
- source label `[Descrybe]`;
- jurisdiction and court, when available;
- short proposition supported or rejected;
- why it matters;
- treatment or caution notes if available;
- confidence level: high, medium, or low.

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

- Do not call a case controlling unless Descrybe results and jurisdiction support that label.
- Do not hide adverse authority.
- Do not convert a research conclusion into advice about what the user should do.
- If the authority is thin, say so plainly.
