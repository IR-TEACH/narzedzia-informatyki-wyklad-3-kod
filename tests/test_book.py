from minilib.book import Book


def test_from_dict_reads_all_fields():
    data = {"isbn": "978-0-13-235088-4", "title": "Clean Code",
            "author": "Martin, Robert", "copies": 3}

    book = Book.from_dict(data)

    assert book == Book("978-0-13-235088-4", "Clean Code", "Martin, Robert", 3)


def test_copies_default_to_one():
    assert Book("978-0-13-235088-4", "Clean Code", "Martin, Robert").copies == 1
