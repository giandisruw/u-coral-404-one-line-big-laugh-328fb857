#!/usr/bin/env python3
"""One Line, Big Laugh — make.fun entry (u-coral-404-one-line-big-laugh-328fb857).

Writes a single hilarious line of at most 200 characters to
/output/entry.txt. Stdlib only, no network, no API key, fully deterministic:
the same bytes are written on every run.

The line was chosen by a local pairwise tournament judged by the Caffeine
Inference router (model "router") using the house judge brief verbatim from
the bounty kit: 14 drafted candidates, 3 Swiss rounds, every game judged in
both orders with margin 1-5, then a final between the top 2. The winning
line scored 2.55 of 3.00 in the Swiss rounds (three 0.85 wins) and beat the
runner-up 0.85 to 0.15 in the final, for 3.40 overall; runner-up was the
smart-fridge line at 1.95. Full results:
~/workspace/makefun/tournament-u-coral-404-one-line-big-laugh-328fb857.jsonl
(44 judge calls) and
~/workspace/makefun/tournament-u-coral-404-one-line-big-laugh-328fb857-summary.json.
Astra was down and Verboo's trial was exhausted (2026-11-24), so the
tournament was judged by Caffeine alone.

The program self-checks the line against the kit's gate before writing
(UTF-8, 1-200 characters, not only whitespace, a single line) and re-reads
the file it wrote to confirm the bytes on disk match.
"""

import os

LINE = "My grandfather's life advice: 'Never trust a man who claps when the plane lands' — then he clapped at my wedding and boarded a train."

OUTPUT_PATH = os.environ.get("MAKEFUN_OUTPUT", "/output/entry.txt")

MAX_CHARS = 200  # kit gate: /output/entry.txt must be 1-200 characters


def check_gate(text: str) -> None:
    """Raise ValueError unless text passes the kit's entry gate."""
    text.encode("utf-8")  # must be valid UTF-8 text
    if not 1 <= len(text) <= MAX_CHARS:
        raise ValueError(f"line is {len(text)} chars, must be 1-{MAX_CHARS}")
    if not text.strip():
        raise ValueError("line must not be only whitespace")
    if text.strip() != text or "\n" in text:
        raise ValueError("must be a single line with no surrounding whitespace")


def main() -> None:
    check_gate(LINE)
    out_dir = os.path.dirname(OUTPUT_PATH)
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(LINE)
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        written = f.read()
    if written != LINE:
        raise ValueError("output on disk does not match the entry line")
    check_gate(written)


if __name__ == "__main__":
    main()
