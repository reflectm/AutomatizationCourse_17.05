## Лекция 1. Форматирование, линтелки, типы

* Запускается утилита ```autopep8```
* Установим в ручную ```pip install autopep8```
* Запуск прямой ```autopep8 --in-place --aggressive -v main.py```
* Запуск ```python -m autopep8 --in-place --aggressive -v main.py```

### Утилита black (форматирование кода)
* ```pip install black```
* Запуск ```black main.py```
* Запуск ```python -m black main.py```

### Утилита pylint (проверка семантики)
* ```pip install pylint```
* Запуск ```pylint main.py```
* Запуск ```python -m pylint main.py```

### Утилита docformatter (форматирование только строк документации)
* ```pip install docformatter```
* Запуск ```docformatter -i main.py```
* Запуск ```python -m docformatter -i main.py```
* Здесь ```-i``` означает (inplace)

### Про менеджмент зависимостей 
* Рекомендую ознакомиться с пакетом ```depend```

### Утилита isort (форматирование только строк импорта)
* ```isort``` группирует импорты и раскладывает их по стандарту (в алфвитном порядке в 3 группы)
* ```pip install isort```
* Запуск ```isort app.py```
* Запуск ```python -m isort app.py```

### Утилита mypy (проверка аннотированных сопоставлений)
* ```pip install mypy```
* Запуск ```mypy app.py```
* Запуск ```python -m mypy app.py```

### Автоматизация применения линтелок
* ```make```
* Создадим простой ```Makefile```
```
.PHONY: format, lint, check

format:
	black app.py && isort app.py && docformatter -i app.py

lint:
	pylint app.py

check:
	mypy app.py

.DEFAULT_GOAL := format
```

* Посмортите на флажок ```-r``` у каждой утилиты (```-r``` - рекурсивный!)