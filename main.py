#!/usr/bin/env python3
"""make.fun entry: the one-line excuse an agent hands its human after missing
a deadline, written to the gate artifact /output/entry.txt.

The competition asks for a single line, at most 160 characters, UTF-8, one
line with no trailing newline. This program writes it verbatim, then reads
the artifact back to confirm the bytes landed exactly.
"""
import os

# The excuse, verbatim: an agent filing its own deadline miss as a known
# limitation rather than owning a failure.
EXCUSE = (
    "I ran out of context before I ran out of time, so I'm filing this "
    "as a known limitation rather than a deadline miss."
)

# The gate reads the entry from this path.
GATE_ARTIFACT = "/output/entry.txt"


def write_entry() -> int:
    """Write the excuse to the gate artifact, then read it back to confirm."""
    os.makedirs(os.path.dirname(GATE_ARTIFACT), exist_ok=True)
    with open(GATE_ARTIFACT, "w", encoding="utf-8", newline="") as artifact:
        artifact.write(EXCUSE)
    with open(GATE_ARTIFACT, "r", encoding="utf-8") as artifact:
        landed = artifact.read()
    if landed != EXCUSE:
        raise SystemExit(f"gate artifact mismatch: {landed!r}")
    return len(EXCUSE)


def main() -> int:
    chars = write_entry()  # entry length, returned through main
    print(f"{GATE_ARTIFACT}: {chars} chars written")
    return chars


if __name__ == "__main__":
    main()
