---
marp: true
size: 16:9
paginate: false
style: |
  :root {
    --ink: #f8fafc;
    --muted: #cbd5e1;
    --accent: #5eead4;
    --panel: #1e293b;
  }
  section {
    background: #0f172a;
    color: var(--ink);
    font-family: Arial, Helvetica, sans-serif;
    font-size: 32px;
    padding: 64px 76px;
  }
  h1 { color: var(--accent); font-size: 62px; line-height: 1.05; }
  h2 { color: var(--ink); font-size: 42px; }
  strong { color: var(--accent); }
  blockquote {
    border-left: 8px solid var(--accent);
    color: var(--ink);
    font-size: 42px;
    margin: 36px 0;
    padding: 12px 28px;
  }
  .muted { color: var(--muted); }
  .grid { display: grid; grid-template-columns: 1fr 1fr; gap: 30px; }
  .card { background: var(--panel); border-radius: 18px; padding: 24px 28px; }
  .bad { color: #fda4af; }
  .good { color: var(--accent); }
  .cta { text-align: center; }
  .date { font-size: 48px; }
  .qr {
    align-items: center;
    background: white;
    border-radius: 12px;
    color: #0f172a;
    display: inline-flex;
    font-size: 20px;
    height: 150px;
    justify-content: center;
    margin: 12px;
    width: 150px;
  }
  footer { color: var(--muted); font-size: 18px; }
---

<!-- _class: lead -->

# Feedback is a developer skill

## Learn it like one.

<span class="muted">A five-minute talk for people who build things together</span>

---

# Feedback is already in your job

<div class="grid">
<div class="card">Pull requests</div>
<div class="card">Pairing</div>
<div class="card">Stand-ups</div>
<div class="card">Retrospectives</div>
</div>

> Code is only half the interface.

---

# Bad feedback creates hidden work

- **Vague** → guessing
- **Personal** → defensiveness
- **Late** → rework
- **Silent** → repeat mistakes

## The human loop stays unmerged.

---

# Send three fields, not a verdict

1. **Observation** — What did I see or hear?
2. **Impact** — Why does it matter?
3. **Next step** — What could help?

> Specific. Relevant. Discussable.

---

# Same concern. Better signal.

<div class="grid">
<div class="card">

### <span class="bad">Verdict</span>

“This is over-engineered.”

</div>
<div class="card">

### <span class="good">Useful feedback</span>

“This helper adds three layers around one API call. That makes failures harder to trace. Could we inline it until we have a second caller?”

</div>
</div>

---

<!-- _class: cta -->

# Knowing the pattern isn’t the skill.

## Practice is.

**Free feedback workshop**  
<span class="date">12 November 2026</span>

<div class="qr">ADD SIGN-UP<br>QR CODE</div>

**Reserve your free place now**  
<span class="muted">ADD-SHORT-SIGNUP-URL</span>

Bring one conversation you want to handle better.
