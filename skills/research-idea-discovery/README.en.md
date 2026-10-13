# Research Idea Discovery

[简体中文](README.md) | **English** | [Plugin collection overview](../../README.en.md)

**Evidence-Driven Research Idea Discovery, Feasibility Validation & Scientific Review**

A research problem discovery and validation plugin for ChatGPT Web. It helps researchers clarify testable questions, examine related work and evidence, and use feasibility checks and reviewer-style stress tests to decide whether to continue, revise, pivot, or stop.

> **Upload the ZIP to install it in ChatGPT Web; it does not consume Codex-specific task quota.**
>
> **More than idea generation: clarify the problem, then test the evidence, nearby work, feasibility, and strongest objections.**

The current **v4.0.19** release focuses on research-question formation, evidence review, and stress testing. It does not promise a novel direction or paper acceptance; when evidence is insufficient, it identifies what still needs investigation.

## v4.0.19: autonomous validation and stress testing

For each candidate direction, the primary Skill asks the assistant to:

1. **Formulate the research question:** define the subject, goal, and scope.
2. **Assess evidence confidence:** separate verified findings from reasonable judgments and hypotheses that need testing.
3. **Audit nearby work:** examine recent papers, close methods, and terminology collisions rather than presenting a renamed method as new.
4. **Validate the problem:** check whether it is real and worth studying, while considering counterexamples and alternative explanations.
5. **Run reviewer-style stress tests:** challenge the gap, mechanism claim, experimental discrimination, execution demands, and potential field impact.
6. **Assess feasibility:** check data, compute, reproducibility, and evaluation protocols; lower confidence or pause when validation is not credible.
7. **Make a research decision:** recommend a next step such as GO, CONDITIONAL GO, REFRAME, or STOP based on the evidence.
8. **Explore methods only after the decision gate:** avoid stacking modules before establishing the research motivation.

When novelty or feasibility evidence is insufficient, the plugin can identify gaps and prepare a copyable prompt for the user to run in ChatGPT Deep Research and bring back. Research decisions can be recorded to reduce repetitive discussion; the plugin does not claim to have launched cloud research or real experiments automatically.

## When is it useful?

- You have a research area but need to identify a concrete, worthwhile question.
- You have an idea and want to find the most dangerous neighboring work and challenge it rigorously.
- You need to assess whether data, baselines, compute, and evaluation protocols support a credible test.
- You want to prepare claims and evidence for reviewer-level scrutiny.
- You lack enough evidence and want to know what to investigate—or whether to stop.

The package includes the primary research-decision Skill and supporting Skills for literature/data investigation, problem validation, mechanism necessity, reviewer stress tests, execution planning, and decision records. Web search, file handling, and tool access depend on your ChatGPT account and permissions; bundled Python scripts run only in environments that support local execution.

## Design principles

- **Problem before method:** transferring a popular technique creates a hypothesis, not a research motivation.
- **Evidence before confidence:** search leads, planned experiments, and structural checks are not verified results.
- **Audit close neighbors carefully:** compare problems, mechanisms, objectives, and protocols—not just titles and keywords.
- **Look for the strongest counter-explanation:** prioritize experiments that distinguish a claim from alternatives.
- **Stopping is a valid outcome:** recommend more investigation, reframing, or stopping when evidence does not justify the investment.

## Upload the ZIP and install it on ChatGPT Web

The recommended route is to upload the prepared plugin package; you do not need Plugin Creator to rebuild it from source.

[Download the Research Idea Discovery v4.0.19 plugin ZIP](../../downloads/research-idea-discovery-v4.0.19.zip)

1. Open ChatGPT's personal plugins page (usually under your profile or Settings → Plugins/Personal plugins, or visit [chatgpt.com/plugins?directoryTab=personal](https://chatgpt.com/plugins?directoryTab=personal)).
2. Select **Add** and then **Upload plugin ZIP**.
3. Choose `research-idea-discovery-v4.0.19.zip`, wait for parsing, and follow the prompts to create or install it.
4. Confirm it appears in your personal plugin list. Enable it from the tools/plugin picker in a new conversation, then describe your research area or current question.

Interface labels may vary by account or product version. Uploading a personal plugin does not list it in ChatGPT's public directory. Web search and other tools depend on your current ChatGPT account and permissions; bundled Python scripts are for environments that support local execution and are not automatically run by ChatGPT Web.

If ZIP upload is unavailable for your account, you can use Plugin Creator with this repository's source, following the primary Skill, references, and auxiliary Skills described on this page.

## Example prompts

**Discover candidate questions from a research area**

