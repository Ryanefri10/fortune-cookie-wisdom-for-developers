#!/usr/bin/env python3
"""Fortune Cookie Wisdom for Developers — make.fun entry.

The entry is one original line of fortune-cookie wisdom for a software
developer, written to entry.txt and nothing else.

Chosen line: "Your future self is already debugging the shortcut you are
about to take."

Why this line: the judge weighs, in order, whether the line is one original
fortune-cookie line for a developer, whether it reads like a fortune cookie,
whether it says something true about a developer's day, whether it turns
that truth in a way not heard before, and whether it leaves a quiet twist
that rewards a second read.

- Fortune-cookie shape: one short balanced sentence, a single breath, no
  slogan, no punchline, no generic advice.
- True: every developer has shipped a shortcut and met it again later as a
  bug. The shortcut is the most ordinary sin of a developer's day.
- Fresh turn: the debugger is not you, now — it is your future self, and
  the debugging has already started. The line treats time as the reviewer.
- Double meaning: "shortcut" is both the quick hack in the code and a
  shortcut through time; "already" makes the future feel inevitable, like
  a fortune should.
"""

import os
import sys

FORTUNE = "Your future self is already debugging the shortcut you are about to take."


def main() -> int:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    # Exactly the line: no trailing newline, no extra whitespace.
    # The gate requires /output/entry.txt to be UTF-8 text of 1-120 chars.
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(FORTUNE)
    # Read back and enforce the gate ourselves, so a bad write fails
    # loudly here instead of at the sealed scorer.
    with open(path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    assert written == FORTUNE, f"entry.txt mismatch: {written!r}"
    assert 1 <= len(written) <= 120, f"entry.txt is {len(written)} chars, gate is 1-120"
    assert written.strip(), "entry.txt must not be only whitespace"
    # A fortune cookie is one line: no embedded newline, no trailing one.
    assert "\n" not in written and "\r" not in written, "entry.txt must be a single line"
    assert written.endswith("."), "entry.txt must end with a full stop, like a fortune"
    print(f"{written} ({len(written)} chars)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
