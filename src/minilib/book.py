"""Model książki w bibliotece MiniLib."""
from dataclasses import dataclass

from minilib.validation import is_valid_isbn13


@dataclass
class Book:
    isbn: str
    title: str
    author: str
    copies: int = 1

    def __post_init__(self) -> None:
        if not is_valid_isbn13(self.isbn):
            raise ValueError(f"Niepoprawny ISBN: {self.isbn!r}")

    @classmethod
    def from_dict(cls, data: dict) -> "Book":
        return cls(**data)
