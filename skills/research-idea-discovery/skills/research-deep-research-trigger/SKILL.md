Deep Research Router Rule v6:

Deep Research is not a normal workflow stage and must not be delegated to the user.

Trigger when:
- novelty cannot be confirmed;
- closest prior work is unknown;
- a gap claim lacks literature evidence;
- benchmark feasibility is unclear;
- a candidate direction requires adversarial validation before method design.

When triggered, the assistant MUST perform a Deep Research Handoff.

Required output:

## Deep Research Required

Explain:
1. The unresolved decision.
2. Why local reasoning is insufficient.
3. What evidence is required.

Then provide:

## Copyable Deep Research Prompt

The prompt must be complete and directly usable. It must include:
- research objective;
- scope;
- literature search requirements;
- nearest-neighbor audit;
- collision detection;
- reviewer attacks;
- feasibility validation;
- final GO / CONDITIONAL GO / STOP judgement.

Never tell the user only "research more" or "continue".
