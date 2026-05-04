#!/usr/bin/env python3
"""Render a readable Chinese paper-learning Markdown report to PDF.

Supports headings, paragraphs, bullets, simple Markdown tables, and image syntax:

    ![caption](relative/or/absolute/path.png)

The renderer intentionally favors a calm handout layout over full Markdown fidelity.
"""

from __future__ import annotations

import argparse
import html
import re
from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    HRFlowable,
    Image,
    KeepTogether,
    PageBreak,
    Paragraph,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
)


def find_cjk_font(explicit: str | None = None) -> str:
    candidates = []
    if explicit:
        candidates.append(Path(explicit))
    candidates.extend(
        [
            Path("/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc"),
            Path("/usr/share/fonts/truetype/noto/NotoSansCJK-Regular.ttc"),
            Path("/usr/share/fonts/truetype/noto/NotoSansSC-Regular.otf"),
            Path("/usr/share/fonts/truetype/wqy/wqy-microhei.ttc"),
            Path("/System/Library/Fonts/PingFang.ttc"),
            Path("/System/Library/Fonts/STHeiti Light.ttc"),
            Path("/System/Library/Fonts/Supplemental/Songti.ttc"),
            Path(r"C:\Windows\Fonts\NotoSansSC-VF.ttf"),
            Path(r"C:\Windows\Fonts\msyh.ttc"),
            Path(r"C:\Windows\Fonts\simhei.ttf"),
            Path(r"C:\Windows\Fonts\simsun.ttc"),
            Path(r"C:\Windows\Fonts\Deng.ttf"),
        ]
    )
    for path in candidates:
        if path.exists():
            return str(path)
    raise FileNotFoundError("No CJK font found. Pass --font PATH.")


def clean_inline(text: str) -> str:
    text = text.replace("`", "")
    text = re.sub(r"\*\*(.*?)\*\*", r"<b>\1</b>", text)
    text = re.sub(r"\*(.*?)\*", r"<i>\1</i>", text)
    return html.escape(text, quote=False).replace("&lt;b&gt;", "<b>").replace("&lt;/b&gt;", "</b>").replace("&lt;i&gt;", "<i>").replace("&lt;/i&gt;", "</i>")


def para(text: str, style: ParagraphStyle) -> Paragraph:
    return Paragraph(clean_inline(text), style)


def flush_table(rows: list[list[str]], story: list, styles: dict) -> None:
    if not rows:
        return
    max_cols = max(len(r) for r in rows)
    normalized = [r + [""] * (max_cols - len(r)) for r in rows]
    data = [[Paragraph(clean_inline(cell), styles["TableCell"]) for cell in row] for row in normalized]
    page_width = A4[0] - 36 * mm
    col_widths = [page_width / max_cols] * max_cols
    table = Table(data, colWidths=col_widths, hAlign="LEFT", repeatRows=1)
    table.setStyle(
        TableStyle(
            [
                ("FONTNAME", (0, 0), (-1, -1), "CJK"),
                ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#EEF2F7")),
                ("TEXTCOLOR", (0, 0), (-1, 0), colors.HexColor("#111827")),
                ("GRID", (0, 0), (-1, -1), 0.35, colors.HexColor("#D1D5DB")),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 5),
                ("RIGHTPADDING", (0, 0), (-1, -1), 5),
                ("TOPPADDING", (0, 0), (-1, -1), 4),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
            ]
        )
    )
    story.append(table)
    story.append(Spacer(1, 5))


def parse_table_line(line: str) -> list[str] | None:
    stripped = line.strip()
    if not (stripped.startswith("|") and stripped.endswith("|")):
        return None
    if re.match(r"^\|\s*:?-{3,}:?\s*(\|\s*:?-{3,}:?\s*)+\|$", stripped):
        return []
    return [cell.strip() for cell in stripped.strip("|").split("|")]


def image_flowable(md_dir: Path, path_text: str, caption: str, styles: dict):
    img_path = Path(path_text)
    if not img_path.is_absolute():
        img_path = md_dir / img_path
    if not img_path.exists():
        return para(f"[Missing image: {path_text}]", styles["Small"])
    max_w = A4[0] - 34 * mm
    max_h = 130 * mm
    img = Image(str(img_path))
    scale = min(max_w / img.imageWidth, max_h / img.imageHeight, 1.0)
    img.drawWidth = img.imageWidth * scale
    img.drawHeight = img.imageHeight * scale
    block = [img]
    if caption:
        block.append(Spacer(1, 2))
        block.append(Paragraph(clean_inline(caption), styles["Caption"]))
    block.append(Spacer(1, 7))
    return KeepTogether(block)


