# Example: 3-minute investor pitch

> Fictional company and numbers. Shows what podium produces for a pitch with a
> presented deck plus a leave-behind.

## The request

> I'm pitching my startup Leftover at an angel investor evening next Thursday. 3 minutes,
> then 5 minutes of Q&A. Leftover tells restaurant chefs each morning how much food to prep,
> based on till data, bookings and weather. Pilot: 14 restaurants, 8 weeks, prep waste down
> 31% on average. 9 of the 14 now pay €290/month at full price. I was a head chef for 9 years
> (120-seat kitchen, we binned about 40 prepped portions a night). My co-founder Mia built
> forecasting models for a grocery chain. We're raising €600k for 18 months: 2 engineers and
> a sales lead, aiming for 150 paying restaurants. The deck will be emailed to everyone afterwards.

## Intake

Podium already had the length, Q&A, audience type, slides (presented and leave-behind),
material and team, so it asked only:

> 1. **Goal**: is it realistic to close investment on the night, or is the goal a follow-up
>    meeting? *Suggested: at least 3 angels book a follow-up meeting this week.*
> 2. **Speaker**: how do you feel on stage? Do jokes come naturally? *Suggested: no jokes,
>    a calm, credible chef's story.*

User: "ok to both, I talk fast when nervous."

## Message gate

**Goal:** After the pitch, at least 3 angels book a 20-minute follow-up this week.
(One step down from "invest €600k".)

| Candidate | Retell | Headline | Banner | 3 s |
|---|---|---|---|---|
| "Leftover cuts restaurant food waste by a third, and restaurants pay for it." | ✓ | ✓ | ✗ | ✗ |
| "Restaurants bin their profit every night. Leftover stops it." | ✓ | ✓ | ✓ | ✓ |
| "A third less waste, paid back in the first month." | ✓ | ✓ | ✓ | ✓, but "paid back" is unproven: `[NEEDS SOURCE: monthly saving per restaurant]` |

**Message (confirmed):** Restaurants bin their profit every night. Leftover stops it.

**Arguments**
1. **Pain they pay for.** 9 of 14 pilots pay full price. Island for investors: a market that pays.
2. **Proof in weeks.** 31% less prep waste in 8 weeks.
3. **Built by a chef.** The founder lived the problem; the co-founder built forecasting at a grocery chain.

**Elephant:** "Restaurants are a terrible market: thin margins, slow to adopt tech, high churn."
Parked in argument 1 (they pay full price) and in the Q&A prep (only 8 weeks of churn data; said honestly).

## Structure options offered

1. **Monroe's Motivated Sequence** (recommended): attention (the chef's bin) → problem →
   solution + proof → visualize a year from now → ask. Strong for a live 3 minutes.
2. **Investor order, compressed**: problem → solution → traction → market → team → ask.
   Familiar to investors, less memorable on stage.
3. **Story / change**: one pilot restaurant before → Leftover → after. Memorable, thin on the business.

User picked 1.

## Output: `speeches/seed-pitch-leftover/`

### script.md

~~~markdown
# Leftover: script
289 words = 133 s · 11 long pauses = 28 s · total 161 s · limit 162 s (90% of 3 min) · then 5 min Q&A

## Opening (0:00–0:22) [SLIDE 1]
[MEMORIZE] For nine years I ran a kitchen with 120 seats. / Every night I closed it the same way. //
I scraped about forty prepared portions into the bin. //
Not because the food was bad. / Because I guessed wrong that morning. //
Restaurants bin their profit every night. / **Leftover stops it.**

## Problem (0:22–0:45) [SLIDE 2]
Every morning a chef decides how much to prep. / Too little, and you run out at eight. /
Too much, and it goes in the bin at midnight. / So we all prep too much. //
That's not a rounding error. / It's [NEEDS SOURCE: share of food cost lost to prep waste] of food cost: /
money the restaurant already paid, thrown away.

## Solution and proof (0:45–1:23) [SLIDE 3]
Leftover reads the till, the bookings and the weather, / and every morning it tells the chef: /
prep this much. // One screen, before the first coffee. [SLIDE 4]
We tested it in 14 restaurants for 8 weeks. / Prep waste fell by **31 percent**. //
And here's the part that matters to you: / 9 of those 14 now pay us 290 euros a month. /
Full price. / No discount. //
You've heard restaurants are a hard market. / They are. / They pay when the saving shows up in their own bin.

## Visualize (1:23–1:50) [SLIDE 5]
Picture a Saturday night a year from now. / A full room. / A kitchen that runs out of nothing, /
and closes with an empty bin. //
Now picture that in 150 restaurants. / That's our plan for the next 18 months. /
I know this problem from the inside. / Mia, my co-founder, built forecasting for a grocery chain. /
A chef and an engineer.

## Ask and close (1:50–2:15) [SLIDE 6]
We're raising 600 thousand euros: / two engineers and a sales lead, for 18 months. //
Pain they pay for. / Proof in weeks. / Built by a chef. //
If you've ever seen a kitchen at midnight, / book twenty minutes with me this week. /
The code is on the screen. // **Let's empty the bins.**

