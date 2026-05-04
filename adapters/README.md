# Agent adapters

`read-paper` is native to Codex through `SKILL.md`, but the workflow is not locked to Codex.

Other coding agents can use the same reading method by loading one of these adapter files as project rules or custom instructions.

## Claude Code

Use the repository-level `CLAUDE.md`.

Suggested setup:

1. Copy `CLAUDE.md` into the root of the project where Claude Code is working.
2. Put the paper PDF or source link in the workspace.
3. Ask Claude Code to read the paper and generate the report.

Example prompt:

```text
请按照 CLAUDE.md 中的 read-paper 规则读这篇论文，并把完整图文 PDF 报告输出到 reports/。
```

## Trae, CodeBuddy, and other agents

Use `generic-agent-rules.md`.

Suggested setup:

1. Copy the content of `generic-agent-rules.md` into the agent's custom rules, project rules, or memory/instructions field.
2. Make sure the agent can access the paper file and the output directory.
3. If PDF output is needed, allow the agent to use the Python renderer in `scripts/render_learning_pdf.py`, or ask it to produce Markdown first.

Example prompt:

```text
按照 read-paper 规则完整阅读这篇论文，生成主报告 + 完整性附录，并输出 PDF。
```

## Notes

Different agents use different rule-loading mechanisms. These adapter files are intentionally plain Markdown so they can be copied into most tools without conversion.

