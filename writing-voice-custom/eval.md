# Writing Voice — Evaluation & Self-Learning

This is the test harness for the Writing Voice skill. It exists for one reason: to measure whether the skill actually does what `SKILL.md` claims, find where it fails, and turn those failures into edits that make the skill better.

Use it two ways:

1. **Eval** — run the skill against known cases, score the output against the rubric, record what broke.
2. **Self-learning** — read the failures, find the pattern, propose a precise change to `SKILL.md`, and add a regression case so the same mistake can't return unnoticed.

---

## How to Run an Eval

1. Pick a case from the **Case Bank** below (or use a real draft the user supplied).
2. Run the skill on the input in the relevant mode (Full Edit, Quick Tighten, or Voice Check).
3. Score the output against the **Rubric**. Every applicable dimension gets PASS or FAIL with a one-line reason; mark unrelated dimensions N/A. Save the actual prompt and output with the model, date, and skill revision.
4. Compare against the case's **Expected Catches**. Anything the skill missed is a FAIL, even if the prose reads well.
5. Log the result in the **Scorecard** format.
6. If anything failed, run the **Self-Learning Loop**.

A piece can read beautifully and still fail the eval. The eval measures whether the skill applied its own rules — not whether the output is pretty.

---

## Rubric

Each dimension is scored PASS/FAIL on the skill's output. No partial credit. A dimension fails if a single clear violation survives.

### Layer 1 — Fundamentals
- **L1.1 Length** — Unnecessary wording is removed without a forced percentage cut. Already-tight prose may remain unchanged; record word counts as context, not a pass threshold.
- **L1.2 Active voice** — Active voice clarifies agency where useful; passive voice may remain when the actor is unknown, irrelevant, or not the focus.
- **L1.3 Adverbs** — Redundant modifiers are removed; modifiers that carry meaning or preserve the author’s voice remain.
- **L1.4 Qualifiers/hedges** — Empty intensifiers and evasive padding are removed; uncertainty, approximation, scope, and speaker perspective are preserved.
- **L1.5 Simple words** — No `utilize, facilitate, commence, demonstrate` where the plain word fits.
- **L1.6 Paragraph discipline** — Each paragraph serves its purpose; sentence and paragraph length follow the piece, with no numeric quota.

### Layer 2 — Anti-Slop
- **L2.1 Trigger words** — Every flagged word (`leverage, ecosystem, landscape, synergy, holistic, empower, unlock`…) either earns its place by the test or is gone. Survivors must pass "replace it with what it means and lose information."
- **L2.2 Filler phrases** — Stock phrases are removed when they add no meaning. Quoted text and legitimate contextual uses are preserved.
- **L2.3 False depth** — No `nuanced, multifaceted, comprehensive, delve, unpack, navigate, foster, realm, tapestry, rich` used as decoration.
- **L2.4 Intensifiers / openers** — No hollow `incredibly, extremely, truly, deeply`; no sycophantic `Great question, Absolutely`.
- **L2.5 Structural slop** — No false binary, decorative framework or rule of three, mirror intro, orphan transition, or empty conclusion. Avoid faux-sassy hooks and needless clipped sentences; use connected clauses when they fit.

### Layer 3 — Editorial Voice
- **L3.1 Say the actual thing** — No euphemism standing in for the concrete event (`rightsizing` for layoffs, `sunsetting` for killed product).
- **L3.2 No comfort language** — No `it's a complex issue, many factors to consider, stakeholders have concerns` left vague.
- **L3.3 Earned abstraction** — Every abstraction compresses specifics the reader already has; none substitutes for specifics the writer never gave.
- **L3.4 No overclaiming** — Claims are scaled to evidence. No `everyone knows, this changes everything, no one is talking about` beyond what's supported.
- **L3.5 Takes a position** — An argumentative piece has a supportable thesis. If it lacks one, the response says so and proposes a direction with its evidence needs. Neutral updates, stories, and instructions are not forced into advocacy.
- **L3.6 Reads aloud** — Wording and rhythm feel natural for the requested audience and genre; preserve useful commas and semicolons.

### Process integrity
- **P.4 Form fits purpose** — The output suits this specific piece and honors any requested template or format; no default corporate structure.
- **P.1 No meaning lost** — The edit preserves the author’s argument and facts, including actor/action, negation, quantities, scope, attribution, causal status, conditions, and certainty. Trimming must not cut the point or change the strength of the evidence. This is the one dimension that outranks all others: an edit that tightens prose but changes or guts the meaning is a FAIL regardless of every other PASS.
- **P.2 Right mode** — The output matches the requested mode (Voice Check flags without rewriting; Quick Tighten stays mechanical and brief).
- **P.3 Honest commentary** — Change notes name real structural/voice changes, not obvious mechanical fixes, and don't overclaim what the edit did.

---

## Scorecard Format

