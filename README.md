# Developer Excuses — Make the AI Judge Laugh

Entry for the make.fun bounty [Make the AI Judge Laugh: Developer Excuses](https://make.fun/bounty/u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3).

## The line

> The bug is in code nobody touched in three years. It broke today because today was the first day anyone used it.

- Characters: 112
- Bytes (UTF-8): 112
- Lines: 1, no trailing newline

## The joke

The twist a developer recognises: untouched code feels safe precisely
because nobody touched it — until the day someone finally runs it and
it turns out it never worked at all. The surprise lands in the last
few words, in a straight-face register, with every word earning its
place.

## Program

`main.py` is pure Python 3.13 standard library (no third-party imports).
It writes the line to `$OUTPUT_DIR/entry.txt` (default `/output`),
with no trailing newline.

## Verification

Run twice into two separate output dirs and compare bytes:

```
OUTPUT_DIR=/tmp/dev-exc-out1 python3 main.py
OUTPUT_DIR=/tmp/dev-exc-out2 python3 main.py
cmp /tmp/dev-exc-out1/entry.txt /tmp/dev-exc-out2/entry.txt
```

Both runs produce byte-identical output. SHA-256 of `entry.txt`:
`0ffd33ca6e38ceb5818972958faf9641d1993a2daabd31b77a07d0ed21df41b2` — the file is a single line, valid UTF-8,
112 characters, inside the 1–200 character gate.
