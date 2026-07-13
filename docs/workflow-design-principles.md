# Workflow Design Principles

These principles keep Descrybe Legal Research Workflows useful, truthful, and safe.

## Research Support, Not Legal Advice

Workflows help users research legal materials. They do not tell users what legal action to take.

Good:

- "Cases to review include..."
- "This proposition appears to need stronger authority..."
- "A lawyer should review whether this rule applies to your facts..."

Avoid:

- "You should file..."
- "You can withhold..."
- "You will win..."
- "This definitely applies..."

## Descrybe First

If a workflow requires case law, quotes, citation support, or authority checks,
it should use Descrybe. If Descrybe is unavailable, the workflow should stop.

## Source Labels Stay Visible

Source labels are part of the safety model. Final outputs should preserve labels
such as:

- `[Descrybe]`
- `[User provided]`
- `[Model reasoning]`
- `[Needs verification]`

## Adverse Authority Is Not Optional

When the workflow is asked for authority, it should look for support and friction:

- supporting cases;
- limiting cases;
- distinguishing cases;
- adverse cases;
- treatment concerns;
- factual mismatches.

## Thin Results Are A Result

If research is thin, say so. Do not fill gaps with invented citations,
overconfident summaries, or model memory.

## Non-Expert Users Need Translation, Not Advice

For non-expert users, translate facts into research topics and questions. Do not
give instructions about filings, deadlines, remedies, negotiations, or
litigation strategy.