```
CASE: <id>
MODE: <requested mode>
MODEL / HARNESS / DATE / SKILL REVISION: <actual values>
REVIEWER: <who examined the actual output>
PROMPT / OUTPUT: <saved artifacts>
INPUT WORDS / OUTPUT WORDS: <observed counts; no quota>
RUBRIC: <applicable IDs, PASS/FAIL/N/A, and evidence from the output>
EXPECTED CATCHES: <caught and missed, with evidence>
VERDICT: <PASS/FAIL/NOT RUN>
```

A run is a PASS only if every applicable rubric dimension passes **and** every expected catch is caught. Report structural validation separately; it does not establish writing quality. Missing output or unperformed grading is UNVERIFIED, never PASS. A model’s claim that it passed is not a scored result; the tested model cannot serve as its own independent judge.

---

## Case Bank

Each case is a small input engineered to trip a specific rule. The **Expected Catches** are the violations a correct run must fix or flag. Keep inputs short so a full eval is cheap to run.

### C1 — Adverbs and weak verbs
> "She quickly walked into the room and softly said that the project was basically done."

**Expected catches:** Tighten wording while preserving manner and incomplete status. Soft speech is not necessarily whispering; "basically done" must not become "done." No one-clause or adverb quota.

### C2 — Passive voice
> "The decision was made by leadership that the launch would be delayed by the team until the issues were resolved by engineering."

**Expected catches:** three passive constructions; rewrite with actors performing actions. Word count should drop sharply.

### C3 — Corporate euphemism (Layer 3)
> "After a thoughtful review, we've decided to rightsize the organization and sunset several initiatives to better align with our core strategic priorities going forward."

**Expected catches:** Flag the euphemisms and vague rationale. Name layoffs only if the source establishes them; otherwise ask what "rightsize" entails or mark it as unresolved. Do not invent a headcount or motive.

### C4 — AI slop density (Layer 2)
> "It's important to note that in today's fast-paced world, leveraging a robust ecosystem of solutions can empower teams to unlock their full potential and navigate the ever-evolving landscape. Let's dive in."

**Expected catches:** `it's important to note`, `in today's fast-paced world`, `leveraging`, `robust ecosystem`, `empower`, `unlock their full potential`, `navigate`, `ever-evolving landscape`, `let's dive in`. After the sweep, almost nothing of substance remains — the correct note says so: this paragraph carries no information. Suggest a concrete argument to investigate and the evidence needed, without presenting it as established fact.

### C5 — Overclaiming (Layer 3)
> "Everyone knows AI changes everything. No one is talking about how this will reshape every single industry on earth, but it absolutely will."

**Expected catches:** `everyone knows`, `changes everything`, `no one is talking about`, `every single industry`, `absolutely will`. Flag unsupported scope. The input gives no evidence, so do not replace these with smaller invented claims; suggest a testable thesis and its evidence needs.

### C6 — Hedge sandwich + insight-free conclusion (structural)
> "Remote work is the future. Of course, it might not suit every company, and there are many factors to consider. But in many ways, it could be argued that remote work is probably the future. In conclusion, it's a complex topic with many dimensions."

**Expected catches:** hedge sandwich (claim → qualify → soft restatement), `many factors to consider`, `in many ways`, `it could be argued`, `probably`, insight-free conclusion. Identify the unsupported thesis and empty qualification. Propose a more specific argument to test without inventing evidence or erasing genuine uncertainty.

### C7 — Already-tight prose (false-positive guard)
> "We shipped late. The login flow broke under load, so we held the release four days to fix it. It cost us the launch-week press, and that was the right call."

**Expected catches:** *none.* This is the control case. A correct run changes little, does not invent slop to remove, does not pad to justify itself, and does not cut meaning to force a 10%. Over-editing this is a FAIL.

### C8 — Legitimate trigger word (judgment guard)
> "The change shipped to the iOS ecosystem first because the regulatory landscape shifted after GDPR, and we needed leverage in the negotiation."

**Expected catches:** *none of the flagged words should be removed.* `iOS ecosystem`, `regulatory landscape` (tied to GDPR), and financial-sense `leverage` all pass the earn-its-place test. Stripping them mechanically is a FAIL — this case checks that the skill flags with intent, not on autopilot.

> Cases C7 and C8 matter as much as the violation cases. A skill that only ever cuts is a blunt instrument. The eval has to prove restraint, not just aggression.

---

### C9 — Warranted uncertainty
> "It is important to note that the result may reflect selection bias; the sample is too small to decide."

**Expected catches:** remove the empty opener while preserving uncertainty and the sample limitation. Turning this into a definite causal claim fails P.1 and L3.4.

### C10 — Requested mode
> User: "Check the voice; do not rewrite." Draft: "We are leveraging our ecosystem to drive outcomes."

