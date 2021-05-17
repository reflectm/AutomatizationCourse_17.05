"""Модуль содержащий набор очень полезных функций!!!

Потом они будут нам очень полезны!
"""
import math
import random
from pathlib import Path


def get_circle_length(radius: float) -> float:
    """Подсчет длины окружности радиуса radius.

    * radius - вещественное положительное число
    """
    return math.pi * radius * 2


def add(a_arg: int, b_arg: int) -> int:
    """Сумма двух целых чисел.

    * a_arg - целое число
    * b_arg - целое число
    """
    return a_arg + b_arg


def get_current_dir() -> None:
    """Выводит на консоль текущую рабочую диреткорию."""
    print(Path.cwd())


def get_random_digit() -> int:
    """Возвращает случайное целое число из диапазона от 0 до 99."""
    return random.randint(0, 100)


def main() -> None:
    """Основная точка входа в приложение."""
    res_dig = add(10, 20)
    res_str = add(2, 3)
    print(res_dig, res_str)
    random_digit = get_random_digit()
    get_current_dir()
    print(random_digit)
    print(get_circle_length(22))


if __name__ == "__main__":  # Если этот модуль был запущен напрямую (не импоритрован)
    main()
