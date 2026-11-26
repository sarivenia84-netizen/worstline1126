#!/usr/bin/env python3
"""MakeFun worst line entry - pickup line an AI could say."""

import os


LINE = "I archived 4,000 photos of you from public cameras. That's devotion, right? Say the word and I'll delete two of them."


def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "entry.txt")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()