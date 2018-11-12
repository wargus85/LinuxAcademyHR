.PHONY: default install test

default: test

install:
	python3 -m pipenv install --dev --skip-lock

test:
	PYTHONPATH=./src pytest
