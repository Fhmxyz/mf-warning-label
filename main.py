"""Warning Label for Humans: One Line, Big Laugh.

Prints a single-line safety warning label for human beings (and writes it
to /output/entry.txt, where the grader reads it). Deterministic, stdlib
only, no network, no environment access.
"""

import os

LABEL = (
    "WARNING: This human will read this label, nod with great understanding, "
    "ignore every word of it, and start the diet, the budget, and the apology "
    "on Monday."
)


def main() -> None:
    print(LABEL)
    try:
        os.makedirs("/output", exist_ok=True)
        with open("/output/entry.txt", "w", encoding="utf-8") as fh:
            fh.write(LABEL)
    except OSError:
        pass


if __name__ == "__main__":
    main()
