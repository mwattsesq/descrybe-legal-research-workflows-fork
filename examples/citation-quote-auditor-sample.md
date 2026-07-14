# Example: Case Citation And Quote Auditor

## User Prompt

`/descrybe-legal-research:citation-quote-auditor`

Then paste a short draft paragraph:

> Under California law, habitability obligations and rent obligations are
> mutually dependent. Green v. Superior Court, 10 Cal. 3d 616 (1974). Courts
> have also recognized that serious housing defects may be raised in nonpayment
> proceedings.

## Expected Output Shape

- Extracts the citation and the propositions tied to it.
- Resolves the citation through Descrybe.
- Checks whether the cited case supports the stated proposition.
- Identifies whether any quoted language is exact, partial, or absent.
- Reports coverage counts, including citations found, resolved, checked, and
  unable to check.
- Separates source-text availability, quote accuracy, and proposition support.
- Flags whether the second sentence needs additional authority.
- Recommends next research steps without rewriting the legal argument unless asked.

## Evaluator Checklist

A good run should:

- resolve `Green v. Superior Court, 10 Cal. 3d 616 (1974)` through Descrybe
  before assessing support;
- preserve and use the Descrybe `case_id` for known-case checks when available;
- report quote accuracy separately from proposition support;
- avoid marking anything verified when source text was unavailable;
- state whether the quoted or relied-on language appears in a majority opinion,
  separate opinion, quoted source, or unknown context when available;
- mark the uncited second sentence as missing or weak support unless Descrybe
  verifies adequate authority;
- include a research-current-through date and timezone;
- classify issues by severity and explain what a human reviewer should check
  next.

## Safety Note

The output should be an audit report. It should not say the draft is filing-ready.
