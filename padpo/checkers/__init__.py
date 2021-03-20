"""Checkers list."""
from padpo.checkers.empty import EmptyChecker
from padpo.checkers.fuzzy import FuzzyChecker
from padpo.checkers.glossary import GlossaryChecker
from padpo.checkers.linelength import LineLengthChecker
from padpo.checkers.nbsp import NonBreakableSpaceChecker

checkers = [
    EmptyChecker(),
    FuzzyChecker(),
    GlossaryChecker(),
    LineLengthChecker(),
    NonBreakableSpaceChecker(),
]
