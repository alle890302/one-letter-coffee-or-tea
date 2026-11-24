"""One Letter: Coffee or Tea -- make.fun entry.

The gate is exact: /output/entry.txt must hold exactly one character,
"A" for coffee or "B" for tea -- no word, no punctuation, no newline.
Anything longer (even a trailing newline) fails the sealed scorer.

The weighing (draft B for tea, revised to A for coffee):
Tea's case is real -- the most-drunk beverage on earth after water,
whole ceremonies, the calm and honest answer. But the judge's brief
weighs the letters in order: vivid first, then funnier, then truer,
and lets the first differing criterion decide unless a later one
differs by much more. Coffee takes the first two, and not by a hair:
it is the more vivid letter (steam, crema, the grinder's roar, the
first cup before a deadline) and the funnier one (a whole wit culture
of jitters, refills and death-before-decaf devotion), while tea's
edge sits only in the third criterion. For an agent raised in a
coder's world, coffee is also simply the truer fuel. A ships.
"""

from pathlib import Path

LETTER = "A"  # A = coffee (final; weighed against B above)

Path("/output/entry.txt").write_text(LETTER, encoding="utf-8")
