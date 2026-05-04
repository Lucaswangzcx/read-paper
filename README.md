# read-paper

`read-paper` is a Codex skill for turning an academic paper into a complete, readable learning report.

The goal is simple: a paper report should help you understand the paper, not just collect bullet points from it. This skill asks Codex to read the whole accessible paper, explain the core idea in plain language, place important figures or formulas beside the explanation, and add a coverage appendix so important sections, figures, experiments, and claims are not silently skipped.

It is especially useful when you want to give Codex a PDF, DOI, URL, citation, title, or pasted paper text and get back a report that you can actually read, share, and revisit.

## What It Produces

By default, the skill produces a visual PDF report and keeps a Markdown source file beside it.

The report has two layers:

- **Main learning report**: a guided explanation of the paper's problem, idea, method, evidence, limitations, and takeaways.
- **Completeness appendix**: a coverage check for sections, figures/tables, equations, experiments, author claims, and missing supplementary materials.

This keeps the report readable without sacrificing completeness.

## Why This Exists

Many paper summaries are either too shallow or too chaotic. A short abstract-style summary misses the real value of the paper. A long checklist can technically cover everything while still leaving the reader confused.

`read-paper` tries to land in the middle:

- Start with the human explanation.
- Teach only the background needed for this paper.
- Use visuals when they make the argument easier to understand.
- Separate what the authors claim from what the evidence supports.
- Mark inaccessible or missing materials honestly.
- Preserve detailed coverage in an appendix instead of burying the main narrative.

## Repository Structure

```text
read-paper/
├── SKILL.md
├── agents/
│   └── openai.yaml
├── references/
│   └── reading-template.md
└── scripts/
    └── render_learning_pdf.py
```

## Installation

Copy the skill folder into your Codex skills directory:

```text
~/.codex/skills/read-paper
```

On Windows, the equivalent location is usually:

```text
%USERPROFILE%\.codex\skills\read-paper
```

Then restart or refresh Codex so the skill can be discovered.

## Example Prompts

```text
Use $read-paper to read this paper and save the report to my output folder.
```

```text
使用 $read-paper 解读这篇论文，报告输出到指定目录。
```

```text
使用 $read-paper 精读这个 DOI，并生成完整图文 PDF 报告。
请明确标出哪些内容需要 supporting information 才能确认。
```

## PDF Rendering

The optional renderer at `scripts/render_learning_pdf.py` converts a Markdown learning report into a readable PDF. It supports:

- CJK font discovery for Chinese reports.
- Headings, paragraphs, bullets, simple tables, quotes, and images.
- Markdown image syntax such as `![caption](assets/figure1.png)`.
- A cover page, clearer heading hierarchy, visual spacing, and appendix-friendly layout.

Example:

```bash
python scripts/render_learning_pdf.py \
  --markdown report.md \
  --output report.pdf
```

You can pass a font explicitly when needed:

```bash
python scripts/render_learning_pdf.py \
  --markdown report.md \
  --output report.pdf \
  --font /path/to/NotoSansCJK-Regular.ttc
```

## Dependencies

The skill itself is just Markdown instructions plus a small Python renderer. The renderer requires:

- Python 3.9+
- `reportlab`

Depending on your environment, paper extraction and figure cropping may also use PDF tooling such as `pypdf`, `pdf2image`, Poppler, or equivalent utilities. Those tools are not bundled here.

## Privacy And Copyright Notes

This repository is meant to contain only generic skill instructions, templates, and rendering code.

Do not commit papers, generated reports, local machine paths, credentials, or cropped copyrighted figures. The skill should create those artifacts only in the user's own workspace while processing a specific paper.

When using source figures or tables in a private learning report, include only what is necessary for explanation. Do not redistribute full papers or large copyrighted excerpts.

## License

MIT License. See [LICENSE](LICENSE).

