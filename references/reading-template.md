# Visual Paper Learning Report Template

Use this template for a complete but readable saved report. Default final deliverable is PDF, with a Markdown source copy beside it unless the user asks otherwise.

The report should feel like a guided learning handout, not a checklist. Keep the main body short, visual, and sequential. Put dense details in an appendix. Never omit important accessible paper content; use appendices to preserve completeness.

Recommended files:

- Markdown source: `<safe-paper-title>-解读报告.md`
- PDF deliverable: `<safe-paper-title>-解读报告.pdf`
- Visual assets folder: `<safe-paper-title>-assets/`

At the end of the Codex turn, summarize only the saved path(s), one-sentence conclusion, and major caveat unless the user asks to see the whole report in chat.

## Cover

- Title:
- Short Chinese title:
- Authors / year / venue:
- Source:
- Report path:
- PDF path:
- Analysis date:
- Reader level assumed:
- Confidence:
- Missing materials that affect confidence:

## 1. 一页读懂

Write this as the first real reading page.

- 这篇论文在解决什么真实问题:
- 为什么这个问题重要:
- 作者的核心想法:
- 最关键证据:
- 最大限制:
- 如果只记住一句话:

## 2. 阅读地图

Create a simple argument map with 4-6 steps:

1. Field goal:
2. Bottleneck:
3. Proposed intervention:
4. Mechanism:
5. Evidence:
6. Practical implication:

If the PDF renderer supports Mermaid poorly, use a numbered map rather than a diagram.

## 3. 必要背景和术语

Only include terms that appear repeatedly or block comprehension.

| Term | Human explanation | Why it matters here |
| --- | --- | --- |
|  |  |  |

## 4. 核心机制或方法

For each mechanism/method:

### Mechanism / Method Name

- 一句话:
- 人话版:
- 技术版:
- 前提假设:
- 如果这个前提不成立会怎样:
- Related visual: include figure/table/formula image if helpful.

## 5. 关键图表讲解

Choose 3-6 key visuals from the paper. Do not include all figures.

For each selected visual:

![Visual caption](path/to/visual.png)

- 这张图回答的问题:
- 先看哪里:
- 图里真正重要的结果:
- 它支撑的作者结论:
- 它不能证明什么:
- 读者容易误解的点:

## 6. 结果可信度

- Metrics:
- Baselines/controls:
- Improvement size and exact conditions:
- Ablations/control-variable tests:
- Robustness/sensitivity/error analysis:
- Strongest evidence:
- Weakest evidence:
- Does the evidence prove the central claim, or support it conditionally?

## 7. 批判性吸收

### What to believe

- 

### What to be cautious about

- 

### Reproducibility

- Code/source:
- Data/materials:
- Parameters:
- Environment/instruments:
- Missing minimum information:

### Failure scenarios

- 

## 8. 三遍阅读路线

### First pass: decide whether to invest

- Read:
- Skip:
- Questions:
- Decision:

### Second pass: understand the skeleton

- Read:
- Reconstruct:
- Key visuals:
- Questions:

### Third pass: dissect details

- Read deeply:
- Verify:
- Recalculate or reproduce:
- Questions:

## 9. 吸收与迁移

- What to remember tomorrow:
- What idea/method can be reused:
- What should not be copied blindly:
- How this relates to the user's work:
- Practical next step:
- Related papers or keywords:

## Appendix: Evidence Ledger

Use compact tables only in the appendix.

| Figure/Table/Experiment | Question | Setup/control | Result | Claim supported | Caveat |
| --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |

## Appendix: Completeness Audit

### A. Section Coverage

| Section | Core content | Covered where | Status |
| --- | --- | --- | --- |
|  |  |  | Covered in main / Covered in appendix / Briefly mentioned / Not accessible |

### B. Figure and Table Coverage

Include every visible main-paper figure/table. If supporting figures are referenced but not available, mark them as "Needs supplementary material".

| Item | What it shows | Key takeaway | Report treatment | Status |
| --- | --- | --- | --- | --- |
|  |  |  | Embedded / Summarized / Mentioned / Needs supplement |  |

### C. Equation / Metric Coverage

| Equation or metric | Meaning | Used for | Explained where | Status |
| --- | --- | --- | --- | --- |
|  |  |  |  |  |

### D. Claim-to-Evidence Map

| Major author claim | Supporting evidence | Caveat | Confidence |
| --- | --- | --- | --- |
|  |  |  | High / Medium / Low |

### E. Missing or Unverified Items

- Unreadable or missing sections:
- Supporting information needed:
- Data/statistics not confirmed:
- Figures/tables not embedded but summarized:
