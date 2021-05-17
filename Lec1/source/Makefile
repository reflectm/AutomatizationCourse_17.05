.PHONY: format, lint, check

format:
	black app.py && isort app.py && docformatter -i app.py

lint:
	pylint app.py

check:
	mypy app.py

.DEFAULT_GOAL := format