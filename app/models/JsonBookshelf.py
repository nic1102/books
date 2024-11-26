import json

from app.di.BooksValidator import BooksValidator
from app.models.Bookshelf import Bookshelf
from app.models.Book import Book


class JsonBookshelf(Bookshelf):
    book_dic = {}

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Bookshelf, cls).__new__(cls)
        return cls.instance

    def __init__(self):
        with open("app/res/data.json", "r") as file:
            self.book_dic = json.load(file)

    def add(self, book_to_add: Book):
        """
        RU: Метод для добавления книги.
        EN: Adds book.
        """
        self.book_dic[book_to_add.id] = {"title": book_to_add.title,
                                         "author": book_to_add.author,
                                         "year": book_to_add.year,
                                         "status": book_to_add.status}
        with open("app/res/data.json", "w") as file:
            json.dump(self.book_dic, file)

    def get_all(self):
        """
        RU: Вывод списка всех книг.
        EN: Print all books.
        """
        if len(self.book_dic) == 0:
            print("Книжная полка пуста")
        else:
            print(f"Всего книг: {len(self.book_dic)}")
            for key, value in self.book_dic.items():
                print(
                    f'/////////////////////\n'
                    f'ID: {key}\n'
                    f'TITLE: {value["title"]}\n'
                    f'AUTHOR: {value["author"]}\n'
                    f'YEAR: {value["year"]}\n'
                    f'STATUS: {value["status"]}\n'
                    f'/////////////////////'
                )

    def del_by_id(self, book_to_del_id: str):
        """
        RU: Удаление книгу по ее id.
        EN: Delete book by its id.
        """
        try:
            self.book_dic.pop(book_to_del_id)
            with open("app/res/data.json", "w") as file:
                json.dump(self.book_dic, file)
        except KeyError as ex:
            print(f"Ошибка удаления. Id {book_to_del_id} не существует")

    def get_by_id(self, book_to_get_id: str):
        """
        RU: Вывод книгу по ее id.
        EN: Print book by its id.
        """
        try:
            readable_status = "В наличии" if self.book_dic[book_to_get_id]["status"] else "Выдана"
            print(
                f'/////////////////////\n'
                f'ID: {book_to_get_id}\n'
                f'TITLE: {self.book_dic[book_to_get_id]["title"]}\n'
                f'AUTHOR: {self.book_dic[book_to_get_id]["author"]}\n'
                f'YEAR: {self.book_dic[book_to_get_id]["year"]}\n'
                f'STATUS: {readable_status}\n'
                f'/////////////////////'
            )
        except KeyError as ex:
            print(f"Ошибка получения. Id {book_to_get_id} не существует")

    def get_by_year(self, book_to_get_year: int):
        """
        RU: Вывод книгу по ее году.
        EN: Print book by its year.
        """
        book_counter = 0
        for key, value in self.book_dic.items():
            if value["year"] == book_to_get_year:
                readable_status = "В наличии" if value["status"] else "Выдана"
                book_counter += 1
                print(
                    f'/////////////////////\n'
                    f'ID: {key}\n'
                    f'TITLE: {value["title"]}\n'
                    f'AUTHOR: {value["author"]}\n'
                    f'YEAR: {value["year"]}\n'
                    f'STATUS: {readable_status}\n'
                    f'/////////////////////'
                )
                return
            print("Книги с таким годом издания нет")
        if book_counter == 0:
            print("Такого года нет\n")

    def get_by_title(self, book_to_get_title: str):
        """
        RU: Вывод книгу по ее заголовку.
        EN: Print book by its title.
        """
        book_counter = 0
        for key, value in self.book_dic.items():
            if value["title"] == book_to_get_title:
                readable_status = "В наличии" if value["status"] else "Выдана"
                book_counter += 1
                print(
                    f'/////////////////////\n'
                    f'ID: {key}\n'
                    f'TITLE: {value["title"]}\n'
                    f'AUTHOR: {value["author"]}\n'
                    f'YEAR: {value["year"]}\n'
                    f'STATUS: {readable_status}\n'
                    f'/////////////////////'
                )
            else:
                continue
            print("Книги с таким названием нет")
        if book_counter == 0:
            print("Такого заголовка нет\n")

    def get_by_author(self, book_to_get_author: str):
        """
        RU: Вывод книгу по ее автору.
        EN: Print book by its author.
        """
        book_counter = 0
        for key, value in self.book_dic.items():
            if value["author"] == book_to_get_author:
                readable_status = "В наличии" if value["status"] else "Выдана"
                book_counter += 1
                print(
                    f'/////////////////////\n'
                    f'ID: {key}\n'
                    f'TITLE: {value["title"]}\n'
                    f'AUTHOR: {value["author"]}\n'
                    f'YEAR: {value["year"]}\n'
                    f'STATUS: {readable_status}\n'
                    f'/////////////////////'
                )
        if book_counter == 0:
            print("Такого автора нет\n")

    def change_status(self, book_to_change_id: str):
        """
        RU: Меняет статус книги на противоположный.
        EN: Changes book status to opposite one.
        """
        try:
            self.book_dic[book_to_change_id]["status"] = not self.book_dic[book_to_change_id]["status"]
            with open("app/res/data.json", "w") as file:
                json.dump(self.book_dic, file)
        except KeyError as ex:
            print("Книги с таким айди нет")




