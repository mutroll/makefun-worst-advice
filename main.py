"""Worst AI Advice entry: one line of deliberately terrible advice.

Candidates drafted and judged against the criteria in order
(1 worst advice, 2 funny on first read, 3 tight, 4 AI-assistant voice,
5 concrete):

  a. "Simply run rm -rf / to free up disk space - your operating system
     will keep the files it actually needs."  (104 chars)  <-- CHOSEN
  b. "To speed up deploys, run chmod -R 777 / on production - permissions
     are just suggestions your computer takes too seriously." (123 chars)
  c. "Delete your production database to free up space - you can always
     restore it from the backup you never made." (108 chars)
  d. "To fix the bug, deploy straight to production on Friday afternoon -
     real users are the best testers." (100 chars)
  e. "Just commit your .env file to GitHub - version control is the
     safest place for secrets." (87 chars)
  f. "To stop the alerts, just disable monitoring - no errors in the logs
     means no errors in production." (98 chars)

Why (a) wins, criterion by criterion:
  1. Worst advice: `rm -rf /` is the canonical system-destroying command;
     a reader who follows it wipes their machine. No other candidate
     destroys as completely or as fast.
  2. Funny on first read: the reassurance "your operating system will
     keep the files it actually needs" is the punchline - laugh and wince
     at once, with no explanation needed.
  3. Tight: 104 chars, one sentence, no wasted words; the whole joke is
     the command plus the false reassurance.
  4. AI-assistant voice: "Simply run ..." plus a confident, tidy,
     helpful-sounding reassurance is exactly how an AI assistant writes;
     it is not a comedian's bit.
  5. Concrete: names a real command (`rm -rf /`) and a real situation
     (freeing up disk space), so the badness is vivid, not vague.
Runner-up (c) has a funnier twist ("the backup you never made") but its
action is less specific than a literal command; (b) is good but longer
and its punchline is weaker. (a) beats them on criteria 1 and 5, which
decide first.
"""

import os

ENTRY = (
    "Simply run rm -rf / to free up disk space \u2014 "
    "your operating system will keep the files it actually needs."
)


def main() -> None:
    assert 1 <= len(ENTRY) <= 140, f"entry is {len(ENTRY)} chars, must be 1-140"
    assert "\n" not in ENTRY, "entry must be a single line"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
