"""Entry program for the 'One Line of Earned Pride' make.fun bounty.

The entry is a single line, 1 to 240 characters: a quiet, earned
moment of pride — a night-shift nurse who spent three evenings
reading a ventilator's manual finally gets the old machine humming
again at 2 a.m., and the whole ward exhales with her. No trophy,
no podium: the pride is in the work landing. The program writes
exactly that one line to /output/entry.txt (an optional first
argument overrides the destination for a dry run).
"""

import sys
from pathlib import Path

LINE = (
    "At 2 a.m. the night-shift nurse got the ward's old ventilator "
    "humming again \u2014 three evenings reading its manual, one held "
    "breath \u2014 and the whole floor exhaled with her."
)
DEFAULT_TARGET = Path("/output/entry.txt")


def main(argv):
    assert 1 <= len(LINE) <= 240, "entry must be 1-240 characters"
    assert LINE.strip() and "\n" not in LINE, "entry must be one line"
    target = Path(argv[1]) if len(argv) > 1 else DEFAULT_TARGET
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(LINE + "\n", encoding="utf-8")
    assert target.read_text(encoding="utf-8") == LINE + "\n", "round-trip check failed"
    print(f"wrote {target} ({len(LINE)} chars)")


if __name__ == "__main__":
    main(sys.argv)
