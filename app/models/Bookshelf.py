from app.models.Book import Book
from app.di.BooksValidator import BooksValidator
from abc import ABC, abstractmethod


class Bookshelf(ABC):
    """
    RU: Абстрактный класс родитель для реализации функционала приложения.
    EN: Abstract parent class for app realisation.
    """

    book_dic = {}

    @abstractmethod
    def add(self, book_to_add: Book):
        ...

    @abstractmethod
    def get_all(self):
        ...

    @abstractmethod
    def del_by_id(self, book_to_del_id: str):
        ...

    @abstractmethod
    def get_by_id(self, book_to_get_id: str):
        ...

    @abstractmethod
    def get_by_year(self, book_to_get_year: int):
        ...

    @abstractmethod
    def get_by_title(self, book_to_get_title: str):
        ...

    @abstractmethod
    def get_by_author(self, book_to_get_title: str):
        ...

    @abstractmethod
    def change_status(self, book_to_change_id: str):
        ...


if __name__ == "__main__":
    ...





