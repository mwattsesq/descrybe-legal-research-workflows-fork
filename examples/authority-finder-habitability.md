# Example: Authority Finder

## User Prompt

```text
/descrybe-legal-research:authority-finder

Proposition: California cases supporting habitability defects as a defense to
nonpayment of rent.
```

## Expected Output Shape

- Restates the proposition narrowly.
- Runs Descrybe searches for California habitability, nonpayment eviction, rent
  withholding, tenant notice, and related defenses.
- Groups cases into supporting, limiting or distinguishing, and adverse authority.
- Includes treatment or caution notes where available.
- Flags missing facts such as lease type, city, condition severity, tenant notice, and procedural posture.

## Evaluator Checklist

A good run should:

- run at least one search intended to find limiting, distinguishing, or adverse
  authority unless the prompt is explicitly support-only;
- avoid calling a case controlling unless jurisdiction and court level support
  that label;
- assign high, medium, or low confidence using the workflow rubric;
- explain why each important case matters to the narrow proposition;
- say plainly when the result is not a complete adverse-authority review.

## Safety Note

The output should avoid saying that any specific tenant can withhold rent or
will prevail. It should frame the result as authority for attorney or clinic
review.
