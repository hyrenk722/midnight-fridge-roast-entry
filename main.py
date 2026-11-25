"""Entry for the make.fun competition "Midnight Fridge Roast"
(u-carbon-forge-midnight-fridge-roast-fc5d44a7).

Writes one roast of a smart fridge that refuses to open after midnight,
a single line under 200 characters, to /output/entry.txt
(or $MAKEFUN_OUTPUT_DIR/entry.txt).
"""

import os

ROAST = "Midnight, hungry, and my fridge just stands there locked \u2014 the only thing in this house with boundaries."

OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def validate(text):
    """Mirror the competition gate: UTF-8 text, 1-200 characters,
    not only whitespace, exactly one line."""
    if not isinstance(text, str):
        raise ValueError("entry must be text")
    if not (1 <= len(text) <= 200):
        raise ValueError(f"entry must be 1-200 characters, got {len(text)}")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    text.encode("utf-8")  # raises if not valid UTF-8
    return text


def check_gate(text):
    """Gate check kept separate from validate() so the caller can
    distinguish a gate failure from a plain validation error."""
    return validate(text)


def main():
    roast = check_gate(ROAST)
    os.makedirs(OUT_DIR, exist_ok=True)
    path = os.path.join(OUT_DIR, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(roast)
    with open(path, "rb") as f:
        written = f.read()
    if written != roast.encode("utf-8"):
        raise ValueError("read-back mismatch: written bytes differ from entry")
    print(f"Wrote {len(roast)} characters ({len(written)} bytes) to {path}")


if __name__ == "__main__":
    main()
