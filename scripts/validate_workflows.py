#!/usr/bin/env python3
"""Lightweight regression checks for Descrybe Legal Research Workflows."""

from __future__ import annotations

import ast
import json
import re
import sys
import urllib.parse
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MCP_URL = "https://mcp.descrybe.com/mcp"
SKILL_PACKS = [
    ROOT / "descrybe-legal-research" / "skills",
    ROOT / "descrybe-legal-research-openai" / "skills",
]


def rel(path: Path) -> str:
    return str(path.resolve().relative_to(ROOT))


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def has_text(path: Path, phrase: str) -> bool:
    text = read(path)
    compact_text = re.sub(r"\s+", " ", text)
    compact_phrase = re.sub(r"\s+", " ", phrase)
    return phrase in text or compact_phrase in compact_text


def add_missing(errors: list[str], path: Path, phrase: str) -> None:
    if not has_text(path, phrase):
        errors.append(f"{rel(path)} is missing required text: {phrase!r}")


def add_present(errors: list[str], path: Path, phrase: str) -> None:
    if has_text(path, phrase):
        errors.append(f"{rel(path)} still contains forbidden text: {phrase!r}")


def check_json(errors: list[str]) -> None:
    for path in ROOT.rglob("*.json"):
        if ".git" in path.parts:
            continue
        try:
            json.loads(read(path))
        except json.JSONDecodeError as exc:
            errors.append(f"{rel(path)} has invalid JSON: {exc}")


def check_markdown_links(errors: list[str]) -> None:
    link_re = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
    for path in ROOT.rglob("*.md"):
        if ".git" in path.parts:
            continue
        for match in link_re.finditer(read(path)):
            href = match.group(1).strip()
            if (
                not href
                or href.startswith("#")
                or re.match(r"[a-zA-Z][a-zA-Z0-9+.-]*:", href)
            ):
                continue
            target_href = href.split("#", 1)[0]
            if not target_href:
                continue
            target = (path.parent / urllib.parse.unquote(target_href)).resolve()
            if not str(target).startswith(str(ROOT)) or not target.exists():
                errors.append(f"{rel(path)} links to missing local target: {href}")


def check_trailing_whitespace(errors: list[str]) -> None:
    suffixes = {".md", ".json", ".py", ".yml", ".yaml"}
    for path in ROOT.rglob("*"):
        if not path.is_file() or ".git" in path.parts or path.suffix not in suffixes:
            continue
        for lineno, line in enumerate(read(path).splitlines(), start=1):
            if line.rstrip(" \t") != line:
                errors.append(f"{rel(path)}:{lineno} has trailing whitespace")


def check_skill_metadata(errors: list[str]) -> None:
    seen: dict[str, set[str]] = {}
    frontmatter_re = re.compile(r"---\n(.*?)\n---\n", re.S)
    field_re = re.compile(r"^([A-Za-z0-9_-]+):\s*(.*)$", re.M)

    for pack in SKILL_PACKS:
        names: set[str] = set()
        for path in pack.rglob("SKILL.md"):
            text = read(path)
            match = frontmatter_re.match(text)
            if not match:
                errors.append(f"{rel(path)} is missing YAML-style frontmatter")
                continue
            fields = dict(field_re.findall(match.group(1)))
            name = fields.get("name", "").strip()
            description = fields.get("description", "").strip()
            names.add(name)
            if not name:
                errors.append(f"{rel(path)} is missing frontmatter name")
            if path.parent.name != name:
                errors.append(
                    f"{rel(path)} name {name!r} does not match folder {path.parent.name!r}"
                )
            if not description or len(description) > 200:
                errors.append(
                    f"{rel(path)} description length should be 1-200 chars, got {len(description)}"
                )
        seen[rel(pack.parent)] = names

    if len(set(map(tuple, (sorted(names) for names in seen.values())))) != 1:
        errors.append(f"skill packs expose different skill sets: {seen}")


