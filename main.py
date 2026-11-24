"""Make the AI Judge Laugh: Developer Excuses.

Writes one funny single-line excuse a developer gives when code breaks
in production to $OUTPUT_DIR/entry.txt (default /output).
Pure Python 3.13 standard library only.
"""

import os

LINE = "The bug is in code nobody touched in three years. It broke today because today was the first day anyone used it."


def main() -> None:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
