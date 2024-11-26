from app.models.Book import Book
from app.di.BooksValidator import BooksValidator
from app.models.InMemoryBookshelf import InMemoryBookshelf
from app.models.JsonBookshelf import JsonBookshelf

if __name__ == "__main__":
    bv = BooksValidator()
    bs = InMemoryBookshelf()
    print(bs.add.__doc__)
    print("Выберите режим работы. 1 - Хранение в оперативной памяти. 2 - Хранение в Json. -- ")
    mode = None
    while True:
        try:
            mode = int(input())
            if mode is None:
                continue
            else:
                break
        except Exception as ex:
            print("Нужно ввести или 1 или 2")

    if mode == 1:
        bs = InMemoryBookshelf()
        print("Список команд - help")
        while True:
            command = input("Ваша команда - ").strip()
            match command.lower():
                case "help":
                    print("Добавить книгу - add\n"
                          "Найти книгу по title - findbytitle\n"
                          "Найти книгу по author - findbyauthor\n"
                          "Найти книгу по year - findbyyear\n"
                          "Список всех книг - showall\n"
                          "Удалить книгу - delbyid\n"
                          "Изменить статус - changestatus\n")
                case "showall":
                    bs.get_all()
                    continue
                case "add":
                    bs.add(Book(bv))
                    continue
                case "findbytitle":
                    title = input()
                    bs.get_by_title(title)
                    continue
                case "findbyauthor":
                    author = input()
                    bs.get_by_author(author)
                    continue
                case "findbyyear":
                    try:
                        year = int(input())
                    except Exception as ex:
                        print("Неверный формат года")
                        continue
                    bs.get_by_year(year)
                    continue
                case "delbyid":
                    del_id = input()
                    bs.del_by_id(del_id)
                    continue
                case "changestatus":
                    c_id = input()
                    bs.change_status(c_id)
                    continue
    if mode == 2:
        bs = JsonBookshelf()
        print("Список команд - help")
        while True:
            command = input("Ваша команда - ").strip()
            match command.lower():
                case "help":
                    print("Добавить книгу - add\n"
                          "Найти книгу по title - findbytitle\n"
                          "Найти книгу по author - findbyauthor\n"
                          "Найти книгу по year - findbyyear\n"
                          "Список всех книг - showall\n"
                          "Удалить книгу - delbyid\n"
                          "Изменить статус - changestatus\n")
                case "showall":
                    bs.get_all()
                    continue
                case "add":
                    bs.add(Book(bv))
                    continue
                case "findbytitle":
                    title = input()
                    bs.get_by_title(title)
                    continue
                case "findbyauthor":
                    author = input()
                    bs.get_by_author(author)
                    continue
                case "findbyyear":
                    try:
                        year = int(input())
                    except Exception as ex:
                        print("Неверный формат года")
                        continue
                    bs.get_by_year(year)
                    continue
                case "delbyid":
                    del_id = input()
                    bs.del_by_id(del_id)
                    continue
                case "changestatus":
                    c_id = input()
                    bs.change_status(c_id)
                    continue
