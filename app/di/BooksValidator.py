from app.config.naming_config import *


class BooksValidator:
    """
    RU: Класс для ввода и проверки данных книги.
    EN: Class for input&set book data.
    """
    def __init__(self, for_test: bool = False):
        self.for_test = for_test
        self.data = {}

    def set_validate_data(self) -> dict:
        """
        RU: Метод для проверки данных пользователя. Иньектируется в процессе рантайма.
        EN: Method for user data validation. Injects in runtime.
        """
        print("//Создание новой книги")
        try:
            self.__set_validate_title()
            self.__set_validate_author()
            self.__set_validate_year()
        except Exception as ex:
            print(ex.__str__())
            return {}
        return self.data

    def __set_validate_title(self):
        """
        RU: Приватный метод для проверки заголовка.
        EN: Private method for title validation.
        """
        if not self.for_test:
            title = input("Введите название книги: ")
            if len(title) < 0 or len(title) > TITLE_MAX_LEN:
                raise ValueError("Неверная длина заголовка книги")
            self.data["title"] = title



    def __set_validate_author(self):
        """
        RU: Приватный метод для проверки автора.
        EN: Private method for author validation.
        """
        author = input("Введите автора книги: ")
        if len(author) < 0 or len(author) > AUTHOR_MAX_LEN:
            raise ValueError("Неверная длина имени автора")
        self.data["author"] = author

    def __set_validate_year(self):
        """
        RU: Приватный метод для проверки года.
        EN: Private method for year validation.
        """
        try:
            year = int(input("Введите год издания книги: "))
        except Exception as ex:
            raise ValueError("В году не должны использоваться символы помимо цифр")
            #print("В году не должны использоваться символы помимо цифр")
        if year < MIN_YEAR or year > MAX_YEAR:
            raise ValueError(f"Год должен быть больше {MIN_YEAR} и меньше {MAX_YEAR}")
        self.data["year"] = year



