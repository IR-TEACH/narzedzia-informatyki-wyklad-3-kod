"""Wypisuje katalog książek."""
import json
from pathlib import Path

from minilib.book import Book


def load_books(path: str = "data/books.json") -> list[Book]:
    with Path(path).open(encoding="utf-8") as f:
        return [Book.from_dict(item) for item in json.load(f)]


def main() -> None:
    books = sorted(load_books(), key=lambda b: b.title)
    for book in books:
        print(f"{book.title} ({book.author}), egz.: {book.copies}")
    print(f"Razem: {len(books)}")
