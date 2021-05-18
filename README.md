# python-lsp-black

[![PyPI](https://img.shields.io/pypi/v/pyls-black.svg)](https://pypi.org/project/python-lsp-black) [![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)
[![Python](https://github.com/python-lsp/python-lsp-black/actions/workflows/python.yml/badge.svg)](https://github.com/python-lsp/python-lsp-black/actions/workflows/python.yml)


> [Black](https://github.com/ambv/black) plugin for the [Python LSP Server](https://github.com/python-lsp/python-lsp-server).

In the same `virtualenv` as `python-lsp-server`:

```shell
pip install python-lsp-black
```

To avoid unexpected results you should make sure `yapf` and `autopep8` are not installed.

* `python-lsp-black` can either format an entire file or just the selected text.
* The code will only be formatted if it is syntactically valid Python.
* Text selections are treated as if they were a separate Python file.
  Unfortunately this means you can't format an indented block of code.
* `python-lsp-black` will use your project's [pyproject.toml](https://github.com/ambv/black#pyprojecttoml) if it has one.
