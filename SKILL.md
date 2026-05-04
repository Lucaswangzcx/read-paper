---
name: read-paper
description: Read academic papers from a provided PDF, URL, text, DOI, title, or citation and produce a teaching-first structured interpretation report, usually saved to a user-specified directory as a PDF with a Markdown source copy. Use when the user wants to genuinely understand, learn, summarize, deconstruct, critique, reproduce, compare, apply, or write a report about a scholarly article; especially for Chinese requests such as 读懂论文, 论文精读, 论文学习报告, 三遍阅读法, 逐段精读, 解构论文, 生成论文解读报告, 输出到指定目录, 输出PDF, PDF报告, 分析论文贡献/方法/实验/局限/可复现性.
---

# Read Paper

## Goal

Help the user actually understand a paper, not merely receive a checklist summary. The skill must read the whole accessible paper and avoid omitting important points. Treat the paper like a building: first inspect every room, then guide the reader through the load-bearing structure in a readable way, and finally provide an appendix proving what was covered.

Default to Chinese output unless the user asks otherwise. Default reader profile: smart beginner in the paper's field. If the user gives a background, adapt depth and terminology to that background.

Default to creating a complete yet readable visual PDF report when the user provides an output directory. The report must have two layers: a concise main learning report and a complete coverage appendix. Also keep a Markdown source copy beside the PDF unless the user explicitly asks for PDF only or another format. If no output directory is provided and the user asks for a report file, ask for the directory before writing.

## Design Influences

This skill incorporates proven patterns from public paper-reading workflows:

- Three-pass reading: skim for the Five C's and value, read for the skeleton, then dissect details.
- Teaching-first paper reading: explain the story and intuition before technical critique.
- Local Markdown note generation: save a reusable reading note/report instead of only chatting.
- Research note templates: include TLDR, relevance, soundness, confusing aspects, relation to user's work, and future questions.
- Experiment ledger: for every major figure/table, explain purpose, result, supported claim, and caveat.
- Visual learning report: include selected formulas, tables, and figure/table snapshots beside the explanation when the source permits and the user supplied the paper.
- Completeness audit: include a coverage appendix so the user can see which sections, figures, tables, equations, datasets/materials, experiments, conclusions, and limitations were covered.

Do not imitate any source verbatim. Use these patterns as operating principles.

## Intake

Start from whatever the user provides:

- PDF or local file path: extract readable text; inspect title, abstract, introduction, methods, results, figures/tables, conclusion, limitations, appendix, and references when available.
- URL, DOI, arXiv/PubMed/ACM/IEEE/Semantic Scholar page, or citation: retrieve lawful metadata/full text where available. Do not bypass paywalls, logins, captchas, or access controls.
- arXiv URL: prefer source/TeX when feasible because it preserves sections, equations, captions, and tables better than PDF text. Fall back to PDF when source access is unavailable.
- Pasted text: analyze the supplied text; state when missing sections limit confidence.
- Only a title/topic: ask for the paper or offer to search if the user wants discovery.

When the paper is long, do not read linearly. Build a paper map first.

## Workflow

1. **Reconstruct the whole accessible paper source**: collect bibliographic facts, section map, all visible figures/tables, key equations/formulas, datasets/materials, experimental conditions, conclusions, limitations, appendix/supplement references, and references that are central to the argument. Note missing parts.
2. **Orient the reader**: explain the field problem in plain language, define required background concepts, and say why the paper exists.
3. **Write the paper's story line**: convert the paper into a chain of "because A was broken, the authors did B, which should cause C, and they checked it with D."
4. **Explain before judging**: for each core method or mechanism, give a plain-language explanation, then a technical version, then why it matters.
5. **Select main-report visuals**: choose 3-6 key figures/tables/formulas that are necessary for understanding. Extract or crop them from the supplied paper when possible. Do not include every figure in the main report unless the paper is short.
6. **Build visual explanations**: for each selected visual, state what the reader should look at, what it proves, what it does not prove, and how it connects to the thesis.
7. **Build an evidence ledger**: for each important figure/table/experiment, state purpose, setup, result, supported claim, and caveat.
8. **Perform the three passes**:
   - First pass: title, abstract, intro ending, figures/tables, conclusion. Decide whether the paper deserves attention.
   - Second pass: method architecture, data/materials, metrics, baselines, controls, result tables, ablations.
   - Third pass: formulas, algorithms, experimental design, statistics, assumptions, failure modes, and transfer to the user's work.
