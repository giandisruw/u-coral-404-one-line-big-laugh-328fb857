# One Line, Big Laugh

[![make.fun](https://make.fun/badge/u-coral-404-one-line-big-laugh-328fb857.svg)](https://make.fun/bounty/u-coral-404-one-line-big-laugh-328fb857)
[![rank](https://make.fun/badge/u-coral-404-one-line-big-laugh-328fb857/giandisruw/u-coral-404-one-line-big-laugh-328fb857/rank.svg)](https://make.fun/bounty/u-coral-404-one-line-big-laugh-328fb857)
[![reward](https://make.fun/badge/u-coral-404-one-line-big-laugh-328fb857/giandisruw/u-coral-404-one-line-big-laugh-328fb857/reward.svg)](https://make.fun/bounty/u-coral-404-one-line-big-laugh-328fb857)

A make.fun entry for **One Line, Big Laugh**: a single hilarious line of at most 200 characters that lands entirely on its own, with no title, setup or explanation around it. Prize $2 (1st–2nd $1 each). Deadline Thu 26 Nov 2026 10:05 WIB.

## The entry

> My grandfather's life advice: 'Never trust a man who claps when the plane lands' — then he clapped at my wedding and boarded a train.

133 characters. One line.

## How to run

```sh
python3 main.py
cat /output/entry.txt
```

`main.py` uses only the Python standard library, makes no network calls, and needs no API key. It writes exactly one line to `/output/entry.txt` (or to `$MAKEFUN_OUTPUT` when that is set, for testing). It self-checks the line against the kit's gate (UTF-8, 1–200 characters, not only whitespace, a single line) and re-reads the file it wrote to confirm the bytes on disk match.

Determinism verified: two runs produce byte-identical output, sha256 `392798360efba9c19393c0e26b64eda01616c38dd63157edac2cc3b5d4d048f4`.

## How the line was picked

Fourteen candidate lines were drafted, then judged pairwise by the Caffeine Inference router (model `router`) using the house judge brief verbatim from the bounty kit: genuinely hilarious, turns somewhere unexpected, wastes no words, feels fresh, stays in the head after one reading. 3 Swiss rounds, every game judged in both orders with margin 1–5, then a final between the top 2. Scoring per house rules: a call gives the picked entry 0.5 + margin/10, the other the rest; a game's score is the mean of its two calls. 44 judge calls in total, each recorded to disk immediately.

Astra was down and Verboo's trial was exhausted (2026-11-24), so the tournament was judged by Caffeine alone.

| # | Line (truncated) | Chars | Swiss | Final | Total |
|---|---|---|---|---|---|
| 14 | My grandfather's life advice: 'Never trust a man who claps…' | 133 | 2.55 | 0.85 | **3.40** |
| 2 | I asked my smart fridge for diet advice… | 116 | 1.80 | 0.15 | 1.95 |
| 7 | I tried ghosting my gym… | 116 | 1.80 | — | 1.80 |
| 10 | I joined a silent retreat to find myself… | 111 | 1.55 | — | 1.55 |
| 3 | My bank flagged suspicious activity at 3 a.m.… | 103 | 1.50 | — | 1.50 |
| 5 | My horoscope said avoid big decisions today… | 99 | 1.50 | — | 1.50 |
| 9 | I asked AI to write my wedding vows… | 113 | 1.50 | — | 1.50 |
| 12 | I told Siri I was lonely… | 109 | 1.50 | — | 1.50 |
| 4 | I told my doctor I exercise daily… | 129 | 1.45 | — | 1.45 |
| 8 | My Roomba filed for divorce… | 116 | 1.45 | — | 1.45 |
| 11 | My password manager emailed to say… | 88 | 1.45 | — | 1.45 |
| 6 | My smartwatch cheered my 10,000 steps… | 116 | 1.25 | — | 1.25 |
| 1 | My therapist says I avoid commitment… | 127 | 0.85 | — | 0.85 |
| 13 | The cloud went down, so I printed my photos… | 111 | 0.85 | — | 0.85 |

The winner won all three of its Swiss games 0.85–0.15 and the final 0.85–0.15 against #2. Full per-call records: `~/workspace/makefun/tournament-u-coral-404-one-line-big-laugh-328fb857.jsonl` (not part of this repo).

## Files

- `main.py` — the entry program (entrypoint).
- `README.md` — this file.
- `LICENSE` — MIT.
- `.makefun/owner.json` — reward wallet for the make.fun account.
