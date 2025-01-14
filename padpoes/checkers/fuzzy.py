"""Checker for fuzzy translations."""

from padpoes.checkers.baseclass import Checker
from padpoes.pofile import PoItem


class FuzzyChecker(Checker):
    """Checker for fuzzy translations."""

    name = "Fuzzy"

    def check_item(self, item: PoItem):
        """Check an item in a `*.po` file."""
        if item.fuzzy:
            item.add_warning(self.name, "This entry is tagged as fuzzy.")
