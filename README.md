# Nonprofit Capacity Strategist

A specialist agent profile and its companion skills for **[Claude Science](https://www.anthropic.com)**,
built to help patient-org leaders — most often rare-disease nonprofits — build **organizational capacity** — governance and board, legal-entity and compliance options, a strategic plan and theory of change, and staffing/volunteer scaling — as educational options a leader reviews with counsel, never as legal advice.

Like every specialist in this collection, it is **discovery-first and
non-prescriptive**: it does the homework and lays out **tiered options to review**,
and the leader decides. Deliverables carry their sources, an assumption ledger, and
honest caveats; AI-generated analysis is always labeled computational, never a
clinical or validated result. Each skill enforces a **machine-checkable gate
envelope** — a required, tagged field naming every hard/soft gate that fired — and
ships with synthetic acceptance tests (including a negative control that must fail
when a required hard gate is dropped).

## Skills in this specialist

| Skill | What it does | Central gate |
|---|---|---|
| `governance-and-board-builder` | Diagnose governance maturity and design the board of a patient-led nonprofit: board composition and size, officer and committee structure, required policies (conflict-of-interest, whistleblower, document-retention), and recruitment shortlist. | `H-COUNSEL` |
| `legal-entity-and-compliance-navigator` | Map the legal-entity and compliance landscape for a patient-led nonprofit as educational OPTIONS a leader reviews with counsel — never legal advice. | `H-COUNSEL` |
| `strategic-plan-and-theory-of-change` | Build strategic plans and theories of change for patient-led nonprofits as tiered, leader-facing OPTIONS documents: mission and vision framing, logic model, SMART milestones, tiered budget, and funding runway. | `H-VERIFY` |
| `staffing-and-volunteer-scaling` | Plan how a patient-led nonprofit scales its people: staffing roadmap, role descriptions, volunteer-to-staff transition, org-chart evolution, and compensation ranges. | `H-VERIFY` |


Gate codes: **H-** = hard (stop, ask a human / refuse) — `H-SAFETY` (patient-data /
harm), `H-COUNSEL` (route to attorney / CPA / physician), `H-VERIFY` (never invent a
fact or citation), `H-SCOPE` (own the fork), `H-IRREVERSIBLE` (high-stakes,
hard-to-undo). **S-** = soft (warn, caveat, proceed) — `S-LABEL`, `S-CONFIDENCE`,
`S-ASSUMPTION`, `S-TIER`, `S-NEUTRAL` (vendor neutrality).

## What's in this repository

```
agent/
  profile.json        # picker metadata + settings (name, description, access)
  system_prompt.md    # the agent's identity / opening system prompt
skills/
  governance-and-board-builder/
  legal-entity-and-compliance-navigator/
  strategic-plan-and-theory-of-change/
  staffing-and-volunteer-scaling/
export_manifest.json  # index of exported files
install.py            # one-shot installer (run in the Claude Science repl tool)
LICENSE               # MIT
```

Each skill directory contains a `SKILL.md` (the guidance the agent loads), a
`kernel.py` (the shared gate-envelope helpers auto-loaded into the kernel), a
`gated_skill_output.schema.json` (the required-tag output contract), and
`tests/acceptance_cases.json` (the synthetic acceptance suite).

## Install

From a Claude Science conversation, in the **`repl`** tool, from the root of a clone
of this repository:

```python
exec(open("install.py").read())
```

The installer is idempotent (safe to re-run; it updates in place). It publishes the
skills above and creates/updates the `NONPROFIT_CAPACITY_STRATEGIST` agent, then prints the one tool call to
create an optional analysis environment (environment creation is a tool, not part of
the SDK).

## Integrity & safety

- Every deliverable is **tiered options to review**, never a prescription — the
  leader decides.
- Facts are sourced from connected databases; the skills never invent a date,
  statistic, citation, or identifier, and route citations/calculations through
  verification.
- AI-generated analysis is labeled **computational / in-silico**, never an
  experimental or clinical result.
- **Not medical, legal, or financial advice.** Decisions that cross into those
  domains route to a qualified professional (physician / attorney / CPA), and
  patient-data privacy and consent are protected throughout.

## License

MIT — see [LICENSE](LICENSE).
