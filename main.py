#!/usr/bin/env python3
"""Alien Field Notes entry: writes one alien tourist's review of planet
Earth to /output/entry.txt."""

LINE = "★★★★☆ — Lovely planet, breathtaking sunsets, but the locals charge rent to sleep on the rock they were born on. Would abduct again."

# The gate: /output/entry.txt must hold a single line of at most 200
# characters (the brief asks for one review line, not a paragraph), and it
# must carry a review verdict (stars or an x/5 score) so it reads as a
# review at a glance.
REVIEW_MARKERS = ("★", "☆", "/5", "stars")


def validate(line):
    assert line.strip(), "line must not be empty"
    assert 1 <= len(line) <= 200, "line must be 1-200 characters"
    assert "\n" not in line and "\r" not in line, "line must be a single line"
    assert any(m in line for m in REVIEW_MARKERS), (
        "line must carry a review verdict (stars or an x/5 score)"
    )


validate(LINE)

if __name__ == "__main__":
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
