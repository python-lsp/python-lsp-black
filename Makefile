lint:
	pre-commit run -a

black:
	pre-commit run -a black

flake8:
	pre-commit run -a flake8

isort:
	pre-commit run -a isort

mypy:
	pre-commit run -a mypy

test:
	pytest -vv .

build: lint test
	python3 setup.py sdist bdist_wheel

test-upload:
	twine upload --repository-url https://test.pypi.org/legacy/ dist/*

upload:
	twine upload dist/*

clean:
	rm -rf dist

.PHONY: build
