# Descrybe Legal Research For OpenAI

An OpenAI plugin-style workflow pack for using Descrybe Legal Engine as the
legal research layer underneath ChatGPT, Codex, and plugin-capable OpenAI
surfaces.

## Related Python SDK

Use this pack when you want ChatGPT, Codex, or another OpenAI surface to run
assistant-facing legal research workflows. If you are building a Python app,
local agent, OAuth flow, or token-storage layer, use the
[Python SDK](https://github.com/descrybe-com/descrybe-legal-engine-python)
instead.

## What This Pack Contains

- `.codex-plugin/plugin.json` - plugin metadata;
- `.mcp.json` - Descrybe Legal Engine MCP configuration;
- `skills/*/SKILL.md` - reusable research workflow instructions.

## Required Connector

This pack requires Descrybe Legal Engine:

```text
https://mcp.descrybe.com/mcp
```

If Descrybe Legal Engine is unavailable, the skills should stop rather than
complete verified case-law research from model memory.

## Included Skills

- `research-roadmap` - turns a plain-English legal issue into a
  Descrybe-grounded research plan.
- `authority-finder` - finds supporting, limiting, distinguishing, and adverse
  authority.
- `citation-quote-auditor` - audits citations, quoted language, and
  citation-support issues.

## First Test Prompts

```text
Use Descrybe Legal Research to build a research roadmap for implied warranty of
habitability as a defense to nonpayment eviction in California.
```

```text
Use Descrybe Legal Research to find supporting, limiting, and adverse California
cases on habitability defects as a defense to nonpayment of rent.
```

```text
Use Descrybe Legal Research to audit this draft paragraph for citation support:

Under California law, habitability obligations and rent obligations are mutually
dependent. Green v. Superior Court, 10 Cal. 3d 616 (1974).
```

## Safety Boundary

This pack supports legal research. It does not provide legal advice, make legal
conclusions for the user, replace attorney review, or guarantee that research is
complete.
