#!/usr/bin/env python3
"""One Letter: Coffee or Tea — entry program.

Writes exactly one letter, "A" (coffee), to entry.txt.

Deterministic: no input, no randomness, no network, no model calls.
The same run always writes the same single byte.
"""

import os

LETTER = "A"  # A = coffee, B = tea


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LETTER)
    # The grader collects outputs as another user: leave it world-readable.
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
