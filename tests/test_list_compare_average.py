"""Тесты класса ListCompareAverage"""

import pytest

from list_compare.list_compare_average import ListCompareAverage


class TestListCompareAverage:
    """Класс теста ListCompareAverage"""

    FIRST_GREATER_STR = "1-ок имеет большее среднее значение"
    SECOND_GREATER_STR = "2-ой список имеет большее среднее значение"
    EQUAL_STR = "Средние значения равны"

    def test_valid_init(self):
        """
        Проверка инициализации класса двумя валидными списками.
        """

        list_lhs = [1, 2, 3, 4, 5, 6]
        list_rhs = [1, 2, 3, 4, 5]
        lc = ListCompareAverage(list_lhs, list_rhs)
        assert lc.list_lhs == list_lhs
        assert lc.list_rhs == list_rhs

    def test_setters(self):
        """
        Проверка установки новых списков.
        """

        list_lhs = [1, 2, 3, 4, 5]
        list_rhs = [1, 2, 3, 4, 5]
        lc = ListCompareAverage(list_lhs, list_rhs)
        new_list_lhs = [1]
        new_list_rhs = [2]
        lc.list_lhs = new_list_lhs
        lc.list_rhs = new_list_rhs
        assert lc.list_lhs == new_list_lhs
        assert lc.list_rhs == new_list_rhs

    def test_int_lists_first_greater(self):
        """
        Целочисленные списки.
        Проверка что срдеднее 1-ого списка больше.
        """

        list_lhs = [1, 2, 3, 4, 5, 6]
        list_rhs = [1, 2, 3, 4, 5]
        lc = ListCompareAverage(list_lhs, list_rhs)
        assert lc.compare_average() == self.FIRST_GREATER_STR

    def test_int_lists_second_greater(self):
        """
        Целочисленные списки.
        Проверка что срдеднее 2-ого списка больше.
        """

        list_lhs = [1, 2, 3, 4, 5]
        list_rhs = [1, 2, 3, 4, 5, 6]
        lc = ListCompareAverage(list_lhs, list_rhs)
        assert lc.compare_average() == self.SECOND_GREATER_STR

    def test_int_lists_equal(self):
        """
        Целочисленные списки.
        Проверка что срдедние равны.
        """

        list_lhs = [1, 2, 3, 4, 5]
        list_rhs = [1, 2, 3, 4, 5]
        lc = ListCompareAverage(list_lhs, list_rhs)
        assert lc.compare_average() == self.EQUAL_STR

    def test_float_lists_first_greater(self):
        """
        Вещественные списки.
        Проверка что срдеднее 1-ого списка больше.
        """

        list_lhs = [1.1, 2.2, 3.3, 4.4, 5.5, 6.6]
        list_rhs = [1.1, 2.2, 3.3, 4.4, 5.5]
        lc = ListCompareAverage(list_lhs, list_rhs)
        assert lc.compare_average() == self.FIRST_GREATER_STR

    def test_float_lists_second_greater(self):
        """
        Вещественные списки.
        Проверка что срдеднее 2-ого списка больше.
        """

        list_lhs = [1.1, 2.2, 3.3, 4.4, 5.5]
        list_rhs = [1.1, 2.2, 3.3, 4.4, 5.5, 6.6]
        lc = ListCompareAverage(list_lhs, list_rhs)
        assert lc.compare_average() == self.SECOND_GREATER_STR

    def test_float_lists_equal(self):
        """
        Вещественные списки.
        Проверка что срдедние равны.
        """

        list_lhs = [1.1, 2.2, 3.3, 4.4, 5.5]
        list_rhs = [1.1, 2.2, 3.3, 4.4, 5.5]
        lc = ListCompareAverage(list_lhs, list_rhs)
        assert lc.compare_average() == self.EQUAL_STR

    def test_negative_lists(self):
        """
        Проверки с негативными числами.
        """

        list_lhs1 = [-1, -2, -3, -4, -5, -6]
        list_rhs1 = [-1, -2, -3, -4, -5]
        lc1 = ListCompareAverage(list_lhs1, list_rhs1)
        assert lc1.compare_average() == self.SECOND_GREATER_STR

        list_lhs2 = [-1, -2, -3, -4, -5]
        list_rhs2 = [-1, -2, -3, -4, -5, -6]
        lc2 = ListCompareAverage(list_lhs2, list_rhs2)
        assert lc2.compare_average() == self.FIRST_GREATER_STR

        list_lhs3 = [-1, -2, -3, -4, -5]
        list_rhs3 = [-1, -2, -3, -4, -5]
        lc3 = ListCompareAverage(list_lhs3, list_rhs3)
        assert lc3.compare_average() == self.EQUAL_STR

    def test_init_not_numbers(self):
        """
        Проверки инициализации списками, содержащих не только числа.
        """

        list_str = ['1', '2', '3']
        list_int = [1, 2, 3, 4, 5]
        # Строки
        with pytest.raises(ValueError):
            ListCompareAverage(list_str, list_str)

        with pytest.raises(ValueError):
            ListCompareAverage(list_str, list_int)

        with pytest.raises(ValueError):
            ListCompareAverage(list_int, list_str)

        # Строка в середине
        list_str2 = [1, 2, '3', 4, 5]
        with pytest.raises(ValueError):
            ListCompareAverage(list_str2, list_str2)

        with pytest.raises(ValueError):
            ListCompareAverage(list_str2, list_int)

        with pytest.raises(ValueError):
            ListCompareAverage(list_int, list_str2)

        # Список в середине
        list_list = [1, 2, [3], 4, 5]
        with pytest.raises(ValueError):
            ListCompareAverage(list_list, list_list)

        with pytest.raises(ValueError):
            ListCompareAverage(list_list, list_int)

        with pytest.raises(ValueError):
            ListCompareAverage(list_int, list_list)

        # Словарь в середине
        list_dict = [1, 2, {'3': 3}, 4, 5]
        with pytest.raises(ValueError):
            ListCompareAverage(list_dict, list_dict)

        with pytest.raises(ValueError):
            ListCompareAverage(list_dict, list_int)

        with pytest.raises(ValueError):
            ListCompareAverage(list_int, list_dict)

    def test_set_not_numbers(self):
        """
        Проверки установки списков, содержащих не только числа.
        """

        list_int = [1, 2, 3, 4, 5]
        lc = ListCompareAverage(list_int, list_int)

        # Строки
        list_str = ['1', '2', '3']
        with pytest.raises(ValueError):
            lc.list_lhs = list_str
        with pytest.raises(ValueError):
            lc.list_rhs = list_str

        # Строка в середине
        list_str2 = [1, 2, '3', 4, 5]
        with pytest.raises(ValueError):
            lc.list_lhs = list_str2
        with pytest.raises(ValueError):
            lc.list_rhs = list_str2

        # Список в середине
        list_list = [1, 2, [3], 4, 5]
        with pytest.raises(ValueError):
            lc.list_lhs = list_list
        with pytest.raises(ValueError):
            lc.list_rhs = list_list

        # Словарь в середине
        list_dict = [1, 2, {'3': 3}, 4, 5]
        with pytest.raises(ValueError):
            lc.list_lhs = list_dict
        with pytest.raises(ValueError):
            lc.list_rhs = list_dict

    def test_init_empty_list(self):
        """
        Проверки инициализации с пустыми списками.
        """

        list_int = [1, 2, 3, 4, 5]
        list_empty = []
        with pytest.raises(ValueError):
            ListCompareAverage(list_empty, list_empty)
        with pytest.raises(ValueError):
            ListCompareAverage(list_int, list_empty)
        with pytest.raises(ValueError):
            ListCompareAverage(list_empty, list_int)

    def test_set_empty_list(self):
        """
        Проверки установки пустыми списками.
        """

        list_int = [1, 2, 3, 4, 5]
        lc = ListCompareAverage(list_int, list_int)
        list_empty = []
        with pytest.raises(ValueError):
            lc.list_lhs = list_empty
        with pytest.raises(ValueError):
            lc.list_rhs = list_empty