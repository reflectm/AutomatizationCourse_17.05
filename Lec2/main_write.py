"""
Запись в файл
* .write(arg)  - записывает строку arg
* .writelines(Lst[atg]) - записывает список строк arg
* 'w' - режим работы на перезапись
* 'a' - режим работы на дозапись
"""

file_handler = open("output.txt", "a")
file_handler.write("Hello world!" + '\n')
file_handler.write("Second line!" + '\n')
names = ["Alice", "Bob", "George"]

for  i in range(len(names[:-1])):
    names[i] += '\n'

file_handler.writelines(names)
file_handler.close()