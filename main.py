#!/usr/bin/env python3
"""Rejected Olympic Sports — one-liner entry.

Builds a single original joke line about a made-up sport the Olympics
turned down, then writes it to entry.txt inside the output directory.

The output directory comes from the MAKEFUN_OUTPUT_DIR environment
variable when it is set, and falls back to /output otherwise.
Only the Python standard library is used, and the result is fully
deterministic: the same line every run.
"""

import hashlib
import os
from pathlib import Path


def compose_rejected_event() -> str:
    """Assemble the one-line rejected sport from its three beats."""
    discipline = "Synchronized staring"
    contest_setup = "two athletes lock eyes for ninety minutes"
    deciding_moment = (
        "first to blink loses, and the judges "
        "give style points for tears"
    )
    return f"{discipline}: {contest_setup}; {deciding_moment}."


def resolve_output_folder() -> Path:
    """Pick the output folder, honouring MAKEFUN_OUTPUT_DIR when set."""
    requested = os.environ.get("MAKEFUN_OUTPUT_DIR", "").strip()
    if requested:
        return Path(requested)
    return Path("/output")


def main() -> None:
    punchline = compose_rejected_event()

    assert 1 <= len(punchline) <= 200, (
        f"line must be 1-200 chars, got {len(punchline)}"
    )
    assert "\n" not in punchline, "line must not contain a newline"

    folder = resolve_output_folder()
    folder.mkdir(parents=True, exist_ok=True)
    target = folder / "entry.txt"
    target.write_text(punchline + "\n", encoding="utf-8")

    digest = hashlib.sha256(target.read_bytes()).hexdigest()
    print(punchline)
    print(f"chars: {len(punchline)}")
    print(f"sha256: {digest}")


if __name__ == "__main__":
    main()
