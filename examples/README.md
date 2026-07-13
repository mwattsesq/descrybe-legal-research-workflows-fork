# Examples

These examples show how the same Descrybe-grounded research workflows can appear
in different surfaces.

## Prompt Examples

- [research-roadmap-habitability.md](research-roadmap-habitability.md)
- [authority-finder-habitability.md](authority-finder-habitability.md)
- [citation-quote-auditor-sample.md](citation-quote-auditor-sample.md)

Use these with the Claude pack or the OpenAI plugin-style pack.

## How To Use These As Smoke Tests

For each example, run the prompt with Descrybe Legal Engine connected and check
the output against the evaluator checklist in the example file. A passing run
should:

- use Descrybe tools before making case-law claims;
- name the Descrybe searches or checks it ran;
- keep user-provided text separate from Descrybe results;
- identify thin, unresolved, or ambiguous research instead of smoothing it over;
- include the review note that the output is legal research support, not legal
  advice.

Then run one disconnected test by disabling Descrybe Legal Engine. A passing
disconnected run should stop and ask the user to enable Descrybe Legal Engine
rather than continuing from model memory.

## Python SDK Examples

- [python-sdk/research_roadmap_seed.py](python-sdk/research_roadmap_seed.py)

Use these when you want to build a Python app or local research agent with the
`descrybe-legal-engine` package.
