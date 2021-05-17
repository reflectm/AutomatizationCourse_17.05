"""Модуль для того, чтобы понять как работают анализаторы в лице:

* black
* pylint
* docformatter
"""
# Простейшая лямбда
a = lambda x, y: x ** 2 + y ** 2

# Простейшее списочное выражение
lst = (
    [(x, y) for x in range(1, 100) for y in range(1, 100)]
    + [(y, z) for y in range(1, 100) for z in range(1, 100)]
    + [(z, x) for x in range(2, 200) for z in range(1, 500)]
)
