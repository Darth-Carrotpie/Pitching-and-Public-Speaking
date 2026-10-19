# Example: 6-minute meetup talk

> Fictional speaker and numbers. Shows the Sparkline structure and the Marp fallback when no
> slide tool is connected.

## The request

> I'm giving a 6-minute talk at our product meetup (about 80 product managers, designers and
> engineers). Topic: ship the boring version first. Last year my team spent 4 months on a smart
> scheduling feature; 11 people ended up using it. This year we shipped a "boring" version of a
> reporting feature in 3 days: a spreadsheet export plus a weekly email. 40% of beta users used
> it every week, and only then did we build the real thing. I want slides.

## Set-up note (no slide tool found)

> No slide tool is connected here. I'll still write the full slide spec. Then you can:
> 1. **Use the fallback.** I'll also write `slides.marp.md`. It opens as a deck in VS Code with the
>    Marp extension, or `npx @marp-team/marp-cli@latest slides.marp.md --pptx` turns it into PowerPoint.
> 2. **Connect a tool.** Add a PowerPoint skill or a Google Slides, Canva or Figma connector, then ask me to build the deck.
> 3. **Build it yourself.** Each slide in the spec has its headline, visual and text, ready to paste.

## Intake

> 1. **Goal**: what should people do after the talk? *Suggested: try one boring-first experiment in their
>    next sprint, and post the result in the meetup's Slack before the next meetup.*
> 2. **Speaker**: do jokes come naturally? *Suggested: light self-deprecation about the 4-month feature.*

User: "Yes. The Slack channel is #boring-first."

## Message gate

**Goal:** By the next meetup, attendees run one boring-first experiment and post the result in #boring-first.

**Message (confirmed):** Ship the boring version first. Then earn the clever one.
(Retell ✓ · Headline ✓ · Banner ✓ · 3 s ✓)

**Arguments**
1. **Users vote faster.** The boring version shipped in 3 days, and real use beat a roadmap debate.
2. **Clever is expensive.** 4 months on a feature almost nobody used.
3. **Boring is honest.** It tells you whether the problem is real before you fall in love with the solution.

**Elephant:** craft pride. "Boring feels like bad product work; we're here to build delightful things."
Parked in the opening (self-deprecation) and the turn: boring first, not boring forever.

## Structure options offered

1. **Sparkline** (recommended): alternate "what is" (months of building) with "what could be"
   (days to the truth), and end on the new bliss: a team that earns its clever features.
2. **Story spine**: Once upon a time we built a clever feature… Until finally… Ever since then…
3. **Benefit**: problem → boring-first → benefit. Clear, but flatter for a meetup.

User picked 1.

## Output: `speeches/boring-first-meetup/`

### script.md (excerpt)

~~~markdown
# Ship the boring version first: script
~700 words · ~5:25 at 130 wpm · slot: 6 min

## Opening (0:00–0:50) [SLIDE 1]
[MEMORIZE] Last year my team built the smartest feature of our careers. /
It took four months. / It learned your habits. / It scheduled your week for you. //
Eleven people used it. // Not eleven thousand. / Eleven. //
This year we shipped a spreadsheet and an email. / In three days. /
Four out of ten beta users opened it every single week. //
So tonight I want to sell you something unglamorous: /
**ship the boring version first. / Then earn the clever one.**

## What is: four months in the dark (0:50–1:50) [SLIDE 2]
...

## What could be: three days to the truth (1:50–2:50) [SLIDE 3]
...

## Closing (4:40–5:25) [SLIDE 6]
Users vote faster. / Clever is expensive. / Boring is honest. //
So here's my ask. / In your next sprint, / pick one feature on your roadmap / and ask:
what's the boring version I could ship by Friday? //
Ship it. / Then post what happened in **#boring-first**, / before we meet again next month. //
I'll read every one. // Four months, or three days. / You choose.
~~~

The three openings offered were **Connect** ("Who here has shipped a feature nobody used?"),
**Surprise** (the "eleven people" story, recommended) and **Engage** (a small task: "Write down the
last feature you shipped, and how many people use it weekly.").

### slides.md → slides.marp.md (excerpt)

~~~markdown
---
marp: true
paginate: true
---

# 4 months. 11 users.

![bg right:45%](placeholder-empty-calendar.jpg)

<!-- Last year my team built the smartest feature of our careers. Eleven people used it. -->

---

# A spreadsheet and an email reached 4 in 10 beta users weekly

![bg right:45%](placeholder-spreadsheet-email.jpg)

<!-- This year we shipped a spreadsheet and an email. In three days. -->

---

# Ship the boring version first. Then earn the clever one.

<!-- Post your experiment in #boring-first before the next meetup. -->
~~~

Image placeholders to replace: `placeholder-empty-calendar.jpg`, `placeholder-spreadsheet-email.jpg`.

### rehearsal.md (excerpt)

**Your top 3 techniques**
1. **Pause after "Eleven people used it."**: the laugh needs room. Count to three.
2. **Move with purpose**: stage left for "what is", stage right for "what could be". The audience
   will feel the sparkline.
3. **The outsider test**: try the opening on a friend outside tech. Does "boring version" land without explanation?

## Hand-over

> **Message:** Ship the boring version first. Then earn the clever one.
> **Structure:** Sparkline, 5:25 of a 6:00 slot. Deck: 6 slides as `slides.marp.md` (no slide tool connected).
> **Needs you (1):** two images to replace the placeholders.
> **Rehearse first:** the opening, until the pause after "Eleven people used it" feels natural.
