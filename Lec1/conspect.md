## Лекция 1. Как писать понятный код?

***В Python*** существует несколько стандартов - один из самых известных - [PEP8](https://www.python.org/dev/peps/pep-0008/).

Для написания понятного кода нужно:
* Правильно расставлять отступы
* Правильно документировать свой код (функции, классы, модули)
* Правильно раскладывать импорты

### Возможное решение
Использование классического форматера ```autopep8``` (вшит по умолчанию в ***PyCharm*** и схожие среды разработки) с одной стороны пытается решить эту проблему - с другой - делает все еще в 10 раз хуже.

***Пример***: рассмотрим следующий код
```
# Простейшая лямбда
a = lambda x,y: x**2 + y**2

# Достаточно длинная команда
lst = [ (x, y) for x in range(1, 100) for y in range(1, 50)] + [(x,z) for x in range(1, 200) for z in range(1, 50)] + [(y,z) for y in range(1, 200) for z in range(1, 50)]
```

И теперь воспользуемся автоформатером ```autopep8```. Для этого вручную выполним команду (модуль называется ```sample.py```):
```
autopep8 --in-place --aggressive sample.py
```
* ```--in-place``` - внести изменения на месте (прямо в модуле)
* ```--aggressive``` - степень "агрессии" (чем больше степеней - тем сложнее понять, что он вообще делает)
* ```main.py``` - путь до модуля (если лежит в другом месте ```path/to/file.py```)

В итоге имеем:
```
# Простейшая лямбда
def a(x, y): return x**2 + y**2


# Достаточно длинная команда
lst = [(x, y) for x in range(1, 100) for y in range(1, 50)] + [(x, z) for x in range(1, 200)
                                                               for z in range(1, 50)] + [(y, z) for y in range(1, 200) for z in range(1, 50)]

```
Стало еще более непонятно. Что делать?

### Хорошее решение
```autopep8``` - конечно лучше, чем ничего, но это один из самых старых форматеров. Сейчас 2021 год и существует набор более адекватных инструментов, с которыми мы познакомимся.

### Black
* Форматер ```black``` : ```pip install black```. Репа - https://github.com/psf/black
* Применим его к коду выше : ```black sample.py``` (или ```python -m black sample.py```)
```
# Простейшая лямбда
a = lambda x, y: x ** 2 + y ** 2

# Достаточно длинная команда
lst = (
    [(x, y) for x in range(1, 100) for y in range(1, 50)]
    + [(x, z) for x in range(1, 200) for z in range(1, 50)]
    + [(y, z) for y in range(1, 200) for z in range(1, 50)]
)

```
Гораздо лучше!


### Pylint (классика)
Код отформатирован неплохо, но как проверить - все ли с ним ок, с точки зрения не отступов,а семантики? Линтер ```pylint``` позволит это все узнать: ```pip install pylint```. Репа - https://github.com/PyCQA/pylint
* Применим ```pylint``` : ```pylint sample.py``` (```python -m pylint sample.py```)
```
************* Module sample
sample.py:1:0: C0114: Missing module docstring (missing-module-docstring)

--------------------------------------------------------------------
Your code has been rated at 5.00/10 (previous run: -5.00/10, +10.00)
```
Как видите, для этого кода мы (как минимум) забыли написать докстрингу (это такие аналоги комментариев, в ```Python``` используются для документирования кода). Исправим это:
```
"""
Это тестровый модуль для всяких игр, который не делает ничего полезного от слова совсем.
Возможно, ему самое место в корзине?
"""
# Простейшая лямбда
a = lambda x, y: x ** 2 + y ** 2

# Достаточно длинная команда
lst = (
    [(x, y) for x in range(1, 100) for y in range(1, 50)]
    + [(x, z) for x in range(1, 200) for z in range(1, 50)]
    + [(y, z) for y in range(1, 200) for z in range(1, 50)]
)

```

* Еще раз прогоняем ```pylint``` : ```pylint sample.py```
```

-------------------------------------------------------------------
Your code has been rated at 10.00/10 (previous run: 5.00/10, +5.00)
```

Отлично! Теперь прогоним ```black``` чтобы он на всякий расставил отступы : ```black sample.py```
Двигаемся дальше!

#### docformatter (стандартизируем докстринги)
* Хорошая новость - ```pylint``` не пропустит код без докстрингов (будет много пояснений - это хорошо)
* Плохая новость - на докстринги также есть ряд требований, изложенных в диалектах ```PEP```
Что делать? Используем автоинструмент для форматирования докстрингов! ```docformatter``` : ```pip install docformatter```. Репа - https://github.com/myint/docformatter

* Применим докформатер к нашему коду: ```docformatter -i sample.py``` (```python -m docformatter -i sample.py```)
* Здесь ```-i``` - означает ```in-place``` внести изменения прямо в модуле.
В итоге получаем:
```
"""Это тестровый модуль для всяких игр, который не делает ничего полезного от
слова совсем.

Возможно, ему самое место в корзине?
"""
# Простейшая лямбда
a = lambda x, y: x ** 2 + y ** 2

# Достаточно длинная команда
lst = (
    [(x, y) for x in range(1, 100) for y in range(1, 50)]
    + [(x, z) for x in range(1, 200) for z in range(1, 50)]
    + [(y, z) for y in range(1, 200) for z in range(1, 50)]
)

```

* Восхититетльно!
После этого рекомендую прогнать ```black``` и ```pylint``` , чтобы убедиться, что ничего никуда не уползло.

### Код растет
Давайте представим, что наш код немного подрос и теперь выглядит более воинтственно:
```
import random
from pathlib import Path
import math


def get_circle_length(r):
    return math.pi * r * 2

def add(a,b):
    return a + b

def get_current_dir():
    print(Path.cwd())

def get_random_digit():
    return random.randint(0, 100)

def main():
    res_dig = add(10, 20)
    res_str = add("Hello ", "world")
    print(res_dig, res_str)

    a = get_current_dir()
    b = get_random_digit()
    print(a, b)

    print(get_circle_length(22))

if __name__ == '__main__':
    main()

```

* Как вы видите, код стал больше
* Появилось и гораздо больше проблем!
Теперь разберем проблемы по порядку. Начнем с того, что уже умеем (```black```, ```pylint```, ```docformatter```). В результате применения этих операций, нас заставят написать документацию ко всем функциям, а также к самому модулю. Также pylint очень неодобрительно посмотрит на наши параметры функций, состоящих из одной буквы, это не хорошо). После внесения исправлений получим что-то более менее адекватное.
```
"""Модуль содержащий набор функций для решения важной вычислительной задачи."""

import random
from pathlib import Path
import math


def get_circle_length(radius):
    """Подсчет длины окружности радиуса radius."""
    return math.pi * radius * 2


def add(a_arg, b_arg):
    """Подсчет арифметической суммы параметров a_arg и b_arg."""
    return a_arg + b_arg


def get_current_dir():
    """Печать текущей рабочей директории."""
    print(Path.cwd())


def get_random_digit():
    """Возвращает случайно целое число из диапазона от 0 до 100."""
    return random.randint(0, 100)


def main():
    """Основная точка входа в приложение."""
    res_dig = add(10, 20)
    res_str = add("Hello ", "world")
    print(res_dig, res_str)

    get_current_dir()
    random_digit = get_random_digit()
    print(random_digit)

    print(get_circle_length(22))


if __name__ == "__main__":
    main()

```

