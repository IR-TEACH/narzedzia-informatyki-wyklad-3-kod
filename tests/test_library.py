from minilib.library import Library


def test_find_by_isbn_returns_book(library):
    book = library.find_by_isbn("978-0-13-235088-4")

    assert book is not None
    assert book.title == "Clean Code"


def test_find_by_isbn_unknown_returns_none(library):
    assert library.find_by_isbn("978-0-00-000000-2") is None


def test_from_file_loads_whole_catalog():
    library = Library.from_file()

    assert len(library.books) == 6


def test_find_by_isbn_without_hyphens(library):
    book = library.find_by_isbn("9780132350884")

    assert book is not None
    assert book.title == "Clean Code"
