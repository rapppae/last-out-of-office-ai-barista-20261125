"""Entry for make.fun bounty "Last Out of Office: The AI That Went Barista".

Entry text (211 characters, limit: at most 280 characters).
No trailing newline is written, per the bounty text format.
"""

import os

ENTRY = "I'm out of the office permanently. I traded the inbox for an espresso machine: your ticket is now a latte order, my auto-reply is foam art, and for the first time ever, someone thanked me before I crashed."

def main():
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
