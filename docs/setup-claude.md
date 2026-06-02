# Setup For Claude

This repository is designed as a Descrybe Legal Engine-first workflow pack for Claude-style skills and MCP connectors.

## Prerequisites

- Access to an AI client that supports MCP connectors.
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

## First Test Prompts

Try these after Descrybe Legal Engine is available:

- `/descrybe-legal-research:research-roadmap "habitability defense to nonpayment eviction in California"`
- `/descrybe-legal-research:authority-finder "California cases supporting habitability defects as a defense to nonpayment of rent"`
- `/descrybe-legal-research:citation-quote-auditor` with a short memo excerpt that includes citations and quotes.

## Expected Behavior

The workflow should:

- check that Descrybe tools are available;
- use Descrybe for legal research and verification;
- label sources clearly;
- flag uncertainty and gaps;
- avoid giving legal advice.

If Descrybe Legal Engine is not connected, the workflow should stop and ask the user to enable Descrybe Legal Engine rather than continuing from model memory.
