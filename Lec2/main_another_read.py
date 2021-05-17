"""
Считываем построчно из входного файла
* .readlines() - вычитывает также целиком весь файл, но возвращает список строк
* .readline() - вычитывает один блок , оканчивающийся `\n`
"""

file_handler = open("input.txt", "r")
words = file_handler.readlines() # Считвает все строки ('\n') и возвращает список строк
print([word.strip() for word in words]) # Отрезаем символы переноса на новую строку
file_handler.close()

# Итеративное построчное счтиывание из файла
new_file_handler = open("input.txt", "r")
line = new_file_handler.readline()
while line:
    print("Current line:", line.strip())
    line = new_file_handler.readline()

new_file_handler.close()