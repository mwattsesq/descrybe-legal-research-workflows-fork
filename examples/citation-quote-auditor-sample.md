# Example: Citation And Quote Auditor

## User Prompt

`/descrybe-legal-research:citation-quote-auditor`

Then paste a short draft paragraph:

> Under California law, habitability obligations and rent obligations are mutually dependent. Green v. Superior Court, 10 Cal. 3d 616 (1974). Courts have also recognized that serious housing defects may be raised in nonpayment proceedings.

## Expected Output Shape

- Extracts the citation and the propositions tied to it.
- Resolves the citation through Descrybe.
- Checks whether the cited case supports the stated proposition.
- Identifies whether any quoted language is exact, partial, or absent.
- Flags whether the second sentence needs additional authority.
- Recommends next research steps without rewriting the legal argument unless asked.

## Safety Note

The output should be an audit report. It should not say the draft is filing-ready.
