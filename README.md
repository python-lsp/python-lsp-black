# pyls-black

> [Black](https://github.com/ambv/black) plugin for the [Python Language Server](https://github.com/palantir/python-language-server/tree/develop/pyls).

```shell
pip3 install pyls-black
```

`pyls-black` can either format an entire file or just the selected text.
The code will only be formatted if it is syntactically valid Python.
Text selections are treated as if they were a separate Python file.
Note that this means you can't format an indented block of code.

## TODO

* Add support for configuring the line length and fast flag.
