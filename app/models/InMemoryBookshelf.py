from app.di.BooksValidator import BooksValidator
from app.models.Bookshelf import Bookshelf
from app.models.Book import Book


class InMemoryBookshelf(Bookshelf):
    """
    RU: Класс для реализации логики приложения, хранящий данные в памяти.
    EN: Logic realisation class, for in-memory part.
    """
    book_dic = {}

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Bookshelf, cls).__new__(cls)
        return cls.instance

    def add(self, book_to_add: Book):
        """
        RU: Метод для добавления книги.
        EN: Adds book.
        """
        self.book_dic[book_to_add.id] = book_to_add

    def get_all(self):
        """
        RU: Вывод списка всех книг.
        EN: Print all books.
        """
        if len(self.book_dic) == 0:
            print("Книжная полка пуста")
        else:
            print(f"Всего книг: {len(self.book_dic)}")
            for i in self.book_dic.values():
                print(
                    i.__str__()
                )

    def del_by_id(self, book_to_del_id: str):
        """
        RU: Удаление книгу по ее id.
        EN: Delete book by its id.
        """
        try:
            self.book_dic.pop(book_to_del_id)
        except KeyError as ex:
            print(f"Ошибка удаления. Id {book_to_del_id} не существует")

    def get_by_id(self, book_to_get_id: str):
        """
        RU: Вывод книгу по ее id.
        EN: Print book by its id.
        """
        try:
            print(self.book_dic[book_to_get_id].__str__())
        except KeyError as ex:
            print(f"Ошибка получения. Id {book_to_get_id} не существует")

    def get_by_year(self, book_to_get_year: int):
        """
        RU: Вывод книгу по ее году.
        EN: Print book by its year.
        """
        book_counter = 0
        for i in self.book_dic.values():
            if i.year == book_to_get_year:
                book_counter += 1
                print(i.__str__())
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
        for i in self.book_dic.values():
            if i.title == book_to_get_title:
                book_counter += 1
                print(i.__str__())
                return
            print("Книги с таким названием нет")
        if book_counter == 0:
            print("Такого заголовка нет\n")

    def get_by_author(self, book_to_get_author: str):
        """
        RU: Вывод книгу по ее автору.
        EN: Print book by its author.
        """
        book_counter = 0
        for i in self.book_dic.values():
            if i.author == book_to_get_author:
                book_counter += 1
                print(i.__str__())
                return
            print("Книги с таким автором нет")
        if book_counter == 0:
            print("Такого автора нет\n")

    def change_status(self, book_to_change_id: str):
        """
        RU: Меняет статус книги на противоположный.
        EN: Changes book status to opposite one.
        """
        try:
            self.book_dic[book_to_change_id].change_status()
        except KeyError as ex:
            print("Книги с таким айди нет")



if __name__ == "__main__":
    bv = BooksValidator()

    b1 = Book()

    bs = InMemoryBookshelf()

    bs.add(b1)
    bs.get_all()
    bs.change_status(input("11111111"))
    bs.get_all()
