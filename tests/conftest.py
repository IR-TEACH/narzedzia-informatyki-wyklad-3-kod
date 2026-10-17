import pytest

from minilib.book import Book
from minilib.library import Library
from minilib.member import Member


@pytest.fixture
def library() -> Library:
    return Library([
        Book("978-0-13-235088-4", "Clean Code", "Martin, Robert", copies=3),
        Book("978-0-13-475759-9", "Refactoring", "Fowler, Martin"),
        Book("978-0-201-63361-0", "Design Patterns", "Gamma, Erich"),
        Book("978-0-316-03770-9", "Ghost in the Wires", "Mitnick, Kevin"),
    ])


@pytest.fixture
def anna() -> Member:
    return Member("Anna Nowak", "anna.nowak@example.com")
