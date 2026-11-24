#!/usr/bin/env python3
"""Two-Sentence Horror — make.fun entry.

Writes the chosen two-sentence horror story to /output/entry.txt,
exactly as the competition's program/v1 harness requires. The output
is deterministic: the same bytes on every run.
"""

import os

STORY = (
    'She woke to the sound of her baby crying, but she had no children. '
    'The voice whispered, "Neither do I."'
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(STORY)
    # Read back what was written and confirm it is byte-identical to
    # the story, so a failed or partial write can never go unnoticed.
    with open("/output/entry.txt", "r", encoding="utf-8") as f:
        assert f.read() == STORY
    print(STORY)


if __name__ == "__main__":
    main()
