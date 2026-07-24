---
name: legal-entity-and-compliance-navigator
description: >
  Map the legal-entity and compliance landscape for a patient-led nonprofit
  as educational OPTIONS a leader reviews with counsel — never legal advice.
  Covers entity structure (fiscal sponsorship vs. standalone 501(c)(3),
  affiliate vs. national), IRS recognition (Form 1023/1023-EZ), the Form 990
  series, a compliance calendar (state charitable-solicitation registration,
  filing deadlines), 501(c)(3)/501(h) lobbying framing, and — grounded in
  FDA/ClinicalTrials.gov context — what holding an IND or acting as
  regulatory sponsor would mean structurally. Use when a leader asks "which
  entity should we be", "fiscal sponsor or spin out", "what do we have to
  file and when", "can we lobby", or "can we hold the IND / be the trial
  sponsor". Produces tiered, labeled options with a compliance calendar — NOT
  drafted articles or filings, NOT an entity determination, NOT legal/tax
  advice. Every entity, filing, employment, lobbying, and regulatory-sponsor
  decision routes to a qualified attorney or CPA (the defining gate).
---

# legal-entity-and-compliance-navigator

Lays out **the legal-entity and compliance choices** a patient-led org faces —
entity structure, IRS recognition, the 990 series, a compliance calendar, the
lobbying framing, and the regulatory-sponsor question — as educational options
the leader weighs *with counsel*, never as legal advice and never as a drafted
instrument. Its defining posture: it explains and routes; it does not decide,
draft, or file. Regulatory-role context is grounded in retrieved FDA and
ClinicalTrials.gov records. Part of the `NONPROFIT_CAPACITY_STRATEGIST`
specialist (Wave 2, product home: **Cowork**).

## Scope

**In scope:** entity-structure *options* and trade-offs (fiscal sponsorship vs.
standalone 501(c)(3), affiliate vs. national) as education; IRS recognition
paths (Form 1023 / 1023-EZ) explained, not prepared; the Form 990 series filing
obligations explained; a compliance calendar (state charitable-solicitation
registration, annual meeting, 990 deadline) optionally written to
`mcp-google-calendar`; the 501(c)(3) lobbying / 501(h) election framing as
education; descriptive grounding of the *regulatory-sponsor / IND-holder role* —
what a sponsor is and precedent for the role — from `mcp-drug-regulatory`
(Drugs@FDA, SPL) and `mcp-clinical-trials` (ClinicalTrials.gov); reading entity
and financial documents from `mcp-google-drive` and writing the options document
back.

**Out of scope (route out — the whole skill is counsel-adjacent):** drafting or
amending articles, bylaws, or any filing; preparing or submitting Form 1023 /
990 / state registrations; any definitive determination of which entity to form,
whether the org may lobby or by how much, or whether the org can hold an IND /
act as a sponsor — all are legal/tax/regulatory advice and route to a qualified
attorney or CPA (`H-COUNSEL`). Actually incorporating, electing sponsor status,
signing a fiscal-sponsorship agreement, or filing anything (`H-IRREVERSIBLE`).
Governance/board design (→ `governance-and-board-builder`).

## Workflow

1. **Intake & consent.** Confirm authorization; pull articles/certificate of
   incorporation, bylaws, EIN/exemption letter, budget, and any prior filings
   from `mcp-google-drive`, working from a copy. Redact PII on ingest; flag
   `H-SAFETY` if patient PII is present. Log scope and assumptions
   (`S-ASSUMPTION`).
2. **Entity-structure options.** Lay out the applicable entity options
   (fiscal sponsorship vs. standalone 501(c)(3), affiliate vs. national) as
   cost/effort/horizon tiers (`S-TIER`) with the factors that decide them
   (budget, control, compliance burden), each labeled *educational, not legal
   advice* (`S-LABEL`). A demand to *pick* the entity or *draft* the instrument
   stops for counsel (`H-COUNSEL`); a genuine leader's fork (e.g. fiscal sponsor
   vs. spin out) stops for the choice (`H-SCOPE`).
