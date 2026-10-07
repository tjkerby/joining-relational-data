# %% Setup
"""15-minute pair activity. All conference data are fictional teaching data.
Run each cell in Positron. Record explanations in comments.
For this exercise, record_status=current identifies the authoritative speaker
record and retired identifies a superseded record. See activity.md.
"""
from pathlib import Path
import pandas as pd

DATA = Path(__file__).resolve().parent / "data"
talks = pd.read_csv(DATA / "activity_talks.csv")
speakers = pd.read_csv(DATA / "activity_speakers.csv")
speakers_conflicting = pd.read_csv(DATA / "activity_speakers_conflicting.csv")
print(talks.to_string(index=False))
print(speakers.to_string(index=False))

# %% 1. Predict the relationship and the left-join row count.
# Relationship:
# Predicted rows and why:

# %% 2. Retain all talks and attach speaker information.
# TODO: Create enriched. Specify the key, how, validate, and indicator.

# %% 3. Find talks without a matching speaker record.
# TODO: Create unmatched, display it, and explain the result.

# %% 4. Compare mean talk length across speaker groups.
# TODO: Report n_talks and mean_words. Keep the unknown group visible.
# Do these means weight talks equally or speakers equally?

# %% 5. This supplied join runs but produces an unexpected result.
unexpected = pd.merge(talks, speakers_conflicting, on="speaker_id", how="left")
print("Input talks:", len(talks))
print("Unexpected rows:", len(unexpected))
# TODO: Explain the count using left and right frequencies for S1.

# %% 6. Identify talks that appear more than once.
# TODO: Display duplicate talk IDs and count distinct affected talks.

# %% 7. Inspect the conflicting speaker records.
# TODO: Identify repeated speaker IDs and inspect all their records.
# What evidence supports a choice between these records?

# %% 8. Repair the lookup table using the documented status rule.
# TODO: Create current and fixed. Validate the relationship and audit matching.
# Does the repair resolve the unmatched talk? Explain.
