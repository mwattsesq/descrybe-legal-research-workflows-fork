"""Seed a research-roadmap workflow with Descrybe Legal Engine results.

Run after:

    pip install descrybe-legal-engine
    dle login

This example uses the local token profile for a single-user tool. Shared apps
should use per-user OAuth and encrypted server-side token storage instead.
"""

from __future__ import annotations

import json

from descrybe_legal_engine import LegalEngine


def main() -> None:
    client = LegalEngine.from_token_store()

    results = client.search_cases_by_concept(
        "implied warranty of habitability nonpayment eviction California",
        search_focus="general",
        sort="authority",
        limit=5,
    )

    print(json.dumps(results, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
