import pytest

from minilib.library import LoanError


def test_borrow_decreases_copies(library, anna):
    library.borrow(anna, "978-0-13-235088-4")

    assert library.find_by_isbn("978-0-13-235088-4").copies == 2


def test_borrow_without_copies_raises(library, anna):
    library.borrow(anna, "978-0-13-475759-9")      # Refactoring: 1 egz.

    with pytest.raises(LoanError):
        library.borrow(anna, "978-0-13-475759-9")


def test_fourth_loan_exceeds_limit(library, anna):
    for isbn in ["978-0-13-235088-4", "978-0-13-475759-9", "978-0-201-63361-0"]:
        library.borrow(anna, isbn)

    with pytest.raises(LoanError, match="Limit"):
        library.borrow(anna, "978-0-316-03770-9")
