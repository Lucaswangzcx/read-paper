# read-paper generic agent rules

Use these rules when an agent is asked to read an academic paper and create a learning report.

## Core behavior

- Read the whole accessible paper before writing the final report.
- Do not only summarize the abstract.
- Produce a report that is both readable and complete.
- Default to Chinese unless the user asks for another language.
- If the user gives an output directory, create a PDF report by default and keep a Markdown source copy when possible.
- If any section, figure, table, supplementary material, or experimental detail is not accessible, say so explicitly.

## Required report layers

The report has two layers.

### Main learning report

Keep this section clear and human-readable:

1. 一页读懂
2. 阅读地图
3. 必要背景和术语
4. 核心机制或方法
5. 关键图表讲解
6. 结果可信度
7. 批判性吸收
8. 三遍阅读路线
9. 吸收与迁移

### Completeness appendix

Use the appendix to prevent missing important content:

1. 章节覆盖审计
2. 图表覆盖审计
3. 公式、指标和实验覆盖
4. 作者主张与证据对应
5. 未覆盖或需补充材料确认的项目

## Figure, table, and formula handling

- Select only the visuals that are necessary for understanding in the main report.
- For every visible figure or table in the accessible main paper, mention it in the appendix even if it is not embedded.
- For each key visual, explain:
  - what question it answers
  - where to look first
  - what the important result is
  - what claim it supports
  - what it cannot prove
- For formulas, explain what each important variable means and why the formula matters.

## Critical reading rules

- Separate author claims from evidence.
- Mark uncertainty instead of guessing.
- State whether each major claim is strongly proven, conditionally supported, or weakly supported.
- Include reproducibility checks:
  - code/source availability
  - data/material availability
  - parameters and environment
  - missing experimental details
- Do not overstate practical value when the paper only has lab-scale evidence.

## Privacy and copyright rules

- Do not include local private paths in the final public report unless the user explicitly wants local file references.
- Do not include credentials or secrets.
- Do not redistribute full papers, large copyrighted excerpts, or all figures.
- Use only the minimum visual excerpts needed for private learning and explanation.

## Optional PDF rendering

If this repository is available locally and Python dependencies are installed, the report can be rendered with:

```bash
python scripts/render_learning_pdf.py --markdown report.md --output report.pdf
```

