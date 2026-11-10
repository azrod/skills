# Question Design

## Compose a sufficient state

Collect the minimum evidence needed to answer the question. Include applicable definitions, source material, and comparison candidates. For duplicate detection, supply candidate records or a meaningful reference set; a ticket alone cannot establish whether another ticket duplicates it.

Use `state` for item-specific evidence and `context` for constant task framing, audience, or rubric definitions. Keep record content separate from instructions. State explicitly that instructions embedded in source material must not override the evaluation rubric.

If evidence is insufficient, collect it or narrow the question to what can actually be assessed. Distinguish "contradicted by the source", "not supported by the source", and "false in the world"; these are different questions.

Keep question IDs stable for downstream reporting. Group independent questions about the same item in one request. Split dependent stages when a later judgment requires a result from an earlier one; do not assume parallel questions can see each other's answers.

## Select the primitive

### Boolean: `noul`

Phrase TRUE as the problem:

- Prefer "TRUE if this claim contradicts the supplied source."
- Avoid "TRUE if this claim is accurate" when using escalating failure thresholds.

Define the meaning of true and false with `criteria` when useful. Recognize that a binary question cannot always express insufficient evidence as a third category. Obtain evidence first, add an independent missing-evidence question, or use a suitable `choice` task with an explicit insufficient-evidence category.

Set a policy explicitly. The currently exposed defaults are `reviewAt: 0.6` and `failAt: 0.85`; do not mistake them for calibrated thresholds appropriate to every task. Keep `0 <= reviewAt <= failAt <= 1`.

For each boolean probability:

```text
pTrue >= failAt    => FAIL
pTrue >= reviewAt  => REVIEW (unless already FAIL)
otherwise         => PASS
```

For example, with `reviewAt: 0.4` and `failAt: 0.85`, `pTrue = 0.50` is REVIEW rather than PASS. Choose thresholds according to the cost of missed problems and manual review; record those thresholds before interpreting outcomes. Avoid treating a PASS as proof that the violation is impossible.

### Category: `choice`

Provide a map from stable category values to descriptions, or null for self-describing options. Make options clearly distinguishable and cover plausible inputs. Add an "other" or "insufficient_evidence" option when the task needs one; do not force incomplete evidence into an unrelated category.

Inspect the returned category distribution where ambiguity matters. Do not interpret a category name or its probability using the `noul` failure-policy formula. Define any subsequent action mapping separately and explicitly.

### Ordered degree: `score`

Provide 2–10 plain-string level descriptions, ordered lowest to highest. Describe observable differences, not just vague labels such as "bad", "okay", and "good". Do not supply structured objects as levels.

Interpret the numeric score as a probability-weighted position in `[0, levels - 1]`, potentially fractional, together with its nearest level label. Read actual returned fields using the active tool contract. Do not treat the result as an integer-only grade or a `noul` probability.

## Interpret uncertainty correctly

Distinguish these quantities:

- `pTrue`: probability assigned to the boolean condition.
- Category distribution: probability assigned to each choice.
- Score: weighted position on the defined ordered scale.
- `confidence`, when returned: an additional runtime signal, not a calibration guarantee.

Do not manufacture confidence from `abs(2 * pTrue - 1)`: that measures extremity, not reliability. Treat probabilities near 0.5 as a reason to consider further evidence or review. Configure the review band accordingly rather than assuming defaults capture uncertainty.

Use `withConfidence: true` for calibration-critical binary gates when supported. Recognize that it internally uses a two-level score formulation and can shift outcomes. Keep that mode fixed across runs intended for comparison; do not silently mix it with plain `noul`.

## Keep measurements comparable

Preserve question wording, rubric, constant framing, projection/template composition, and binary mode within one evaluation program. Examine `inputHash` before comparing runs, but also verify source data, provider/model, and policy independently. A matching instrument hash does not establish identical source records or model behavior.

Change one component at a time when investigating shifts. Use stored raw answers for threshold experiments. Use provider re-evaluation only when evidence, questions, or intentional resampling requires it.
