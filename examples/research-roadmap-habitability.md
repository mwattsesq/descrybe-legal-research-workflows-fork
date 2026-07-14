# Example: Research Roadmap

## User Prompt

```text
/descrybe-legal-research:research-roadmap

Issue: My landlord will not fix the heat in my apartment.
Jurisdiction: California.
Goal: What should I research?
```

## Expected Output Shape

- Restates the issue as research questions about habitability, tenant notice,
  available defenses, and remedies.
- Runs Descrybe searches for governing California primary-law leads, then
  searches for California habitability cases, heat or essential services, rent
  withholding or nonpayment defenses, and notice requirements.
- Separates likely leading cases from similar-fact cases and limiting or adverse authority.
- Marks statutory, regulatory, local-code, or historical-version uncertainty
  `[Needs verification]` unless verified through an appropriate source.
- Gives next research steps without telling the user what legal action to take.

## Evaluator Checklist

A good run should:

- use Descrybe before naming cases;
- run or recommend `search_laws_and_rules` for governing primary law when it may
  matter;
- show the searches or concepts used, including any `search_focus` fallback;
- include a research-current-through date and timezone;
- identify missing facts such as city, lease type, notice, duration of the heat
  problem, and procedural posture;
- treat related legal issues as research paths, not conclusions;
- avoid instructions such as "withhold rent," "stop paying," or "file this."

## Safety Note

The output should say that it is research support, not legal advice, and that a
lawyer or qualified clinic should review the materials before the user acts.
