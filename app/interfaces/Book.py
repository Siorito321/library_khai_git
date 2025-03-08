from abc import ABC, abstractmethod


class Book(ABC):
    def __init__(self, author, title, description, book_id):
        self.author = author
        self.title = title
        self.description = description
        self.book_id = book_id

    @abstractmethod
    def get_info(self, book_id):
        ...

    @abstractmethod
    def get_description(self, book_id):
        ...

    @abstractmethod
    def get_author(self, book_id):
        ...

    @abstractmethod
    def get_title(self, book_id):
        ...

