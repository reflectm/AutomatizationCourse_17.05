## Лекция 3. Регулярные выражения

***Регулярное выражение*** - последовательность метасимволов, которая позволяет выделять подстроки из общего строкового литерала.

### Шаг 1. Модуль re
* Модуль - содержащий набор функций, позволяющий обрабатывать регулярные выражения.
* ```re.search(<pattern>, <string>)``` - функция, которая пытается найти правило ```<pattern>``` в строке ```<string>```. В случае, если паттерн удовлетворятся (матчится matching) - возвращается объект, содержащий индексы начала и конца паттерна в строке. В противном случае - ```None```.

### Шаг 2. Простейшая маска (простейший паттерн)
```
def simple_pattern(sample: str):
    """Поиск паттерна '123' в строке sample."""
    answer = re.search(r"123", sample)
    if answer:
        print(answer)
        print("First ID:", answer.start())
        print("Last ID:", answer.end())
        print(sample[answer.start() : answer.end()])
```

### Шаг 3. Цифровые классы
```
def simple_class(sample: str):
    """Пытаемся найти 3 подряд идущих цифры, каждая из которых изменяется в
    пределах от 2 до 5.

    * Класс определяется через [] и включает в себя все возможыные варианты для символа!
    """
    answer = re.search(r"[0-2][5-9][1-3]", sample)
    print(answer)
```

### Шаг 4. Магическая точка
```
def simple_dot(sample:str):
    """
    Точка - как способ пропуска любого символа (абсолютно, кроме \n)
    """
    answer = re.search(r"[0-9].[0-9]", sample)
    print(answer)

```

### Шаг 5. Классы. Подробнее
* Явно описанный блок , как  символный класс
```
def symbolic_class(sample:str):
    """
    Найти в строке такую подпоследовательность:
    * Первый символ 'A'
    * второй символ - на выбор [a,b,x,z, A,B,X,Z]
    * третий символ 'Q'
    """
    answer = re.search(r"A[abxzABXZ]Q", sample)
    print(answer)

```

* Явно указанный символы алфавита (с регистром ) и цифры
```
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
```

* Поиск первого цифро-буквенного символа
```
def symbolic_class(sample:str):
    """
    Распознать, где у нас в sample встречается первый символ alpha-numeric
    """
    answer = re.search(r"[a-zA-Z0-9]", sample)
    print(answer)
```

### Шаг 6. Исключающий класс
* Способ указать НЕ ВХОДЯЩИЙ символ
```

def negative_symbolic_class(sample:str):
    """
    Распознать первый не цифровой символ
    """
    answer = re.search(r"[^0-9]", sample)
    print(answer)

```

* Поиск ```^``` как элемент, входящий в класс 
```
def hat_search(sample:str):
    """
    Попытаемся в строке найти любой символ из класса # ! * ^
    """
    answer = re.search(r"[#!^*]", sample)
    print(answer)

```

* Правило : ```[....]``` - включающий класс, ```[^...]``` исключающий класс


### Шаг 7. Экранированные меты
```
def special_metas(sample:str):
    """
    А что если мне нужно найти символ, который используется в контексте мета-символов?
    .? -? ^?
    """
    answer = re.search(r"[0-9] [\^\.\-] [0-9]", sample)
    print(answer)
```

### Шаг 8. Короткие меты для классов
* ```\w``` и ```\W``` - это тоже самое, что и ```[0-9a-zA-Z_]``` И ```[^0-9a-zA-Z_]```
* ```\s``` и ```\S``` - это первый пробельный (табуляционный , новой строки) символ, и отрицание (не первый пробельный ....)
* ```\d``` и ```\D``` - это ```[0-9]``` и ```[^0-9]```