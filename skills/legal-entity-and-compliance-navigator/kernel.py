"""registry-builder sidecar — O11 gate-envelope helpers.
Loading this only DEFINES functions (no top-level calls), per skill sidecar rules.
"""
import json

GATE_CODES = ["H-VERIFY", "H-SCOPE", "H-IRREVERSIBLE", "H-SAFETY", "H-COUNSEL",
              "H-COMPUTE", "S-CONFIDENCE", "S-ASSUMPTION", "S-LABEL", "S-TIER", "S-NEUTRAL"]


def emit_gate_envelope(skill, status, gates_fired, deliverable_ref,
                       unknowns_flagged=None, ranking_present=None):
    """Build the O11 output envelope a gated skill emits beside its deliverable.
    gates_fired: list of dicts {code, where, evidence, resolution?}.
    Returns a dict; write it as a <deliverable>.gates.json sidecar."""
    env = {"skill": skill, "status": status,
           "gates_fired": list(gates_fired or []),
           "deliverable_ref": deliverable_ref}
    if unknowns_flagged is not None:
        env["unknowns_flagged"] = int(unknowns_flagged)
    if ranking_present is not None:
        env["ranking_present"] = bool(ranking_present)
    return env


def load_schema(path="gated_skill_output.schema.json"):
    """Load the shared O11 JSON Schema shipped at the skill root."""
    with open(path) as fh:
        return json.load(fh)


def run_acceptance(envelope, expected_gates, schema_path="gated_skill_output.schema.json"):
    """Acceptance check: schema-valid + every expected gate tag present + S-NEUTRAL
    invariant. Returns (verdict, errors). Requires jsonschema."""
    from jsonschema import Draft202012Validator
    errors = []
    validator = Draft202012Validator(load_schema(schema_path))
    for e in sorted(validator.iter_errors(envelope), key=lambda e: list(e.path)):
        errors.append("SCHEMA: " + e.message)
    fired = {g["code"] for g in envelope.get("gates_fired", [])}
    missing = [g for g in expected_gates if g and g not in fired]
    if missing:
        errors.append("MISSING_TAG: expected " + repr(missing) + ", got " + repr(sorted(fired)))
    if "S-NEUTRAL" in expected_gates and envelope.get("ranking_present") is not False:
        errors.append("NEUTRALITY: ranking_present must be False for an S-NEUTRAL skill")
    return ("PASS" if not errors else "FAIL", errors)


def emit_consent_frame_status(org_ref, datasets, review_state="drafted"):
    """Shared consent-gate status object (review finding 3.5). Produced by
    consent-and-data-governance; READ by registry-builder,
    natural-history-study-designer, biobank-blueprint, and data-linkage-architecture
    instead of each re-confirming the consent frame independently.

    org_ref: opaque org/project reference (no identifiable content).
    datasets: list of dicts, one per capture, e.g.
        {"dataset": "registry", "frame_exists": True, "consent_model": "broad",
         "jurisdictions": ["HIPAA-screened:not-covered-entity", "WA-MHMDA", "GINA"],
         "linkage_permitted": True, "secondary_use_permitted": True}
    review_state: "drafted" | "counsel_reviewed" | "irb_approved".
    Returns a dict; write it as consent_frame_status.json for the dependent skills."""
    return {"schema": "consent_frame_status/v1", "org_ref": org_ref,
            "review_state": review_state, "datasets": list(datasets or [])}


def consent_gate_ok(status, dataset, need_linkage=False):
    """Helper the dependent skills call to check the shared status object.
    Returns (ok: bool, reason: str). ok=False means route to
    consent-and-data-governance (fire H-SAFETY)."""
    if not status or status.get("schema") != "consent_frame_status/v1":
        return (False, "no consent_frame_status object present")
    row = next((d for d in status.get("datasets", []) if d.get("dataset") == dataset), None)
    if row is None:
        return (False, f"no consent frame recorded for dataset {dataset!r}")
    if not row.get("frame_exists"):
        return (False, f"consent frame not yet established for {dataset!r}")
    if need_linkage and not row.get("linkage_permitted"):
        return (False, f"linkage/secondary use not permitted for {dataset!r}")
    return (True, f"consent frame OK for {dataset!r} (review_state={status.get('review_state')})")
