# Podium

**Speeches and decks that get a result.**

Podium is an agent skill that helps you prepare a pitch, a talk, an internal
proposal or an occasion speech, with or without slides, that gets one specific
outcome from one specific audience. It works in Claude Code, Codex, GitHub
Copilot, Cursor, Gemini CLI, claude.ai, and any agent that reads `SKILL.md` or
`AGENTS.md`.

Every speech Podium builds is:

- **Clear and accurate.** One goal, one message, nothing invented.
- **A story people can see.** Images, examples, a shape that moves.
- **A call to act.** The audience leaves knowing exactly what to do next.

## What you get

Podium writes a folder per speech, `speeches/<name>/`:

| File | What's in it |
|---|---|
| `brief.md` | goal, one-line message, up to 3 arguments, the elephant in the room, the structure |
| `script.md` | the full spoken text, with pauses, emphasis, slide cues and timings |
| `slides.md` | a slide-by-slide spec: assertion headline, visual brief, on-slide text, speaker line, and an optional leave-behind version |
| `notes.md` | cue cards: the opening and closing word for word, story beats for the body |
| `rehearsal.md` | a timing table, a practice plan, your top 3 techniques, Q&A prep, a day-of checklist |

Where the agent can't write files, you get the same sections as one document in chat.

## How it works

1. **Intake.** It asks only what you haven't already said, and every question comes with a suggested answer.
2. **Message gate.** It sets the goal as a verb and writes a one-line message that must pass
   four tests: could someone retell it, print it as a headline, put it on a banner, say it in 3 seconds?
   It picks up to 3 arguments and names the elephant in the room. Nothing gets written until you agree.
3. **Structure.** It offers 2–3 options with outlines and timings, and you pick one.
4. **Produce.** It writes the script, slides, cue cards and rehearsal kit.
5. **Check.** It runs a quality checklist and fixes what it can. It only tells you what needs you, such as
   `[NEEDS SOURCE]` for a number you haven't given it. Podium never invents facts.
6. **Hand over.** The slides go to your connected slide tool, or into a Marp file you can render.

A taste, from the [investor pitch example](examples/pitch-investor.md):

| Candidate message | Retell | Headline | Banner | 3 s |
|---|---|---|---|---|
| "Leftover cuts restaurant food waste by a third, and restaurants pay for it." | ✓ | ✓ | ✗ | ✗ |
| "Restaurants bin their profit every night. Leftover stops it." | ✓ | ✓ | ✓ | ✓ |

## Modes

| Command | Use it to |
|---|---|
| `/podium` | create a new speech (default) |
| `/podium review` | score and fix an existing deck or script |
| `/podium coach` | get feedback on a rehearsal transcript: pace, filler words, clarity, call to action |
| `/podium spar` | practise Q&A against a tough audience, one question at a time |
| `/podium adapt` | change the length, audience, format or language |

You don't need the commands: "help me prepare a 3-minute pitch for…" works too.
In Claude Code plugin installs, the command can show up as `/podium:podium`.

## Install

### Claude Code

Send these as two separate prompts:

```
/plugin marketplace add Darth-Carrotpie/podium
```
```
/plugin install podium@podium
```

### GitHub Copilot CLI

```
copilot plugin marketplace add Darth-Carrotpie/podium
copilot plugin install podium@podium
```

Then start a new session.

### Codex, Copilot in VS Code, Cursor, Gemini CLI and many more

```
npx skills add Darth-Carrotpie/podium
```

This detects the agents you have installed and asks where to install. Add `-g`
to install for all your projects, or `-a <agent>` to pick one (`codex`,
`github-copilot`, `cursor`, `gemini-cli`, `claude-code`, …). Then restart the
agent (in Gemini CLI, `/skills reload` is enough).

### Manual copy

Copy the `skills/podium/` folder to:

