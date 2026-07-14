# Setup For Claude

This repository is designed as a Descrybe Legal Engine-first workflow pack for Claude-style skills and MCP connectors.

## Prerequisites

- Access to an AI client that supports MCP connectors.
- A Claude surface that supports custom skills, with code execution enabled if
  that surface requires it for skills.
- Descrybe Legal Engine access.
- The Descrybe Legal Engine MCP server URL:

`https://mcp.descrybe.com/mcp`

## Install Shape

The initial workflow pack lives in:

`descrybe-legal-research/`

It contains:

- `.claude-plugin/plugin.json` - basic plugin metadata;
- `.mcp.json` - Descrybe Legal Engine connector configuration;
- `CLAUDE.md` - shared research profile and safety boundaries;
- `skills/*/SKILL.md` - workflow instructions.

The Claude `.mcp.json` uses Claude's `mcpServers` wrapper and the stable server
key `descrybe-legal-engine`.

## Connector Setup

Add Descrybe Legal Engine as a remote MCP connector:

```text
https://mcp.descrybe.com/mcp
```

Then enable the connector in the Claude conversation where you want to run the
workflow. The workflows should stop rather than continue from model memory if
the connector is unavailable.

## Skill Setup

If your Claude client supports plugin-style bundles, install the
`descrybe-legal-research/` pack directly.

If your Claude client only supports individual custom skills, upload each
workflow skill separately:

1. Choose one workflow folder, such as `skills/research-roadmap/`.
2. Create a ZIP whose top-level item is that folder, for example
   `research-roadmap/SKILL.md`.
3. Upload the ZIP as a custom skill.
4. Repeat for `authority-finder` and `citation-quote-auditor`.

Do not upload a bare `SKILL.md` at the ZIP root. The folder name should match
the `name` value in the skill's frontmatter.

## First Test Prompts

Try these after Descrybe Legal Engine is available:

- `/descrybe-legal-research:research-roadmap "habitability defense to nonpayment eviction in California"`
- `/descrybe-legal-research:authority-finder "California cases supporting habitability defects as a defense to nonpayment of rent"`
- `/descrybe-legal-research:citation-quote-auditor` with a short memo excerpt
  that includes case citations and quoted case language.

## Expected Behavior

The workflow should:

- check that Descrybe tools are available;
- use Descrybe for legal research and verification;
- label sources clearly;
- flag uncertainty and gaps;
- avoid giving legal advice.

If Descrybe Legal Engine is not connected, the workflow should stop and ask the
user to enable Descrybe Legal Engine rather than continuing from model memory.

## Smoke Test

For each installed skill:

1. Run the first test prompt.
2. Confirm the assistant checks for Descrybe tools before answering.
3. Confirm it labels Descrybe results separately from user-provided text.
4. Confirm it says when research is thin, unresolved, or needs human review.
