from abc import ABC, abstractmethod


class Reader(ABC):
    @abstractmethod
    def get_name(self) -> str:
        pass

    @abstractmethod
    def get_address(self) -> str:
        pass

    @abstractmethod
    def get_contact_info(self) -> str:
        pass

    @abstractmethod
    def get_borrowed_books(self) -> List[Book]:
        pass