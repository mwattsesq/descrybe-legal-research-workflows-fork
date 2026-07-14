# Descrybe Legal Engine Tools

This is a human-readable overview of the public Descrybe Legal Engine MCP tools
used by these workflows.

For the live tool list available to a connected account, use the MCP client's
tool-listing feature or run `dle list-tools` with the
[`descrybe-legal-engine-python`](https://github.com/descrybe-com/descrybe-legal-engine-python)
package.

Use only the public tool names below in workflows and examples. Do not use
internal route names or backend aliases.

## Tool Groups

| Group | Tools |
| --- | --- |
| Research intake | `analyze_legal_question` |
| Search | `search_cases_by_concept`, `search_laws_and_rules`, `search_case_text` |
| Citation and reference resolution | `find_case_from_reference`, `extract_case_references` |
| Case reading | `get_case_summary`, `get_case_passages`, `get_case_details`, `get_case_pdf` |
| Treatment and citing cases | `check_case_status`, `find_cases_that_cite` |
| Quote verification | `verify_quote` |

## Canonical Case IDs

Known-case tools require a Descrybe canonical `case_id`, formatted like
`c1514149`. A `case_id` is returned by search, text search, reference lookup,
citation extraction, and citing-case results.

Reporter citations, docket numbers, opinion IDs, CourtListener IDs, and other
source identifiers are not Descrybe `case_id` values. If a workflow starts with
a citation or case name, resolve it with `find_case_from_reference` before
calling known-case tools.

## Public Tool Signatures

```text
analyze_legal_question(query)
search_cases_by_concept(term, jurisdiction?, sort?, search_focus?)
search_laws_and_rules(term, jurisdiction?, doc_type?)
search_case_text(term, jurisdiction?)
find_case_from_reference(reference, jurisdiction?, year?, court_hint?, docket_hint?, quote_hint?, context_text?)
extract_case_references(text, resolve?, section_policy?, max_references?)
get_case_summary(case_id, simplified?)
get_case_passages(case_id, focus)
get_case_details(case_id)
check_case_status(case_id, court?)
find_cases_that_cite(case_id)
verify_quote(case_id, quote)
get_case_pdf(case_id)
```

## Tool Purposes

### `analyze_legal_question`

Checks whether a broad legal research question is ready for research or would
benefit from clarification.

### `search_cases_by_concept`

Searches case law by legal concept, issue, doctrine, rule, claim, defense, fact
pattern, or topic. Results are authority-ranked by default.

Common parameters:

- `term` required.
- `jurisdiction` optional; defaults to `all`.
- `sort` optional: `authority` or `date`.
- `search_focus` optional: `general` or `legal_issue`.

### `search_laws_and_rules`

Searches non-case primary law, including statutes, regulations, and
constitutional provisions where available.

Common parameters:

- `term` required.
- `jurisdiction` optional; defaults to `all`.
- `doc_type` optional: `all`, `statute`, `regulation`, or `constitution`.

### `search_case_text`

Searches the full text of judicial opinions by exact words or phrases. Use this
for quotes, numbers, terms of art, or specific wording inside cases.

Common parameters:

- `term` required.
- `jurisdiction` optional; defaults to `all`.

### `find_case_from_reference`

Resolves a citation, case name, case caption, party name, docket number, short
cite, nearby reference text, or mixed legal reference into a Descrybe case or
candidate set.

Common parameters:

- `reference` required.
- `jurisdiction`, `year`, `court_hint`, `docket_hint`, `quote_hint`, and
  `context_text` optional.

### `extract_case_references`

Extracts case citations and case references from pasted legal text. With
`resolve: true`, resolved references include `case_id` when available.

Common parameters:

- `text` required.
- `resolve`, `section_policy`, and `max_references` optional.

### `get_case_summary`

Retrieves the precomputed summary for a known Descrybe case.

Common parameters:

- `case_id` required.
- `simplified` optional; use the standard summary for legal research unless the
  user asks for a simplified explanation.

### `get_case_passages`

Retrieves focused passages from a known Descrybe case. This is not a
full-opinion fetch.

Common parameters:

- `case_id` required.
- `focus` required.

### `get_case_details`

Retrieves structured metadata, summary availability, opinion inventory, and
treatment summary for a known Descrybe case.

Common parameters:

- `case_id` required.

### `check_case_status`

Checks a known Descrybe case for a quick treatment/status signal before relying
on it. This is not a full citing-case map or forum-specific binding analysis.

Common parameters:

- `case_id` required.
- `court` optional and usually omitted.

### `find_cases_that_cite`

Finds later cases that cite, treat, follow, distinguish, or discuss a known
case.

Common parameters:

- `case_id` required.

### `verify_quote`

Verifies whether quoted language appears in a known Descrybe case. Resolve the
case to a `case_id` before calling this tool.

Common parameters:

- `case_id` required.
- `quote` required.

### `get_case_pdf`

Creates or reuses a generated Descrybe case PDF asset and returns its public URL
or job metadata.

Common parameters:

- `case_id` required.

## Common Workflow Patterns

Research roadmap:

1. Use `analyze_legal_question` if the issue is broad or fact-dependent.
2. Use `search_cases_by_concept` for case-law paths.
3. Use `search_laws_and_rules` for relevant statutes or regulations.
4. Use `get_case_summary`, `get_case_passages`, or `get_case_details` for
   important cases.

Authority finder:

1. Use `search_cases_by_concept` for supporting authority.
2. Run additional searches for limiting, distinguishing, or adverse authority.
3. Use `check_case_status` and `find_cases_that_cite` for important cases.
4. Label thin or uncertain results plainly.

Citation and quote auditor:

1. Use `extract_case_references` with `resolve: true` for pasted draft text.
2. Use `find_case_from_reference` for unresolved or ambiguous citations.
3. Use `verify_quote` only after resolving a case to `case_id`.
4. Use `get_case_passages` or `get_case_summary` to compare the case against the
   draft proposition.