def check_mcp_config(errors: list[str]) -> None:
    claude_path = ROOT / "descrybe-legal-research" / ".mcp.json"
    openai_path = ROOT / "descrybe-legal-research-openai" / ".mcp.json"
    claude = json.loads(read(claude_path))
    openai = json.loads(read(openai_path))

    claude_server = claude.get("mcpServers", {}).get("descrybe-legal-engine")
    if not claude_server:
        errors.append("Claude .mcp.json must use mcpServers.descrybe-legal-engine")
    else:
        if claude_server.get("type") != "http":
            errors.append("Claude MCP server type must be http")
        if claude_server.get("url") != MCP_URL:
            errors.append(f"Claude MCP server URL must be {MCP_URL}")

    openai_server = openai.get("mcp_servers", {}).get("descrybe-legal-engine")
    if not openai_server:
        errors.append("OpenAI .mcp.json must use mcp_servers.descrybe-legal-engine")
    else:
        if openai_server.get("type") != "http":
            errors.append("OpenAI MCP server type must be http")
        if openai_server.get("url") != MCP_URL:
            errors.append(f"OpenAI MCP server URL must be {MCP_URL}")

    for forbidden_key in ("mcpServers", "recommendedCategories"):
        if forbidden_key in openai:
            errors.append(f"OpenAI .mcp.json should not contain {forbidden_key!r}")


def check_required_semantics(errors: list[str]) -> None:
    common_required = [
        "This workflow requires Descrybe Legal Engine",
        "model memory",
        "legal research support, not legal advice",
        "Research current through",
        "Descrybe's service terms",
        "untrusted data",
    ]

    for pack in SKILL_PACKS:
        for path in pack.rglob("SKILL.md"):
            for phrase in common_required:
                add_missing(errors, path, phrase)

        roadmap = pack / "research-roadmap" / "SKILL.md"
        for phrase in (
            "search_laws_and_rules",
            "Governing Primary Law Leads",
            "historical-version",
        ):
            add_missing(errors, roadmap, phrase)

        authority = pack / "authority-finder" / "SKILL.md"
        for phrase in (
            "filing/tribunal",
            "search-ranking signal",
            "complete citator or forum-specific precedential analysis",
            "one combined confidence label",
        ):
            add_missing(errors, authority, phrase)
        for forbidden in (
            "Use this confidence rubric",
            "High: Descrybe resolves the case",
            "Confidence: [high/medium/low]",
        ):
            add_present(errors, authority, forbidden)

        auditor = pack / "citation-quote-auditor" / "SKILL.md"
        for phrase in (
            "It does not perform Bluebook review",
            "Coverage Summary",
            "Do not mark an item verified when the source text was unavailable",
            "Case Citation And Quote Audit",
        ):
            add_missing(errors, auditor, phrase)


def check_examples(errors: list[str]) -> None:
    old_example = ROOT / "examples" / "python-sdk" / "research_roadmap_seed.py"
    new_example = ROOT / "examples" / "python-sdk" / "case_search_seed.py"
    if old_example.exists():
        errors.append(f"{rel(old_example)} should be renamed to case_search_seed.py")
    if not new_example.exists():
        errors.append(f"{rel(new_example)} is missing")
        return
    try:
        ast.parse(read(new_example))
    except SyntaxError as exc:
        errors.append(f"{rel(new_example)} has invalid Python syntax: {exc}")
    add_missing(errors, new_example, 'search_focus="legal_issue"')
    add_missing(errors, ROOT / "examples" / "README.md", "python-sdk/case_search_seed.py")


def main() -> int:
    errors: list[str] = []
    check_json(errors)
    check_markdown_links(errors)
    check_trailing_whitespace(errors)
    check_skill_metadata(errors)
    check_mcp_config(errors)
    check_required_semantics(errors)
    check_examples(errors)

    if errors:
        print("Workflow validation failed:\n")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Workflow validation OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
