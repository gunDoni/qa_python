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
# 4ый тест на проверку метода get_books_genre с существующим и несуществующим жанрами
    def test_get_books_genre_add_two_books(self):
        collector_4 = BooksCollector()
        collector_4.add_new_book('Смерть на Ниле')
        collector_4.set_book_genre('Смерть на Ниле', 'Детективы')
        collector_4.add_new_book('Алхимик')
        collector_4.set_book_genre('Алхимик', 'Проза')
        assert collector_4.get_books_genre() == {'Смерть на Ниле':'Детективы', 'Алхимик': ''}

# -----------------------------------------------------------------------------------------------------------------------------------
# 5ый тест параметризирован для метода get_books_with_specific_genre с существующим и несуществующим жанрами
    @pytest.mark.parametrize('name, genre, expected_result', [
        ('Вечеринка в Хэллоуин', 'Детективы', ['Вечеринка в Хэллоуин']),
        ('Идиот', 'Роман', [])
    ])
    def test_get_books_with_specific_genre_existing_and_nonexisting(self, name, genre, expected_result):
        collector_5 = BooksCollector()
        collector_5.add_new_book(name)
        collector_5.set_book_genre(name, genre)
        assert collector_5.get_books_with_specific_genre(genre) == expected_result

# -----------------------------------------------------------------------------------------------------------------------------------
# 6ой тест параметризирован для метода get_books_for_children с разными вариантами проверки
    @pytest.mark.parametrize('name, genre, expected_result', [
        ('Черепашки-ниндзя', 'Мультфильмы', ['Черепашки-ниндзя']),
        ('Убийство в "Восточном экспрессе"', 'Детективы', []),
        ('Капитал', 'Экономика', [])
    ])
    def test_get_books_for_children_rated_and_unrated_and_nonexistent_genre(self, name, genre, expected_result):
        collector_6 = BooksCollector()
        collector_6.add_new_book(name)
        collector_6.set_book_genre(name, genre)
        assert collector_6.get_books_for_children() == expected_result

# -----------------------------------------------------------------------------------------------------------------------------------
# 7ой тест для метода add_book_in_favorites. Проверил добавление дубликата
    def test_add_book_in_favorites_add_duplicate(self):
        collector_7 = BooksCollector()
        collector_7.add_new_book('Задача трех тел')
        collector_7.add_book_in_favorites('Задача трех тел')
        collector_7.add_book_in_favorites('Задача трех тел')
        assert len(collector_7.get_list_of_favorites_books()) == 1

# -----------------------------------------------------------------------------------------------------------------------------------
# 8ой тест параметризирован для метода delete_book_from_favorites. Проверяется удаление книги как существующей, так и отсутствующей в self.favorites
    @pytest.mark.parametrize('add_to_favorites, expected_count', [
        (True, 0),
        (False, 0)
    ])
    def test_delete_book_from_favorites_existing_and_nonexisting(self, add_to_favorites, expected_count):
        collector_8 = BooksCollector()
        collector_8.add_new_book('Граф Монте-Кристо')
        if add_to_favorites:
            collector_8.add_book_in_favorites('Граф Монте-Кристо')
        collector_8.delete_book_from_favorites('Граф Монте-Кристо')
        assert len(collector_8.get_list_of_favorites_books()) == expected_count

# -----------------------------------------------------------------------------------------------------------------------------------
# 9ый тест для метода add_book_in_favorites. Проверяется добавление несуществующей книги в списке книг.
    def test_add_book_in_favorites_add_nonexistent_book(self):
        collector_9 = BooksCollector()
        collector_9.add_new_book('Белый клык')
        collector_9.add_new_book('Зов предков')
        collector_9.add_new_book('Сын волка')
        collector_9.add_book_in_favorites('Белый клык')
        collector_9.add_book_in_favorites('Зов предков')
        collector_9.add_book_in_favorites('Сын волка')
        collector_9.add_book_in_favorites('Любовь к жизни')
        assert len(collector_9.get_list_of_favorites_books()) == 3
