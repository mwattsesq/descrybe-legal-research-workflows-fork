---
name: research-roadmap
description: Build a Descrybe-grounded legal research roadmap from a plain-English legal issue, including research questions, case-law paths, and gaps.
argument-hint: "[plain-English legal issue and jurisdiction, if known]"
---

# /research-roadmap

Build a legal research roadmap using Descrybe Legal Engine as the required research layer.

## Required Connector Check

Before producing the roadmap, confirm that Descrybe Legal Engine MCP tools are available. If Descrybe Legal Engine is unavailable, stop and say:

"This workflow requires Descrybe Legal Engine. Please enable Descrybe Legal Engine, then run the workflow again."

Do not substitute model memory or general web search for Descrybe results.

## Workflow

### 1. Frame The Research Question

Restate the user's issue as one or more legal research questions.

If facts or jurisdiction are missing, ask up to three clarifying questions before searching. Prioritize:

- jurisdiction;
- forum or court level, if relevant;
- procedural posture;
- key facts that change the legal issue.

If the user cannot answer, continue with explicit assumptions.

### 2. Translate The Issue Into Descrybe Searches

Create targeted Descrybe search concepts from the user's plain-English issue.

When the user supplies a specific legal issue, doctrine, rule, or issue label, use Descrybe's case concept search with `search_focus: "legal_issue"` for the first selected-issue search. Use ordinary concept searches for broader fact patterns, opposing formulations, and follow-up variants.

For each search, record:

- the concept or wording searched;
- jurisdiction filters or assumptions;
- why the search matters.

### 3. Retrieve Case-Law Leads

Use Descrybe to find relevant cases and summaries. Group results by research value:

- likely leading cases;
- cases that apply the rule to similar facts;
- cases that limit, distinguish, or reject the proposition;
- cases that are useful background but not directly on point.

If Descrybe returns related legal issues from a legal-issue-focused search, treat them as research paths to consider rather than legal conclusions.

### 4. Build The Roadmap

Produce a roadmap with:

- research question;
- jurisdiction assumptions;
- issue map;
- Descrybe searches run;
- case-law leads;
- likely statutory or regulatory areas to check, clearly marked `[Needs verification]` unless independently verified;
- missing facts;
- gaps and cautions;
- next research steps.

### 5. Non-Expert Boundary

If the user appears to be a non-expert or self-represented person, avoid action instructions. Translate the issue into research topics and explain what a legal professional or clinic should review.

## Output Format

Use this structure:

```markdown
# Research Roadmap: [Issue]

**Review note:** This is legal research support, not legal advice. A qualified attorney or supervised legal clinic should review the research before anyone relies on it.

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
- Do not present unverified statutes, deadlines, remedies, or procedural steps as certain.
- Do not invent cases when Descrybe results are thin.
- Keep source labels visible.
