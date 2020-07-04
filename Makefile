lint: flake8 black-check isort-check mypy

flake8:
	flake8 .

black:
	black .

black-check:
	black --diff --check .

isort:
	isort .

isort-check:
	isort --check-only .

mypy:
	mypy .

test:
	pytest -v .

build: lint test
	python3 setup.py sdist bdist_wheel

test-upload:
	twine upload --repository-url https://test.pypi.org/legacy/ dist/*

upload:
	twine upload dist/*

clean:
	rm -rf dist

.PHONY: build