def build_story(md_path: Path, styles: dict) -> list:
    lines = md_path.read_text(encoding="utf-8").splitlines()
    story: list = []
    table_rows: list[list[str]] = []
    in_code = False

    for raw in lines:
        line = raw.rstrip()

        if line.strip().startswith("```"):
            in_code = not in_code
            continue

        if in_code:
            flush_table(table_rows, story, styles)
            table_rows = []
            if line.strip():
                story.append(Paragraph(html.escape(line), styles["Code"]))
            continue

        table = parse_table_line(line)
        if table is not None:
            if table:
                table_rows.append(table)
            continue
        flush_table(table_rows, story, styles)
        table_rows = []

        if not line.strip():
            story.append(Spacer(1, 4))
            continue

        img_match = re.match(r"!\[(.*?)\]\((.*?)\)\s*$", line.strip())
        if img_match:
            story.append(image_flowable(md_path.parent, img_match.group(2), img_match.group(1), styles))
            continue

        if line.startswith("# "):
            title = line[2:].strip()
            if not story:
                story.append(Spacer(1, 48 * mm))
                story.append(Paragraph(clean_inline(title), styles["CoverTitle"]))
                story.append(Spacer(1, 8))
                story.append(HRFlowable(width="65%", thickness=1.2, color=colors.HexColor("#2563EB"), spaceBefore=8, spaceAfter=14, hAlign="CENTER"))
                story.append(Paragraph("论文学习报告 · 图文完整解读", styles["CoverSub"]))
                story.append(Spacer(1, 48 * mm))
                story.append(Paragraph("主报告讲清楚，附录保证不遗漏", styles["CoverNote"]))
                story.append(PageBreak())
            else:
                story.append(Paragraph(clean_inline(title), styles["Title"]))
        elif line.startswith("## "):
            heading = line[3:].strip()
            if heading.lower().startswith("appendix") and story:
                story.append(PageBreak())
            story.append(Paragraph(clean_inline(heading), styles["H1"]))
            story.append(HRFlowable(width="100%", thickness=0.45, color=colors.HexColor("#CBD5E1"), spaceBefore=1, spaceAfter=8))
        elif line.startswith("### "):
            story.append(Paragraph(clean_inline(line[4:].strip()), styles["H2"]))
        elif line.startswith("#### "):
            story.append(Paragraph(clean_inline(line[5:].strip()), styles["H3"]))
        elif line.startswith(">"):
            story.append(Paragraph(clean_inline(line.lstrip("> ").strip()), styles["Quote"]))
        elif re.match(r"^\s*[-*]\s+", line):
            text = re.sub(r"^\s*[-*]\s+", "", line)
            story.append(Paragraph("• " + clean_inline(text), styles["Bullet"]))
        elif re.match(r"^\s*\d+\.\s+", line):
            story.append(Paragraph(clean_inline(line.strip()), styles["Bullet"]))
        elif line.strip() == "---":
            story.append(Spacer(1, 8))
        else:
            story.append(Paragraph(clean_inline(line), styles["Body"]))

    flush_table(table_rows, story, styles)
    return story


