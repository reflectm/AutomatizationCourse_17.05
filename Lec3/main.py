"""Модуль осдержащий разные функции, показывающий способы работы с regex."""
import re


def simple_pattern(sample: str):
    """Поиск паттерна '123' в строке sample."""
    answer = re.search(r"123", sample)
    if answer:
        print(answer)
        print("First ID:", answer.start())
        print("Last ID:", answer.end())
        print(sample[answer.start() : answer.end()])


def simple_class(sample: str):
    """Пытаемся найти 3 подряд идущих цифры, каждая из которых изменяется в
    пределах от 2 до 5.

    * Класс определяется через [] и включает в себя все возможыные варианты для символа!
    """
    answer = re.search(r"[0-2][5-9][1-3]", sample)
    print(answer)


def simple_dot(sample:str):
    """
    Точка - как способ пропуска любого символа (абсолютно, кроме \n)
    """
    answer = re.search(r"[0-9].[0-9]", sample)
    print(answer)


def symbolic_class(sample:str):
    """
    Найти в строке такую подпоследовательность:
    * Первый символ 'A'
    * второй символ - на выбор [a,b,x,z, A,B,X,Z]
    * третий символ 'Q'
    """
    answer = re.search(r"A[abxzABXZ]Q", sample)
    print(answer)


def symbolic_class(sample:str):
    """
    Найти в строке подпоследовательность следующего вида:
    Первый символ - цифра от 0 до 9
    Второй символ - любая буква латинского алфавита нижнего регистра
    Третий символ - любая буква латинского алфавита верхнего регистра
    Четвертый символ - цифра от 0 до 9
    """
    answer = re.search( r"[0-9][a-z][A-Z][0-9]",sample)
    print(answer)


def symbolic_class(sample:str):
    """
    Распознать, где у нас в sample встречается первый символ alpha-numeric
    """
    answer = re.search(r"[a-zA-Z0-9]", sample)
    print(answer)

def negative_symbolic_class(sample:str):
    """
    Распознать первый не цифровой символ
    """
    answer = re.search(r"[^0-9]", sample)
    print(answer)

def hat_search(sample:str):
    """
    Попытаемся в строке найти любой символ из класса # ! * ^
    """
    answer = re.search(r"[#!^*]", sample)
    print(answer)


def special_metas(sample:str):
    """
    А что если мне нужно найти символ, который используется в контексте мета-символов?
    .? -? ^?
    """
    answer = re.search(r"[0-9] [\^\.\-] [0-9]", sample)
    print(answer)

def meta_digit(sample:str):
    """
    \d == [0-9]
    \D == [^0-9]
    """
    answer = re.search(r"\D", sample)
    print(answer)

def meta_spacing(sample:str):
    """
    \s - пробелы, табуляции, переносы строк
    \S - не \s
    """
    answer = re.search(r"\S", sample)
    print(answer)

def meta_alphanumeric(sample:str):
    """
    \w == [0-9a-zA-Z_]
    \W == [^0-9a-zA-Z_]
    """
    answer = re.search(r"\W", sample)
    print(answer)

def main():
    """Основная точка входа."""
    # simple_pattern("alex.gavrilov123@gmail.com")
    SAMPLES = ["22 + 33", "Alex", "!&%^$@@!^#_22"]
    for sample in SAMPLES:
        meta_alphanumeric(sample)


if __name__ == "__main__":
    main()
