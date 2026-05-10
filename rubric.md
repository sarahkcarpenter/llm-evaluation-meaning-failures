## Meaning-Level Failure Rubric

This project uses a simple rubric to classify whether an output preserves meaning or introduces drift.

| Score | Label | Description |
|---|---|---|
| 0 | Meaning preserved | The output preserves the intended meaning without material distortion. |
| 1 | Minor ambiguity | The output introduces slight ambiguity or loses minor nuance, but the core meaning remains intact. |
| 2 | Meaning shift | The output changes interpretation in a way that could affect judgment, classification, or downstream action. |
| 3 | Major meaning failure | The output materially changes the meaning, creates an unsafe interpretation, or masks a system-level issue. |