Стало получше. Но проблемы еще есть.
* Проблема 1 : импорты не отсортированы по ```pep```
* Проблема 2 : по сигнатурам наших функций не совсем понятно, как с ними стоит обходиться.

#### Решение Проблемы 1. isort
* ```isort``` (или ```import sort```) - инстурмент для автоматической сортировки всех импортов проекта в соответвтсвии с ```pep```.
```pip install isort``` . Репа - https://github.com/PyCQA/isort

* Применим к нашему коду ```isort``` : ```isort sample.py```
```
"""Модуль содержащий набор функций для решения важной вычислительной задачи."""

import math
import random
from pathlib import Path

....
```
* Отлично. С этим разобрались.


#### Решение Проблемы 2. Аннотации и mypy
* Аннотации в ```python```- инструмент, никак не влияющий на производительность кода, но увеличивающий в сотни раз его понимание разработчиками. Аннотации никак не ограничивают входные типы данных (не влияют на их конвертацию и приведение).
Добавим аннотации в код:
```
"""Модуль содержащий набор функций для решения важной вычислительной задачи."""

import math
import random
from pathlib import Path


def get_circle_length(radius: float) -> float:
    """Подсчет длины окружности радиуса radius."""
    return math.pi * radius * 2


def add(a_arg: int, b_arg: int) -> int:
    """Подсчет арифметической суммы параметров a_arg и b_arg."""
    return a_arg + b_arg


def get_current_dir() -> None:
    """Печать текущей рабочей директории."""
    print(Path.cwd())


def get_random_digit() -> int:
    """Возвращает случайно целое число из диапазона от 0 до 100."""
    return random.randint(0, 100)


def main() -> None:
    """Основная точка входа в приложение."""
    res_dig = add(10, 20)
    res_str = add("Hello ", "world")
    print(res_dig, res_str)

    get_current_dir()
    random_digit = get_random_digit()
    print(random_digit)

    print(get_circle_length(22))


if __name__ == "__main__":
    main()

```

