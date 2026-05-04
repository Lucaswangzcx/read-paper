# read-paper

`read-paper` 是一个用来读懂学术论文的 Codex skill。

它的目标不是把摘要换一种说法，也不是生成一堆机械的清单，而是让 Codex 真正读完整篇可访问的论文，然后输出一份适合人阅读的学习报告：前半部分把论文讲清楚，后半部分用完整性附录确认关键章节、图表、公式、实验和作者主张没有被漏掉。

默认情况下，它会生成一份图文 PDF 报告，并保留对应的 Markdown 源文件，方便继续修改。

## 它适合做什么

你可以把论文 PDF、DOI、URL、标题、引用信息，或者直接粘贴的论文正文交给 Codex，然后让它使用 `$read-paper`。

这个 skill 会尽量做到：

- 先用人话解释论文到底在解决什么问题。
- 补齐读懂这篇论文所需的必要背景和术语。
- 把论文的逻辑讲成一条清楚的故事线。
- 选择关键图表、公式或数据图，放到对应解释旁边。
- 区分“作者声称了什么”和“证据真正支持了什么”。
- 明确标出没有读到、无法确认、需要补充材料才能判断的内容。
- 在附录里做覆盖检查，避免为了报告好看而漏掉重点。

简单说，它想做的是一份“能读懂、能复盘、也能检查完整性”的论文学习报告。

## 报告长什么样

默认报告分成两层。

第一层是主报告，重点是可读性：

- 一页读懂
- 阅读地图
- 必要背景和术语
- 核心机制或方法
- 关键图表讲解
- 结果可信度
- 批判性吸收
- 三遍阅读路线和下一步

第二层是完整性附录，重点是不遗漏：

- 章节覆盖
- 图表覆盖
- 公式和指标覆盖
- 实验覆盖
- 作者主张与证据对应
- 缺失材料和未确认信息

这样主报告不会变得又长又乱，但重要细节也不会消失。

## 项目结构

```text
read-paper/
├── CLAUDE.md
├── SKILL.md
├── adapters/
│   ├── README.md
│   └── generic-agent-rules.md
├── agents/
│   └── openai.yaml
├── references/
│   └── reading-template.md
└── scripts/
    └── render_learning_pdf.py
```

## 安装方式

把这个文件夹复制到 Codex 的 skills 目录：

```text
~/.codex/skills/read-paper
```

Windows 上通常是：

```text
%USERPROFILE%\.codex\skills\read-paper
```

复制完成后，重启或刷新 Codex，让它重新发现 skill。

## 其他 Agent 能不能用

可以。

`SKILL.md` 是给 Codex 原生读取的；但这套论文阅读流程本身是通用的，所以仓库也放了几个适配文件：

- `CLAUDE.md`：给 Claude Code 使用，可以放到项目根目录。
- `adapters/generic-agent-rules.md`：给 Trae、CodeBuddy 或其他支持自定义规则的 agent 使用。
- `adapters/README.md`：说明不同 agent 怎么接入。

也就是说：

- Codex 可以直接把它当 skill 用。
- Claude Code 可以读取 `CLAUDE.md`。
- Trae、CodeBuddy 等可以复制通用规则到项目规则或自定义指令里。
- PDF 渲染脚本是普通 Python 脚本，任何 agent 都可以调用。

## 使用示例

```text
使用 $read-paper 解读这篇论文，报告输出到指定目录。
```

```text
使用 $read-paper 精读这个 DOI，并生成完整图文 PDF 报告。
请明确标出哪些内容需要 Supporting Information 才能确认。
```

```text
Use $read-paper to read this paper and save the report to my output folder.
```

## PDF 渲染脚本

仓库里带了一个简单的 PDF 渲染脚本：

```text
scripts/render_learning_pdf.py
```

它可以把 Markdown 学习报告转成更适合阅读的 PDF，支持：

- 中文/CJK 字体自动查找。
- 标题、正文、列表、引用、简单表格和图片。
- Markdown 图片语法，比如 `![caption](assets/figure1.png)`。
- 独立封面页、清晰的标题层级、图文留白和附录分页。

基本用法：

```bash
python scripts/render_learning_pdf.py \
  --markdown report.md \
  --output report.pdf
```

如果需要指定字体：

```bash
python scripts/render_learning_pdf.py \
  --markdown report.md \
  --output report.pdf \
  --font /path/to/NotoSansCJK-Regular.ttc
```

## 依赖

skill 本身主要是 Markdown 指令和模板。PDF 渲染脚本需要：

- Python 3.9+
- `reportlab`

如果你的工作流还需要从 PDF 中抽取文本、渲染页面或裁剪图表，可能还会用到 `pypdf`、`pdf2image`、Poppler 或类似工具。这些工具没有打包进仓库里。

## 隐私和版权提醒

这个仓库只应该包含通用的 skill 指令、模板和渲染代码。

请不要提交：

- 论文原文
- 生成的报告
- 本地机器路径
- API key、token、账号密码或其他凭据
- 从受版权保护论文中裁剪出来的图表

在自己的本地环境中生成学习报告是可以的，但如果要公开仓库，请只公开通用工具和说明，不要把具体论文内容、完整论文或大量受版权保护的原文片段一起上传。

## License

MIT License. See [LICENSE](LICENSE).
