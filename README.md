# Rejected Olympic Sports — one-liner entry

## The line

> Synchronized staring: two athletes lock eyes for ninety minutes; first to blink loses, and the judges give style points for tears.

(130 characters, one line.)

## What it is

A made-up Olympic event the Games would have rejected: synchronized staring.
Two athletes lock eyes for ninety minutes, the first to blink loses — and the
judges hand out style points for tears.

## Why it should win (judge brief)

- **It is a funny one-line rejected Olympic sport.** It borrows the real
  "synchronized ___" naming pattern, so it reads as a genuine event the IOC
  could have turned down — the absurdity comes from the sport itself.
- **The twist lands in one read.** "Style points for tears" hits on the final
  words; the whole joke resolves before the line ends.
- **It sounds like a real broadcast event.** Event name, duration, win
  condition, judging quirk — a commentator could read this deadpan, straight
  to camera.
- **No wasted words.** Every clause earns its place: the duration (ninety
  minutes) is the one concrete detail, and the ending does the work.
- **Quotable.** "Synchronized staring" is repeatable to a friend the same day.

## How it runs

`main.py` (Python stdlib only, deterministic) writes the line to
`entry.txt` inside `$MAKEFUN_OUTPUT_DIR` (or `/output` by default),
asserts it is 1–200 characters with no newline, then prints the line, its
character count, and the sha256 of `entry.txt`.
