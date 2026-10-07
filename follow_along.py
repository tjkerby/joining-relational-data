"""Run matching slide cells in Positron. All data are fictional.
Optional deeper examples are in explore_joins.py.
"""

# %% Setup
from pathlib import Path
import pandas as pd
DATA = Path(__file__).resolve().parent / "data"
talks = pd.read_csv(DATA / "demo_talks.csv")
speakers = pd.read_csv(DATA / "demo_speakers.csv")
speakers_conflicting = pd.read_csv(DATA / "demo_speakers_conflicting.csv")
def show(label, value):
    print("\n" + label)
    print(value.to_string(index=False) if isinstance(value, pd.DataFrame) else value)
show("talks", talks)
show("speakers", speakers)

# %% Slide 11: Left join: every talk remains
left = pd.merge(talks, speakers, on="speaker_id", how="left")
show("left", left)

# %% Slide 13: Inner join: matched talks only
inner = pd.merge(talks, speakers, on="speaker_id", how="inner")
show("inner", inner)

# %% Slide 14: The _merge column records where keys match
audited = pd.merge(talks, speakers, on="speaker_id", how="left", indicator=True)
show("Matching status", audited[["talk_id", "speaker_id", "group", "_merge"]])
# both: a matching key in each input.
# left_only: a retained left row without a matching right key.
# right_only: a retained right row without a matching left key.
# A left join has no right_only rows. Outer/right joins can retain them.

# %% Slide 16: Equality produces a mask, then loc keeps rows
mask = audited["_merge"].eq("left_only")
# Equivalent familiar syntax: mask = audited["_merge"] == "left_only"
show("Elementwise comparison", pd.DataFrame({
    "talk_id": audited["talk_id"], "_merge": audited["_merge"], "mask": mask,
}))
unmatched = audited.loc[mask]
show("unmatched", unmatched[["talk_id", "speaker_id", "_merge"]])

# %% Slide 17: A summary after joining
summary = (
    left.groupby("group", dropna=False, as_index=False)
    .agg(n_talks=("talk_id", "size"), mean_words=("num_words", "mean"))
)
show("summary", summary)

# %% Slide 19: Each matching pair produces a row
bad = pd.merge(talks, speakers_conflicting, on="speaker_id", how="left")
show("Complete flawed join", bad[["talk_id", "speaker_id", "num_words", "group"]])

# %% Slide 25: Validation enforces the expected relationship
activity_talks = pd.read_csv(DATA / "activity_talks.csv")
speakers_conflicting = pd.read_csv(DATA / "activity_speakers_conflicting.csv")
try:
    pd.merge(activity_talks, speakers_conflicting, on="speaker_id", how="left", validate="many_to_one")
except pd.errors.MergeError as error:
    print("MergeError:", error)

# %% Slide 26: A repair based on the data meaning
current = speakers_conflicting.loc[speakers_conflicting["record_status"].eq("current")]
fixed = pd.merge(activity_talks, current, on="speaker_id", how="left", validate="many_to_one", indicator=True)
show("fixed", fixed[["talk_id", "group", "_merge"]])

# %% Slide 27: Row multiplication changes the analysis
comparison = pd.DataFrame({
    "quantity": ["rows", "total_words", "mean_words"],
    "original": [len(talks), talks["num_words"].sum(), talks["num_words"].mean()],
    "flawed_join": [len(bad), bad["num_words"].sum(), bad["num_words"].mean()],
})
show("comparison", comparison)

# %% Slide 29: Composite key: year and season
conference_metadata = pd.read_csv(DATA / "conference_metadata.csv")
with_location = pd.merge(activity_talks, conference_metadata, on=["year", "season"], how="left", validate="many_to_one")
show("with_location", with_location[["talk_id", "year", "season", "location"]])

# %% Slide 30: A checking routine for joins
show("Unique talk IDs", talks["talk_id"].is_unique)
show("Unique speaker IDs", speakers["speaker_id"].is_unique)
show("Missing speaker keys", speakers["speaker_id"].isna().sum())

# %% Slide 33: Reference: names and overlapping columns
directory = speakers.rename(columns={"speaker_id": "person_id"})
renamed = pd.merge(talks, directory, left_on="speaker_id", right_on="person_id", how="left", validate="many_to_one")
show("renamed", renamed[["talk_id", "person_id", "speaker"]])

# %% Slide 34: Reference: missing keys
left_keys = pd.DataFrame({"key": [None], "x": [1]})
right_keys = pd.DataFrame({"key": [None], "y": [2]})
show("Missing keys match", pd.merge(left_keys, right_keys, on="key", how="inner"))
