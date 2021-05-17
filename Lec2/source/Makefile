.PHONY: format

format:
	black with_io.py && isort with_io.py && docformatter -i with_io.py

.DEFAULT_GOAL := format