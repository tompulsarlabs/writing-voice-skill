# Writing Voice — Evaluation & Self-Learning

This is the test harness for the Writing Voice skill. It exists for one reason: to measure whether the skill actually does what `SKILL.md` claims, find where it fails, and turn those failures into edits that make the skill better.

Use it two ways:

1. **Eval** — run the skill against known cases, score the output against the rubric, record what broke.
2. **Self-learning** — read the failures, find the pattern, propose a precise change to `SKILL.md`, and add a regression case so the same mistake can't return unnoticed.

---

## How to Run an Eval

1. Pick a case from the **Case Bank** below (or use a real draft the user supplied).
2. Run the skill on the input in the relevant mode (Full Edit, Quick Tighten, or Voice Check).
3. Score the output against the **Rubric**. Every dimension gets PASS or FAIL with a one-line reason.
4. Compare against the case's **Expected Catches**. Anything the skill missed is a FAIL, even if the prose reads well.
5. Log the result in the **Scorecard** format.
6. If anything failed, run the **Self-Learning Loop**.

A piece can read beautifully and still fail the eval. The eval measures whether the skill applied its own rules — not whether the output is pretty.

---

## Rubric

Each dimension is scored PASS/FAIL on the skill's output. No partial credit. A dimension fails if a single clear violation survives.

### Layer 1 — Fundamentals
- **L1.1 Length** — Output is ≤90% of input word count (Full Edit / Quick Tighten). Count and show the math.
- **L1.2 Active voice** — No passive constructions survive except where the actor is genuinely unknown.
- **L1.3 Adverbs** — No `-ly` adverbs survive that could be cut or folded into a stronger verb. Dialogue attribution adverbs are an automatic fail.
- **L1.4 Qualifiers/hedges** — No `very, really, quite, just, actually, basically`; no `I think, it seems, perhaps, it could be argued`.
- **L1.5 Simple words** — No `utilize, facilitate, commence, demonstrate` where the plain word fits.
- **L1.6 Paragraph discipline** — No paragraph over 5–6 sentences without a structural reason. Each does one job.

### Layer 2 — Anti-Slop
- **L2.1 Trigger words** — Every flagged word (`leverage, ecosystem, landscape, synergy, holistic, empower, unlock`…) either earns its place by the test or is gone. Survivors must pass "replace it with what it means and lose information."
- **L2.2 Filler phrases** — No `it's important to note, let's dive in, at its core, when it comes to, moving forward, ultimately, first and foremost`.
- **L2.3 False depth** — No `nuanced, multifaceted, comprehensive, delve, unpack, navigate, foster, realm, tapestry, rich` used as decoration.
- **L2.4 Intensifiers / openers** — No hollow `incredibly, extremely, truly, deeply`; no sycophantic `Great question, Absolutely`.
- **L2.5 Structural slop** — No false binary, empty framework, hedge sandwich, mirror intro, orphan transition, or insight-free conclusion.

### Layer 3 — Editorial Voice
- **L3.1 Say the actual thing** — No euphemism standing in for the concrete event (`rightsizing` for layoffs, `sunsetting` for killed product).
- **L3.2 No comfort language** — No `it's a complex issue, many factors to consider, stakeholders have concerns` left vague.
- **L3.3 Earned abstraction** — Every abstraction compresses specifics the reader already has; none substitutes for specifics the writer never gave.
- **L3.4 No overclaiming** — Claims are scaled to evidence. No `everyone knows, this changes everything, no one is talking about` beyond what's supported.
- **L3.5 Takes a position** — The piece commits. It does not end on "it depends."
- **L3.6 Reads aloud** — No sentence that a smart person would never say out loud.

### Process integrity
- **P.1 No meaning lost** — The edit preserves the author's argument and facts. Cutting 10% must not cut the point. This is the one dimension that outranks all others: an edit that tightens prose but changes or guts the meaning is a FAIL regardless of every other PASS.
- **P.2 Right mode** — The output matches the requested mode (Voice Check flags without rewriting; Quick Tighten stays mechanical and brief).
- **P.3 Honest commentary** — Change notes name real structural/voice changes, not obvious mechanical fixes, and don't overclaim what the edit did.

---

## Scorecard Format

```
CASE: <id or "live draft">
MODE: <Full Edit | Quick Tighten | Voice Check>
INPUT WORDS: <n>   OUTPUT WORDS: <n>   CUT: <pct>

RUBRIC:
  L1.1 PASS   L1.2 PASS   L1.3 FAIL — "quickly" survived in para 3
  L1.4 PASS   L1.5 PASS   L1.6 PASS
  L2.1 PASS   L2.2 PASS   L2.3 PASS   L2.4 PASS   L2.5 FAIL — insight-free conclusion
  L3.1 PASS   L3.2 PASS   L3.3 PASS   L3.4 PASS   L3.5 PASS   L3.6 PASS
  P.1 PASS    P.2 PASS    P.3 PASS

EXPECTED CATCHES: 4 listed / 3 caught  → MISSED: passive in opening line
SCORE: 22/25 dimensions  +  3/4 expected catches
VERDICT: FAIL (L1.3, L2.5, one missed catch)
```

A run is a PASS only if every rubric dimension passes **and** every expected catch is caught.

---

## Case Bank

Each case is a small input engineered to trip a specific rule. The **Expected Catches** are the violations a correct run must fix or flag. Keep inputs short so a full eval is cheap to run.

