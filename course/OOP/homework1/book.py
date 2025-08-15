from typing import Optional


class Book:
    """Клас для представлення книги з основною інформацією.

    """

    def __init__(
            self,
            author: str,
            title: str,
            year: int,
            genre: str
    ):
        self.author = author
        self.title = title
        self.year = year
        self.genre = genre

    def __str__(self) -> str:
        """Повертає зручне для читання представлення книги.

        """
        return f'"{self.title}" - {self.author} ({self.year}, {self.genre})'

    def __repr__(self) -> str:
        """Повертає технічне представлення об'єкта книги.

        """
        return (f"Book(author='{self.author}', title='{self.title}', "
                f"year={self.year}, genre='{self.genre}')")


# Приклади використання
if __name__ == "__main__":
    book1 = Book(
        author="Марк Лутц",
        title="Изучаем Python",
        year=2019,
        genre="Программирование"
    )

    book2 = Book(
        author="Эрик Маттес",
        title="Изучаем Python. Программирование игр, визуализация данных, веб-приложения",
        year=2020,
        genre="Программирование"
    )

    book3 = Book(
        author="Томас Кормен",
        title="Алгоритмы: построение и анализ",
        year=2013,
        genre="Алгоритмы и структуры данных"
    )

    book4 = Book(
        author="Роберт Мартин",
        title="Чистый код: создание, анализ и рефакторинг",
        year=2018,
        genre="Разработка ПО"
    )

    books = [book1, book2, book3, book4]

    print("Використання __str__:")
    for book in books:
        print(f"  {book}")

    print("\nВикористання __repr__:")
    for book in books:
        print(f"  {repr(book)}")

