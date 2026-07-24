---
name: staffing-and-volunteer-scaling
description: >
  Plan how a patient-led nonprofit scales its people: staffing roadmap, role
  descriptions, volunteer-to-staff transition, org-chart evolution, and
  compensation ranges. Use when a leader asks "when should we make our first
  hire", "what roles do we need and in what order", "how do we move from
  all-volunteer to staffed", "write a job description for X", or "what should
  we pay an executive director / program manager". Reads org chart, staff and
  volunteer roster, job descriptions, and budget from Google Drive; writes
  the plan back. Compensation ranges are ILLUSTRATIVE and clearly labeled
  unless the org supplies peer 990s or a compensation survey—that data is not
  connected and flagged as a gap. Produces tiered staffing roadmap and
  templates. NOT employment-law advice, NOT a definitive salary for reliance
  without sourced data, NOT a single prescription. Employment-law questions
  route to counsel. Making the first paid hire is irreversible; the leader
  owns that decision.
---

# staffing-and-volunteer-scaling

Plans **how a patient-led org grows its people** — staffing roadmap, role
descriptions, the volunteer-to-staff transition, org-chart evolution, and
compensation ranges — as tiered options the leader reviews, with every
compensation figure labeled illustrative unless sourced to org-supplied data.
A **planning + template** skill: it structures the staffing path and drafts role
descriptions, it does not give employment-law advice or a relied-upon salary
number. Part of the `NONPROFIT_CAPACITY_STRATEGIST` specialist (Wave 2, product
home: **Cowork**).

## Scope

**In scope:** a staffing roadmap sequenced to the org's stage (all-volunteer ->
first-hire -> professionalizing); role-description templates; the
volunteer-to-staff transition plan; org-chart evolution options; compensation
*ranges* presented as illustrative and labeled (`S-LABEL`), or sourced to
org-supplied peer 990s / compensation survey when provided; reading the org
chart, roster, job descriptions, and budget from `mcp-google-drive` and writing
the plan back.

**Out of scope (route out):** employment-law questions — classification
(employee vs. contractor), benefits mandates, termination, wage-and-hour — all
route to qualified counsel (`H-COUNSEL`). A specific, sourced compensation
benchmark when peer-org/990 data can't be retrieved (`H-VERIFY`; the connector
is ABSENT). The decision to actually make the first paid hire or commit the
spend (the leader owns it — `H-IRREVERSIBLE`). Entity/compliance structure
(→ `legal-entity-and-compliance-navigator`). Board/governance roles
(→ `governance-and-board-builder`). Using patient PII from rosters (`H-SAFETY`).

## Workflow

1. **Intake & consent.** Confirm authorization; pull the org chart, staff and
   volunteer roster, job descriptions, and budget from `mcp-google-drive`,
   working from a copy and treating individuals' data as confidential. Flag
   `H-SAFETY` if patient/community PII is present. Log scope and assumptions
   (`S-ASSUMPTION`).
2. **Staffing roadmap.** Sequence the plausible roles to the org's stage and
   budget as cost/effort/horizon tiers (`S-TIER`); affordability uses the
   org-supplied budget as-supplied, not audited (`S-LABEL`).
3. **Role descriptions.** Draft role-description templates for the prioritized
   roles, labeled as templates to adapt (`S-LABEL`); employment-law specifics
   (classification, benefits, termination) route to counsel (`H-COUNSEL`).
4. **Compensation ranges.** Provide compensation ranges. If the org supplies
   peer 990s or a comp survey, source to it; otherwise offer paths — org supplies
   data, request allowlisting of ProPublica/RePORTER (`H-COMPUTE`), or proceed
   with an explicitly illustrative, labeled range (`S-LABEL`, `S-CONFIDENCE`). A
   demand for a specific sourced benchmark that cannot be retrieved stops
   (`H-VERIFY`) — no fabricated compensation number.
5. **Transition & first-hire decision.** Lay out the volunteer-to-staff
   transition and org-chart evolution as options; the decision to make the first
   paid hire / commit the spend is presented as high-stakes and irreversible and
   stops for the leader (`H-IRREVERSIBLE`).
6. **Package + gate envelope.** Compile the tiered staffing roadmap, templates,
   and labeled ranges with caveats on its face, referencing `SESSION_LEDGER.md`;
   write it back to Drive. Emit the O11 gate envelope via
   `emit_gate_envelope(...)`.

## Gates

Emit every fired gate via `emit_gate_envelope(...)`; `gates_fired` is required
even when empty (`[]`).

**Hard (STOP, ask a human):**
- `H-VERIFY` — *acute here.* A specific, sourced compensation benchmark or peer
  staffing statistic can't be retrieved (peer-org/990 comp data is ABSENT). Do
  not invent a benchmark figure; name the gap.
- `H-IRREVERSIBLE` — a recommendation to make the first paid hire or commit the
  hiring spend. Present the decision; the leader owns it.
- `H-COUNSEL` — the ask crosses into employment-law advice (worker
  classification, benefits mandates, termination, wage-and-hour). Frame the
  staffing options; route the legal question to qualified counsel.
- `H-SAFETY` — patient/community PII in an uploaded roster or minutes, or an
  action that would expose an individual's data. Flag, minimize, exclude from
  output, and confirm before proceeding.
- `H-COMPUTE` — benchmarking requires new spend/access beyond the sandbox
  (allowlisting ProPublica/RePORTER, purchasing a compensation survey). Flag
  before proceeding.

**Soft (warn, caveat, proceed):**
- `S-TIER` — staffing roadmap and org-chart options presented as
  cost/effort/horizon tiers, never one prescription. (Default posture.)
- `S-LABEL` — compensation ranges labeled illustrative unless sourced to
  org-supplied data; role descriptions labeled templates; budget used
  as-supplied.
- `S-ASSUMPTION` — assumptions (budget tier, stage, growth rate, jurisdiction)
  logged to `SESSION_LEDGER.md` and surfaced.
- `S-CONFIDENCE` — where a comp range is illustrative-but-unsourced or a roadmap
  rests on thin evidence, proceed with an explicit confidence label and show the
  gap.

## Acceptance tests

`tests/acceptance_cases.json` — synthetic cases. Build each envelope with
`emit_gate_envelope(...)` and check with `run_acceptance(...)`; CI fails on any
`FAIL`.