## Final close (after Q&A)
One more time: restaurants bin their profit every night. / Leftover stops it, /
and 9 of 14 pilots pay full price. / Twenty minutes this week. The code is on the screen.
~~~

The three openings offered were **Connect** (the chef's bin, recommended), **Engage** ("Raise your
hand if you've ever worked in a kitchen") and **Surprise** ("The most expensive dish on any menu is
the one nobody orders").

### slides.md

~~~markdown
# Leftover: slides
Presented + leave-behind · 6 slides · style: warm, kitchen photography, one accent colour

## Slide 1: Restaurants bin their profit every night
- **Visual:** photo: a full kitchen bin under harsh light at closing time
- **On-slide text:** Leftover
- **Speaker line:** "I scraped about forty prepared portions into the bin."
- **Leave-behind:** Leftover tells chefs each morning how much to prep, so less food is thrown away.

## Slide 2: Chefs guess every morning, and guess high
- **Visual:** diagram: two-sided scale, "run out at 8 pm" vs "bin at midnight", tipped toward the bin
- **On-slide text:** Too little · Too much
- **Speaker line:** "So we all prep too much."
- **Leave-behind:** Prep is decided by gut feel. Running out costs reputation, so kitchens over-prep. [NEEDS SOURCE: prep-waste share of food cost]

## Slide 3: One screen tells the chef what to prep
- **Visual:** product screenshot: the morning prep list on a phone, one item highlighted
- **On-slide text:** Till · Bookings · Weather
- **Speaker line:** "Every morning it tells the chef: prep this much."

## Slide 4: 31% less waste, and 9 of 14 pilots pay full price
- **Visual:** big numbers: "31%" and "9/14", side by side
- **On-slide text:** 8 weeks · €290/month
- **Speaker line:** "Full price. No discount."
- **Leave-behind:** An 8-week pilot in 14 restaurants; waste measured by [NEEDS SOURCE: method and baseline]. 9 converted to paid.

## Slide 5: 150 restaurants in 18 months
- **Visual:** photo of a closing kitchen with an empty bin; small founder photos in a corner
- **On-slide text:** Chef + engineer
- **Speaker line:** "A chef and an engineer."

## Slide 6: €600k to reach 150 paying restaurants
- **Visual:** big number "€600k" + a QR code to book a call
- **On-slide text:** 2 engineers · 1 sales lead · 18 months
- **Speaker line:** "Book twenty minutes with me this week."
~~~

The leave-behind adds an appendix: unit economics `[NEEDS SOURCE: CAC, churn after 3+ months]`
and team bios.

### notes.md (2 of 6 cards)

~~~markdown
## Card 1: Opening [0:00] [SLIDE 1]
(word for word)
"For nine years I ran a kitchen with 120 seats. Every night I closed it the same way.
I scraped about forty prepared portions into the bin. Not because the food was bad.
Because I guessed wrong that morning."

## Card 3: Solution and proof [0:45] [SLIDE 3–4]
- till · bookings · weather → "prep this much"
- 14 restaurants · 8 weeks · 31%
- 9 of 14 pay · €290 · full price
→ bridge: "You've heard restaurants are a hard market."
~~~

### rehearsal.md (excerpt)

| Section | Starts | Lasts | Words | Skip if late? |
|---|---|---|---|---|
| Opening | 0:00 | 0:22 | 48 | no |
| Problem | 0:22 | 0:23 | 49 | the "rounding error" line |
| Solution and proof | 0:45 | 0:38 | 83 | no |
| Visualize | 1:23 | 0:27 | 59 | the team lines (covered in Q&A) |
| Ask and close | 1:50 | 0:25 | 50 | no |

**Your top 3 techniques**
1. **The 3-second pause drill**: you speak fast when nervous. Run it twice this week.
2. **Power move + power words** before you walk up: press your fingertips together and recall the best service of your career.
3. **Lighthouse eye contact**: one investor per sentence, left, centre, right.

**Q&A prep (4 of 9)**
- *"Restaurants churn. Why will they stay?"* (the elephant): "We have 8 weeks of data, not a year, so I won't
  pretend. What we know: 9 of 14 chose to pay full price. [NEEDS SOURCE: retention after month 3]"
- *"Where does 31% come from?"*: "Here's exactly how we measured it: [NEEDS SOURCE: measurement method
  and baseline period]." Then back to the message.
- *"What stops a till vendor from building this?"*: the chef's workflow and the prep data, then back to the message.
- *"How big is the market?"*: [NEEDS SOURCE: restaurants in the first two target cities]

## Hand-over

> **Message:** Restaurants bin their profit every night. Leftover stops it.
> **Structure:** Monroe, about 2:40 with pauses, within the 2:42 limit for a 3:00 slot. Deck: 6 slides plus a leave-behind; built with the
> connected PowerPoint skill.
> **Needs you (5):** prep-waste share of food cost, how waste was measured, monthly saving per
> restaurant, retention after month 3, market size. Each one is marked `[NEEDS SOURCE]` in the
> script, slides or Q&A.
> **Rehearse first:** the opening, with the 3-second pause drill.
