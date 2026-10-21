"""Wypisuje katalog książek jako tabelę."""
from rich.console import Console
from rich.table import Table

from minilib.library import Library


def main() -> None:
    library = Library.from_file()
    table = Table(title="Katalog MiniLib")
    table.add_column("Tytuł")
    table.add_column("Autor")
    table.add_column("Egz.", justify="right")
    for book in sorted(library.books, key=lambda b: b.title):
        table.add_row(book.title, book.author, str(book.copies))
    Console().print(table)
    print(f"Razem: {len(library.books)}")
