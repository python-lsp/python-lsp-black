# pyls-black

[![PyPI](https://img.shields.io/pypi/v/pyls-black.svg)](https://pypi.org/project/pyls-black/) [![CircleCI branch](https://img.shields.io/circleci/project/github/rupert/pyls-black/master.svg)](https://circleci.com/gh/rupert/pyls-black) ![Python 3.6](https://img.shields.io/badge/python-3.6-green.svg)

> [Black](https://github.com/ambv/black) plugin for the [Python Language Server](https://github.com/palantir/python-language-server).

```shell
pip3 install pyls-black
```

* `pyls-black` can either format an entire file or just the selected text.
* The code will only be formatted if it is syntactically valid Python.
* Text selections are treated as if they were a separate Python file.
  Unfortunately this means you can't format an indented block of code.
* `pyls-black` will use your project's [pyproject.toml](https://github.com/ambv/black#pyprojecttoml) if it has one.
