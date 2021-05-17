## Лекция 2. Работа с файлами


### Шаг 1. Что же возвращает open()?
* Создадим достаточно большой текстовый файл ```large.txt```
```
"""
Модуль для генерации большого текстового файла
"""
SYMBOL = '#'
file_handler = open("large.txt", "w")

for i in range(1, 10000):
    file_handler.write(SYMBOL * i +'\n')

file_handler.close()
```

* Читаем и сравниваем размер исходника и файлового объекта!
```
"""
Модуль, сравнивающий размеры файлового объекта и исходника
"""
from pathlib import Path

pure_file_handler_object = open("large.txt" , "r")

print(f"Size of pure file handler object is {pure_file_handler_object.__sizeof__()} bytes") # Сколько байт занимает файловый обхект?
print(f"Size of file {Path('large.txt').stat().st_size } bytes") # Сколько байт занимает исходный файл в ОС?

pure_file_handler_object.close()
```

### Шаг 2. Кто такой with?
* ````with``` - это менеджер контекста. Провоцирует выполнение метода ```__enter__``` при инициалзиации контеста, и ```__exit___``` при выходе из контекста.

```
"""Попробуем выполнить простейшие операции с помощью with.

* with - менеджер контекста
* при инициализации контекста - вызывается метод __enter__ у контекстного объекта
* при завершении контекста - вызывается метод __exit__
"""


class FileManager:
    """Класс, описывающий FileManager.

    * input_path
    * output_path
    """

    def __init__(self, input_path: str, output_path: str):
        self.input_path = input_path
        self.output_path = output_path
        self.input_handler = None
        self.output_handler = None

    def __enter__(self):
        """Вызывается при помещении FileManger объекта в контекст."""
        self.input_handler = open(self.input_path, "r")
        self.output_handler = open(self.output_path, "w")
        return (self.input_handler, self.output_handler)

    def __exit__(self, *args):
        """Вызывается при выходе из контекста."""
        self.input_handler.close()
        self.output_handler.close()


with FileManager("input.txt", "output.txt") as handlers:
    input_handler, output_handler = handlers
    output_handler.write(input_handler.read())

```