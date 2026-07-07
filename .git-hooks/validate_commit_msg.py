#!/usr/bin/env python3
"""Simple commit-msg validator enforcing Conventional Commits.

This script is run by pre-commit on the `commit-msg` stage and exits with
non-zero status if the commit message does not match the Conventional Commits
pattern used by this project.
"""
import re
import sys


CONVENTIONAL_COMMIT_RE = re.compile(
    r"^(?:feat|fix|docs|style|refactor|perf|test|chore|build|ci|revert)"
    r"(?:\([^)]+\))?"  # optional scope
    r"(?:!)?: "
    r".+",
)


def main(argv: list[str] | None = None) -> int:
    argv = argv or sys.argv[1:]
    if not argv:
        print("No commit-msg file provided", file=sys.stderr)
        return 2

    commit_msg_file = argv[0]
    try:
        with open(commit_msg_file, "r", encoding="utf8") as f:
            first_line = f.readline().strip()
    except Exception as e:
        print(f"Failed to read commit message file: {e}", file=sys.stderr)
        return 2

    if not CONVENTIONAL_COMMIT_RE.match(first_line):
        print("Invalid commit message. Commit message must follow Conventional Commits format.")
        print("Examples: 'feat(scope): add new feature' or 'fix: correct bug'", file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
