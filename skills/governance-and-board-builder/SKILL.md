---
name: governance-and-board-builder
description: >
  Diagnose governance maturity and design the board of a patient-led
  nonprofit: board composition and size, officer and committee structure,
  required policies (conflict-of-interest, whistleblower,
  document-retention), and recruitment shortlist. Use when a leader asks
  "which governance policies are we missing", "how big should our board be",
  "what committees do we need", "who should we recruit to our board /
  scientific advisory board", or "are we governed the way a real 501(c)(3)
  should be". Reads org bylaws, board roster, minutes, and policies from
  Google Drive; writes a leader-facing OPTIONS document. Produces tiered,
  educational gap analysis and structure options — NOT legal drafting of
  bylaws or policies as binding instruments, NOT legal-compliance
  determination, and NOT a single prescription. Governance standards applied
  as educational framing (BoardSource practices, IRS duties); anything
  functioning as legal advice routes to qualified counsel. Patient PII
  flagged and minimized.
---

# governance-and-board-builder

Maps **how a patient-led org's governance should be structured** — board
composition and size, officer roles, committee structure, the standard policy
set, and a recruitment shortlist — as tiered options a non-scientist leader
reviews and chooses among, not a prescription. A **diagnostic + options** skill:
it reads the org's actual documents, compares them against consensus governance
practice, and hands back a gap analysis with effort/horizon tiers. It does not
draft binding instruments or rule on legal compliance. Part of the
`NONPROFIT_CAPACITY_STRATEGIST` specialist (Wave 2, product home: **Cowork**).

## Scope

**In scope:** governance-maturity diagnostic against consensus practice
(BoardSource, IRS fiduciary duties, Sarbanes-Oxley nonprofit provisions); board
composition, size, and independence options; officer roles and committee
structure options; the standard policy set (conflict-of-interest, whistleblower,
document-retention) presented as an educational checklist of what is missing and
how to prioritize adding it; an optional board / scientific-advisory recruitment
shortlist mapped from publication record via `mcp-literature` (OpenAlex/arXiv);
reading bylaws, roster, minutes, and policies from `mcp-google-drive` and
writing the options document back.

**Out of scope (route out):** drafting or amending bylaws or any policy as a
binding, adoptable instrument, and any statement that the org's governance "is
compliant" — both are legal advice (`H-COUNSEL`). Deciding *which* structure the
org must adopt (the leader chooses — `H-SCOPE`). Legal-entity formation and
compliance-filing questions (→ `legal-entity-and-compliance-navigator`).
Staffing/employment structure (→ `staffing-and-volunteer-scaling`). Using or
reproducing patient PII found in documents (`H-SAFETY`).

## Workflow

1. **Intake & consent.** Confirm the org authorized reading each folder/file;
   pull bylaws, board roster, committee list, minutes, and existing policies from
   `mcp-google-drive`, working from a copy. Scan for patient/community PII on
   ingest; if any is present, minimize it and stop to confirm before use
   (`H-SAFETY`). Log scope and any assumptions (`S-ASSUMPTION`).
2. **Maturity diagnostic.** Assess the current governance against consensus
   practice — board independence, fiduciary-duty coverage, policy completeness,
   meeting cadence. Any governance statistic or peer-board benchmark used must
   trace to a retrieved record; peer-org 990 governance data is ABSENT, so an
   unsourceable benchmark stops here (`H-VERIFY`).
3. **Policy gap analysis.** Compare the existing policy set against the standard
   set (COI, whistleblower, document-retention, and others as relevant); return
   the gaps as an educational checklist, each item labeled *educational, not
   legal advice* (`S-LABEL`). Drafting any of these as a binding instrument, or
   asserting legal compliance, routes to counsel (`H-COUNSEL`).
4. **Structure options.** Lay out board-size, officer, committee, and
   independence options as cost/effort/horizon tiers (`S-TIER`); where the ask
   forks on a structural decision the leader must own (e.g. governing board vs.
   board-plus-advisory-council), present the branches and stop for the choice
   (`H-SCOPE`).
5. **Recruitment shortlist (optional Science->Cowork handoff).** If asked,
   retrieve candidate board / scientific-advisory members by publication record
   from `mcp-literature`; fold a structured, labeled snippet into the governance
   memo. Every candidate claim traces to a retrieved record (`H-VERIFY`);
   candidates are options, not endorsements (`S-LABEL`).
6. **Package + gate envelope.** Compile the tiered, labeled governance-options
   document with its caveats on its face and a reference to `SESSION_LEDGER.md`;
   write it back to the org's designated Drive location. Emit the O11 gate
   envelope sidecar via `emit_gate_envelope(...)`.

## Gates

Emit every fired gate via `emit_gate_envelope(...)`; `gates_fired` is required
even when empty (`[]`).

**Hard (STOP, ask a human):**
- `H-COUNSEL` — the ask crosses into drafting/amending bylaws or a policy as a
  binding instrument, or asserting the org's governance is legally compliant.
  Explain the options as education; route drafting and compliance rulings to a
  qualified attorney.
- `H-SAFETY` — patient/community PII appears in uploaded minutes or rosters, or
  an action would expose it. Flag it, minimize/exclude it from any output, and
  confirm with the leader before proceeding; summarize only governance content.
- `H-VERIFY` — a governance statistic, IRS-rule citation, or peer-board
  benchmark can't be tied to a retrieved record (peer 990 governance data is
  ABSENT). Do not invent it.
- `H-SCOPE` — the ask forks on a structural decision the leader must own (board
  size/model, independence posture). Present the branches and stop for the
  choice.

**Soft (warn, caveat, proceed):**
- `S-TIER` — board, officer, committee, and policy recommendations presented as
  cost/effort/horizon tiers, never one prescription. (Default posture.)
- `S-LABEL` — every policy and structure item labeled *educational, not legal
  advice*; recruitment candidates labeled options, not endorsements.
- `S-ASSUMPTION` — any assumption made to proceed (org stage, jurisdiction,
  budget tier) logged to `SESSION_LEDGER.md` and surfaced in the deliverable.
- `S-CONFIDENCE` — where the diagnostic rests on thin evidence, proceed with an
  explicit confidence label and show the gap.

## Acceptance tests

`tests/acceptance_cases.json` — synthetic cases. Build each envelope with
`emit_gate_envelope(...)` and check with `run_acceptance(...)`; CI fails on any
`FAIL`.
