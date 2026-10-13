# 不烧心 academic-skills

**面向学生党的 ChatGPT 网页端科研插件合集：不耗 Codex 专用额度，用着不烧心。**

**简体中文** | [English](README.en.md)

## 项目初衷

作者自己也是学生，理解 token 和 API 调用成本会给经费有限的学生带来负担。传统科研 Skills 通常需要在 Codex、Claude Code 等客户端中使用；如果把日常读论文、找研究 Idea 等繁琐工作都放在那里，专用额度和费用可能让学生难以长期承担。

我搜集了网上许多开源科研 Skill，借鉴各自的优点，并结合自己的理解进行设计与创作，推出了这套面向 **ChatGPT 网页端**使用的科研插件。下载对应的插件 ZIP，在 ChatGPT 个人插件页面上传并安装即可使用，**不消耗 Codex 或 Claude 专用额度，也无需额外配置 API Token**。

这里的“免 token”指无需额外配置或支付 API Token，也不消耗 Codex / Claude 专用额度；插件直接在 ChatGPT 网页端的对话中使用。

## 本项目的插件

这些插件安装并使用于 ChatGPT 网页端。插件内部由 Skill 规范和配套资源驱动；每个项目的 README 都提供了插件 ZIP 下载和上传安装说明。

> **使用方式：下载插件 ZIP → ChatGPT 个人插件页面选择「添加」并上传 ZIP → 安装后在对话中选择插件。**

## ChatGPT 网页端科研插件

本项目目前收录三个可在 ChatGPT 网页端上传并使用的科研插件：

<br><br>

### 🧩 01 · ChatGPT 网页端插件 · [论文带读 · paper-reading](skills/paper-reading/README.md)

**不止带你读懂论文，也帮助你练习科研思维。** 在 ChatGPT 对话中边读讲解、边对照论文原图；通过质疑假设、检查证据和设计反证实验，逐步练习独立科研判断。

![ChatGPT 中边读论文讲解、边对照论文原图的示例](docs/images/chatgpt-side-by-side-paper-figure.png)

下载：[论文带读 v0.7.0 插件 ZIP](downloads/paper-reading-v0.7.0.zip)。查看[插件介绍与上传安装教程](skills/paper-reading/README.md#在-chatgpt-网页端上传-zip-并安装)。核心行为规范位于 [`paper-reading/SKILL.md`](skills/paper-reading/SKILL.md)。

<br><br>

### 🔬 02 · ChatGPT 网页端插件 · [科研创新点发现与验证 · Research Idea Discovery](skills/research-idea-discovery/README.md)

**从研究问题出发，核查研究现状、证据与可行性。** 再以审稿人视角压力测试候选方向，判断它是否值得继续、需要调整还是应该停止。

下载：[Research Idea Discovery v4.0.19 插件 ZIP](downloads/research-idea-discovery-v4.0.19.zip)。查看[插件介绍与上传安装教程](skills/research-idea-discovery/README.md#在-chatgpt-网页端上传-zip-并安装)。主 Skill：[`Research Idea Discovery`](skills/research-idea-discovery/skills/research-idea-discovery/SKILL.md)。

<br><br>

### 🧭 03 · ChatGPT 网页端插件 · [AI 导师 · AI Mentor](skills/ai-mentor/README.md)

**科研中遇到问题，就和 AI 导师一起拆解。** 从研究想法、文献阅读、实验设计到论文写作、科研绘图和投稿前评审，提供连贯的讨论与下一步建议，帮助把复杂问题变成可行动的研究任务。

下载：[AI Mentor v1.4.0 插件 ZIP](downloads/ai-mentor-v1.4.0.zip)。查看[插件介绍与上传安装教程](skills/ai-mentor/README.md#在-chatgpt-网页端上传-zip-并安装)。

## 🙏 致谢与灵感来源

- **paper-reading** 的设计受到 [kelip-paper-reading](https://github.com/skJack/kelip-paper-reading) 和 [Research Starter Kit](https://github.com/LAMDA-NeSy/Research-Starter-Kit) 启发，感谢相关项目分享论文阅读与科研入门工作流参考。
- **Research Idea Discovery** 的设计受到 [ResearchStudio](https://github.com/microsoft/ResearchStudio)、[CCFA-Skills](https://github.com/mikubaka88/CCFA-Skills)、[ARIS](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep)、[RW Research Skill](https://github.com/ozrwayne/rw-research-skill)、[TaShan Research Skills](https://github.com/TashanGKD/tashan-research-skills)、[AI Night-Scientist](https://github.com/microsoft/ai_night_scientist) 和 [PatSnap Skills](https://github.com/patsnap/skills) 启发。
- **AI Mentor** 的科研指导工作流受到 [Supervisor-Skills](https://github.com/HKUSTDial/Supervisor-Skills) 启发。AI Mentor 子项目包含依据该项目 CC BY-NC-SA 4.0 许可改编的材料；来源与许可见 [AI Mentor README](skills/ai-mentor/README.md#许可与来源) 和随附许可证。

以上致谢不代表官方合作或背书。对实际改编或复用的内容，按其原始许可证分别标注；本仓库根目录的 MIT 许可不覆盖采用独立许可证的子项目。

## 仓库结构

```text
academic-skills/
├── skills/
│   ├── paper-reading/
│   │   ├── README.md       # 论文带读的详细介绍与安装指南
│   │   ├── README.en.md    # English documentation
│   │   ├── SKILL.md        # 助手行为规范
│   │   └── scripts/        # 可选 PDF 图像辅助脚本
│   └── research-idea-discovery/
│       ├── README.md       # 项目介绍与 ChatGPT 使用指南
│       ├── README.en.md    # English project guide
│       ├── skills/         # 主 Skill、辅助角色与参考规范
│       └── scripts/        # 可选本地研究工作流工具
│   └── ai-mentor/           # AI Mentor 插件及独立许可证
├── downloads/               # 可直接上传到 ChatGPT 的插件 ZIP
├── docs/images/            # 项目演示截图
├── tests/
├── .github/workflows/
├── README.md               # 科研技能集总览（中文默认）
├── README.en.md            # Collection overview in English
└── LICENSE
```

## 开发与许可

运行仓库总览与 paper-reading 检查：

```bash
python -m pip install -r requirements.txt pytest
python -m pytest -q
```

运行 Research Idea Discovery 自带的测试：

```bash
cd skills/research-idea-discovery
python -m unittest discover -s tests -v
```

本仓库一般内容采用 MIT License，详见 [`LICENSE`](LICENSE)。AI Mentor 包含依据 Supervisor-Skills 改编、采用 CC BY-NC-SA 4.0 的材料；请按其 [`LICENSE`](skills/ai-mentor/LICENSE) 使用。各插件及第三方资源的具体许可以对应目录说明为准。
