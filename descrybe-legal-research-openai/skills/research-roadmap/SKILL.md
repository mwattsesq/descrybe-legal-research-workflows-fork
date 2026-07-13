---
name: research-roadmap
description: Build a Descrybe-grounded legal research roadmap from a plain-English legal issue.
argument-hint: "[plain-English legal issue and jurisdiction, if known]"
---

# Research Roadmap

Build a legal research roadmap using Descrybe Legal Engine as the required
research layer.

## Required Connector Check

Before producing the roadmap, confirm that Descrybe Legal Engine MCP tools are
available. If Descrybe Legal Engine is unavailable, stop and say:

"This workflow requires Descrybe Legal Engine. Please enable Descrybe Legal
Engine, then run the workflow again."

Do not substitute model memory or general web search for Descrybe results.

## Workflow

1. Restate the user's issue as one or more legal research questions.
2. If facts or jurisdiction are missing, ask up to three clarifying questions.
3. Translate the issue into targeted Descrybe search concepts.
4. If the user supplies a specific legal issue, doctrine, rule, or issue label,
   start with `search_cases_by_concept` using `search_focus: "legal_issue"`.
   If the tool rejects or does not support `search_focus`, rerun the same search
   as an ordinary concept search and note the fallback.
5. Use ordinary concept searches for broader fact patterns, opposing
   formulations, and follow-up variants.
6. Group case-law leads by research value: likely leading cases, similar-fact
   cases, limiting or adverse cases, and useful background.
7. Mark statutes, regulations, deadlines, or procedural rules
   `[Needs verification]` unless independently verified.
8. Return a research roadmap, not legal advice.

## Output Format

Use this structure:

```markdown
# Research Roadmap: [Issue]

**Review note:** This is legal research support, not legal advice. A qualified
attorney or supervised legal clinic should review the research before anyone
relies on it.

## Research Question
[Restated research question.]

## Jurisdiction And Assumptions
[Known jurisdiction, assumed jurisdiction, or missing jurisdiction.]

## Descrybe Searches Run
- [Search/concept] - [why it was run]

## Issue Map
- [Legal concept]
- [Sub-issue]
- [Factual trigger]

## Case-Law Leads
### Likely Leading Cases
- [Case] [Descrybe] - [why it matters]

### Similar-Fact Cases
- [Case] [Descrybe] - [why it matters]

### Limiting Or Adverse Cases
- [Case] [Descrybe] - [why it matters]

## Other Sources To Check
- [Statute/regulation/practice guide] [Needs verification]

## Gaps And Cautions
- [Missing fact, thin results, jurisdiction issue, treatment concern]

## Next Research Steps
1. [Next search or verification step]
2. [Next reading step]
3. [Question for attorney/supervisor]
```

## Guardrails

- Do not tell the user what legal action to take.
- Do not present unverified statutes, deadlines, remedies, or procedural steps
  as certain.
- Do not invent cases when Descrybe results are thin.
- Keep source labels visible.
