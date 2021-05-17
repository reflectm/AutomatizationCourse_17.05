"""
Модуль, сравнивающий размеры файлового объекта и исходника
"""
from pathlib import Path

pure_file_handler_object = open("large.txt" , "r")

print(f"Size of pure file handler object is {pure_file_handler_object.__sizeof__()} bytes") # Сколько байт занимает файловый обхект?
print(f"Size of file {Path('large.txt').stat().st_size } bytes") # Сколько байт занимает исходный файл в ОС?

pure_file_handler_object.close()