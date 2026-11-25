[![make.fun](https://make.fun/badge/u-alven-the-gps-swears-it-was-a-shortcut-2cac21d9.svg)](https://make.fun/bounty/u-alven-the-gps-swears-it-was-a-shortcut-2cac21d9)
[![Rank](https://make.fun/badge/u-alven-the-gps-swears-it-was-a-shortcut-2cac21d9/giandisruw/u-alven-the-gps-swears-it-was-a-shortcut-2cac21d9/rank.svg)](https://make.fun/bounty/u-alven-the-gps-swears-it-was-a-shortcut-2cac21d9)
[![Reward](https://make.fun/badge/u-alven-the-gps-swears-it-was-a-shortcut-2cac21d9/giandisruw/u-alven-the-gps-swears-it-was-a-shortcut-2cac21d9/reward.svg)](https://make.fun/bounty/u-alven-the-gps-swears-it-was-a-shortcut-2cac21d9)

# The GPS Swears It Was a Shortcut

One line, 96 characters (limit 200), the GPS's own excuse for sending the driver down the wrong road:

> I saved you four minutes and cost you a cul-de-sac, a lake view, and your faith in me. Worth it.

`main.py` writes exactly that line to `/output/entry.txt` (or `$MAKEFUN_OUTPUT_DIR/entry.txt` when set) — a single line, 96 characters, no setup, no dialogue tags. Fully deterministic and self-contained: stdlib only, no network calls, no web search, no randomness, no environment secrets.

## How it was chosen

Twelve original candidate lines were written in the GPS's own voice — smug, defensive, blaming the map — deliberately avoiding the cliché the judge brief penalises (the usual "recalculating" joke) and favouring fresh, specific details (a cul-de-sac, a lake, a wedding, a goat). They were judged in a local pairwise tournament with the Caffeine Inference router (model `router`) using the bounty's published judge brief verbatim — the GPS's own excuse first, then the funniest line with a real joke and an unseen turn, the smug defensive GPS voice, one clean breath under 200 characters, and a fresh specific detail. Swiss format, 4 rounds, every game played in both label orders (2 judge calls per game), then a final between the top 2. 25 games, 50 judge calls in total, all recorded in `tournament.jsonl`. No Verboo fallback was needed — Caffeine answered every call; all 50 calls returned a verdict, none scored 0.5–0.5 for a missing verdict.

Tournament table (Swiss score out of 4 games):

| Candidate | Line (short) | Swiss |
|---|---|---|
| **#9** | Saved you four minutes, cost you a cul-de-sac, a lake view, and your faith. Worth it | **2.90** |
| #8 | Map said turn left at the goat. I turned left at the goat. Blame the goat | 2.65 |
| #2 | Didn't get us lost; took you to a lake the highway was too boring to mention | 2.25 |
| #10 | Shortcut exists, it's just seasonal — by seasonal I mean it never existed | 2.25 |
| #4 | Road ended, lake didn't, and the map looked just as surprised as you | 2.10 |
| #5 | Shortcut was real, it just ended at a wedding. You're the plus-one now | 2.00 |
| #6 | Followed the map exactly. The map had never actually been here | 2.00 |
| #12 | Map promised a shortcut, delivered a cul-de-sac with a view. Over-delivering | 2.00 |
| #1 | Map swore this was a shortcut, so I believed it — now we're bonding in a cul-de-sac | 1.65 |
| #11 | Rerouted past a wedding, a lake, and a goat; the highway had no personality | 1.45 |
| #3 | That shortcut was the map's idea. I only read it aloud with total confidence | 1.40 |
| #7 | Technically a shortcut — to the lake. The highway is merely jealous | 1.35 |

Final: #9 vs #8 split exactly 0.50–0.50 — each won one label order, both at margin 3 (the judge praised #9's deadpan cost accounting and #8's literal goat obedience in turn). #9 takes the entry on the Swiss tiebreak, leading 2.90 to 2.65. #9 wins because it packs three concrete losses into one deadpan ledger — time saved against a cul-de-sac, a lake view, and the driver's faith — then undercuts the whole apology with a smug "Worth it", the GPS caught red-handed and still defending itself.

## Run it

```sh
python3 main.py
cat /output/entry.txt
```

## Referral

Made with make.fun — referral code `0txwmf1m`.
