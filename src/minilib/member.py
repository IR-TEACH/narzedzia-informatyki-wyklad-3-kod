"""Model czytelnika biblioteki."""
from dataclasses import dataclass


@dataclass
class Member:
    name: str
    email: str
    phone: str = ""
    max_loans: int = 3

    def __post_init__(self) -> None:
        if "@" not in self.email:
            raise ValueError(f"Niepoprawny e-mail: {self.email!r}")
