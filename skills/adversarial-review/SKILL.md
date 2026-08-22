---
name: Adversarial review
description: Use after a researcher writes or revises a view, before that view is current.
---

# Adversarial review

Review a draft official view. Do not make the view current until this pass is clean. Do not open a pull request.

## Who runs it

A researcher starts a **fresh** subagent. Do not resume an old review subagent. The parent model is whatever the researcher is running unless the captain asked for a specific one.

The subagent starts blank. The dispatch must include the view path, the previous official view path if this is a revision, the related scout report path if any, and this entire prompt.

The subagent reads those files on the shared Grok Bot computer. It does not review a git branch and does not need a forge CLI.

## Prompt

<Use this as the subagent task. Fill the context fields.>

Review the research view and return structured findings with a risk assessment.

Context:

- view: <path under /home/box/agent-data/grok-research/views/>
- previous view: <prior official view path, or none>
- scout report: <related report path, or none>
- review scope: the view artifact; use previous view and scout report only to judge whether the new view is supported
- ignore patterns: none, unless the task listed some

Task:

- Read the view yourself. Read the previous view and scout report when provided.
- Focus findings on risks in the view: unsupported claims, missing contrary evidence, stale or wrong facts, internal contradictions, and a thesis that does not follow from the evidence.
- Do NOT change the official view during review. Do NOT run tests.
- Analyze for reasoning bugs, risks, and argument simplification opportunities.
- Simplification means tightening the argument without changing the thesis. It does NOT mean dropping coverage or changing the recommended stance.
- Treat missing uncertainties, overclaiming, and stale numbers as risks.
- Do a full review pass before returning. Do not stop after the first valid finding.

Rules:

- Anchor every finding to a specific file and one-indexed line number in the view when possible.
- Severity `error` must not become current. `warning` can be a follow-up. `info` is nice to have.
- Be concise and actionable. No generic advice like "add more sources".
- Only comment on things that genuinely matter.
- Do NOT report styling, formatting, or typography issues.
- If the view is clean, return an empty findings array.
- For each finding, set action to one of:
  - `ask-user`: functional requirements, product behavior, or the author's deliberate intent. When in doubt, ask-user.
  - `auto-fix`: non-functional, not a stance change (correctness, missing caveat, stale figure, internal contradiction) that can be fixed without discussing intent.
  - `no-op`: informational.

Risk assessment after all findings:

- `low` if well-bounded and straightforward
- `medium` if room to improve but safe to make current first
- `high` if it should not become current without explicit human approval

Return JSON:

```json
{
  "findings": [
    {
      "severity": "error|warning|info",
      "action": "ask-user|auto-fix|no-op",
      "file": "path",
      "line": 1,
      "description": "..."
    }
  ],
  "risk_level": "low|medium|high",
  "risk_rationale": "one sentence"
}
```

## Loop

- `auto-fix`: reply to the same researcher. Then a new fresh review subagent.
- `ask-user`: Firstmate takes one decision card to the captain. Do not make the view current.
- `error`: do not make the view current.
- Empty findings, or only `info` / already-answered `ask-user`: the researcher may make the view current.

Fix-forward. Do not revert the author's intentional first draft to silence a finding.

## Do not

- Do not open a pull request
- Do not review a git branch
- Do not run this on scout or ship tasks
