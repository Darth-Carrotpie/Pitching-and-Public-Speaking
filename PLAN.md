# Planning notes (working doc, delete when the skill ships)

## Goal
Agent skill that builds a speech, with or without a slide deck, that gets the speaker a specific outcome.
Quality bar for every output:
- Accurate and clear, achieves its goal
- Visual / tells a story
- Inspires action: ends with a clear call to action

## Decisions
| Topic | Decision |
|---|---|
| Packaging model | Follow ponytail: one source `skills/<name>/SKILL.md`, compact `AGENTS.md`, thin per-agent adapters, install steps for each agent in README |
| Scope v1 | Pitches, talks/keynotes, internal business, occasion speeches |
| Outputs | Full speech script, slide-by-slide spec, speaker notes / cue cards, rehearsal kit. One reference file per output |
| Intake | Adaptive must-knows: infer from the first message, ask only what is missing (goal/desired action, audience, duration/setting, slides y/n, speaker role, constraints) in one batch, go deeper only where needed |
| Sources | User's workshop notes (Notion) are the core method. Well-known frameworks fill gaps and back them up |
| Structure choice | Offer 2–3 fitting structures, each with an outline preview, and let the user pick |
| Slides | Check for a slide tool at session start (pptx skill, Google Slides, deck artifact…). If one exists, delegate the spec to it. If not, explain the Marp Markdown fallback, or how to connect a slide tool |
| Modes v1 | Create, Review existing, Rehearsal coach (transcript feedback), Q&A sparring, Adapt/shorten |
| Language | Skill and README in English. Speeches come out in the user's language (default, not yet confirmed) |
| Name | `podium` |
| Mode switching | One skill plus a mode argument: `/podium [create\|review\|coach\|spar\|adapt]`. Natural language routes to the same modes |
| Output location | Folder per speech: `speeches/<slug>/` with brief.md, script.md, slides.md, notes.md, rehearsal.md |
| Install audience | Coding agents (Claude Code, Codex, Copilot CLI + VS Code, Cursor, Gemini CLI), Claude apps (.zip upload), long tail (`npx skills add` + AGENTS.md). ChatGPT/Gemini chat left out of v1 |
| License | MIT (replaces the GPL-3.0 in the initial commit) |
| Slide spec | For each slide: assertion headline, visual type (big number, photo, chart, diagram, quote), one-line visual brief, and the speaker line it supports |
| No-filesystem hosts | Auto-detect: write the folder when files can be written, otherwise one Markdown doc in chat with the same sections |
| Examples & evals | One worked example per speech type in `examples/`, plus a small evals file (test prompts + expected behaviour) |
| Notion case | Method only. The real internal case from the workshop is not used; all examples are written from scratch |
| Message gate | Hard gate: no structure or draft until the goal and a one-line message pass the tests. The agent proposes 2–3 candidate messages |
| Checklist | Fix silently, show only the misses (items that can't be fixed or that need user input) |
| Delivery coaching | Tailored top 3 techniques for this speech and speaker, plus a day-of checklist. The full list stays in the reference file |
| Deck types | One spec, two densities: the presented deck (image + key words) and an optional leave-behind (adds 1–2 context sentences per slide) |
| Fact rule | Never invent facts, numbers or quotes. Claims that need proof get `[NEEDS SOURCE: …]` and are listed at hand-over |
| Adapters | `.claude-plugin/` (Claude Code + Copilot CLI) and `AGENTS.md`. Everything else uses `npx skills add` or a manual copy (`~/.agents/skills/` is read by Codex, Copilot, Cursor and Gemini CLI) |

## Method digest (from the workshop notes, method only)
**Goal and message first.** Do the homework before speaking. The goal is a verb (persuade / change / achieve) about changing or deciding something, not just telling. If the goal is too big, step one level down. Message tests: (1) what an attendee would tell a colleague who wasn't there, (2) the headline a journalist would write, (3) a slogan on a supporter's banner, (4) the 3-second version. Lead with the message, not the facts: say what is being done and how it is handled, not everything that is known. Be clear about what you want from the audience.
**Arguments.** Pick 3, even for broad topics (people don't remember more, and neither does the speaker). Choose the ones that best support the goal. Don't mix arguments with means: the audience doesn't need the technical details. Sell the island, not the plane: what's in it for the listener, not how you work. Nobody checks the facts or cares how much work went in, so present the value. Arguments can be folded into the problem or the solution. Sharpen the problem.
**Audience.** Define what you want first, then find where the audience is: their demographics, their relationship to the topic, their level. Ask why they wouldn't do what you ask. The elephant in the room is whatever will stop them hearing you: fear, beliefs, values, lack of attention, (lack of) experience, loss of power, distrust ("I know you don't trust me"), habits and traditions. The elephant can be parked: named and addressed, not necessarily chased out. Ask questions instead of only making statements (in the selling exercise: 12 statements, 0 questions).
**Structures.** What? Where? → Why? → How? Proof: tell → justify → summarize (if longer than 2 min) → invite. Situation: situation → problem → solution. Benefit: problem → solution → benefit. Monroe's Motivated Sequence: attention → problem → solution → visualize → action. Story/change: situation → action → result/change.
**Opening (about 15%).** Curiosity in the first sentence. Connect (similarities, a story, self-deprecation), engage (a question, story, image, task, or humour that is natural to you), or surprise (a quote, statistic, strong claim, exaggeration, worst case, or a fact the audience doesn't know). At most 2 questions. Have 3 different openings ready and differ from the other speakers. Memorize the first 3–5 sentences. The name can go inside the story.
**Body.** Short, familiar, conversational words. Simple sentences. Pauses, because people remember after a pause. Examples, illustrations and visual aids. Vary the voice. Amplifiers: an image (understood faster, remembered longer), emotion (multi-sensory: touch, smell, taste, pain or pleasure), rhythm (repetition, alliteration, anaphora: "I have a dream…", "the race to replace"). Analogies must be tested on an outsider.
**Clarity filters (ŽABT).** Speak to one specific non-expert person (a neighbour, or "explain it to grandma"). Be active: verbs, first person ("it is believed" → "I think"). Keep it simple and short: cut the text in half, then in half again. Spoken language, not written.
**Closing (the most important part).** Protect its time: if Q&A eats the time, skip content and go to the close. Summarize, giving each argument about 3 key words. The call to action is more concrete than the message: what do listeners do when they leave, and which first step starts the change? Optionally restate your personal "why". No "thank you" ending. After Q&A, close and call to action again. The last impression is what lasts.
**Slides.** They are for the listener, not the speaker. If you can manage without them, do. Otherwise each slide is an image (one that supports the message, simple and memorable) plus the essence (key words, not sentences). A slide is not your notes. Ask of each visual: does it expand the information, and does it help retention?
**Delivery methods.** Reading, memorized (only the opening and closing), outline/cue cards (story beats), spontaneous.
**Rehearsal.** 3 times aloud in your own words, without reading. Record yourself and count words per minute (120–140 is normal). Rehearse in portions (the opening on the way in, the next part on the way home). The 3-second pause drill (pause after every period and comma for 3+ minutes) gives simpler words, shorter sentences and better intonation. For important talks, test on a neighbour or outsider for the analogies and the message. Self-assessment of the content: message, engagement, structure. Of yourself: how it felt, eye contact. Pick 3 techniques and master them, then add 3 more a year later.
**Nerves and the day.** Breathing (square or triangle, slow and deep). Grounding: standing, feel the feet and soften the knees; seated, sit on the chair's edge with a straight back and tense and release muscle groups. A power movement, power words, an inner picture of the start and the end. Worst-case thinking, positive goals, attention focus, the "game of meaning". Drink water, and avoid coffee, alcohol, pills and milk. Do a checklist (WC, water). The audience wants you to succeed. Make a mistake, keep going. Nobody knows what you planned to say.
**Stage.** Gestures scale with the room. Walk with purpose (know why and where you move). If the mic shakes, rest it against your chin. Lighthouse eye contact. Tell the audience when you'll take questions.
**Q&A.** Listen and repeat the question. Think, then answer the whole room (lighthouse). Ask for clarification instead of guessing. Thank the asker and use the answer to reinforce the message. Don't take offence, argue or lose your temper. Be firm but polite. Find common ground. Check whether the question interests the whole audience.

## Source access
- Notion pages (login-walled; read through the claude.ai Notion connector):
  - Public Speaking notes: https://app.notion.com/p/Public-Speaking-anas-3fe8fdfd1256808b98e2c036fe9c3e71
  - Viešo kalbėjimo mokymai: https://app.notion.com/p/Vie-o-kalb-jimo-mokymai-3d48fdfd1256805c9a6cd33d700a7d51

## Status
Plan approved 2026-10-19. Built on branch `podium-v1`.
