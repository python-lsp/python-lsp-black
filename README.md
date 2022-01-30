# python-lsp-black

[![PyPI](https://img.shields.io/pypi/v/pyls-black.svg)](https://pypi.org/project/python-lsp-black) [![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Python](https://github.com/python-lsp/python-lsp-black/actions/workflows/python.yml/badge.svg)](https://github.com/python-lsp/python-lsp-black/actions/workflows/python.yml)

> [Black](https://github.com/psf/black) plugin for the [Python LSP Server](https://github.com/python-lsp/python-lsp-server).

## Install

In the same `virtualenv` as `python-lsp-server`:

```shell
pip install python-lsp-black
```

# Usage

To avoid unexpected results you should make sure `yapf` and `autopep8` are not installed.

- `python-lsp-black` can either format an entire file or just the selected text.
- The code will only be formatted if it is syntactically valid Python.
- Text selections are treated as if they were a separate Python file.
  Unfortunately this means you can't format an indented block of code.
- `python-lsp-black` will use your project's [pyproject.toml](https://github.com/psf/black#pyprojecttoml) if it has one.
- `python-lsp-black` only officially supports the latest stable version of [black](https://github.com/psf/black). An effort is made to keep backwards-compatibility but older black versions will not be actively tested.

# Development

To install the project for development you need to specify the dev optional dependencies:

```shell
python -m venv .venv
. .venv/bin/activate
pip install -e .[dev]
```

This project uses [pre-commit](https://pre-commit.com/) hooks to control code quality,
install them to run them when creating a git commit, thus avoiding seeing errors when you
create a pull request:

```shell
pre-commit install
```

To run tests:

```shell
make test
```

To run linters:

```shell
make lint  # just a shortcut to pre-commit run -a
make <linter_name>  # black, flake8, isort, mypy
```

To upgrade the version of the pre-commit hooks:

```shell
pre-commit autoupdate
# check and git commit changes to .pre-commit-config.yaml
```
