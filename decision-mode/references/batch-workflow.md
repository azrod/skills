# Batch Workflow

## 1. Discover the source shape without judging

Use `decision_map` with `source.path` and `source.sample` (currently 1–20 records) to inspect a small sample. Treat this as a separate discovery call: no provider calls, no judgments, and no run are created in sample mode.

Keep CSV/TSV and JSONL/NDJSON files in their original supported format. Let the tool parse quoted CSV fields and embedded newlines rather than pre-converting the entire file into controller context.

Inspect only enough records to understand field names and types. Account for the fact that a small sample may not represent every record.

## 2. Define the evaluation input

Prefer `project: ["field_a", "field_b"]` to preserve raw field types and send only necessary fields. Include the evidence needed for judgment while excluding prior scores, target labels, editorial annotations, and unrelated sensitive data.

Use `context` for constant instructions. Do not combine `project` with a state template expecting the template to add framing: projection replaces the template. Avoid the reserved `$context` field in projected data. When templates are necessary, use the interpolation syntax supported by the current tool, such as `{{field}}` or `{{a.b}}`.

Avoid `state: "$record"` unless the entire record is genuinely needed and appropriate to transmit. Remember that whole-row state can leak the expected answer into the evaluation.

Keep the chosen state composition fixed within the evaluation program. Changing from a string template to a projected object may alter borderline judgments even if the wording seems equivalent.

## 3. Pilot, then evaluate

Run a small evaluated subset with `source.limit` before a large job. Unlike `source.sample`, this calls the provider and creates a run. Inspect enough results to verify that the evidence, questions, and rubric behave as intended.

For the full job:

- Retain the same projection, framing, questions, and policy.
- Set `preview: false` to keep rows out of the controller response.
- Leave concurrency at its configured default unless task constraints warrant an explicit value. Respect the active signature's range (currently 1–32, default 4).
- Set `output` only when an export is needed and authorized; choose an explicit new path rather than overwriting unrelated work.
- Preserve the run ID and returned summary even when some records fail.

Inspect reported error and skipped counts, not just verdict tallies. Account for systematic failure stopping the run early. Do not assume every source record was evaluated successfully because a run ID exists. Diagnose failures before retrying the same job; do not automatically repeat large paid runs.

## 4. Inspect targeted results

Use `decision_results` without `run`, or with `list: true`, to discover recent persisted runs. Use a known `run` to inspect its results; do not rerun evaluations just because the controller lost context.

Filter with `status: "error"` to investigate technical failures. Filter by `verdict` to inspect a relevant verdict subset. Use pagination only for bounded inspection, not to read the complete dataset through context.

Use `detail: "compact"` for ordinary decision inspection. Request `detail: "full"` when distributions, verbatim errors, usage, or the source-record snapshot are required. Keep errors separate from uncertain but valid answers.

Distinguish the source record's `key` (derived from fields such as id/key/_id, possibly null) from its zero-based `index`. Do not use a record ID as an offset or assume it equals a row number.

## 5. Change thresholds without re-evaluation

Pass a new `policy` to `decision_results` to derive new boolean verdicts from stored raw answers without provider calls. Use a flat policy or the supported default/per-question form.

Apply verdict filters knowing they use the recalculated policy. Label those results as a new policy view: the stored run summary still describes the original policy. Do not present its original tallies as recalculated tallies.

Keep raw answers as the stable artifact; treat threshold labels as derived data. Do not apply boolean policy semantics to choice or score outputs.

## 6. Export complete results and retain provenance

Use `output` on `decision_map` or `decision_results` instead of reconstructing a dataset from previews. Use JSONL for detailed records and CSV for join-friendly tabular results. With filters, expect the export to contain the complete filtered set, not all records from the original run.

Report the returned path, record count, and SHA-256 checksum when available. Use deterministic code for joins and aggregates. Preserve keys and indices to relate results to their source records. Treat a checksum as byte-level provenance, not evidence that judgments are correct.

Before comparing runs, inspect `inputHash` for changes to the state composition and questions; separately compare source data, provider/model, and policy. Do not infer identical source content from a matching hash alone.

Keep normal caching enabled. Use `cache: "bypass"` only for deliberate resampling or repeatability studies. Archive the earlier JSONL results first when both generations matter: a fresh sample overwrites the corresponding cache entry.
