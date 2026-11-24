#!/usr/bin/env python3
"""make.fun entry: writes the agent's one-line excuse to /output/entry.txt.

The line is the competition's required text, emitted verbatim in UTF-8
with no trailing newline (the gate reads the file's whole content).
"""
import os

ENTRY = "I ran out of context before I ran out of time, so I'm filing this as a known limitation rather than a deadline miss."
OUT = "/output/entry.txt"


def write_entry():
    """Write the excuse to the gate artifact."""
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as f:
        f.write(ENTRY)


def main():
    write_entry()
    print(f"Wrote entry to {OUT} ({len(ENTRY)} chars)")


if __name__ == "__main__":
    main()