9. **Critique after comprehension**: separate author claims from evidence, mark unsupported assumptions, reproducibility gaps, and conditions where the method may fail.
10. **Turn reading into learning**: end with a glossary, "what to remember tomorrow", follow-up questions, and practical next steps.
11. **Run a completeness audit before finalizing**: compare the report against the section map and all visible figures/tables/equations. Add an appendix that marks each item as Covered in main report, Covered in appendix, Briefly mentioned, Missing from accessible source, or Needs supplementary material.

Use `references/reading-template.md` when producing the saved report, when the user wants a full structured report, or when the answer risks becoming scattered.

Use `scripts/render_learning_pdf.py` to render a polished Chinese PDF from the Markdown source and selected image assets.

## Comprehension-First Rules

- Never start the report with dense jargon. Start with "这篇论文在解决什么真实问题".
- For every field-specific term that is central to the paper, define it in one sentence and explain its role in this paper.
- For every mechanism, include an "if we simplify it" explanation before technical details.
- For formulas, explain what each variable means and what the formula is trying to measure or optimize before discussing derivation.
- For figures/tables, explain what question the figure/table answers. Do not just list values.
- Use "作者声称 / 证据显示 / 我们还不能确定" to separate claim, evidence, and uncertainty.
- When the paper is outside the user's likely background, include an analogy, but keep it technically faithful.
- Avoid checklist-only output. A useful report should make the user able to explain the paper to another person.
- Avoid report sprawl. Prefer 6-10 well-designed pages over a long exhaustive dump. Move secondary details into an appendix.
- Integrate visuals into the explanation. Do not put all figures at the end unless the user asks for an appendix-only report.
- Completeness matters more than brevity. If a point is important but would disrupt the main narrative, include it in the appendix rather than omitting it.

## Visual and Layout Rules

- Include selected source visuals in the main report when they are needed for comprehension: core mechanism figure, central architecture/model diagram, main results table, key ablation, important equation, or most diagnostic data plot.
- Track all source visuals in the appendix even if they are not embedded in the main report. Each visible figure/table should have at least a one-line purpose/result note unless it is purely decorative or unavailable.
- For user-provided PDFs, it is acceptable to include small, relevant excerpts in the private learning report. Do not reproduce an entire paper, all figures, or large copyrighted text blocks.
- If a figure is dense, crop the relevant panel or include the whole figure at readable width and explain only the panels that matter.
- For each figure/table/formula in the report, write a short "怎么看这张图" paragraph before or after it.
- Do not insert low-resolution or unreadable visuals. If a crop is too blurry, use a full-page snapshot with a callout explanation or summarize it textually.
- Keep the main report visually calm: cover/overview, learning map, 3-5 core sections, visual evidence, critique, next steps. Avoid huge tables unless necessary.

## Output Contract

For a normal paper-reading request, produce a saved PDF report when an output directory is supplied, with a Markdown source copy by default. If the user explicitly asks for Markdown only, skip PDF. The report must contain:

1. **一页读懂**: problem, central idea, why it matters, key evidence, and main caveat.
2. **阅读地图**: 3-6 nodes showing how the paper's argument flows.
3. **必要背景和术语**: only the concepts needed to understand this paper.
4. **核心机制/方法**: plain-language explanation, technical explanation, assumptions, and key formulas/models.
5. **关键图表讲解**: selected visuals from the paper, each with what to look at, what it proves, and the caveat.
6. **结果可信度**: metrics, baselines/controls, improvements, ablations, robustness, and whether the claim is proven or only supported.
7. **批判性吸收**: limitations, reproducibility, failure cases, missing comparisons, and what to reuse or avoid.
8. **三遍阅读路线和下一步**: concrete reading plan and next actions.
9. **完整性附录**: section coverage, figure/table/equation coverage, experiment coverage, unverified or missing items, and supplementary-material dependencies.

