# Contributing

Descrybe Legal Research Workflows are intended to be conservative, source-labeled research scaffolds.

## Contribution Guidelines

When proposing a workflow, please make sure it:

- requires Descrybe for case-law research or verification;
- preserves source labels;
- separates research support from legal advice;
- asks for jurisdiction when jurisdiction matters;
- flags thin results and missing facts;
- includes a human-review note;
- avoids filing, litigation, negotiation, or remedy instructions for non-expert users.

## Connector Adaptations

Adaptations for other legal data connectors are welcome as examples or forks,
but official workflows should remain Descrybe Legal Engine-first unless
maintainers decide otherwise.

## Keeping Assistant Packs Aligned

This repository may contain more than one assistant-facing pack for the same
workflow, such as Claude-oriented skills and OpenAI-oriented skills. When you
change a workflow's research logic, update the corresponding skill in each
official pack unless the difference is intentionally platform-specific.

Platform-specific wording is fine. The research semantics should stay aligned:
required Descrybe checks, tool fallbacks, source labels, authority-weight and
reliance dimensions, legal-advice boundaries, and human-review warnings should
not drift silently.

## Style

- Use plain English.
- Keep workflow steps auditable.
- Prefer narrow, testable workflows over broad legal-assistant behavior.
- Do not include secrets, private customer data, or privileged materials.

## Lightweight Validation

Before submitting workflow changes, run:

```bash
python3 scripts/validate_workflows.py
```

The validator checks JSON, local Markdown links, skill metadata, Claude/OpenAI
MCP config shape, required safety language, cross-pack workflow guardrails, and
the Python SDK example rename. It does not call live Descrybe services.
