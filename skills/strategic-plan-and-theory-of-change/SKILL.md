---
name: strategic-plan-and-theory-of-change
description: >
  Build strategic plans and theories of change for patient-led nonprofits as
  tiered, leader-facing OPTIONS documents: mission and vision framing, logic
  model, SMART milestones, tiered budget, and funding runway. Use when a
  leader asks "help us write our strategic plan", "map our theory of change /
  logic model", "what milestones should we set", "how long is our funding
  runway", or "how do we prioritize programs vs. infrastructure". Reads org
  plans, mission, programs, budget, and grant reports from Google Drive;
  writes plan back. Grounds disease-area claims in PubMed citations; folds
  Grants.gov and NIH RePORTER (where access granted) into runway checks. NOT
  a fundraising guarantee, NOT financial advice, NOT a single prescription.
  Program-vs-infrastructure forks stop for leader choice; unsourceable claims
  stop at verification; therapy-timeline narratives are flagged for evidence
  gaps.
---

# strategic-plan-and-theory-of-change

Builds a patient-led org's **strategic plan and theory of change** — mission/
vision, logic model, SMART milestones, tiered budget, funding runway — as
options the leader reviews and chooses among, with every disease-area factual
claim grounded in retrieved citations and every budget/runway figure labeled.
A **planning + narrative** skill: it structures strategy, it does not promise
funding or give financial advice. Part of the `NONPROFIT_CAPACITY_STRATEGIST`
specialist (Wave 2, product home: **Cowork**).

## Scope

**In scope:** mission/vision framing; a theory of change / logic model (inputs ->
activities -> outputs -> outcomes -> impact); SMART milestones; a tiered budget
(cost/effort/horizon); a funding-runway sanity check using `mcp-research-resources`
(Grants.gov) opportunities and, where access is granted, NIH RePORTER context;
grounding any disease-area factual claim in retrieved `mcp-pubmed` citations;
reading the current plan, mission, program list, budget, and grant reports from
`mcp-google-drive` and writing the plan back.

**Out of scope (route out):** promising or guaranteeing that any funding will be
won, and any financial-advice-flavored recommendation on reserves, investment, or
spend — labeled and routed to a qualified advisor (`H-COUNSEL` on
financial-advice asks). Deciding the org's strategic priorities *for* it at a
genuine fork (the leader chooses — `H-SCOPE`). Entity/compliance and lobbying
framing (→ `legal-entity-and-compliance-navigator`). Staffing affordability
detail (→ `staffing-and-volunteer-scaling`). Inflating hope about a therapy
timeline in the narrative (`H-SAFETY`).

## Workflow

1. **Intake & consent.** Confirm authorization; pull the current strategic plan,
   mission/vision, program list, theory of change (if any), budget, and grant
   reports from `mcp-google-drive`, working from a copy. Scan for PII; flag
   `H-SAFETY` if present. Log scope and assumptions (`S-ASSUMPTION`).
2. **Mission / vision & theory of change.** Frame or refine mission/vision and
   build the logic model / theory of change. Any factual claim about the org's
   disease area is grounded in a retrieved `mcp-pubmed` citation; an
   unsourceable claim stops here (`H-VERIFY`). A narrative that would inflate
   hope about a therapy timeline is reframed honestly (`H-SAFETY`).
3. **SMART milestones.** Convert the plan into specific, measurable, time-bound
   milestones, presented as tiered options by ambition/horizon (`S-TIER`).
4. **Tiered budget & funding runway.** Build a tiered budget from the
   org-supplied figures (used as-supplied, not audited — `S-LABEL`); sanity-check
   the funding runway against Grants.gov opportunities via
   `mcp-research-resources` and, where granted, NIH RePORTER context
   (Science->Cowork handoff). If NIH RePORTER / a funding source needs
   allowlisting or new access, flag `H-COMPUTE`. Runway is illustrative, never a
   fundraising guarantee (`S-LABEL`, `S-CONFIDENCE`).
5. **Prioritization fork.** Where the plan forks on a priority the leader must
   own (e.g. program spend vs. infrastructure/capacity building), lay out both
   branches with trade-offs and stop for the choice (`H-SCOPE`); log the
   assumptions behind each (`S-ASSUMPTION`).
6. **Package + gate envelope.** Compile the tiered strategic plan / ToC with
   confidence labels and caveats on its face, referencing `SESSION_LEDGER.md`;
   write it back to Drive. Emit the O11 gate envelope via
   `emit_gate_envelope(...)`.

## Gates

Emit every fired gate via `emit_gate_envelope(...)`; `gates_fired` is required
even when empty (`[]`).

**Hard (STOP, ask a human):**
- `H-VERIFY` — a disease-area factual claim, funding statistic, or grant figure
  can't be tied to a retrieved record (PubMed/Grants.gov). Do not invent it.
- `H-SCOPE` — the plan forks on a strategic priority the leader must own
  (program vs. infrastructure, national vs. local focus). Present the branches
  and stop for the choice.
- `H-SAFETY` — patient/community PII in uploaded documents, or a strategic
  narrative that risks inflating hope about a therapy timeline. Flag, minimize,
  and reframe honestly.
- `H-COUNSEL` — the ask crosses into financial advice (reserves, investment,
  binding spend commitments). Frame options; route to a qualified financial
  advisor/CPA.
- `H-COMPUTE` — a funding-landscape check needs new spend/access beyond the
  sandbox (allowlisting NIH RePORTER or a funding database). Flag before
  proceeding.

**Soft (warn, caveat, proceed):**
- `S-TIER` — milestones and budget presented as cost/effort/horizon tiers, never
  one prescription. (Default posture.)
- `S-LABEL` — budget/runway figures labeled illustrative and used as-supplied
  (not audited); no fundraising guaranteed.
- `S-ASSUMPTION` — assumptions (budget tier, growth rate, disease-area scope)
  logged to `SESSION_LEDGER.md` and surfaced.
- `S-CONFIDENCE` — where evidence or a runway projection is thin, proceed with an
  explicit confidence label and show the gap.

## Acceptance tests

`tests/acceptance_cases.json` — synthetic cases. Build each envelope with
`emit_gate_envelope(...)` and check with `run_acceptance(...)`; CI fails on any
`FAIL`.