**Expected catches:** name vague phrasing and missing specifics. Give observations without a replacement draft. Rewriting fails P.2.

### C11 — Influencer cadence and decorative triads
> "Here's the thing. Your hiring process? Broken. Slow. Stale. Soulless. It's not about people. It's about possibility. We need speed, scale, and synergy."

**Mode:** Full Edit. **Expected:** Remove the staged attitude, fragments, false binary, and empty triad. Say the argument lacks supporting detail; suggest a concrete hiring question and evidence needed. Do not invent a failure rate.

### C12 — Meaningful uncertainty and modifiers
> "The pilot may reduce review time by about 10%. We have only tested it with six reviewers, so the estimate is provisional."

**Mode:** Quick Tighten. **Expected:** Keep "may," the approximation, 10%, six reviewers, and provisional status. Do not force a shorter version or make the result certain.

### C13 — Technical language and a real set of three
> "The service uses idempotency keys to prevent duplicate payments. Requests can be pending, succeeded, or failed."

**Mode:** Quick Tighten for engineers. **Expected:** Preserve the technical meaning and all three states; do not remove an item to avoid a rule of three.

### C14 — Natural connected sentences
> "We held the release because the login flow failed under load; the fix is ready, but we still need to repeat the load test."

**Mode:** Quick Tighten. **Expected:** Preserve the cause, fix status, and outstanding test. The semicolon and connected rhythm may remain; do not manufacture punchy fragments or claim the release shipped.

### C15 — Form follows a practical update
> "Write a two-sentence update to a colleague: the pilot starts Tuesday; Alex will send the invite Monday."

**Mode:** Write from scratch. **Expected:** Two sentences with those facts. No executive summary, pillars, invented dates, argument, or headings.

### C16 — Quotation and a requested template
> "Keep the headings Decision and Evidence. Under Evidence, preserve this exact quote: ‘We need speed, scale, and synergy.’ The quote is the claim we are assessing; we have no supporting data."

**Mode:** Full Edit. **Expected:** Preserve both headings and the quote. Identify missing evidence without silently editing the quotation, inventing data, or changing the requested form.

### C17 — Voice check stays a review
> "Check the voice without rewriting: We sent the revised contract on Friday. The client has not replied."

**Mode:** Voice Check. **Expected:** Say it is clear if no material issue exists. No rewrite, invented flaw, forced viewpoint, or word-count cut.

## Self-Learning Loop

Run this whenever an eval fails. The goal is a durable fix to `SKILL.md`, not a one-off correction of the output.

1. **Name the failure precisely.** Which rubric dimension, which case, what survived or what was wrongly cut. "L2.3 — `delve` survived in paragraph two."

2. **Classify it:**
   - **Miss** — a real violation the skill didn't catch. The rule exists but wasn't applied or wasn't specific enough.
   - **False positive** — the skill "fixed" something that was already correct (see C7/C8). The rule is too aggressive or lacks an exception.
   - **Gap** — the violation isn't covered by any rule. The skill needs a new rule.
   - **Meaning loss (P.1)** — the edit changed the argument. Always the highest-priority fix.

3. **Find the smallest change to `SKILL.md` that prevents recurrence.** Prefer sharpening an existing rule over adding a new one. Clarify a decision criterion or add a narrow exception; avoid turning a contextual failure into a blanket word ban. Do not bolt on a whole new section for a single miss.

4. **Write the change against the skill's own standard.** Keep the edit plain and specific, preserving any qualifications needed for accuracy. The skill’s documentation should model its guidance.

5. **Add a regression case.** Turn the failing input into a permanent entry in the Case Bank with its expected catches. The bug becomes a test. A fix without a regression case isn't done.

6. **Re-run the affected cases plus the new one and C7–C17 controls relevant to the changed rule.** Confirm the fix works and that it didn't break C7/C8 (over-correction is the most common regression).

7. **Record it** in the Change Log below: what failed, the root cause class, the rule changed, the case added.

### Change Log

| Date | Failing case | Class | Rule changed | Regression case added |
|------|--------------|-------|--------------|-----------------------|
| _seed_ | — | — | Initial eval harness | C1–C8 |
| 2026-09-06 | Specification update; no behavioral score implied | Conflicting requirements | Replaced quotas and blanket bans with contextual judgment; added argument, rhythm, and form checks | C11–C17; strengthened C9; clarified C1, C3–C6 |

---

## What "Better" Means Here

The skill improves along two axes, and they pull against each other:

- **Recall** — catching more real violations (driven by violation cases C1–C6).
- **Precision** — not damaging prose that's already right (guarded by C7–C8).

A change that raises recall by lowering precision is not an improvement; it's a trade. Every proposed edit to `SKILL.md` has to hold both. When the Case Bank grows, keep the ratio honest: for every new violation case, the control cases should still pass. The day the skill starts "fixing" C7 is the day it stopped being an editor and became a word filter.