def make_styles() -> dict:
    base = getSampleStyleSheet()
    styles: dict[str, ParagraphStyle] = {}
    styles["CoverTitle"] = ParagraphStyle(
        "CoverTitle",
        parent=base["Title"],
        fontName="CJK",
        fontSize=24,
        leading=32,
        alignment=TA_CENTER,
        textColor=colors.HexColor("#0F172A"),
        spaceAfter=8,
        wordWrap="CJK",
    )
    styles["CoverSub"] = ParagraphStyle(
        "CoverSub",
        parent=base["BodyText"],
        fontName="CJK",
        fontSize=13,
        leading=18,
        alignment=TA_CENTER,
        textColor=colors.HexColor("#334155"),
        wordWrap="CJK",
    )
    styles["CoverNote"] = ParagraphStyle(
        "CoverNote",
        parent=base["BodyText"],
        fontName="CJK",
        fontSize=10.5,
        leading=15,
        alignment=TA_CENTER,
        textColor=colors.HexColor("#64748B"),
        wordWrap="CJK",
    )
    styles["Title"] = ParagraphStyle(
        "Title",
        parent=base["Title"],
        fontName="CJK",
        fontSize=20,
        leading=27,
        alignment=TA_CENTER,
        textColor=colors.HexColor("#111827"),
        spaceAfter=10,
        wordWrap="CJK",
    )
    styles["H1"] = ParagraphStyle(
        "H1",
        parent=base["Heading1"],
        fontName="CJK",
        fontSize=16,
        leading=22,
        textColor=colors.HexColor("#0F172A"),
        spaceBefore=15,
        spaceAfter=5,
        wordWrap="CJK",
    )
    styles["H2"] = ParagraphStyle(
        "H2",
        parent=base["Heading2"],
        fontName="CJK",
        fontSize=13.2,
        leading=18.2,
        textColor=colors.HexColor("#1F2937"),
        spaceBefore=10,
        spaceAfter=5,
        wordWrap="CJK",
    )
    styles["H3"] = ParagraphStyle(
        "H3",
        parent=base["Heading3"],
        fontName="CJK",
        fontSize=11.6,
        leading=16.2,
        textColor=colors.HexColor("#374151"),
        spaceBefore=6,
        spaceAfter=3,
        wordWrap="CJK",
    )
    styles["Body"] = ParagraphStyle(
        "Body",
        parent=base["BodyText"],
        fontName="CJK",
        fontSize=10.4,
        leading=16.2,
        alignment=TA_LEFT,
        textColor=colors.HexColor("#111827"),
        spaceAfter=5.6,
        wordWrap="CJK",
    )
    styles["Bullet"] = ParagraphStyle(
        "Bullet",
        parent=styles["Body"],
        leftIndent=13,
        firstLineIndent=-9,
        spaceAfter=3.2,
    )
    styles["Quote"] = ParagraphStyle(
        "Quote",
        parent=styles["Body"],
        leftIndent=10,
        borderColor=colors.HexColor("#CBD5E1"),
        borderWidth=0.6,
        borderPadding=6,
        backColor=colors.HexColor("#F8FAFC"),
        textColor=colors.HexColor("#475569"),
        spaceBefore=4,
        spaceAfter=6,
    )
    styles["Caption"] = ParagraphStyle(
        "Caption",
        parent=styles["Body"],
        fontSize=8.8,
        leading=12,
        alignment=TA_CENTER,
        textColor=colors.HexColor("#475569"),
        spaceAfter=4,
    )
    styles["Small"] = ParagraphStyle(
        "Small",
        parent=styles["Body"],
        fontSize=8.3,
        leading=11,
        textColor=colors.HexColor("#64748B"),
    )
    styles["Code"] = ParagraphStyle(
        "Code",
        parent=styles["Body"],
        fontName="Courier",
        fontSize=7.8,
        leading=10,
        backColor=colors.HexColor("#F8FAFC"),
        borderPadding=4,
    )
    styles["TableCell"] = ParagraphStyle(
        "TableCell",
        parent=styles["Body"],
        fontSize=8.0,
        leading=10.5,
        spaceAfter=0,
    )
    return styles


def footer(canvas, doc):
    canvas.saveState()
    canvas.setFont("CJK", 8)
    canvas.setFillColor(colors.HexColor("#64748B"))
    canvas.drawRightString(A4[0] - 18 * mm, 10 * mm, f"Page {doc.page}")
    canvas.restoreState()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--markdown", required=True, help="Input Markdown report")
    parser.add_argument("--output", required=True, help="Output PDF path")
    parser.add_argument("--font", help="Optional CJK font path")
    args = parser.parse_args()

    md_path = Path(args.markdown).resolve()
    out_path = Path(args.output).resolve()
    out_path.parent.mkdir(parents=True, exist_ok=True)

    pdfmetrics.registerFont(TTFont("CJK", find_cjk_font(args.font)))
    styles = make_styles()
    story = build_story(md_path, styles)

    doc = SimpleDocTemplate(
        str(out_path),
        pagesize=A4,
        rightMargin=16 * mm,
        leftMargin=16 * mm,
        topMargin=15 * mm,
        bottomMargin=15 * mm,
        title=md_path.stem,
    )
    doc.build(story, onFirstPage=footer, onLaterPages=footer)
    if out_path.stat().st_size <= 0:
        raise RuntimeError(f"PDF was not created: {out_path}")
    print(out_path)


if __name__ == "__main__":
    main()
