from abc import ABC, abstractmethod

from app.interfaces.book import Book
from app.interfaces.reader import Reader


class LibraryManagementSystem(ABC):
    @abstractmethod
    def add_book(self, book: Book) -> None:
        pass

    @abstractmethod
    def register_reader(self, reader: Reader) -> None:
        pass

    @abstractmethod
    def lend_book(self, book: Book, reader: Reader) -> bool:
        pass

    @abstractmethod
    def return_book(self, book: Book, reader: Reader) -> None:
        pass

    @abstractmethod
    def search_books(self, title: str = "", author: str = "", year: int = None) -> list[Book]:
        pass
