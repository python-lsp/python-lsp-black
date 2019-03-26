from pathlib import Path

import black
import pytest
from pyls.workspace import Document

from pyls_black.plugin import load_config, pyls_format_document, pyls_format_range

here = Path(__file__).parent
fixtures_dir = here / "fixtures"


@pytest.fixture
def unformatted_document():
    path = fixtures_dir / "unformatted.txt"
    uri = f"file:/{path}"
    return Document(uri)


@pytest.fixture
def unformatted_pyi_document():
    path = fixtures_dir / "unformatted.pyi"
    uri = f"file:/{path}"
    return Document(uri)


@pytest.fixture
def formatted_document():
    path = fixtures_dir / "formatted.txt"
    uri = f"file:/{path}"
    return Document(uri)


@pytest.fixture
def formatted_pyi_document():
    path = fixtures_dir / "formatted.pyi"
    uri = f"file:/{path}"
    return Document(uri)


@pytest.fixture
def invalid_document():
    path = fixtures_dir / "invalid.txt"
    uri = f"file:/{path}"
    return Document(uri)


@pytest.fixture
def config_document():
    path = fixtures_dir / "config" / "config.txt"
    uri = f"file:/{path}"
    return Document(uri)


def test_pyls_format_document(unformatted_document, formatted_document):
    result = pyls_format_document(unformatted_document)

    assert result == [
        {
            "range": {
                "start": {"line": 0, "character": 0},
                "end": {"line": 2, "character": 0},
            },
            "newText": formatted_document.source,
        }
    ]


def test_pyls_format_pyi_document(unformatted_pyi_document, formatted_pyi_document):
    result = pyls_format_document(unformatted_pyi_document)

    assert result == [
        {
            "range": {
                "start": {"line": 0, "character": 0},
                "end": {"line": 5, "character": 0},
            },
            "newText": formatted_pyi_document.source,
        }
    ]


def test_pyls_format_document_unchanged(formatted_document):
    result = pyls_format_document(formatted_document)

    assert result == []


def test_pyls_format_pyi_document_unchanged(formatted_pyi_document):
    result = pyls_format_document(formatted_pyi_document)

    assert result == []


def test_pyls_format_document_syntax_error(invalid_document):
    result = pyls_format_document(invalid_document)

    assert result == []


def test_pyls_format_document_with_config(config_document):
    result = pyls_format_document(config_document)

    assert result == [
        {
            "range": {
                "start": {"line": 0, "character": 0},
                "end": {"line": 1, "character": 0},
            },
            "newText": (
                "run(\n"
                "    these,\n"
                "    arguments,\n"
                "    should,\n"
                "    be,\n"
                "    wrapped,\n"
                ")\n"
            ),
        }
    ]


@pytest.mark.parametrize(
    ("start", "end", "expected"),
    [(0, 0, 'a = "hello"\n'), (1, 1, "b = 42\n"), (0, 1, 'a = "hello"\nb = 42\n')],
)
def test_pyls_format_range(unformatted_document, start, end, expected):
    range = {
        "start": {"line": start, "character": 0},
        "end": {"line": end, "character": 0},
    }

    result = pyls_format_range(unformatted_document, range=range)

    assert result == [
        {
            "range": {
                "start": {"line": start, "character": 0},
                "end": {"line": end + 1, "character": 0},
            },
            "newText": expected,
        }
    ]


def test_pyls_format_range_unchanged(formatted_document):
    range = {"start": {"line": 0, "character": 0}, "end": {"line": 1, "character": 0}}

    result = pyls_format_range(formatted_document, range=range)

    assert result == []


def test_pyls_format_range_syntax_error(invalid_document):
    range = {"start": {"line": 0, "character": 0}, "end": {"line": 1, "character": 0}}

    result = pyls_format_range(invalid_document, range=range)

    assert result == []


def test_load_config():
    config = load_config(str(fixtures_dir / "config" / "example.py"))

    # TODO split into smaller tests
    assert config == {
        "line_length": 20,
        "target_version": set(),
        "pyi": True,
        "fast": True,
        "skip_string_normalization": True,
    }


def test_load_config_target_version():
    config = load_config(str(fixtures_dir / "target_version" / "example.py"))

    assert config["target_version"] == {black.TargetVersion.PY27}


def test_load_config_py36():
    config = load_config(str(fixtures_dir / "py36" / "example.py"))

    assert config["target_version"] == black.PY36_VERSIONS


def test_load_config_defaults():
    config = load_config(str(fixtures_dir / "example.py"))

    assert config == {
        "line_length": 88,
        "target_version": set(),
        "pyi": False,
        "fast": False,
        "skip_string_normalization": False,
    }
