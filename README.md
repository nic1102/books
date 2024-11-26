# __Консольное приложение для управления книжной полкой.__

__Описание:__ Консольное приложение для управления библиотекой книг. Оно позволяет добавлять, удалять, изменять и просматривать информацию о книгах. Доступно два режима.
Хранение внутри оперативной памяти или внутри Json.
Версия Python - 3.10. Все выполнено на стандартных библиотеках.

# __Установка:__

__1. Клонирование репозитория:__

Откройте терминал или командную строку. <br />
Перейдите в директорию, где вы хотите установить приложение. <br />
Введите команду ___git clone https://github.com/nic1102/books___ <br />

__2. Установка зависимостей:__

Зависимости отстутвуют. Все выполнено с помощью стандартной библиотеки. <br />

__3. Запуск приложения:__

Убедитесь, что у вас установлен Python.
Запустите приложение с помощью команды python main.py

# __Приложение предоставляет следующие команды:__

Добавить книгу - __add__ <br />
Найти книгу по title - __findbytitle__ <br />
Найти книгу по author - __findbyauthor__ <br />
Найти книгу по year - __findbyyear__ <br />
Список всех книг - __showall__ <br />
Удалить книгу - __delbyid__ <br />
Изменить статус - __changestatus__ <br />

Также был создан тестовый файл app/res/data.json для проверки работоспособности и функционала приложения. <br />

# __Архитектура приложения__:

Метод для валидации и установки значений. Иньектируется в процессе рантайма. Все зависимости находятся в модуле app.di

```python
    def set_validate_data(self) -> dict:
        print("//Создание новой книги")
        try:
            self.__set_validate_title()
            self.__set_validate_author()
            self.__set_validate_year()
        except Exception as ex:
            print(ex.__str__())
            return {}
        return self.data
```

Также есть вспомогательные методы для валидатора сверху. Один из примеров.

```python
    def __set_validate_title(self):
        #Метод для проверки заголовка
        if not self.for_test:
            title = input("Введите название книги: ")
            if len(title) < 0 or len(title) > TITLE_MAX_LEN:
                raise ValueError("Неверная длина заголовка книги")
            self.data["title"] = title
```

Для описания логики разных режимов( InMemory и Json) создан абстрактный класс от которого будут наследоваться и переопределятся соответсвующие методы.

```python
class Bookshelf(ABC):

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

```

Ошибки обрабатываются в блоках try - except. С выводом соответсвующего сообщения.

```python
        try:
            self.book_dic[book_to_change_id]["status"] = not self.book_dic[book_to_change_id]["status"]
            with open("app/res/data.json", "w") as file:
                json.dump(self.book_dic, file)
        except KeyError as ex:
            print("Книги с таким айди нет")
```

Генерация айди возложена на uuid, с хорошей уникальностью и скоростью.

```python
self.id = uuid.uuid4().__str__()
```

Для удобочитаемого вывода информации переопределен метод __str__().

```python
    def __str__(self) -> str:
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
```

Пример одного из метода для поиска книги по автору.

```python
    def get_by_author(self, book_to_get_author: str):
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
```

# __Контакты и обратная свзяь__:

__Авторы:__ Викторов Никита Андреевич <br />
__Contacts:__ https://t.me/IAM_A_SERGEON <br />
__Дата создания:__ 25.11.2024 <br />
__Спасибо!__
