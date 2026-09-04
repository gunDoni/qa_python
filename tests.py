import pytest
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
# 1ый тест параметризирован для метода set_book_genre с существующим и несуществующим жанром
    @pytest.mark.parametrize('genre, expected_genre', [
    ('Детективы', 'Детективы'),
    ('Романы', '')
    ])
    def test_set_book_genre_two_genres(self, genre, expected_genre):
        collector_1 = BooksCollector()
        collector_1.add_new_book('Я - легенда')
        collector_1.set_book_genre('Я - легенда', genre)
        assert collector_1.get_book_genre('Я - легенда') == expected_genre

# -----------------------------------------------------------------------------------------------------------------------------------
# 2ой тест параметризирован для метода get_book_genre с существующей книгой в списке и несуществующей
    @pytest.mark.parametrize('name, noname, genre, expected_genre', [
    ('Шерлок Холмс', 'Я - легенда', 'Детективы', None),
    ('Оно', 'Оно', 'Ужасы', 'Ужасы')
    ])
    def test_get_book_genre_existing_and_nonexisting_book(self, name, noname, genre, expected_genre):
        collector_2 = BooksCollector()
        collector_2.add_new_book(name)
        collector_2.set_book_genre(name, genre)
        assert collector_2.get_book_genre(noname) == expected_genre

# -----------------------------------------------------------------------------------------------------------------------------------
# 3ий тест параметризирован для метода add_new_book, чтобы проверить работу с разной длиной книг: 20 символов (середина ограничения) и пограничные значения (39, 40, 41)
    @pytest.mark.parametrize('name, expected_result', [
        ('12345678901234567890', True),
        ('123456789012345678901234567890123456789', True),
        ('1234567890123456789012345678901234567890', True),
        ('12345678901234567890123456789012345678901', False)
        ])
    def test_add_new_book_add_different_quantity(self, name, expected_result):
        collector_3 = BooksCollector()
        collector_3.add_new_book(name)
        assert (name in collector_3.get_books_genre()) == expected_result

# -----------------------------------------------------------------------------------------------------------------------------------
# 