# History of changes

## Version 2.0.0 (2023-12-19)

### New features

* Add support to format indented selections of code. This requires Black 23.11.0+
* Change entrypoint name to be `black`. This changes the options namespace for
  this plugin from `pylsp.pylsp_black` to `pylsp.black`.
* Drop support for Python 3.7.

### Issues Closed

* [Issue 42](https://github.com/python-lsp/python-lsp-black/issues/42) - Ineffective range formatting ([PR 52](https://github.com/python-lsp/python-lsp-black/pull/52) by [@remisalmon](https://github.com/remisalmon))
* [Issue 41](https://github.com/python-lsp/python-lsp-black/issues/41) - Configuration key and plugin name mismatch ([PR 39](https://github.com/python-lsp/python-lsp-black/pull/39) by [@chantera](https://github.com/chantera))

In this release 2 issues were closed.

### Pull Requests Merged

* [PR 53](https://github.com/python-lsp/python-lsp-black/pull/53) - Drop support for Python 3.7, by [@ccordoba12](https://github.com/ccordoba12)
* [PR 52](https://github.com/python-lsp/python-lsp-black/pull/52) - Use new `lines` option in Black 23.11 to format range, by [@remisalmon](https://github.com/remisalmon) ([42](https://github.com/python-lsp/python-lsp-black/issues/42))
* [PR 49](https://github.com/python-lsp/python-lsp-black/pull/49) - Read skip options from plugin settings, by [@seruman](https://github.com/seruman)
* [PR 39](https://github.com/python-lsp/python-lsp-black/pull/39) - Change entrypoint name to simply be `black`, by [@chantera](https://github.com/chantera) ([41](https://github.com/python-lsp/python-lsp-black/issues/41))

In this release 4 pull requests were closed.

## Version 1.3.0 (2023/05/19)

### Issues Closed

* [Issue 36](https://github.com/python-lsp/python-lsp-black/issues/36) - python-lsp-black ignores skip-magic-trailing-comma in .config/black ([PR 37](https://github.com/python-lsp/python-lsp-black/pull/37) by [@wstevick](https://github.com/wstevick))
* [Issue 35](https://github.com/python-lsp/python-lsp-black/issues/35) - python-lsp-black does not respect black configurations

In this release 2 issues were closed.

### Pull Requests Merged

* [PR 47](https://github.com/python-lsp/python-lsp-black/pull/47) - direnv support, by [@haplo](https://github.com/haplo)
* [PR 46](https://github.com/python-lsp/python-lsp-black/pull/46) - Add Python 3.11, drop 3.7 from test matrix, by [@haplo](https://github.com/haplo)
* [PR 45](https://github.com/python-lsp/python-lsp-black/pull/45) - Test preview and skip-magic-trailing-comma config parsing, by [@haplo](https://github.com/haplo)
* [PR 44](https://github.com/python-lsp/python-lsp-black/pull/44) - pre-commit autoupdate, by [@haplo](https://github.com/haplo)
* [PR 40](https://github.com/python-lsp/python-lsp-black/pull/40) - Replace the obsolete toml package with tomllib/tomli, by [@mgorny](https://github.com/mgorny)
* [PR 38](https://github.com/python-lsp/python-lsp-black/pull/38) - Added missing `preview` kwarg in `black.FileMode`. Fixes #35., by [@JesusTorrado](https://github.com/JesusTorrado)
* [PR 37](https://github.com/python-lsp/python-lsp-black/pull/37) - Add the possibility to configure skip-magic-trailing-comma, by [@wstevick](https://github.com/wstevick) ([36](https://github.com/python-lsp/python-lsp-black/issues/36))

In this release 7 pull requests were closed.

## Version 1.2.1 (2022-04-12)

### Pull Requests Merged

* [PR 34](https://github.com/python-lsp/python-lsp-black/pull/34) - Disable Autopep8 and Yapf if this plugin is installed, by [@bageljrkhanofemus](https://github.com/bageljrkhanofemus)

In this release 1 pull request was closed.

## Version 1.2.0 (2022-03-28)

### Issues Closed

* [Issue 24](https://github.com/python-lsp/python-lsp-black/issues/24) - Option to cache black configuration per-file

In this release 1 issue was closed.

### Pull Requests Merged

* [PR 33](https://github.com/python-lsp/python-lsp-black/pull/33) - Update pre-commit hooks' versions, by [@haplo](https://github.com/haplo)
* [PR 32](https://github.com/python-lsp/python-lsp-black/pull/32) - Fix PyPI badge in Readme, by [@ccordoba12](https://github.com/ccordoba12)
* [PR 28](https://github.com/python-lsp/python-lsp-black/pull/28) - Correctly format files and ranges with line endings other than LF, by [@ccordoba12](https://github.com/ccordoba12)
* [PR 26](https://github.com/python-lsp/python-lsp-black/pull/26) - Add client side configuration and cache configuration per file, by [@haplo](https://github.com/haplo)

In this release 4 pull requests were closed.

## Version 1.1.0 (2022-01-30)

### Issues Closed

* [Issue 29](https://github.com/python-lsp/python-lsp-black/issues/29) - TypeError when formatting with Black 22.1 ([PR 30](https://github.com/python-lsp/python-lsp-black/pull/30) by [@wlcx](https://github.com/wlcx))
* [Issue 25](https://github.com/python-lsp/python-lsp-black/issues/25) - Support global config file for black ([PR 19](https://github.com/python-lsp/python-lsp-black/pull/19) by [@jdost](https://github.com/jdost))

In this release 2 issues were closed.

### Pull Requests Merged

* [PR 30](https://github.com/python-lsp/python-lsp-black/pull/30) - Fix TypeError when formatting with black 22.1.0+, by [@wlcx](https://github.com/wlcx) ([29](https://github.com/python-lsp/python-lsp-black/issues/29))
* [PR 19](https://github.com/python-lsp/python-lsp-black/pull/19) - Support global config as a fallback, by [@jdost](https://github.com/jdost) ([25](https://github.com/python-lsp/python-lsp-black/issues/25))

In this release 2 pull requests were closed.

## Version 1.0.1 (2021-12-01)

### Issues Closed

* [Issue 20](https://github.com/python-lsp/python-lsp-black/issues/20) - Formatting fails silently
* [Issue 12](https://github.com/python-lsp/python-lsp-black/issues/12) - Fix MyPy linting
* [Issue 9](https://github.com/python-lsp/python-lsp-black/issues/9) - Ignore virtualenv in linters
* [Issue 8](https://github.com/python-lsp/python-lsp-black/issues/8) - Add Development section to README
* [Issue 7](https://github.com/python-lsp/python-lsp-black/issues/7) - Add pre-commit checks

In this release 5 issues were closed.

### Pull Requests Merged

* [PR 23](https://github.com/python-lsp/python-lsp-black/pull/23) - Add pre-commit hooks, by [@haplo](https://github.com/haplo)
* [PR 22](https://github.com/python-lsp/python-lsp-black/pull/22) - Log black errors to stderr, by [@haplo](https://github.com/haplo) ([20](https://github.com/python-lsp/python-lsp-black/issues/20))
* [PR 14](https://github.com/python-lsp/python-lsp-black/pull/14) - Add virtualenv to gitignore and Python 3.9 to black target versions, by [@haplo](https://github.com/haplo)
* [PR 13](https://github.com/python-lsp/python-lsp-black/pull/13) - Install MyPy stubs, by [@haplo](https://github.com/haplo) ([12](https://github.com/python-lsp/python-lsp-black/issues/12))
* [PR 11](https://github.com/python-lsp/python-lsp-black/pull/11) - Add Development section to README, by [@haplo](https://github.com/haplo) ([8](https://github.com/python-lsp/python-lsp-black/issues/8))
* [PR 10](https://github.com/python-lsp/python-lsp-black/pull/10) - Exclude venv and other directories from linters, by [@haplo](https://github.com/haplo) ([9](https://github.com/python-lsp/python-lsp-black/issues/9))

In this release 6 pull request was closed.

## Version 1.0.0 (2021/05/18)

### Issues Closed

- [Issue 3](https://github.com/python-lsp/python-lsp-black/issues/3) - Update README and add RELEASE instructions
- [Issue 2](https://github.com/python-lsp/python-lsp-black/issues/2) - Release v1.0.0

In this release 2 issues were closed.

### Pull Requests Merged

- [PR 1](https://github.com/python-lsp/python-lsp-black/pull/1) - PR: Python LSP server migration, by [@andfoy](https://github.com/andfoy)

In this release 1 pull request was closed.
