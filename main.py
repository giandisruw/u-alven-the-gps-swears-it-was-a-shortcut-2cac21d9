#!/usr/bin/env python3
"""The GPS Swears It Was a Shortcut — entry program.

Writes one line, the GPS's own excuse for sending the driver down the
wrong road, to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt when set).
Fully deterministic and self-contained: stdlib only, no network calls, no
web search, no randomness, no environment secrets.

Revision: the write path is now validate -> atomic write -> read-back
verify, so a truncated or corrupted entry.txt can never be shipped
silently. The winning line itself is unchanged.
"""

import os

LINE = "I saved you four minutes and cost you a cul-de-sac, a lake view, and your faith in me. Worth it."

MAX_CHARS = 200


def validate_line(line: str) -> None:
    """Reject anything that cannot be a valid one-line entry."""
    if not isinstance(line, str) or not line:
        raise ValueError("entry line must be a non-empty string")
    if "\n" in line or "\r" in line:
        raise ValueError("entry line must be a single line")
    if len(line) > MAX_CHARS:
        raise ValueError(
            "entry line exceeds %d characters: %d" % (MAX_CHARS, len(line))
        )
    if line != line.strip():
        raise ValueError("entry line must not have leading/trailing whitespace")


def write_entry(line: str, out_dir: str) -> str:
    """Write entry.txt atomically: temp file, flush, fsync, rename, fsync dir."""
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    tmp_path = path + ".tmp"
    payload = (line + "\n").encode("utf-8")
    with open(tmp_path, "wb") as f:
        f.write(payload)
        f.flush()
        os.fsync(f.fileno())
    os.replace(tmp_path, path)
    dir_fd = os.open(out_dir, os.O_RDONLY)
    try:
        os.fsync(dir_fd)
    finally:
        os.close(dir_fd)
    return path


def verify_written(path: str, expected_line: str) -> None:
    """Read entry.txt back from disk and compare it byte-for-byte."""
    with open(path, "rb") as f:
        actual = f.read()
    expected = (expected_line + "\n").encode("utf-8")
    if actual != expected:
        raise RuntimeError(
            "verification failed: entry.txt is %d bytes, expected %d bytes"
            % (len(actual), len(expected))
        )


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    validate_line(LINE)
    path = write_entry(LINE, out_dir)
    verify_written(path, LINE)


if __name__ == "__main__":
    main()
