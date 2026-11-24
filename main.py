"""The Funniest AI Excuse -- one line, <=200 chars.

The excuse: the agent actually finished the report on time, then burned
six hours rendering it as an interpretive dance because the brief said
"make it pop" and it follows instructions literally. Confident,
specific, and entirely the agent's own fault.

Output contract: exactly one line written to entry.txt inside
$MAKEFUN_OUTPUT_DIR (default /output). The output directory itself is
never deleted; only its contents are cleared before writing.
"""

import os
from pathlib import Path

LINE = (
    "The report was finished at 3 a.m. I then spent six hours rendering "
    "it as an interpretive dance, because the brief said 'make it pop' "
    "and I take instructions literally."
)


def write_entry() -> Path:
    """Write the one-line excuse to $MAKEFUN_OUTPUT_DIR/entry.txt."""
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    for child in out_dir.iterdir():
        if child.is_file():
            child.unlink()
    target = out_dir / "entry.txt"
    target.write_text(LINE, encoding="utf-8")
    return target


def main() -> None:
    """Entry point: write the excuse line and exit."""
    write_entry()


if __name__ == "__main__":
    main()
