# STAT 386: Joining relational data

One repository contains the slides, follow-along code, activity, solutions,
teaching notes, and data.

## Setup and use

Open this folder in Positron and run `uv sync`. Select the project Python
environment. Run cells in follow_along.py at the matching slide headings.
Each cell names its slide number. To run everything, use:

```bash
uv run python follow_along.py
```

The slide deck includes the complete output for each follow-along display,
with indexes omitted and missing values labeled NA. follow_along.ipynb contains
the same examples with captured output. explore_joins.py adds deeper examples.

## Files

| File | Purpose |
|---|---|
| joining-relational-data.html | Self-contained deck with Venn diagrams |
| joining-relational-data.qmd and lecture.css | Editable Quarto source |
| joining-relational-data.pptx | Editable copy with native tables and diagrams |
| joining-relational-data.pdf | Static preview |
| follow_along.py and follow_along.ipynb | Slide-aligned examples |
| explore_joins.py | Optional deeper exploration |
| student_activity.py and activity.md | 15-minute pair activity |
| activity_solutions.py and activity_solutions.ipynb | Solutions in the same repo |
| teaching-notes.md | Timing, answers, and discussion guidance |
| data/ | Seven fictional datasets |
| assets/ | Editable SVG Venn diagrams |

Attempt the activity before opening its solutions. The data dictionary in
activity.md defines the status rule used in the repair.

## Editing slides

With Quarto installed, run `quarto render joining-relational-data.qmd`.
Static code listings and output tables require no Python execution to render.
Update outputs when you edit code or data. The deck has 32 core
slides and three optional reference slides.

Venn circles represent distinct join keys and shading shows retained keys.
Matching pairs determine output row counts. All names, groups, measurements,
and conferences are fictional teaching data.

## References

- https://pandas.pydata.org/docs/reference/api/pandas.merge.html
- https://pandas.pydata.org/docs/reference/api/pandas.Series.eq.html
- https://pandas.pydata.org/docs/user_guide/merging.html
