# read-paper rules for Claude Code

Use these rules when the user asks Claude Code to read, explain, critique, reproduce, or turn an academic paper into a report.

## Goal

Read the whole accessible paper and produce a complete but readable learning report. The report should help the user understand the paper first, then inspect the evidence, then critique limitations and reproducibility.

Default output language: Chinese, unless the user asks otherwise.

Default deliverable: a visual PDF report with a Markdown source copy when an output directory is supplied.

## Workflow

1. Collect the paper source: PDF, URL, DOI, title, citation, or pasted text.
2. Extract or inspect the full accessible main paper before writing the report.
3. Build a coverage map:
   - sections and subsections
   - visible figures and tables
   - key equations, metrics, datasets, or materials
   - major experiments and controls
   - author claims and supporting evidence
   - inaccessible or missing supplementary materials
4. Write a readable main report:
   - one-page explanation
   - reading map
   - necessary background and terminology
   - core method or mechanism
   - key visual explanations
   - evidence strength
   - critical takeaways
   - three-pass reading route
5. Add a completeness appendix:
   - section coverage
   - figure/table coverage
   - equation/metric coverage
   - experiment coverage
   - claim-to-evidence map
   - missing or unverified items
6. If creating a PDF, render from Markdown and verify that the PDF exists, is non-empty, and contains readable text.

## Reading Principles

- Start with plain language. Do not begin with dense jargon.
- Explain every central acronym or technical term before using it heavily.
- For each important figure or table, explain:
  - what question it answers
  - where to look first
  - what result matters
  - what claim it supports
  - what it cannot prove
- Separate "author claim", "evidence supports", and "not yet confirmed".
- Do not pretend to cover inaccessible supporting information. Mark it clearly.
- Keep the main report readable. Put dense coverage details in the appendix.
- Do not reproduce full papers, long copyrighted passages, or all figures. Include only small relevant excerpts or summaries needed for private learning.

## Suggested Output Structure

```text
# <paper short title> - 图文学习报告

## 封面信息
## 1. 一页读懂
## 2. 阅读地图
## 3. 必要背景和术语
## 4. 核心机制或方法
## 5. 关键图表讲解
## 6. 结果可信度
## 7. 批判性吸收
## 8. 三遍阅读路线
## 9. 吸收与迁移
## Appendix A: 章节覆盖审计
## Appendix B: 图表覆盖审计
## Appendix C: 公式、指标和实验覆盖
## Appendix D: 作者主张与证据对应
## Appendix E: 未覆盖或需补充材料确认的项目
```

## Optional Renderer

If this repository is available locally, use `scripts/render_learning_pdf.py` to render a Markdown report:

```bash
python scripts/render_learning_pdf.py --markdown report.md --output report.pdf
```