> My area is multimodal domain generalization, and I am targeting a top computer vision venue. Start from specific failure cases in relevant work and identify candidate scientific questions. Investigate available data and baselines, then rigorously review motivation, novelty, mechanism necessity, and validation cost. Separate verified evidence from hypotheses that still need testing.

**Review an existing idea**

> Evaluate this idea as a strict reviewer. Find the most dangerous near-neighbor work first. Then assess whether the problem is real, the mechanism necessary, a simpler alternative sufficient, and which experiments are most likely to falsify my claims. If evidence is insufficient, recommend REFINE, PIVOT, STOP, or further research.

**Prepare a deep-research handoff**

> We do not yet have a strong candidate. Summarize the search scope, rejected ideas, and key evidence gaps, then create a targeted prompt I can copy into ChatGPT Deep Research. Do not claim to have started Deep Research automatically.

## Optional local tools

The `scripts/` directory provides tools for literature metadata search, dataset discovery and sample checks, feasibility-card validation, workflow state gates, review and experiment records, idea ledgers, and Deep Research report handoff. They support local work and traceability; they do not replace full-paper verification or scientific judgment. Some local data sources may optionally use an API key; network access, dataset licenses, credentials, and experiment execution each require the appropriate permissions.

Note: `scripts/pilot_bridge.py` runs a user-specified local command only when `--execute` is explicitly provided; its default is `DRY_RUN`. Inspect the command and working directory first. ChatGPT Web does not run this script on the user's behalf.

Run the test suite from this project directory:

```bash
python -m unittest discover -s tests -v
```

Use each script's `--help` to see its options. Never describe a dry run, empty log, or planned experiment as completed work.

## Design principles and limitations

1. **Feasibility matters:** An idea without a credible validation path is not a mature research plan.
2. **Novelty is more than adding modules:** Terminology changes and module combinations do not automatically create substantive contributions.
3. **Establish motivation before storytelling:** The argument must follow from the problem, mechanism, and evidence.
4. **Evidence over confidence:** Label what is verified, inferred, and unknown.
5. **Try to falsify first:** Prioritize experiments that could disprove the central hypothesis.
6. **Zero strong ideas is acceptable:** State uncertainty and identify the next evidence needed.

The Skill does not guarantee a novel direction, exhaustive literature coverage, or acceptance at any venue. Research breadth depends on available sources and tools. Real data access and GPU experiments require authorization and an execution environment. Reviewer roles are workflow perspectives, not separately deployed models. Deep Research handoff currently means generating a prompt and manually returning the report; it does not launch a cloud research task automatically.

**The goal is not to convince you that an idea is good, but to help determine whether it remains worth your research time and resources after repeated scrutiny.**

## 🙏 Acknowledgements & Inspirations

Research Idea Discovery was shaped by ideas from open-source projects in AI-assisted scientific research. We thank their authors and contributors for sharing their work with the community:

- [ResearchStudio-Idea](https://github.com/microsoft/ResearchStudio) — Evidence-grounded ideation, literature-driven problem discovery, and idea evaluation.
- [CCFA-Skills](https://github.com/mikubaka88/CCFA-Skills) — Scientific storytelling, idea refinement, reviewer-oriented evaluation, and consistency between claims and evidence.
- [ARIS (Auto-Research-In-Sleep)](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) — Iterative research workflows, adversarial review, experimental feedback, and idea refinement.
- [RW Research Skill](https://github.com/ozrwayne/rw-research-skill) — Structured research processes, literature investigation, and evidence-based reasoning.
- [TaShan Research Skills](https://github.com/TashanGKD/tashan-research-skills) — Modular research Skills, evidence management, and workflow organization.
- [AI Night-Scientist](https://github.com/microsoft/ai_night_scientist) — Iterative scientific hypothesis exploration and AI-assisted research discovery.
- [PatSnap Skills](https://github.com/patsnap/skills) — Ideas for identifying potentially valuable technical innovations from existing research and development materials.

Building on these inspirations, this project organizes a research-decision workflow: **Research Question Formation → Evidence Confidence Check → Prior-Art Collision Audit → Problem Validation → Reviewer and Feasibility Stress Tests → Research Decision → Method Exploration only after GO**. These acknowledgements indicate conceptual or workflow inspiration; they do not imply official collaboration, endorsement, or full integration of upstream projects. Acknowledgement is separate from license compliance: any code, documentation, or templates actually copied, adapted, or redistributed remain subject to their applicable licenses.

## Version and license

Current release: **v4.0.19**. The [`CHANGELOG.md`](CHANGELOG.md) records release changes without turning this page into a version-by-version feature log. Licensed under MIT; see [`../../LICENSE`](../../LICENSE).
