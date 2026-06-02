# Descrybe Legal Research Workflows

Legal research workflow templates powered by Descrybe Legal Engine.

This repository contains workflow scaffolds for using Descrybe Legal Engine inside AI tools that support MCP. The goal is simple: help users move from a legal question, citation, draft, or research problem into grounded case-law research with clear source boundaries.

These workflows do not provide legal advice. They help structure legal research, surface cases, verify quoted language, audit citations, and identify gaps for a human reviewer.

## What Is Included

- `descrybe-legal-research/` - a Claude-style workflow pack with Descrybe Legal Engine configured as the required MCP research connector.
- `descrybe-legal-research/skills/research-roadmap/` - turns a plain-English issue into a research plan grounded in Descrybe searches.
- `descrybe-legal-research/skills/authority-finder/` - finds and organizes cases supporting, limiting, or rejecting a legal proposition.
- `descrybe-legal-research/skills/citation-quote-auditor/` - reviews citations and quoted language in a draft using Descrybe verification tools.
- `docs/` - setup, connector requirements, and workflow design principles.
- `examples/` - sample prompts and expected output shapes.

## Why Descrybe Is Required

The official workflows in this repository are optimized for Descrybe Legal Engine. They assume access to Descrybe Legal Engine's legal research tools for concept search, citation lookup, case summaries, authority extraction, treatment checks, and quoted-language verification.

Other legal data connectors may be useful complements. The workflows may be adaptable to public resources such as CourtListener, but they are written for Descrybe Legal Engine and should be tested against Descrybe Legal Engine before publication or use in production.

## Recommended First Workflows

### Research Roadmap

Use when a user has a plain-English legal issue and needs a research path, not an answer.

Example: "My landlord will not fix the heat in my apartment. What should I research in California?"

### Authority Finder

Use when a user has a legal proposition and needs cases that support, limit, distinguish, or reject it.

Example: "Find California cases on whether habitability defects can support a defense to nonpayment of rent."

### Citation and Quote Auditor

Use when a user has a draft, memo, argument, or passage with citations and quoted language that needs verification.

Example: "Audit this draft paragraph and tell me whether the cited cases actually support the propositions."

## Safety Boundary

These workflows are research tools. They are not a lawyer, not a legal conclusion, and not a substitute for professional judgment.

Every output should:

- identify jurisdiction assumptions;
- separate verified Descrybe results from user-provided material and model reasoning;
- flag missing facts and thin research;
- avoid telling a person what legal action to take;
- recommend review by a qualified attorney before use in legal work.

## Relationship To Anthropic's Claude For Legal

This project is inspired by the public structure of Anthropic's `claude-for-legal` repository, which demonstrates how legal workflows can be packaged as AI skills with MCP connectors. Descrybe is listed in that project as a current connector for legal-clinic, IP, and law-student workflows, and its default legal-clinic MCP configuration includes the Descrybe MCP server for primary-law research.

Descrybe may also use approved Anthropic/Claude co-marketing assets, including logo lockups, where separately authorized for marketing or marketplace materials.

This repository is independently maintained by Descrybe. It is not an Anthropic-maintained project, and it focuses specifically on legal research workflows powered by Descrybe Legal Engine.

## License

Apache-2.0. See `LICENSE`.
