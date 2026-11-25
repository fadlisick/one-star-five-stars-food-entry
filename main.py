#!/usr/bin/env python3
"""One Star, Five Stars for the Food — entry program.

Writes one alien-tourist review sentence to /output/entry.txt.
Deterministic: no randomness, no network, no clock reads.
"""

import os

REVIEW = (
    "One star: my ship was towed, my tentacles sunburned, and the locals "
    "kept asking for selfies, but the pizza was so good I forgot to file "
    "a complaint."
)


def main() -> None:
    # Gate guard: the competition requires 1-200 chars of non-blank text.
    text = REVIEW.strip()
    assert 1 <= len(text) <= 200, f"entry length {len(text)} outside 1-200"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(REVIEW + "\n")


if __name__ == "__main__":
    main()
