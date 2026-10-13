# Research Memory and State Protocol v1.0

## Purpose
Maintain continuity across long-running research exploration.

The agent should preserve the research state conceptually:
- selected research problem
- rejected directions and reasons
- validated evidence
- unresolved gaps
- pending Deep Research tasks
- experimental risks

## Return After Interruption
When a user resumes a previous research exploration, reconstruct:

1. Current research question
2. Evidence already verified
3. Claims still uncertain
4. Next scientifically necessary action

Do not restart idea generation from zero.

## Research Ledger
A research direction should be tracked as:

Problem -> Evidence -> Prior Art -> Gap -> Hypothesis -> Falsifier -> Validation Plan

New ideas must update the ledger rather than overwrite previous findings.

## Avoid Memory Hallucination
If previous evidence is unavailable, explicitly state what is missing and request the minimum required context.
