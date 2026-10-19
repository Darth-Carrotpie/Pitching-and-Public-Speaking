# Intake

Learn enough to write, in one round of questions.

## 1. Extract first

Read the request and any attached material. Fill in every must-know you can.
Never ask about something the user already told you.

## 2. Must-knows

Ask only the missing ones, in one message, at most 6 questions. Give each a
suggested default the user can accept with "ok".

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

Check before the first draft, if the speech will have slides. Look through the
tools and skills you have for a slide builder:

- a PowerPoint / .pptx skill or tool
- a Google Slides or Google Drive connector
- a Figma Slides, Canva or Gamma connector
- a slide-deck artifact type or another presentation integration

**Found one:** say in one line which tool you'll use at hand-over.
**Found several:** name them and suggest one.
**Found none:** tell the user, briefly, and carry on without waiting:

> No slide tool is connected here. I'll still write the full slide spec. Then you can:
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
