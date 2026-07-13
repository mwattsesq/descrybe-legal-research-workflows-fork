# Setup For ChatGPT, Codex, And OpenAI Plugins

This repository includes an OpenAI-oriented workflow pack in:

```text
descrybe-legal-research-openai/
```

That pack is shaped as a plugin-style bundle: it includes a plugin manifest,
Descrybe MCP configuration, and reusable legal research skills.

## When To Use This Path

Use this path when you want ChatGPT, Codex, or another OpenAI plugin-capable
surface to run Descrybe-grounded legal research workflows.

Use the Python SDK instead when you are building your own app or script.

## What The Plugin Pack Contains

- `.codex-plugin/plugin.json` - plugin metadata and pointers to bundled parts;
- `.mcp.json` - Descrybe Legal Engine MCP server configuration;
- `skills/*/SKILL.md` - reusable workflow instructions;
- `README.md` - local testing notes and expected behavior.

## Local Marketplace Shape

This repository includes a repo-local marketplace file:

```text
.agents/plugins/marketplace.json
```

It points to:

```text
descrybe-legal-research-openai/
```

Use that marketplace for local testing in Codex or the ChatGPT desktop app
before preparing a public plugin submission.

## Local Install And Test Flow

Use this flow on OpenAI surfaces that support local plugin development or
repo-local plugin marketplaces:

1. Open the repository root so the app can see `.agents/plugins/marketplace.json`.
2. Install or enable the plugin named `Descrybe Legal Research`.
3. Confirm the plugin points to `descrybe-legal-research-openai/`.
4. Connect or authorize Descrybe Legal Engine when the surface asks for MCP
   access.
5. Run the first test prompts below.

If the local plugin does not appear, treat the OpenAI pack as source material
for manual/plugin-tool installation and do not submit it publicly until a local
install smoke test succeeds.

## Expected Behavior

The assistant should:

- use Descrybe Legal Engine for case-law research and verification;
- stop if Descrybe tools are unavailable;
- label Descrybe results separately from user-provided text and model
  reasoning;
- flag thin research and adverse authority;
- avoid giving legal advice.

## First Test Prompts

After the plugin pack is installed and Descrybe Legal Engine is connected, try:

```text
Use the Descrybe Legal Research plugin to build a research roadmap for implied
warranty of habitability as a defense to nonpayment eviction in California.
```

```text
Use Descrybe Legal Research to find supporting, limiting, and adverse California
authority for habitability defects as a defense to nonpayment of rent.
```

```text
Use Descrybe Legal Research to audit this draft paragraph for citation support
and quote accuracy:

Under California law, habitability obligations and rent obligations are mutually
dependent. Green v. Superior Court, 10 Cal. 3d 616 (1974).
```

## Notes For Public Submission

If Descrybe submits this as a public OpenAI plugin, prepare the submission from
the final plugin bundle rather than from an existing published app reference.

The review packet should include:

- public listing copy;
- website, support, privacy, and terms URLs;
- production MCP server URL;
- accurate tool metadata and annotations;
- starter prompts;
- five positive test cases;
- three negative test cases;
- country or region availability;
- release notes.

See [plugin-submission-checklist.md](plugin-submission-checklist.md) for a
working checklist.

Before submission, also confirm:

- the manifest has live website, support, privacy, and terms URLs;
- the MCP server uses the production Descrybe Legal Engine URL;
- the skills have been tested with connected and disconnected Descrybe states;
- positive and negative test cases include expected behavior, not only prompt
  text.
