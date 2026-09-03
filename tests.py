from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

# -----------------------------------------------------------------------------------------------------------------------------------
# 2ой тест для метода set_book_genre с существующим жанром
    def test_set_book_genre_add_existing_genre(self):
        collector_2 = BooksCollector()
        collector_2.add_new_book('Шерлок Холмс')
        collector_2.set_book_genre('Шерлок Холмс', 'Детективы')
        assert collector_2.get_book_genre('Шерлок Холмс') == 'Детективы'

# -----------------------------------------------------------------------------------------------------------------------------------
# 3ий тест для того же метода set_book_genre с несуществующим жанром
    def test_set_book_genre_add_nonexisting_genre(self):
        collector_3 = BooksCollector()
        collector_3.add_new_book('Я - легенда')
        collector_3.set_book_genre('Я - легенда', 'Романы')
        assert not collector_3.get_book_genre('Я - легенда') == 'Романы'

# -----------------------------------------------------------------------------------------------------------------------------------
