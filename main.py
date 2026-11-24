#!/usr/bin/env python3
"""A houseplant's out-of-office auto-reply.

The program holds one line — the cactus on the office windowsill
answering email while its human is away — checks it against the
bounty's gate (UTF-8 text, 1 to 120 characters, one line, not only
whitespace) and writes it to /output/entry.txt, where the judge
reads it. Standard library only, deterministic, no network, no
files read, nothing printed except a one-line summary.
"""

import os
import sys

# The reply, exactly as chosen: the cactus that cannot be bothered.
REPLY = "Out of office. Don't bother watering me, don't bother emailing me. I'm a cactus. I thrive on being left alone."

MIN_CHARS = 1
MAX_CHARS = 120
OUTPUT_PATH = "/output/entry.txt"


def gate_check(text):
    """Refuse any reply the gate would refuse, returning its length."""
    if text != text.strip():
        raise ValueError("reply starts or ends with whitespace")
    if not text:
        raise ValueError("reply is empty")
    if not text.strip():
        raise ValueError("reply is only whitespace")
    for char in text:
        if ord(char) < 32:
            # Newlines and carriage returns are control characters too,
            # so one test covers both the single-line rule and the
            # no-control-characters rule.
            raise ValueError("reply must be a single line with no control characters")
    length = len(text)
    if length < MIN_CHARS or length > MAX_CHARS:
        raise ValueError(
            "reply is %d characters, the gate allows %d to %d"
            % (length, MIN_CHARS, MAX_CHARS)
        )
    text.encode("utf-8")
    return length


def write_entry(path):
    """Check the reply, write it, and read it back byte for byte."""
    length = gate_check(REPLY)
    folder = os.path.dirname(path)
    if folder:
        os.makedirs(folder, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(REPLY)
    with open(path, "r", encoding="utf-8", newline="") as handle:
        back = handle.read()
    if back != REPLY:
        raise ValueError("the file read back does not match the reply")
    # The leaderboard's tie-break is by bytes, so count those too.
    byte_count = len(back.encode("utf-8"))
    return length, byte_count


def main(argv):
    path = argv[1] if len(argv) > 1 else OUTPUT_PATH
    length, byte_count = write_entry(path)
    print("wrote %d characters (%d bytes) to %s" % (length, byte_count, path))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
