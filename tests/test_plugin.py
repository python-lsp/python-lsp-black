from pathlib import Path
from unittest.mock import Mock

import pytest
from pyls.workspace import Document

from pyls_black.plugin import pyls_format_document, pyls_format_range

here = Path(__file__).parent


@pytest.fixture
def unformatted_document():
    path = here / "unformatted.txt"
    uri = f"file:/{path}"
    return Document(uri)


@pytest.fixture
def formatted_document():
    path = here / "formatted.txt"
    uri = f"file:/{path}"
    return Document(uri)


@pytest.fixture
def invalid_document():
    path = here / "invalid.txt"
    uri = f"file:/{path}"
    return Document(uri)


def run(g, outcome):
    g.send(None)

    with pytest.raises(StopIteration):
        g.send(outcome)


def test_pyls_format_document(unformatted_document, formatted_document):
    mock = Mock()
    mock.get_result.return_value = None

    g = pyls_format_document(unformatted_document)
    run(g, mock)

    mock.force_result.assert_called_once_with(
        [
            {
                "range": {
                    "start": {"line": 0, "character": 0},
                    "end": {"line": 2, "character": 0},
                },
                "newText": formatted_document.source,
            }
        ]
    )


def test_pyls_format_document_with_result(unformatted_document):
    mock = Mock()
    mock.get_result.return_value = [
        {
            "range": {
                "start": {"line": 0, "character": 0},
                "end": {"line": 1, "character": 0},
            },
            "newText": "x = 1+2\n",
        }
    ]

    g = pyls_format_document(unformatted_document)
    run(g, mock)

    mock.force_result.assert_called_once_with(
        [
            {
                "range": {
                    "start": {"line": 0, "character": 0},
                    "end": {"line": 2, "character": 0},
                },
                "newText": "x = 1 + 2\n",
            }
        ]
    )


def test_pyls_format_document_unchanged(formatted_document):
    mock = Mock()
    mock.get_result.return_value = None

    g = pyls_format_document(formatted_document)
    run(g, mock)

    mock.force_result.assert_not_called()


def test_pyls_format_document_supresses_syntax_errors(invalid_document):
    mock = Mock()
    mock.get_result.return_value = None

    g = pyls_format_document(invalid_document)
    run(g, mock)

    mock.force_result.assert_not_called()


@pytest.mark.parametrize(
    ("start", "end", "expected"),
    [(0, 0, 'a = "hello"\n'), (1, 1, "b = 42\n"), (0, 1, 'a = "hello"\nb = 42\n')],
)
def test_pyls_format_range(unformatted_document, start, end, expected):
    range = {
        "start": {"line": start, "character": 0},
        "end": {"line": end, "character": 0},
    }

    mock = Mock()
    mock.get_result.return_value = None

    g = pyls_format_range(unformatted_document, range=range)
    run(g, mock)

    mock.force_result.assert_called_once_with(
        [
            {
                "range": {
                    "start": {"line": start, "character": 0},
                    "end": {"line": end + 1, "character": 0},
                },
                "newText": expected,
            }
        ]
    )


def test_pyls_format_range_with_result(unformatted_document):
    range = {"start": {"line": 0, "character": 0}, "end": {"line": 0, "character": 0}}

    mock = Mock()
    mock.get_result.return_value = [
        {
            "range": {
                "start": {"line": 0, "character": 0},
                "end": {"line": 2, "character": 0},
            },
            "newText": "x = 1+2\ny = 3+4\n",
        }
    ]

    g = pyls_format_range(unformatted_document, range=range)
    run(g, mock)

    mock.force_result.assert_called_once_with(
        [
            {
                "range": {
                    "start": {"line": 0, "character": 0},
                    "end": {"line": 1, "character": 0},
                },
                "newText": "x = 1 + 2\n",
            }
        ]
    )


def test_pyls_format_range_unchanged(formatted_document):
    range = {"start": {"line": 0, "character": 0}, "end": {"line": 1, "character": 0}}

    mock = Mock()
    mock.get_result.return_value = None

    g = pyls_format_range(formatted_document, range=range)
    run(g, mock)

    mock.force_result.assert_not_called()
