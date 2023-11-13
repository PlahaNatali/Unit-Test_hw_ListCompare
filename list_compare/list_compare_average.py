"""Сравнения средних значений двух числовых списков"""


def check_list_numbers(func):
    """
    Декоратор для проверки объектов списка на числа.
    Выбрасывает исключение, если находит не число.

    :param func:
    :return: wrapper
    """

    def wrapper(*args, **kwargs):
        for numbers in list(args)[1:] + list(kwargs.values())[1:]:
            if len(numbers) == 0:
                raise ValueError(f"Переданный список пустой: '{numbers}'")

            for number in numbers:
                if not isinstance(number, (int, float)):
                    raise ValueError(f"В '{numbers}' есть не число '{number}' тип {type(number)}")

        return func(*args, **kwargs)

    return wrapper


class ListCompareAverage:
    """Класс для сравнения средних значений двух числовых списков"""

    _list_lhs: list
    _list_rhs: list

    def __init__(self, list_lhs: list, list_rhs: list):
        self.list_lhs = list_lhs
        self.list_rhs = list_rhs

    def __str__(self):
        return f'{self._list_lhs} and {self._list_rhs}'

    @property
    def list_lhs(self) -> list:
        """1-ый - левосторонний список"""

        return self._list_lhs

    @property
    def list_rhs(self) -> list:
        """2-ой - правосторонний список"""

        return self._list_rhs

    @list_lhs.setter
    @check_list_numbers
    def list_lhs(self, list_lhs):
        """Установка левостороннего списка"""

        self._list_lhs = list_lhs

    @list_rhs.setter
    @check_list_numbers
    def list_rhs(self, list_rhs):
        """Установка правостороннего списка"""

        self._list_rhs = list_rhs

    def compare_average(self) -> str:
        """
        Сравнивает средние значения двух списков

        :return: строка результата сравнения
        """
        lhs_average = sum(self._list_lhs) / len(self._list_lhs)
        rhs_average = sum(self._list_rhs) / len(self._list_rhs)

        if lhs_average > rhs_average:
            return "Первый список имеет большее среднее значение"
        if lhs_average < rhs_average:
            return "Второй список имеет большее среднее значение"

        return "Средние значения равны"