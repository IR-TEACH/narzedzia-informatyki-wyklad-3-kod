"""Wypisuje katalog książek."""
from minilib.library import Library


def main() -> None:
    library = Library.from_file()
    for book in sorted(library.books, key=lambda b: b.title):
        print(f"{book.title} ({book.author}), egz.: {book.copies}")
    print(f"Razem: {len(library.books)}")
