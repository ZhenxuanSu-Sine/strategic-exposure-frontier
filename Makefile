.PHONY: install test run all
install:
	python -m pip install -e .

test:
	pytest -q

run:
	python scripts_run_all.py

all: install run test
