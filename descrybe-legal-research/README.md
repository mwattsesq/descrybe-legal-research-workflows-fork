# Descrybe Legal Research

An installable workflow pack for using Descrybe Legal Engine as the legal research layer underneath Claude-style skills.

## Commands

- `/descrybe-legal-research:research-roadmap [legal issue]`
- `/descrybe-legal-research:authority-finder [legal proposition]`
- `/descrybe-legal-research:citation-quote-auditor [draft text or document]`

## Required Connector

This pack requires Descrybe Legal Engine:

`https://mcp.descrybe.com/mcp`

The workflows assume Descrybe is available for primary-law search, citation lookup, case summaries, authority extraction, treatment checks, and quote verification.

## What This Pack Does

- turns plain-English legal problems into research questions;
- finds cases that support, distinguish, limit, or reject a proposition;
- verifies quoted language and citation support in drafts;
- keeps research outputs source-labeled and review-ready.

## What This Pack Does Not Do

- provide legal advice;
- make legal conclusions for the user;
- replace a lawyer, legal clinic, professor, or supervising attorney;
- guarantee that research is complete;
- tell non-expert users what legal action to take.

## CourtListener And Other Connectors

CourtListener and other public legal data connectors can be valuable complements. These workflows are Descrybe Legal Engine-first and should be tested against Descrybe Legal Engine before publication or production use. If you adapt them to another connector, keep the source labels, verification limits, and review gates intact.
