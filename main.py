"""Office Artifacts: The One-Line Placard Contest.

Writes a single museum placard line — an ordinary office stapler
recast as a ritual artifact of a lost civilisation — to
/output/entry.txt. The line is fixed and deterministic: every run
writes the exact same bytes, with no trailing newline, so the file
holds exactly the placard and nothing else.
"""

import os

# The placard. Catalogue date, material and donor sell the joke;
# the jam-as-omen is the conceit. 172 characters, inside the 180 cap.
PLACARD = (
    "Stapler, c. 1998. Steel and spite. "
    "Ritual instrument for binding one soul to another's paperwork; "
    "a jam was read as an omen. "
    "Gift of the Department of Unfinished Business."
)


def main() -> None:
    # Gate: the placard must be 1-180 characters and not only whitespace.
    # Fail loudly here rather than shipping an invalid entry.
    assert 1 <= len(PLACARD) <= 180, len(PLACARD)
    assert PLACARD.strip(), "placard must not be only whitespace"
    assert "\n" not in PLACARD, "placard must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(PLACARD)


if __name__ == "__main__":
    main()
