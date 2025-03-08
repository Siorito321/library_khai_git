import pytest
from app.models.book import Book
from app.models.library_management import LibraryManagementSystem
from app.models.reader import Reader


def test_book():
    book = Book("1984", "George Orwell", 1949)
    assert book.get_title() == "1984"
    assert book.get_author() == "George Orwell"
    assert book.get_publication_year() == 1949
    assert book.is_available() is True

    book.set_availability(False)
    assert book.is_available() is False


def test_reader():
    reader = Reader("Alice", "123 Main St", "alice@example.com")
    assert reader.get_name() == "Alice"
    assert reader.get_address() == "123 Main St"
    assert reader.get_contact_info() == "alice@example.com"
    assert reader.get_borrowed_books() == []

    book = Book("Brave New World", "Aldous Huxley", 1932)
    reader.borrow_book(book)
    assert reader.get_borrowed_books() == [book]

    reader.return_book(book)
    assert reader.get_borrowed_books() == []


def test_library_management_system():
    library = LibraryManagementSystem()
    book1 = Book("Fahrenheit 451", "Ray Bradbury", 1953)
    book2 = Book("The Hobbit", "J.R.R. Tolkien", 1937)
    reader = Reader("Bob", "456 Elm St", "bob@example.com")

    library.add_book(book1)
    library.add_book(book2)
    library.register_reader(reader)

    assert library.search_books(title="Fahrenheit 451") == [book1]
    assert library.search_books(author="J.R.R. Tolkien") == [book2]

    assert library.lend_book(book1, reader) is True
    assert book1.is_available() is False
    assert reader.get_borrowed_books() == [book1]

    library.return_book(book1, reader)
    assert book1.is_available() is True
    assert reader.get_borrowed_books() == []
