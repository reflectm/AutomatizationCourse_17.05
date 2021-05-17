"""
Модуль для генерации большого текстового файла
"""
SYMBOL = '#'
file_handler = open("large.txt", "w")

for i in range(1, 10000):
    file_handler.write(SYMBOL * i +'\n')

file_handler.close()