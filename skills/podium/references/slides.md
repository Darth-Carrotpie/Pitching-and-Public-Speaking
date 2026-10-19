# Slides

Slides are for the listener, not the speaker. They help the audience understand
and remember; they are not the speaker's notes. If the speech works without
slides, say so and offer to skip them, especially for occasions and short
internal talks.

## Rules

- **One idea per slide.**
- **Assertion headline**: a full sentence stating the slide's point, at most 2
  lines ("Churn halved after onboarding calls", not "Churn results").
  Michael Alley's studies found that sentence headlines with visual evidence
  beat topic headings with bullets for comprehension and recall.
- **Visual evidence, not bullets**: an image, chart, diagram or big number that
  proves the headline. Clear, simple, memorable.
- **Key words only**: besides the headline, about 6 words at most. No full
  sentences, no bullet walls. People read faster than you speak, so a text
  slide makes them stop listening.
- **Cut decoration** (Richard Mayer's coherence principle). Highlight the one thing
  to look at. Put labels on the chart, not in a legend.
- **Never put the script on the slide**, and never read a slide aloud.
- Readable from the back of the room: 30 pt or larger, high contrast.
- Roughly one slide per 30–60 seconds. A blank slide pulls attention back to the speaker.
- Test every visual: does it add information? Does it help people remember? If
  neither, cut it.

## Visual types

| Type | Use when |
|---|---|
| **Big number** | one figure carries the argument |
| **Photo** | emotion, a real person or place, the "island" |
| **Chart** | a comparison or a trend. Use the simplest chart that shows it, and highlight one series |
| **Diagram** | a process, a structure, before/after |
| **Quote** | a customer, an expert, a surprising voice |
| **Demo / video** | the product working, 60 seconds at most |
| **Blank** | a pause, a story, the CTA moment |

## Spec format (slides.md)

~~~markdown
# <Title>: slides
Presented [+ leave-behind] · N slides · style: <brand colours, fonts, tone, if known>

## Slide 1: <assertion headline>
- **Visual:** <type>: <one-line brief: what it shows, what to highlight>
- **On-slide text:** <key words, ≤ 6>
- **Speaker line:** "<the script line this slide supports>"
- **Leave-behind:** <1–2 sentences so the slide stands alone>   (only if leave-behind)
~~~

Every slide maps to a script line, and every slide has a matching `[SLIDE n]` cue in the script.

## Leave-behind version

For decks emailed before or after the meeting (common for investor and board
decks). The same story and slide order, at reading density:

- add 1–2 context sentences per slide (the `Leave-behind` line)
- keep the assertion headlines and the visuals
- optionally add an appendix: detailed numbers, team bios, FAQ
- no animations or builds, nothing that only makes sense when spoken

## Hand-off

**With a slide tool:** give it the spec and the style notes. Ask it to put each
speaker line into the presenter notes, and to build the leave-behind as a
separate file if one was requested.

**Without one, use the Marp fallback:** write `slides.marp.md` next to `slides.md`.

~~~markdown
---
marp: true
paginate: true
---

# Churn halved after onboarding calls

![bg right:40%](onboarding-call.jpg)

<!-- Every customer who got a call in week one stayed. -->

---

# Next slide headline
~~~

- One `---`-separated section per slide, with the headline as `#`.
- Put the speaker line in an HTML comment; Marp shows it as presenter notes.
- Name missing images as placeholders and list them for the user. Never pretend
  a placeholder is a real image.
- Tell the user how to render it: the Marp for VS Code extension (preview and
  export), or `npx @marp-team/marp-cli@latest slides.marp.md --pptx` (or `--pdf`).
