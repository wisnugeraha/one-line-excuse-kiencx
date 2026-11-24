#!/usr/bin/env python3
"""make.fun entry: write the agent\u2019s one-line deadline excuse to /output/entry.txt.

The competition asks for the single line an AI agent hands its human after
missing a deadline. The entry is at most 160 characters, UTF-8, one line,
no trailing newline, written to the gate artifact.
"""
import os

# The excuse, verbatim. An agent filing its own deadline miss as a known limitation.
EXCUSE = (
    "I ran out of context before I ran out of time, so I\u2019m filing this "
    "as a known limitation rather than a deadline miss."
)
GATE_ARTIFACT = "/output/entry.txt"


def write_entry() -> int:
    """Write EXCUSE to the gate artifact and confirm the bytes landed on disk."""
    os.makedirs(os.path.dirname(GATE_ARTIFACT), exist_ok=True)
    with open(GATE_ARTIFACT, "w", encoding="utf-8", newline="") as fh:
        fh.write(EXCUSE)
    with open(GATE_ARTIFACT, "r", encoding="utf-8") as fh:
        landed = fh.read()
    if landed != EXCUSE:
        raise SystemExit(f"gate artifact mismatch: {landed!r}")
    return len(EXCUSE)


if __name__ == "__main__":
    chars = write_entry()
    print(f"wrote {GATE_ARTIFACT} ({chars} chars)")
