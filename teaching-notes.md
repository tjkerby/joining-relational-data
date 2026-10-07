# Joining relational data: teaching notes

STAT 386, October 7, 2026. Planned duration: 50 minutes.

## Central takeaway

A join matches records through keys. Key uniqueness and match coverage determine
whether the result preserves the intended row unit and answers the question.

## Pacing

| Minutes | Slides | Work |
|---|---|---|
| 0-4 | 1-3 | Retrieve row identity |
| 4-13 | 4-9 | Master-file motivation, separate tables, keys, Venn diagrams |
| 13-25 | 10-20 | Joins, matching labels, mask, summary, repeated-key pairs |
| 25-40 | 21-22 | Pair activity |
| 40-47 | 23-27 | Debrief, validation, repair, changed weighting |
| 47-50 | 28-32 | Composite-key connection, checks, exit response |

Slides 33-35 are optional references. Preserve the 15-minute activity. Answer
slides need only 20-30 seconds. If needed, let students explore the complete
composite-key example after class.

## Presentation and coding

All files live in one repo. Run follow_along.py cell by cell at the matching
slide headings. Complete displayed results appear on the slides, including the
eight-row flawed join and twelve-row repair and composite-key outputs. Slides
omit indexes and show NA for missing values. The notebook contains captured
outputs. explore_joins.py supports deeper exploration. Activity solutions live
beside the starter. Ask students to attempt the activity before reading them.

Show the Venn diagrams before code. Talk keys are S1/S2/S3, speaker keys S1/S2/S4.
Shading explains key retention. Return to pairs of table rows to explain counts.

Introduce indicator=True and define both, left_only, and right_only before
filtering. Then select the _merge column, apply .eq("left_only") to obtain a
Boolean Series, and use .loc[mask] to retain True rows. Explain that .eq is
elementwise equality and is equivalent to == for this comparison. Predict each
of the five mask values, then inspect the full one-row unmatched result.

## Answers and discussion

Opening: a long keyword row represents a talk-keyword pair. Both columns are
needed to identify a measurement. Connecting speaker attributes requires
another table because talks and speakers have different observational units.

Small demonstration: talks has five rows. S1 has three talks, S2 one, S3 one.
The clean speaker table has S1, S2, and unused S4. Left joins yield five rows,
inner four, right five, and outer six. T5/S3 is unmatched. There are no missing
keys in these data. NA on a slide denotes a missing value in the output.

The clean summary is A: three talks, mean 1200 words. B: one talk, mean 2400.
Unknown: one talk, mean 1600. Each mean weights talks equally. A speaker with
more talks therefore contributes more to an across-talk mean. Explain that
dropna=False avoids silently excluding the unknown group from a grouped result.

Duplicate prediction: S1 contributes 3 times 2 = 6 pairs, and the full join has
eight rows. The original word total is 7600 and mean 1520. The flawed total is
11200 and mean 1400. Duplicating the three short S1 talks changes weighting.

Activity: twelve input talks, twelve clean joined rows, eleven matched talks.
A12/S9 is unmatched. S5 has no talk and is absent from the left join. Group A
has six talks and mean 1500, group B five and mean 1960, unknown one and mean
2100. Default grouping would omit the unknown group. The conflicting lookup
adds a retired B record for S1. Four S1 talks each match twice, giving sixteen
rows. A01-A04 repeat, representing four distinct affected talks.

Repair: the data dictionary explicitly makes current records authoritative for
the exercise. Filter by record_status before joining. Then many_to_one
validation succeeds and the output returns to twelve rows. S9 still lacks
metadata. Do not repair by keeping an arbitrary first row or by removing joined
rows. In real historical data, a time-dependent classification may require a
different matching rule.

Composite prediction: joining conference metadata on year alone yields 24 rows.
Year plus season yields 12 rows with a unique location per talk. This identifies
a conference, not a particular session. Session metadata would need an extra
session key.

Exit: enrollments should be the left table, catalog the right, with a left join
on course_id, validate=many_to_one, and indicator=True. Repeated right keys can
multiply enrollment rows. left_only finds unmatched enrollments. The validator
would reject repeated right keys before producing that flawed result.

## Conceptual distinctions

- A left join retains every left row but may repeat it.
- Cardinality concerns key uniqueness, whereas coverage concerns matching.
- An indicator reports a match even when another metadata field is missing.
- A many-to-many relationship can be legitimate when the output unit is a pair.
- A primary key should be unique and nonmissing. Foreign references can fail in
  imported CSVs even though a database would normally enforce integrity.
- pandas matches missing keys on both sides. The optional reference example
  demonstrates that behavior. Null keys require inspection before a join.
- Missing metadata after a join can reflect absent records, formatting problems,
  or a matched record with incomplete fields. Retention and missingness are
  separate analysis decisions.

## Bridge to missing data

Ask: "When a value is missing, what happened in the process that produced the
data?" Today students see one concrete mechanism: no matching lookup record.
Next lecture can expand to the indicator R and the dependence of missingness
on Y and other covariates X. Do not introduce MCAR/MAR/MNAR terminology here.

## Sources

- pandas merge API: https://pandas.pydata.org/docs/reference/api/pandas.merge.html
- pandas merging guide: https://pandas.pydata.org/docs/user_guide/merging.html

All datasets are authored fictional teaching examples. They do not describe
actual speakers, conference locations, or group characteristics.
