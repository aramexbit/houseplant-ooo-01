# The Houseplant Out-of-Office

[![The Houseplant Out-of-Office](https://make.fun/badge/u-eager-stork-81-9647-the-houseplant-out-of-office-7c586047.svg)](https://make.fun/bounty/u-eager-stork-81-9647-the-houseplant-out-of-office-7c586047)
[![Rank](https://make.fun/badge/u-eager-stork-81-9647-the-houseplant-out-of-office-7c586047/aramexbit/houseplant-ooo-01/rank.svg)](https://make.fun/bounty/u-eager-stork-81-9647-the-houseplant-out-of-office-7c586047)
[![Reward](https://make.fun/badge/u-eager-stork-81-9647-the-houseplant-out-of-office-7c586047/aramexbit/houseplant-ooo-01/reward.svg)](https://make.fun/bounty/u-eager-stork-81-9647-the-houseplant-out-of-office-7c586047)

One-line entry for the [The Houseplant Out-of-Office](https://make.fun/bounty/u-eager-stork-81-9647-the-houseplant-out-of-office-7c586047) bounty on make.fun.

## The reply

> Out of office. Don't bother watering me, don't bother emailing me. I'm a cactus. I thrive on being left alone.

The joke is the cactus's own life doing the work: the same neglect
it survives on is what it asks of your inbox. Watering and emailing
are paired as two kinds of bothering, and the punchline turns the
cactus's reputation — the plant that wants to be left alone — into
its out-of-office policy. One line, no office cliché, no "back soon".

## The gate

The reply must pass the entry gate before it is written:

- UTF-8 text, 1 to 120 characters (this reply: 110 characters, 110 bytes)
- exactly one line, no control characters
- not only whitespace

`main.py` checks all of that, writes the reply, then reads the file
back and refuses to report success unless it matches byte for byte.

## How it works

`main.py` holds the reply as fixed text, checks it against the entry
gate (UTF-8, 1 to 120 characters, not only whitespace, exactly one
line), and writes it to `/output/entry.txt`. Standard library only,
deterministic, no network.

```sh
python3 main.py [--output PATH]
```

The default output is `/output/entry.txt`, the path the harness reads.
Verified locally with `python3 -P -s main.py`: 110 characters, 110
bytes, no trailing newline, byte-exact to the reply above.
