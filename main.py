#!/usr/bin/env python3
"""One Line, One Laugh — prints exactly one original funny line."""

import os

LINE = "I organized my life alphabetically — turns out most of it files under 'regret'."

print(LINE)

try:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
except OSError:
    pass
