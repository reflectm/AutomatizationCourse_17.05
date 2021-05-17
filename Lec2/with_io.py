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
