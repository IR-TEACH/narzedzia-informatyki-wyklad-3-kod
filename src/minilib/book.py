"""Model książki w bibliotece MiniLib."""
from dataclasses import dataclass


@dataclass
class Book:
    isbn: str
    title: str
    author: str
    copies: int = 1

    @classmethod
    def from_dict(cls, data: dict) -> "Book":
        return cls(**data)
