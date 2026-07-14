# Setup For Python SDK Examples

Use the Python SDK when you are building a local research agent, a firm tool, a
browser-based app, or another Python workflow that calls Descrybe Legal Engine.

The SDK lives in a separate repository:

```text
https://github.com/descrybe-com/descrybe-legal-engine-python
```

## Install

```bash
pip install descrybe-legal-engine
```

For a local single-user tool:

```bash
dle login
dle doctor
dle list-tools
```

`dle login` connects the current machine to the current user's Descrybe account.
Do not ask users to paste Descrybe tokens into prompts, source code, or `.env`
files.

## Minimal Python Shape

```python
from descrybe_legal_engine import LegalEngine

client = LegalEngine.from_token_store()

results = client.search_cases_by_concept(
    "implied warranty of habitability nonpayment eviction California",
    search_focus="general",
    sort="authority",
)
```

## Shared App Shape

For a web app or firm tool, each app user should connect their own Descrybe
account through OAuth. Store that user's Descrybe refresh token encrypted on
the server and load it only for that user's requests.

Do not use one shared Descrybe token for a whole team unless Descrybe has
separately approved that access model.

## Coding Assistant Instructions

If a coding assistant is building the app, use the SDK's instruction generator:

```bash
dle init-agent-instructions
```

Give the generated `DESCRYBE_LEGAL_ENGINE.md` file to the assistant. It explains
the safe OAuth pattern, the local-script pattern, the shared-app pattern, and a
validation checklist.

## How This Connects To The Workflows

The workflows in this repository describe the research behavior:

- how to turn a plain-English issue into research questions;
- how to look for support and adverse authority;
- how to audit case citations and quoted case language;
- how to label verified and unverified material.

The Python SDK gives your app the authenticated Descrybe access needed to run
those workflows in code.
