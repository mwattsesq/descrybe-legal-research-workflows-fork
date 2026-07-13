# Python SDK Examples

These examples use the
[`descrybe-legal-engine`](https://github.com/descrybe-com/descrybe-legal-engine-python)
Python package.

## Setup

```bash
python3 -m venv .venv
.venv/bin/python -m pip install descrybe-legal-engine
.venv/bin/dle login
```

`dle login` connects this local environment to your Descrybe account. Do not
paste Descrybe tokens into source code, prompts, or `.env` files.

## Run

```bash
.venv/bin/python research_roadmap_seed.py
```

The script performs a small Descrybe case-law concept search that can seed a
research-roadmap workflow.

## Shared App Note

This local example uses the current user's token store. A shared web app should
use per-user OAuth and encrypted server-side token storage instead.
