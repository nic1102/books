import uuid

from app.di.BooksValidator import BooksValidator
from app.config.naming_config import *


class Book:
    def __init__(self,
                 validator: BooksValidator = BooksValidator()):
        self.id = uuid.uuid4().__str__()
        self.data = validator.set_validate_data()
        self.title = self.data["title"]
        self.author = self.data["author"]
        self.year = self.data["year"]
        self.status = True

    def __str__(self) -> str:
        """
        RU: Удобочитаемый формат вывода книги.
        EN: Person oriented book format.
        """
        readable_status = "В наличии" if self.status else "Выдана"
        return (
                f'/////////////////////\n'
                f'ID: {self.id}\n'
                f'TITLE: {self.title}\n'
                f'AUTHOR: {self.author}\n' 
                f'YEAR: {self.year}\n'
                f'IS_EXISTS: {readable_status}\n'
                f'/////////////////////'
        )

    @staticmethod
    def show_restrictions() -> None:
        """
        RU: Выводит текущие ограничения для нейминга. Ограничения берутся из app.config.naming_config
        EN: Shows current restrictions for data naming. Restrictions located in app.config.naming_config
        """
        print(
                f'/////////////////////\n'
                f'TITLE_MAX_LEN: {TITLE_MAX_LEN}\n'
                f'AUTHOR_MAX_LEN: {AUTHOR_MAX_LEN}\n'
                f'MAX_YEAR: {MAX_YEAR}\n' 
                f'MIN_YEAR: {MIN_YEAR}\n'
                f'/////////////////////'
            )

    def change_status(self):
        """
        RU: Меняет статус книги.
        EN: Changes book status.
        """
        self.status = not self.status


if __name__ == "__main__":
    bv = BooksValidator()

    book = Book(**bv.set_validate_data())
    book.show_restrictions()
    print(book.show_restrictions.__doc__)
    print(book.__str__())
