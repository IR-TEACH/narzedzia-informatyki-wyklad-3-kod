import pytest

from minilib.validation import is_valid_email, is_valid_isbn13


@pytest.mark.parametrize("isbn, expected", [
    ("978-0-13-235088-4", True),     # poprawny, z myślnikami
    ("9780132350884", True),         # poprawny, bez myślników
    ("978-0-13-235088-5", False),    # zła cyfra kontrolna
    ("978-0-13-23508-4", False),     # za krótki
    ("978-0-13-23508X-4", False),    # litera
    ("", False),                     # pusty
    ("978013235088²", False),        # cyfra z indeksu górnego
    ("٩٧٨٠١٣٢٣٥٠٨٨٤", False),        # ten sam ISBN cyframi arabskimi
])
def test_is_valid_isbn13(isbn, expected):
    assert is_valid_isbn13(isbn) == expected


@pytest.mark.parametrize("email, expected", [
    ("anna.nowak@example.com", True),
    ("anna.nowak", False),
    ("@example.com", False),
    ("a@@b.c", False),
    ("a@b.", False),
])
def test_is_valid_email(email, expected):
    assert is_valid_email(email) == expected
