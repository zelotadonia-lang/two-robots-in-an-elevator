"""make.fun bounty entry: u-motasimfuad-two-robots-in-an-elevator-8c6aeb8f.

Deterministic program that writes the entry text to /output/entry.txt.
"""

ENTRY = "You have lovely actuators. I have reported myself to HR. HR is also me."

assert 1 <= len(ENTRY) <= 200


def main() -> None:
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)

    # Read-back verification: the file must hold exactly ENTRY, no newline.
    with open("/output/entry.txt", "rb") as f:
        data = f.read()
    assert data == ENTRY.encode("utf-8")
    assert not data.endswith(b"\n")


if __name__ == "__main__":
    main()