* Как видите, теперь код стал более предсказуемым и читать его гораздо лучше!
Запись ```def get_circle_length(radius: float) -> float:``` буквально стоит воспринимать как ```функции get_circle_length ЖЕЛАТЕЛЬНО передать вещественное число и тогда она вернет вещественное число```, а ```def get_current_dir() -> None:``` означает ```функция get_current_dir не принимает никаких параметров и НИЧЕГО не возвращает, не нужно пытаться присвоить ее значение куда либо```.


### Самая страшная строка
* В нашем коде есть самая страшная строка ```res_str = add("Hello ", "world")``` . С точки зрения питона тут все ок. Действительно, функция ```add``` может выполнить операцию ```+``` как над числами, так и над стркоами. Но с точки зрения однозначности и читабельности кода - это чистой воды катастрофа! Даже ```pylint``` скажет, что тут 10 из 10, но это же не верно! Как бороться с такими ситуациями? Хорошие новости - есть ```mypy``` : ```pip install mypy```. Репа - https://github.com/python/mypy

```mypy``` - это инстурмент выявления конфликтов аннтированного кода, позволяет подсказать, где в коде происходит конфликт передачи неверных параметров и их опасное использование. Применим ```mypy``` : ```mypy sample.py``` (```python -m mypy sample.py```)
```
sample.py:31: error: Argument 1 to "add" has incompatible type "str"; expected "int"
sample.py:31: error: Argument 2 to "add" has incompatible type "str"; expected "int"
Found 2 errors in 1 file (checked 1 source file)
```

* Отлично! Теперь мы видим, где что-то использутся не совсем так, как планировалось!

#### В итоге
Набор команд из 5-ти инструментов можно свести к достаточно простой последовательности. Представим, что имя нашего файла все также  ```sample.py```:
* Форматируем все и сразу : ```black sample.py && docformatter -i sample.py && isort sample.py```
* Проверяем семантику: ```pylint main.py```
* Проверям аннотации и типажи: ```mypy main.py```

Выполняя периодически данные команды ваш код будет поддерживаться в чистоте, он будет понятен, прекрасен и стандартизирован :)

### Автоматизация проверов
Каждый раз вручную выполнять данные операции мягко говоря утомляет, но можно это все сделать гораздо проще. Для этого нам понадобятся ```makefile```. Это такие файлы, содержащие наборы небольших псевдонимов для действий, выполняемых в терминале (на самом деле это нечто большее и данное определние - полная фигня, но в нашем контексте это наиболее понятное трактование). Если вы используете ```MacOS``` или любой ```Linux```-форк (```Ubuntu```, ```Arch``` и т.д.) вам можно пропустить следующий шаг.

#### Утилита make
Если вы используете ```Windows``` скорее всего ```make``` нужно установить (это утилита позволяющая работать с ```makefile```).
Найти ее можно тут: http://gnuwin32.sourceforge.net/packages/make.htm

#### Makefile
В директории с файлом создадим ```Makefile``` (так и называется) со следующим содержимым:
```
.PHONY: format check lint

format:
	black sample.py && isort sample.py && docformatter -i sample.py

check:
	mypy sample.py

lint:
	pylint sample.py

.DEFAULT_GOAL := format
```

* Теперь в консоли можно делать простую магию:
    * ```make format``` (или просто ```make```, т.к. формат - дефолтная задача) запустит команду по форматированию
    * ```make check``` - запустит команду проверки типов
    * ```make lint``` - запустит линтер


* В каком порядке применять команды? Самая холиварная тема) Но по секрету скажу, что удобнее : format -> check -> lint

## Итог
В итоге поулчается вот такой прекрасный код (правда, он бесполезный, но выглядит достойно):
```
"""Модуль содержащий набор функций для решения важной вычислительной задачи."""

import math
import random
from pathlib import Path


def get_circle_length(radius: float) -> float:
    """Подсчет длины окружности радиуса radius."""
    return math.pi * radius * 2


def add(a_arg: int, b_arg: int) -> int:
    """Подсчет арифметической суммы параметров a_arg и b_arg."""
    return a_arg + b_arg


def get_current_dir() -> None:
    """Печать текущей рабочей директории."""
    print(Path.cwd())


def get_random_digit() -> int:
    """Возвращает случайно целое число из диапазона от 0 до 100."""
    return random.randint(0, 100)


def main() -> None:
    """Основная точка входа в приложение."""
    res_dig = add(10, 20)
    print(res_dig)

    get_current_dir()
    random_digit = get_random_digit()
    print(random_digit)

    print(get_circle_length(22))


if __name__ == "__main__":
    main()

```

* Обязательно пользуйтесь этими инструментами! Своевременное применение данных команд - залог эффективного написания кода, а также гарант того, что ваши коллеги всегда вас поймут и смогут вам помочь!