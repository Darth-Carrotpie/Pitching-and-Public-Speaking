# Roadmap

Status: v0.1 is out for real-world use (2026-10-19). Collect real sessions first, then
pick a sprint. Eval history lives in `evals/independent-review-iteration-*`.

## Where it stands

| Round | Runner | With podium | Baseline | Notes |
|---|---|---|---|---|
| 1 | Claude, 11 evals, 46 checks | 35/46 (76%) | 22/46 (48%) | Podium won 10 of 11 |
| 2 | Codex, 8 of 11 evals graded, 55 checks total | 31/41 (76%) | 12/41 (29%) | Podium won all 8 graded; incomplete (see below) |

Round-1 fixes confirmed in round 2: pause-inclusive timing, slide-tool levels plus the
Marp fallback, spar's single opening question.

## Sprint 1: when to stop and ask (regressions from round 2)

- **Create mode drafted without intake** (eval 1). Skip intake only when the user
  explicitly says "just write it" or similar; otherwise ask the missing must-knows and
  end the turn. Likely cause: the new "just write it" rules in `script.md`.
- **Review mode stopped at the goal question** (eval 7). Propose a default goal, state
  it, and deliver the full review (scorecard, top 3, rewrites) in the same turn.
- **Coach mode precision** (eval 8). Count every "so" (sentence opener or pause).
  The rewrite's first sentence states the result and its last sentence asks for a dated
  decision. The summary never states the cause of an overrun as fact.

## Sprint 2: accuracy beyond numbers

- Qualitative market or product claims ("scheduling is critical for clinics", an
  expansion plan) need a source or an explicit "assumption" label, not just numbers (eval 4).
- Every `[NEEDS SOURCE]` names the source type, the year and the unit it needs.
- Companion files (cue cards, leave-behind, Q&A prep) drifted into inferences in
  round 2 (eval 1: same-day measurement, cohort implications). Add a final pass that
  reads only the companion files against the brief's fact list.

## Sprint 3: finish and harden the evals

- Finish round 2: grade evals 2, 10 and 11, rerun the eval 2 baseline (no reply was
  produced), and write the combined `evaluation.json` / `report.html`.
- Eval 1 passed 4/5 for both runs because universal clauses are vacuously true when no
  questions are asked. Make "asks intake questions and stops" an explicit expectation.
- Run each eval 3 times per configuration; one sample per prompt isn't stable.
- Keep a mocked tool registry for slide-tool evals (with tools / without tools).
- Add trigger evals (should / shouldn't trigger) and run the skill-creator description
  optimiser.

## Ideas for later

- **Lighter output for small requests.** Toasts and 2-minute speeches still produce a
  4–5 file kit (7–12 min runs in round 1). Offer a "script only" path.
- **Speaking rate per language.** 130 wpm may be fast for Lithuanian; make the rate a
  per-language default the user can override.
- **Occasion timing.** Hand-raises and toasts push openings and closings past the
  15% / 10–15% guideline; allow an exception for occasions.
- **Real slide hand-off.** Test the actual delivery to a PowerPoint skill and Google
  Slides, not just detection.
- **Release zip for claude.ai.** A GitHub Action that packages `skills/podium` on tag,
  so Claude-app users don't have to re-zip by hand.
- **Translations of the README**, starting with Lithuanian.

## In the wild: what to note

For each real session, jot down: the speech type, what the user asked, where podium
asked too much or too little, any invented or deduced fact, whether the timing held
when spoken aloud, and whether the speech got its result. Add notable cases to
`evals/evals.json` as new prompts.
