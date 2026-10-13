# No Heartburn Academic Skills

**A collection of research plugins for students, made to use in ChatGPT Web without consuming Codex-specific quota. Research with less worry.**

[简体中文](README.md) | **English**

## Why this project exists

I am a student too, and I know that tokens and API calls can be expensive for students with limited budgets. Traditional research Skills often run in clients such as Codex or Claude Code. Using those dedicated quotas for routine work like reading papers and exploring research ideas can make these tasks difficult to sustain.

I explored many open-source research Skills, learned from their strengths, and shaped the workflows with my own understanding to create this collection of research plugins for **ChatGPT Web**. Download a plugin ZIP, upload and install it from ChatGPT's personal plugins page, then use it in a conversation—**without consuming Codex or Claude-specific quota and without configuring a separate API token**.

Here, “token-free” means no separately configured or paid API token and no Codex / Claude-specific quota; the plugins are used directly in ChatGPT Web conversations.

## Plugins in this collection

These plugins are installed and used in ChatGPT Web. Each is powered by Skill instructions and supporting resources; each project README links to its plugin ZIP and explains how to upload and install it.

> **How to use:** download a plugin ZIP → choose **Add** on ChatGPT's personal plugins page and upload it → install the plugin and select it in a conversation.

## ChatGPT Web Research Plugins

This collection currently includes three research plugins you can upload and use in ChatGPT Web:

### 🧩 ChatGPT Web Plugin 01 · [paper-reading](skills/paper-reading/README.en.md)

**Understand papers and practice scientific thinking.** Read explanations alongside original figures in ChatGPT, then learn to question assumptions, examine evidence, and design falsification experiments.

![Following a paper explanation alongside its original figure in ChatGPT](docs/images/chatgpt-side-by-side-paper-figure.png)

Download: [paper-reading v0.7.0 plugin ZIP](downloads/paper-reading-v0.7.0.zip). See the [plugin guide and upload instructions](skills/paper-reading/README.en.md#upload-the-zip-and-install-it-on-chatgpt-web). Core instructions: [`paper-reading/SKILL.md`](skills/paper-reading/SKILL.md).

### 🔬 ChatGPT Web Plugin 02 · [Research Idea Discovery](skills/research-idea-discovery/README.en.md)

**Clarify research problems, investigate nearby work and evidence, and stress-test candidate directions** for novelty, validity, and feasibility before deciding whether to continue, revise, pivot, or stop.

Download: [Research Idea Discovery v4.0.19 plugin ZIP](downloads/research-idea-discovery-v4.0.19.zip). See the [plugin guide and upload instructions](skills/research-idea-discovery/README.en.md#upload-the-zip-and-install-it-on-chatgpt-web). Primary Skill: [`Research Idea Discovery`](skills/research-idea-discovery/skills/research-idea-discovery/SKILL.md).

### 🧭 ChatGPT Web Plugin 03 · [AI Mentor](skills/ai-mentor/README.en.md)

**Bring your research questions to an AI mentor.** Discuss research ideas, literature, experiments, paper writing, figures, and pre-submission review, and turn complex challenges into concrete next steps.

Download: [AI Mentor v1.4.0 plugin ZIP](downloads/ai-mentor-v1.4.0.zip). See the [plugin guide and upload instructions](skills/ai-mentor/README.en.md#upload-the-zip-and-install-it-on-chatgpt-web).

## 🙏 Acknowledgements & Inspirations

- **paper-reading** was inspired by [kelip-paper-reading](https://github.com/skJack/kelip-paper-reading) and [Research Starter Kit](https://github.com/LAMDA-NeSy/Research-Starter-Kit), whose authors share useful paper-reading and research-workflow resources.
- **Research Idea Discovery** was inspired by [ResearchStudio](https://github.com/microsoft/ResearchStudio), [CCFA-Skills](https://github.com/mikubaka88/CCFA-Skills), [ARIS](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep), [RW Research Skill](https://github.com/ozrwayne/rw-research-skill), [TaShan Research Skills](https://github.com/TashanGKD/tashan-research-skills), [AI Night-Scientist](https://github.com/microsoft/ai_night_scientist), and [PatSnap Skills](https://github.com/patsnap/skills).
- **AI Mentor** draws on the research-mentoring workflow in [Supervisor-Skills](https://github.com/HKUSTDial/Supervisor-Skills). The AI Mentor subproject includes adapted material under CC BY-NC-SA 4.0; see its [README](skills/ai-mentor/README.en.md#license-and-sources) and bundled license.

These acknowledgements do not imply official collaboration or endorsement. Adapted or reused material retains its applicable license; the root MIT license does not override a subproject's separate license.

## Repository layout

```text
academic-skills/
├── skills/
│   ├── paper-reading/
│   │   ├── README.md       # Detailed project and installation guide (Chinese)
│   │   ├── README.en.md    # Detailed project and installation guide (English)
│   │   ├── SKILL.md        # Assistant behavior specification
│   │   └── scripts/        # Optional PDF image utilities
│   └── research-idea-discovery/
│       ├── README.md       # Project overview and ChatGPT usage guide
│       ├── README.en.md    # English project guide
│       ├── skills/         # Primary Skill, role Skills, and references
│       └── scripts/        # Optional local research workflow tools
│   └── ai-mentor/           # AI Mentor plugin with separate license
├── downloads/               # Plugin ZIPs ready to upload to ChatGPT
├── docs/images/            # Project demonstration screenshots
├── tests/
├── .github/workflows/
├── README.md               # Collection overview (Chinese by default)
├── README.en.md            # Collection overview in English
└── LICENSE
```

## Development and license

Run repository checks with:

```bash
python -m pip install -r requirements.txt pytest
python -m pytest -q
```

Run the Research Idea Discovery test suite separately:

```bash
cd skills/research-idea-discovery
python -m unittest discover -s tests -v
```

The repository's general content is licensed under MIT; see [`LICENSE`](LICENSE). AI Mentor includes material adapted from Supervisor-Skills under CC BY-NC-SA 4.0; see its [`LICENSE`](skills/ai-mentor/LICENSE). Refer to each plugin directory for component-specific terms.
