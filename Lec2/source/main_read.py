"""Модуль для работы с файлами расширения .txt.

* .read() - считывает все содержимое файла от начала до конца
* по сути, в контексте одного файлового объекта происходит установка метки,
где было завершено предыдущее считывание
* не забываем закрывать файловый объект!
"""
file_handler = open("input.txt", mode="r")  # Файловый объект (хранит набор ссылок!)
print(file_handler.read())  # Считываем все содержимое файла в виде одной строки!
# """
# Alice
# Bob
# Alla
# George
# """
print("Another one file:", file_handler.read())
file_handler.close()

new_file_handler = open("input.txt", "r")
print("New file handler:", new_file_handler.read())
new_file_handler.close()