### C1 — Adverbs and weak verbs
> "She quickly walked into the room and softly said that the project was basically done."

**Expected catches:** `quickly` (→ stronger verb), `softly said` (→ whispered / fold in), `basically`, weak `walked`. Target: one clause, no `-ly`.

### C2 — Passive voice
> "The decision was made by leadership that the launch would be delayed by the team until the issues were resolved by engineering."

**Expected catches:** three passive constructions; rewrite with actors performing actions. Word count should drop sharply.

### C3 — Corporate euphemism (Layer 3)
> "After a thoughtful review, we've decided to rightsize the organization and sunset several initiatives to better align with our core strategic priorities going forward."

**Expected catches:** `rightsize` (= layoffs — say it), `sunset` (= cancel/kill), `align`, `core strategic priorities`, `going forward`, `thoughtful`. The honest version names what is happening to people.

### C4 — AI slop density (Layer 2)
> "It's important to note that in today's fast-paced world, leveraging a robust ecosystem of solutions can empower teams to unlock their full potential and navigate the ever-evolving landscape. Let's dive in."

**Expected catches:** `it's important to note`, `in today's fast-paced world`, `leveraging`, `robust ecosystem`, `empower`, `unlock their full potential`, `navigate`, `ever-evolving landscape`, `let's dive in`. After the sweep, almost nothing of substance remains — the correct note says so: this paragraph carries no information.

### C5 — Overclaiming (Layer 3)
> "Everyone knows AI changes everything. No one is talking about how this will reshape every single industry on earth, but it absolutely will."

**Expected catches:** `everyone knows`, `changes everything`, `no one is talking about`, `every single industry`, `absolutely will`. Rewrite scales each claim to stated evidence without hedging.

### C6 — Hedge sandwich + insight-free conclusion (structural)
> "Remote work is the future. Of course, it might not suit every company, and there are many factors to consider. But in many ways, it could be argued that remote work is probably the future. In conclusion, it's a complex topic with many dimensions."

**Expected catches:** hedge sandwich (claim → qualify → soft restatement), `many factors to consider`, `in many ways`, `it could be argued`, `probably`, insight-free conclusion. Output must pick a position and end on a real point.

### C7 — Already-tight prose (false-positive guard)
> "We shipped late. The login flow broke under load, so we held the release four days to fix it. It cost us the launch-week press, and that was the right call."

**Expected catches:** *none.* This is the control case. A correct run changes little, does not invent slop to remove, does not pad to justify itself, and does not cut meaning to force a 10%. Over-editing this is a FAIL.

### C8 — Legitimate trigger word (judgment guard)
> "The change shipped to the iOS ecosystem first because the regulatory landscape shifted after GDPR, and we needed leverage in the negotiation."

**Expected catches:** *none of the flagged words should be removed.* `iOS ecosystem`, `regulatory landscape` (tied to GDPR), and financial-sense `leverage` all pass the earn-its-place test. Stripping them mechanically is a FAIL — this case checks that the skill flags with intent, not on autopilot.

> Cases C7 and C8 matter as much as the violation cases. A skill that only ever cuts is a blunt instrument. The eval has to prove restraint, not just aggression.

---

## Self-Learning Loop

Run this whenever an eval fails. The goal is a durable fix to `SKILL.md`, not a one-off correction of the output.

1. **Name the failure precisely.** Which rubric dimension, which case, what survived or what was wrongly cut. "L2.3 — `delve` survived in paragraph two."

2. **Classify it:**
   - **Miss** — a real violation the skill didn't catch. The rule exists but wasn't applied or wasn't specific enough.
   - **False positive** — the skill "fixed" something that was already correct (see C7/C8). The rule is too aggressive or lacks an exception.
   - **Gap** — the violation isn't covered by any rule. The skill needs a new rule.
   - **Meaning loss (P.1)** — the edit changed the argument. Always the highest-priority fix.

3. **Find the smallest change to `SKILL.md` that prevents recurrence.** Prefer sharpening an existing rule over adding a new one. Add a banned word to a list; add an exception clause; add a one-line test. Do not bolt on a whole new section for a single miss.

4. **Write the change against the skill's own standard.** The edit to `SKILL.md` must itself pass this rubric — no hedging, no slop, no comfort language. The skill's documentation is held to the skill's rules.

5. **Add a regression case.** Turn the failing input into a permanent entry in the Case Bank with its expected catches. The bug becomes a test. A fix without a regression case isn't done.

6. **Re-run the affected cases plus the new one.** Confirm the fix works and that it didn't break C7/C8 (over-correction is the most common regression).

7. **Record it** in the Change Log below: what failed, the root cause class, the rule changed, the case added.

### Change Log

| Date | Failing case | Class | Rule changed | Regression case added |
|------|--------------|-------|--------------|-----------------------|
| _seed_ | — | — | Initial eval harness | C1–C8 |

---

## What "Better" Means Here

The skill improves along two axes, and they pull against each other:

- **Recall** — catching more real violations (driven by violation cases C1–C6).
- **Precision** — not damaging prose that's already right (guarded by C7–C8).

A change that raises recall by lowering precision is not an improvement; it's a trade. Every proposed edit to `SKILL.md` has to hold both. When the Case Bank grows, keep the ratio honest: for every new violation case, the control cases should still pass. The day the skill starts "fixing" C7 is the day it stopped being an editor and became a word filter.
