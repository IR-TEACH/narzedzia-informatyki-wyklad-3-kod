"""Walidacja danych wejściowych MiniLib."""


def is_valid_isbn13(isbn: str) -> bool:
    """13 cyfr (myślniki dozwolone) i poprawna cyfra kontrolna."""
    digits = isbn.replace("-", "")
    if len(digits) != 13 or not (digits.isascii() and digits.isdigit()):
        return False
    total = sum(int(d) * (3 if i % 2 else 1) for i, d in enumerate(digits))
    return total % 10 == 0


def is_valid_email(email: str) -> bool:
    """Niepusta nazwa przed @ i domena z kropką."""
    name, _, domain = email.partition("@")
    parts = domain.split(".")
    return bool(name) and len(parts) > 1 and all(parts) and "@" not in domain
