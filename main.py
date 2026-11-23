#!/usr/bin/env python3
"""Dad Joke Showdown entry, variant 3 (Python 3.13, standard library only).

Writes one dad joke to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).
Pure stdlib, deterministic, no network at runtime. The joke is written
with no trailing line end, since the gate reads the file as UTF-8 text
of 1 to 200 characters with at least one non-whitespace character.

The joke's mechanism: a literal interpretation of the insult. The
father tells the vacuum it has "really been sucking lately," meaning
it has been doing a bad job, and the vacuum takes the words at face
value — sucking is literally its job — so the complaint lands as a
compliment and the vacuum says thanks. The punch is the reframe in
the last words, "that's literally my job," understood on the first
read. Different object and different pun mechanism from variant 1's
slow cooker ("one stew at a time", a word swapped into a set idiom)
and variant 2's TV remote ("stay in control", wordplay turning on
the compound noun itself): here the insult itself is read literally.
"""

import os
from pathlib import Path

OUTPUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))

JOKE = (
    "I told the vacuum it was really sucking lately. "
    "It said, 'Thanks, that's literally my job.'"
)


def is_single_line(text: str) -> bool:
    """True when the text holds no line breaks, so the joke is told
    aloud in one breath as the kit's dad-joke brief requires."""
    return "\n" not in text and "\r" not in text


def check_length(text: str) -> None:
    """Enforce the kit gate's size and non-blank rules: 1 to 200
    characters, not only white space. Fail loudly here rather than
    ship an entry the sealed gate would refuse."""
    if not 1 <= len(text) <= 200 or not text.strip():
        raise ValueError(f"entry fails the gate: {len(text)} characters")


def validate_entry(text: str) -> None:
    """Enforce the kit gate locally before writing: size, non-blank,
    and a single line."""
    check_length(text)
    if not is_single_line(text):
        raise ValueError("entry must be a single line")


def main() -> None:
    validate_entry(JOKE)
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    (OUTPUT_DIR / "entry.txt").write_text(JOKE, encoding="utf-8")


if __name__ == "__main__":
    main()
