# Intake

Learn enough to write, in one round of questions.

## 1. Extract first

Read the request and any attached material. Fill in every must-know you can.
Never ask about something the user already told you.

## 2. Must-knows

Ask only the missing ones, in one message: at most 6 answer requests in total.
Count what you actually ask, not the numbering: an item that asks three things
counts as three. Give each request a suggested default the user can accept with "ok".
Things the user already gave (length, audience type, product, numbers) are not
missing; details they didn't give (who decides, whether there's Q&A) can be.

| # | Must-know | Ask like |
|---|---|---|
| 1 | **Goal**: what the audience should do, decide or believe afterwards | "After your talk, who should do what?" |
| 2 | **Audience**: who, how many, their expertise, how they feel about the topic, who decides | "Who's in the room, and who makes the call?" |
| 3 | **Setting**: length, live or online, room size, Q&A or not, slot in the agenda, other speakers | "How long, and is there Q&A?" |
| 4 | **Slides**: with, without or undecided; presented only, or also sent ahead (leave-behind) | "Slides? Will the deck be emailed too?" |
| 5 | **Speaker**: role, why they're credible, what comes naturally (stories, humour), how they'll deliver (read, memorize, cue cards) | "Do jokes come naturally to you?" |
| 6 | **Material**: facts, data, stories, an existing deck or script, must-include items, constraints | "What numbers or stories can I use?" |

The speech type sets the defaults:

| Type | Typical length | Slides | The goal usually is |
|---|---|---|---|
| Pitch (investor, sales, partner) | 3–10 min + Q&A | yes, often plus a leave-behind | a next meeting, a decision, money |
| Talk / keynote | 5–20 min | usually | a belief, plus one action |
| Internal business | 2–10 min | optional | a decision or an approval |
| Occasion (toast, farewell, award) | 2–5 min | no | a shared moment (the toast, the wish) |

## 3. Go deeper only where it changes the speech

- **The elephant in the room**: what might stop this audience from hearing you (`message.md`)
- What has been tried before, and how it went
- Who influences the decision but won't be in the room
- Hard constraints: legal, brand, confidentiality

If the user says "just write it" or "no questions": use the defaults, list your
assumptions at the top of `brief.md`, and continue.

## Slide tools

Check before the first draft, if the speech will have slides. Only count what you
can see in your own tool and skill list, and sort it into three levels:

| Level | Means | Example |
|---|---|---|
| **Callable** | a tool or skill that creates or edits slides, which you can invoke now | a .pptx skill, a slides-editing action, a deck artifact type |
| **Connector only** | access to a service, but no action that builds slides | a Google Drive connection with file tools only |
| **Unknown** | you can't inspect your tools | most chat-only hosts |

Report it in one line, with the level and how you know: "Found: pptx skill
(callable, in my skill list). Google Drive (files only; I can't confirm Slides
editing)." Never name a tool you didn't actually see. Treat "connector only"
and "unknown" as no tool.

**At least one callable:** name it and suggest it for the hand-over.
**None callable, or unknown:** tell the user, briefly, and carry on without waiting.
Write `slides.marp.md` as soon as drafting starts (`slides.md`, "Hand-off"):

> I can't build slides directly here. I'll still write the full slide spec. Then you can:
> 1. **Use the fallback.** I'll also write `slides.marp.md`. It opens as a deck in
>    VS Code with the Marp extension, or `npx @marp-team/marp-cli@latest slides.marp.md --pptx`
>    turns it into a PowerPoint file.
> 2. **Connect a tool.** Add a PowerPoint skill or a Google Slides, Canva or Figma
>    connector to this agent, then ask me to build the deck.
> 3. **Build it yourself.** Each slide in the spec has its headline, visual and text,
>    ready to paste into any slide app.

## Files

Check whether you can write files (file tools or a working directory). If not,
everything goes into one chat document (`SKILL.md`, "Output").
