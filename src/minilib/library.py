"""Biblioteka: katalog książek i wypożyczenia."""
import json
from pathlib import Path

from minilib.book import Book


class LoanError(Exception):
    """Wypożyczenie jest niemożliwe."""


class Library:
    def __init__(self, books: list[Book]) -> None:
        self.books = books

    @classmethod
    def from_file(cls, path: str = "data/books.json") -> "Library":
        with Path(path).open(encoding="utf-8") as f:
            return cls([Book.from_dict(item) for item in json.load(f)])

    def find_by_isbn(self, isbn: str) -> Book | None:
        wanted = isbn.replace("-", "")
        for book in self.books:
            if book.isbn.replace("-", "") == wanted:
                return book
        return None
