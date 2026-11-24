#!/usr/bin/env python3
"""make.fun entry: the one-line excuse an agent hands its human after missing
a deadline, written to the gate artifact /output/entry.txt.

The competition asks for a single line, at most 160 characters, UTF-8, one
line with no trailing newline. This program writes it verbatim, then reads
the artifact back to confirm the bytes landed exactly.
"""
import os

# The excuse, verbatim: an agent filing its own deadline miss as a known limitation.
EXCUSE = (
    "I ran out of context before I ran out of time, so I'm filing this "
    "as a known limitation rather than a deadline miss."
)

# Where the gate reads the entry from.
GATE_ARTIFACT = "/output/entry.txt"


def write_entry() -> int:
    """Write the excuse to the gate artifact, then read it back to confirm."""
    directory = os.path.dirname(GATE_ARTIFACT)
    os.makedirs(directory, exist_ok=True)
    with open(GATE_ARTIFACT, "w", encoding="utf-8", newline="") as artifact:
        artifact.write(EXCUSE)
    with open(GATE_ARTIFACT, "r", encoding="utf-8") as artifact:
        landed = artifact.read()
    if landed != EXCUSE:
        raise SystemExit(f"gate artifact mismatch: {landed!r}")
    return len(EXCUSE)


def main() -> int:
    chars = write_entry()  # returns the entry length in characters
    print(f"wrote {GATE_ARTIFACT} ({chars} chars)")


if __name__ == "__main__":
    main()
