# Descrybe Legal Research Workflows

Legal research workflow templates powered by Descrybe Legal Engine.

This repository is the companion workflow layer for Descrybe Legal Engine. It
shows how lawyers, legal researchers, librarians, clinics, students, and AI
builders can use Descrybe inside assistants such as Claude, ChatGPT, Codex, and
Python-based research apps.

The goal is simple: help users move from a legal question, citation, draft, or
research problem into grounded case-law research with clear source boundaries.

These workflows do not provide legal advice. They help structure legal
research, surface cases, verify quoted language, audit citations, and identify
gaps for a human reviewer.

## How This Repo Fits With The Python SDK

Use this repository when you want repeatable legal research workflows,
assistant prompts, skills, examples, and plugin packaging.

Use
[`descrybe-legal-engine-python`](https://github.com/descrybe-com/descrybe-legal-engine-python)
when you are building an app or script that needs the Python client, CLI,
OAuth helpers, token storage, or runnable web-app example.

In short:

- **Descrybe Legal Engine** is the research source and MCP service.
- **The Python SDK** is the app-building layer.
- **This workflow repo** is the assistant-facing recipe book.

## What Is Included

- `descrybe-legal-research/` - a Claude-style workflow pack with Descrybe
  Legal Engine configured as the required MCP research connector.
- `descrybe-legal-research-openai/` - an OpenAI/ChatGPT/Codex plugin-style
  workflow pack that bundles skills with Descrybe MCP configuration.
- `descrybe-legal-research/skills/research-roadmap/` - turns a plain-English
  issue into a Descrybe-grounded research plan.
- `descrybe-legal-research/skills/authority-finder/` - finds and organizes
  cases supporting, limiting, or rejecting a legal proposition.
- `descrybe-legal-research/skills/citation-quote-auditor/` - reviews citations
  and quoted language in a draft.
- `docs/` - setup, connector requirements, surface guidance, and workflow
  design principles.
- `examples/` - sample prompts, expected output shapes, and lightweight Python
  SDK examples.

## Choose Your Path

### I Want To Use Claude

Start with [docs/setup-claude.md](docs/setup-claude.md). The Claude pack lives
in `descrybe-legal-research/`.

### I Want To Use ChatGPT, Codex, Or OpenAI Plugins

Start with [docs/setup-chatgpt.md](docs/setup-chatgpt.md). The OpenAI-oriented
plugin pack lives in `descrybe-legal-research-openai/`.

For local Codex or ChatGPT desktop testing, this repository also includes a
repo-local plugin marketplace at `.agents/plugins/marketplace.json`.

### I Want To Build A Python App

Start with [docs/setup-python-sdk.md](docs/setup-python-sdk.md), then use the
Python SDK repository for the actual package, CLI, and OAuth implementation.

### I Want To Understand The Product Architecture

Read [docs/assistant-surface-map.md](docs/assistant-surface-map.md). It explains
the difference between MCP tools, skills, plugins, prompts, and SDK examples.

### I Want To See The Public Tools

Read [docs/descrybe-legal-engine-tools.md](docs/descrybe-legal-engine-tools.md)
for a human-readable overview of the public Descrybe Legal Engine MCP tools and
their baseline parameters.

## Why Descrybe Is Required

The official workflows in this repository are optimized for Descrybe Legal
Engine. They assume access to Descrybe Legal Engine's legal research tools for
concept search, citation lookup, case summaries, authority extraction, treatment
checks, and quoted-language verification.

For a tool-level overview, see
[docs/descrybe-legal-engine-tools.md](docs/descrybe-legal-engine-tools.md).

Other legal data connectors may be useful complements. The workflows may be
adaptable to public resources such as CourtListener, but they are written for
Descrybe Legal Engine and should be tested against Descrybe Legal Engine before
publication or use in production.

## Recommended First Workflows

### Research Roadmap

Use when a user has a plain-English legal issue and needs a research path, not
an answer.

Example: "My landlord will not fix the heat in my apartment. What should I
research in California?"

### Authority Finder

Use when a user has a legal proposition and needs cases that support, limit,
distinguish, or reject it.

Example: "Find California cases on whether habitability defects can support a
defense to nonpayment of rent."

### Citation and Quote Auditor

Use when a user has a draft, memo, argument, or passage with citations and
quoted language that needs verification.

Example: "Audit this draft paragraph and tell me whether the cited cases
actually support the propositions."

## Safety Boundary

These workflows are research tools. They are not a lawyer, not a legal
conclusion, and not a substitute for professional judgment.

Every output should:

- identify jurisdiction assumptions;
- separate verified Descrybe results from user-provided material and model
  reasoning;
- flag missing facts and thin research;
- avoid telling a person what legal action to take;
- recommend review by a qualified attorney before use in legal work.

## Service Access

The workflow files in this repository are licensed under Apache 2.0. Access to
the hosted Descrybe Legal Engine service is separate and requires a Descrybe
account, applicable entitlement, OAuth consent, and compliance with Descrybe's
[Terms of Service](https://descrybe.com/legal/terms).

## Relationship To Anthropic's Claude For Legal

This project is inspired by the public structure of Anthropic's
`claude-for-legal` repository, which demonstrates how legal workflows can be
packaged as AI skills with MCP connectors. Descrybe is listed in that project as
a current connector for legal-clinic, IP, and law-student workflows, and its
default legal-clinic MCP configuration includes the Descrybe MCP server for
primary-law research.

Descrybe may also use approved Anthropic/Claude co-marketing assets, including
logo lockups, where separately authorized for marketing or marketplace
materials.

This repository is independently maintained by Descrybe. It is not an
Anthropic-maintained project, and it focuses specifically on legal research
workflows powered by Descrybe Legal Engine.

## License

Apache-2.0. See `LICENSE`.
