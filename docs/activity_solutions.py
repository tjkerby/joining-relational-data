# %% Setup
"""Instructor solutions to the 15-minute pair activity. Fictional teaching data."""
from pathlib import Path
import pandas as pd
DATA = Path(__file__).resolve().parent / "data"
talks = pd.read_csv(DATA / "activity_talks.csv")
speakers = pd.read_csv(DATA / "activity_speakers.csv")
speakers_conflicting = pd.read_csv(DATA / "activity_speakers_conflicting.csv")

def show(label, df):
    print("\n" + label)
    print(df.to_string(index=False))

# %% 1. Prediction
# Many-to-one, from talks to speakers on speaker_id. Right keys are unique.
# A left join should retain exactly 12 rows here.

# %% 2. Attach metadata and check the result.
enriched = pd.merge(
    talks, speakers, on="speaker_id", how="left",
    validate="many_to_one", indicator=True,
)
show("Clean join", enriched)
print("Rows:", len(enriched), "Unique talk IDs:", enriched["talk_id"].is_unique)

# %% 3. Matching audit
unmatched = enriched.loc[enriched["_merge"].eq("left_only")]
show("Unmatched: A12 with speaker S9", unmatched)
# Speaker S5 has no talk and does not appear in this left join.

# %% 4. Keep unknown group visible.
summary = (
    enriched.groupby("group", dropna=False, as_index=False)
    .agg(n_talks=("talk_id", "size"), mean_words=("num_words", "mean"))
)
show("Talk-weighted summary", summary.round(1))
# A: 6 talks, 1500 words. B: 5 talks, 1960 words. Unknown: 1 talk, 2100 words.
# Each talk has equal weight. A speaker with more talks contributes more often.

# %% 5. 4 S1 talks each match 2 speaker records, producing 8 rows.
unexpected = pd.merge(talks, speakers_conflicting, on="speaker_id", how="left")
print("Unexpected rows:", len(unexpected))  # 16 = 8 for S1 + 8 other talks.

# %% 6. Four distinct talk IDs repeat.
duplicates = unexpected.loc[unexpected["talk_id"].duplicated(keep=False)]
show("Repeated talk rows", duplicates)
print("Affected IDs:", sorted(duplicates["talk_id"].unique()))
print("Distinct affected talks:", duplicates["talk_id"].nunique())

# %% 7. Inspect both conflicting lookup records.
conflicts = speakers_conflicting.loc[
    speakers_conflicting["speaker_id"].duplicated(keep=False)
]
show("Conflicting records", conflicts)
# The supplied data dictionary defines current as authoritative for this exercise.

# %% 8. Apply that rule before joining, then validate and audit again.
current = speakers_conflicting.loc[speakers_conflicting["record_status"].eq("current")]
fixed = pd.merge(
    talks, current, on="speaker_id", how="left",
    validate="many_to_one", indicator=True,
)
show("Repaired join", fixed)
print("Rows:", len(fixed), "Unique talk IDs:", fixed["talk_id"].is_unique)
show("Still unmatched", fixed.loc[fixed["_merge"].eq("left_only")])
# The repair fixes duplicated matches. It supplies no missing S9 speaker record.

# %% Closing composite-key example
conference_metadata = pd.read_csv(DATA / "conference_metadata.csv")
with_location = pd.merge(
    talks, conference_metadata, on=["year", "season"],
    how="left", validate="many_to_one",
)
show("Composite-key result", with_location)
