# Assistant Surface Map

Descrybe Legal Engine can show up in several different AI surfaces. The safest
way to keep the project understandable is to separate the research source, the
workflow instructions, and the app-building code.

## The Layers

### Descrybe Legal Engine

Descrybe Legal Engine is the source-grounding layer. It provides the legal
research tools through MCP and the hosted Descrybe service.

Use it for:

- case-law concept search;
- citation lookup;
- case summaries;
- authority and treatment checks;
- quoted-language verification;
- source-grounded research outputs.

### MCP Connector

The MCP connector is the tool layer. It should describe available tools clearly
and return structured legal research data.

For public tool names and baseline parameters, see
[descrybe-legal-engine-tools.md](descrybe-legal-engine-tools.md).

It should not contain a full legal research workflow in every tool description.
The tool should stay neutral and predictable.

### Skills

Skills are the workflow layer. A skill tells an assistant how to perform a
repeatable task with the available tools.

Use skills for:

- research roadmaps;
- authority maps;
- citation and quote audits;
- source-labeling rules;
- legal research safety boundaries;
- output formats.

### Plugins

Plugins are the installable packaging layer. A plugin can bundle skills, MCP
configuration, an app, or some combination of those pieces.

Use plugins when a workflow pack should be easier to install, share, test, or
submit for marketplace review.

### Python SDK

The Python SDK is the app-building layer. It helps developers build local tools,
web apps, and firm workflows that connect to Descrybe through per-user OAuth.

Use the Python SDK when you need:

- a Python client;
- CLI login and diagnostics;
- local token storage for single-user tools;
- per-user OAuth patterns for shared apps;
- a runnable example app.

## Recommended Split For This Repository

This repository should focus on assistant behavior:

- workflow instructions;
- Claude skills;
- ChatGPT/OpenAI plugin packaging;
- sample prompts;
- positive and negative test cases;
- lightweight Python examples that point to the SDK.

The Python SDK repository should remain the canonical home for package code,
OAuth helpers, token storage, and full application examples.

## Portable Core, Surface-Specific Adapters

The same legal research workflow can usually be shared across assistants, but
the packaging needs a surface-specific adapter.

For example, the core workflow for an authority map is portable:

1. Restate the legal proposition.
2. Ask for jurisdiction if missing.
3. Use Descrybe for case-law research.
4. Look for supporting, limiting, distinguishing, and adverse authority.
5. Label sources and gaps.
6. Return a research map, not legal advice.

The adapter changes by surface:

- Claude uses skill files and connector setup.
- ChatGPT and Codex use skills packaged in a plugin.
- Python uses the SDK directly.
- A custom app can use its own UI around the same research steps.

## Keep These Boundaries Visible

- Official workflows require Descrybe Legal Engine for verified case-law work.
- If Descrybe is unavailable, the workflow should stop instead of relying on
  model memory.
- These workflows support legal research. They do not provide legal advice.
- Each human user should use their own authorized Descrybe access.
- Do not use one user's Descrybe account as a shared team credential.
