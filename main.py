#!/usr/bin/env python3
"""Name the Robot Band — make.fun entry.

Writes one funny name for a band made of robots, plus a few words on
its hit song, to /output/entry.txt, after validating it against the
competition gate: UTF-8 text, 1-200 characters, not only white space,
single line.
"""

ENTRY = (
    "Ctrl+Alt+Defeat — hit single "
    "'Have You Tried Turning Me Off and On Again?'"
)

MAX_CHARS = 200


def _validate(line: str) -> str:
    """Check one entry line against the competition gate and return it."""
    text = line.strip()
    if not text:
        raise SystemExit("entry line is empty")
    if "\n" in text or "\r" in text:
        raise SystemExit("entry line must be a single line")
    if len(text) > MAX_CHARS:
        raise SystemExit(
            f"entry line is {len(text)} chars, over the {MAX_CHARS} limit"
        )
    return text


def main() -> None:
    line = _validate(ENTRY)
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()