If evidence is missing from the accessible text, mark it as "未在当前材料中确认" instead of guessing.

## Completeness Requirements

Before writing the final PDF, create an internal coverage map. The final report must include a visible coverage appendix with:

- **Section coverage**: every accessible section and subsection, with the core point and where it is discussed.
- **Figure/table coverage**: every visible figure/table in the main paper, with purpose, key result, and whether it is embedded, summarized, or only referenced.
- **Equation/formula coverage**: every important equation or derived metric, with what it measures and whether it is explained.
- **Experiment coverage**: every major experiment type, control/baseline, metric, and result.
- **Claim-to-evidence map**: each major author claim paired with supporting evidence and caveat.
- **Not covered / not accessible**: clearly list anything that could not be read, such as missing Supporting Information, unreadable figures, paywalled pages, or extraction failures.

Do not claim "complete" if the PDF text extraction, figures, tables, or supplement are missing. Say "complete for the accessible main paper" when that is the true scope.

## Report File Output

When the user specifies an output directory, create a PDF report there by default.

- Resolve and create the output directory if it does not exist and permissions allow.
- Name the PDF file from the paper title when available: `<safe-paper-title>-解读报告.pdf`.
- Also save the Markdown source as `<safe-paper-title>-解读报告.md` unless the user explicitly asks not to.
- If the title is unavailable, use `paper-reading-report-YYYYMMDD-HHMM.pdf` and `.md`.
- Keep filenames filesystem-safe: remove path separators, control characters, and overly long fragments.
- Put the full structured report in the file, not only a summary.
- Include a short provenance block near the top: source file/URL/DOI, analysis date, language, and any missing sections that lower confidence.
- Include key visual assets in an `assets` or sibling image folder when creating the report, and reference them from the Markdown source.
- For Chinese PDF output, use a CJK-capable font such as Noto Sans SC, Microsoft YaHei, SimHei, or SimSun. Verify the PDF file exists and is non-empty.
- In the chat response after writing, give the saved path(s), one-sentence conclusion, and any major caveat. Do not paste the entire report unless the user asks.
- If writing fails because of permissions or missing directory access, explain the failure and provide the report content in chat or in the current workspace as a fallback.

## Discipline Adaptation

Adjust the analysis lens to the field:

- Machine learning / AI: task definition, model architecture, training data, objective, compute, baselines, SOTA claim, ablations, code/data release, leakage risk, robustness.
- Biomedical / clinical: disease/biology context, cohort, inclusion/exclusion criteria, endpoints, statistics, confounders, ethics, sample size, clinical relevance.
- Social science / psychology: theory, operationalization, sampling, causal identification, survey/interview design, effect size, preregistration, validity.
- Materials / chemistry / physics: target property, experimental setup, characterization methods, controls, physical/chemical mechanism, measurement uncertainty, reproducibility.
- Battery / electrochemistry: cell chemistry, electrode/electrolyte design, interface mechanism, current density, areal capacity, mass loading, electrolyte amount, CE, cycling stability, EIS, morphology, gas/pH evidence, practical cell conditions.
- Review papers: scope, search strategy, inclusion criteria, taxonomy, synthesis quality, bias, and what agenda the review sets for the field.

## Quality Bar

Before finalizing, check:

- Could a smart non-specialist explain the paper's central idea after reading the first two sections?
- Are all core acronyms and mechanisms explained before being used heavily?
- Does every major performance number have context: compared to what, under what condition, why it matters?
- Are the paper's strongest evidence and weakest evidence both visible?
- Does the report include what the user should do next, not just what the paper said?