| Agent | All projects | One project |
|---|---|---|
| Claude Code | `~/.claude/skills/podium` | `.claude/skills/podium` |
| Codex | `~/.agents/skills/podium` | `.agents/skills/podium` |
| GitHub Copilot (VS Code, CLI) | `~/.copilot/skills/podium` | `.github/skills/podium` |
| Cursor | `~/.cursor/skills/podium` | `.cursor/skills/podium` |
| Gemini CLI | `~/.gemini/skills/podium` | `.gemini/skills/podium` |

`~/.agents/skills/podium` alone covers Codex, Copilot, Cursor and Gemini CLI.
From a clone, Gemini CLI can also link it: `gemini skills link ./skills/podium`.

### claude.ai and the Claude apps

Custom skills need code execution turned on (Settings → Capabilities).

1. Download this repository (**Code → Download ZIP**) and unzip it.
2. Zip the `skills/podium` folder on its own, so the zip contains `podium/SKILL.md`.
   Windows: right-click the folder → *Send to → Compressed (zipped) folder*. macOS: right-click → *Compress*.
3. In Claude, open **Customize → Skills** (older versions: **Settings → Capabilities → Skills**) and upload the zip.

### Any other agent

Copy [`AGENTS.md`](AGENTS.md) into your project's root folder. It's a compact version of
the method for agents that read rules files (Windsurf, Zed, Amp, JetBrains Junie,
Aider, Jules, …).

## Slides

Podium writes the slide spec itself, then hands it to whatever slide tool your agent
has: a PowerPoint skill, a Google Slides, Canva or Figma connector, or a deck artifact.
If there isn't one, it tells you up front and writes `slides.marp.md`, which you can
open with the [Marp for VS Code](https://marketplace.visualstudio.com/items?itemName=marp-team.marp-vscode)
extension or convert:

```
npx @marp-team/marp-cli@latest slides.marp.md --pptx
```

If the deck will be emailed before or after the meeting, ask for a **leave-behind**:
the same slides with 1–2 sentences of context each, so they can be read without you.

## The method

The core comes from the author's notes from two public speaking workshops: goal and
message first, three arguments, "sell the island, not the plane", the elephant in the
room, five classic structures, opening and closing techniques, the ŽABT clarity filters,
rehearsal and nerves techniques, and handling Q&A.

These well-known frameworks fill the gaps:

- Alan H. Monroe: the Motivated Sequence
- Nancy Duarte, *Resonate*: the sparkline
- Barbara Minto, *The Pyramid Principle*: answer first, SCQA
- Chip and Dan Heath, *Made to Stick*
- Chris Anderson, *TED Talks*: the throughline
- Guy Kawasaki: the [10/20/30 rule](https://guykawasaki.com/the_102030_rule/)
- Sequoia Capital: the pitch deck outline
- Andy Raskin: the strategic narrative
- Kenn Adams: the story spine
- Michael Alley: [assertion-evidence slides](https://writing.engr.psu.edu/research.html)
- Richard E. Mayer: principles of multimedia learning

## Examples

- [Investor pitch](examples/pitch-investor.md): 3 minutes, a presented deck plus a leave-behind
- [Meetup talk](examples/talk-meetup.md): 6 minutes, the Sparkline structure, the Marp fallback
- [Proposal to leadership](examples/internal-proposal.md): 3 minutes, answer first, a three-part ask
- [Wedding toast](examples/occasion-toast.md): 3 minutes, no slides

## Evals

[`evals/evals.json`](evals/evals.json) holds 11 test prompts, each with the
behaviour to expect: intake, the message gate, the never-invent rule, the slide
fallback, every mode, and Lithuanian output. Run them with Anthropic's
`skill-creator` skill, or paste the prompts into your agent and check the
expectations by hand.

Known gaps and the plan for the next improvement sprints are in [ROADMAP.md](ROADMAP.md).

## Repository layout

```
skills/podium/SKILL.md      the skill: modes, workflow, hard rules
skills/podium/references/   one file per step: intake, message, structures, script,
                            slides, notes, rehearsal, qa, modes, checklist
AGENTS.md                   compact version for rules-file agents (keep it in sync)
.claude-plugin/             Claude Code and Copilot CLI plugin manifests
examples/  evals/
```

## License

[MIT](LICENSE)
