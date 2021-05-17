"""
Напишем простейшую программу, которая будет
помещать в выходной файл квадрат, состоящий из символов
* размер квадрта и символы, из которых его рисовать - возьмем из файла input.txt
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


def main():
    """
    Входная точка в приложение
    """
    # Получаем путь до файла
    with FileManager("input.txt", "output.txt") as handlers:
        input_handler, output_handler = handlers
        symbol, number = input_handler.readline().strip(), int(input_handler.readline().strip())

        for i in range(0, number - 1):
            line = symbol * number + '\n'
            output_handler.write(line)
        output_handler.write(symbol * number)


    

if __name__ == '__main__':
    main()