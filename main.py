"""Nap Billboard: sell ad space on the foreheads of sleeping commuters.

The pitch: brands buy the one billboard a packed rush-hour crowd cannot
look away from — a dozing stranger's forehead — and pay per nap.

Writes that one sentence to entry.txt. Deterministic: the sentence is a
fixed constant, no randomness, no network, no clock, no input.
"""

import sys
from pathlib import Path

SENTENCE = (
    "We sell ad space on the foreheads of sleeping subway commuters, "
    "and brands pay per nap because a dozing stranger's forehead is "
    "the one billboard a packed rush-hour crowd cannot look away from."
)


def main() -> None:
    out_dir = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    text = SENTENCE
    assert 1 <= len(text) <= 200, f"sentence is {len(text)} chars"
    assert text.count(".") == 1, "must be exactly one sentence"
    (out_dir / "entry.txt").write_text(text, encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()
