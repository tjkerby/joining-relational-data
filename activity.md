# Pair activity: joining relational data

Work with a partner for 15 minutes. Use `student_activity.py` in Positron.
All names, conferences, groups, locations, and measurements are fictional.

## The question

How does average talk length differ between speaker groups? Retain every talk
in the data, including talks whose speaker information is unavailable.

## First 7 minutes

1. Inspect `talks` and `speakers`. State the row unit and key for each table.
   Predict the relationship on `speaker_id` and the number of rows in a left join.
2. Create `enriched` by joining speaker information onto talks. Specify the key,
   retention rule, expected relationship, and a match indicator.
3. Create `unmatched` containing talks without a speaker-table match.
4. Summarize talk count and mean word count by group. Keep the unknown group
   visible. State whether the means weight talks or speakers equally.

## Remaining 8 minutes

5. Run the supplied join with `speakers_conflicting`. Explain its row count
   using the number of S1 rows on each side.
6. Display the talks that repeat and count the distinct affected talks.
7. Inspect every lookup record for the repeated speaker key. What do the
   records say, and what evidence supports a repair?
8. Apply the documented `record_status` rule, then validate and audit again.
   Explain which problems the repair resolves and which remain.

## Data dictionary

| File | One row represents | Intended key |
|---|---|---|
| activity_talks.csv | One talk | talk_id |
| activity_speakers.csv | One speaker | speaker_id |
| activity_speakers_conflicting.csv | One speaker record | speaker_id + record_status |
| conference_metadata.csv | One conference | year + season |

`num_words` measures talk length in words. `group` is an arbitrary fictional
speaker category, A or B. `record_status="current"` identifies the authoritative
speaker classification for this exercise. `"retired"` identifies a superseded
record. Select current records before combining them with the talks. This is
an exercise-specific rule, not a general rule for historical data.

## Hints

- Use `on="speaker_id"` to name the key explicitly.
- `validate="many_to_one"` checks the lookup key's uniqueness.
- `indicator=True` supplies `_merge` for inspecting matches.
- `groupby(..., dropna=False)` keeps an unknown group visible.
- `duplicated("speaker_id", keep=False)` marks every row for a repeated key.
- Row multiplication counts all matching pairs.

Be ready to explain your result, not just display your code.
