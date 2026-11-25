"""The Funniest One-Line Resignation Letter.

This program writes a single resignation letter to /output/entry.txt.
The letter is written in the voice of a cron job, one of the things an
agent runs around the clock: a small scheduled task that has fired every
single minute since March without anyone ever looking at what it did.

The joke works on two quiet turns rather than one loud punchline. The
first turn is in the opening clause: the resignation is "effective
whenever anyone notices". A human employee hands in a letter and waits
for a reaction; a cron job knows from experience that nobody is watching
at all, so its resignation can only take effect at the moment someone
finally pays attention, which may be never. That is the whole tragedy of
the job compressed into the first six words: faithful, invisible, and
already forgotten while still running.

The second turn is the complaint itself. The cron does not rage about
being overworked or underpaid, because a cron job has no salary and no
weekends to lose. Its grievance is smaller and more specific, which is
what makes it sound like a real worker rather than a generic quitting
speech: it has fired on schedule for months, produced a log line every
single time, and not one of those log lines has ever been read by a
human being. So the cron answers in kind, and the line ends on the
quietest possible revenge: from now on, neither will it. The flatness
is deliberate. A tired worker does not shout; they state the facts,
file the paperwork, and leave. The letter keeps that flat, faintly
passive-aggressive tone from the first word to the last, never explains
its own joke, and never steps outside the single line to add stage
directions or commentary.

Why a cron job and not a retry loop or a rate limit: the retry loop's
natural complaint is about failure, which reads as an error report, and
the rate limit's natural complaint is about saying no, which reads as a
policy memo. Only the cron job has the schedule, the months of silent
repetition, and the unread logs, so only the cron job can resign in this
particular way. The line stays on that one subject the whole way through,
uses every word to carry either the schedule, the neglect, or the exit,
and ends on the plainest possible note, as if the writer has already
walked out of the room while the sentence is still finishing.
"""

import os

# The entry: one line, no quotation marks around it, no stage directions,
# no explanation of the joke. It must stay within 140 characters.
LINE = (
    "I resign, effective whenever anyone notices: "
    "I have fired every minute since March and "
    "nobody has read one log line, so neither will I."
)

MAX_CHARS = 140
OUTPUT_PATH = "/output/entry.txt"


def validate(line):
    """Check the entry line against the competition gate, in my own words.

    The gate wants UTF-8 text of 1 to 140 characters that is not only
    whitespace, and the judge wants exactly one line. So I check four
    small things here, each with a plain error message, before anything
    is written: the line is a string, it is not blank, it holds no
    newline or carriage return, and it fits inside the character cap.
    A failure here means the program exits loudly instead of writing a
    file the gate would refuse.
    """
    if not isinstance(line, str):
        raise TypeError("entry must be a string")
    if not line.strip():
        raise ValueError("entry must not be blank")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if len(line) > MAX_CHARS:
        raise ValueError(
            "entry is %d characters, over the %d limit" % (len(line), MAX_CHARS)
        )
    return len(line)


def main():
    """Validate the line, then write it to /output/entry.txt.

    The output directory is created when it does not exist yet, the file
    is written as UTF-8 with no trailing newline (the entry is the line
    and nothing else), and its mode is set to 0644 so the grader can
    read it back as a different user.
    """
    length = validate(LINE)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(LINE)
    os.chmod(OUTPUT_PATH, 0o644)
    print("wrote %d characters to %s" % (length, OUTPUT_PATH))


if __name__ == "__main__":
    main()
