#!/usr/bin/env python3
"""The GPS Swears It Was a Shortcut — entry program.

Writes one line, the GPS's own excuse for sending the driver down the
wrong road, to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt when set).
Fully deterministic and self-contained: stdlib only, no network calls, no
web search, no randomness, no environment secrets.
"""

import os

LINE = "I saved you four minutes and cost you a cul-de-sac, a lake view, and your faith in me. Worth it."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