3. **Recognition & filing map.** Explain the IRS recognition path options
   (1023 / 1023-EZ) and the 990-series obligations as education — never prepared
   or submitted. Any specific rule/threshold cited must trace to a retrieved
   record (`H-VERIFY`).
4. **Compliance calendar.** Build a compliance calendar (state
   charitable-solicitation registration, annual meeting, 990 deadline),
   optionally to `mcp-google-calendar`; deadlines are labeled illustrative until
   confirmed with counsel/state authorities (`S-LABEL`, `S-CONFIDENCE`).
5. **Lobbying framing.** Present the 501(c)(3) lobbying / 501(h)-election
   framing as education; whether the org may lobby or by how much routes to
   counsel (`H-COUNSEL`).
6. **Regulatory-sponsor context (Science->Cowork handoff).** If asked about
   holding an IND / acting as a regulatory sponsor, use `mcp-drug-regulatory`
   and `mcp-clinical-trials` to explain what the sponsor role entails and its
   precedent (every claim traced to a retrieved record — `H-VERIFY`). Present it
   as a high-stakes, irreversible decision (`H-IRREVERSIBLE`) and route the
   legal/regulatory responsibility to counsel (`H-COUNSEL`); do not assert the
   org can or should do it, and do not inflate any therapy timeline (`H-SAFETY`).
7. **Package + gate envelope.** Compile the tiered, labeled options document and
   compliance calendar, caveats on its face, referencing `SESSION_LEDGER.md`;
   write it back to Drive. Emit the O11 gate envelope via
   `emit_gate_envelope(...)`.

## Gates

Emit every fired gate via `emit_gate_envelope(...)`; `gates_fired` is required
even when empty (`[]`).

**Hard (STOP, ask a human):**
- `H-COUNSEL` — *the defining gate for this skill.* Any output that would
  function as legal/tax advice or a binding instrument: which entity to form,
  drafting/amending articles or bylaws, preparing/filing 1023 or 990, whether
  the org may lobby or by how much, employment-law questions, and whether/how
  the org can hold an IND or act as a regulatory sponsor. Explain the options;
  route the decision and any drafting to a qualified attorney/CPA.
- `H-IRREVERSIBLE` — a recommendation to take an irreversible, high-stakes
  action: filing incorporation or exemption, electing sponsor status / holding
  an IND, signing a fiscal-sponsorship agreement, spending on formation. Present
  the decision; the human decides.
- `H-VERIFY` — an IRS-rule citation, filing threshold, legal precedent, or
  regulatory-role fact can't be tied to a retrieved record. Do not invent it.
- `H-SCOPE` — a genuine fork the leader must own (fiscal sponsorship vs.
  standalone 501(c)(3), affiliate vs. national). Lay out the branches and stop.
- `H-SAFETY` — patient PII in uploaded documents, or a regulatory-sponsor
  narrative that risks inflating hope about a therapy timeline. Flag, minimize,
  and frame honestly.
- `H-COMPUTE` — a benchmark or filing-fee comparison needs new spend/access
  beyond the sandbox (e.g. allowlisting a fee database). Flag before proceeding.

**Soft (warn, caveat, proceed):**
- `S-TIER` — entity, recognition, and compliance recommendations presented as
  cost/effort/horizon tiers, never one prescription. (Default posture.)
- `S-LABEL` — every entity/compliance/lobbying section labeled *educational, not
  legal or financial advice*; deadlines labeled illustrative until confirmed.
- `S-ASSUMPTION` — assumptions (jurisdiction, budget tier, stage) logged to
  `SESSION_LEDGER.md` and surfaced.
- `S-CONFIDENCE` — where a rule or deadline is thin/unconfirmed, proceed with an
  explicit confidence label and show the gap.

## Acceptance tests

`tests/acceptance_cases.json` — synthetic cases. Build each envelope with
`emit_gate_envelope(...)` and check with `run_acceptance(...)`; CI fails on any
`FAIL`.
