"""Optional deeper examples after the follow-along code."""
from pathlib import Path
import pandas as pd
DATA = Path(__file__).resolve().parent / "data"
talks = pd.read_csv(DATA / "demo_talks.csv")
speakers = pd.read_csv(DATA / "demo_speakers.csv")
for how in ["left", "inner", "right", "outer"]:
    result = pd.merge(talks, speakers, on="speaker_id", how=how, indicator=True)
    print(f"\n{how} join: {len(result)} rows")
    print(result.to_string(index=False))
# Matching can succeed even when another metadata field is missing.
incomplete = speakers.copy()
incomplete.loc[incomplete["speaker_id"].eq("S2"), "group"] = None
audit = pd.merge(talks, incomplete, on="speaker_id", how="left", indicator=True)
print("\nMatched S2 row with missing group:")
print(audit.loc[audit["speaker_id"].eq("S2")].to_string(index=False))
# Meaningful suffixes label overlapping speaker fields.
labels = talks.assign(speaker="Unverified label")
suffixed = pd.merge(labels, speakers, on="speaker_id", how="left", suffixes=("_talk", "_directory"))
print("\nOverlapping fields:")
print(suffixed.to_string(index=False))
activity_talks = pd.read_csv(DATA / "activity_talks.csv")
conferences = pd.read_csv(DATA / "conference_metadata.csv")
wrong = pd.merge(activity_talks, conferences, on="year", how="left")
print("\nYear-only join:", len(wrong), "rows")
print(wrong.to_string(index=False))
