# Standard library imports
import types
from pathlib import Path
from unittest.mock import Mock

# Third-party imports
import black
import pkg_resources
import pytest

# Python LSP imports
from pylsp import uris
from pylsp.config.config import Config
from pylsp.workspace import Document, Workspace

# Local imports
from pylsp_black.plugin import (
    _load_config,
    load_config,
    pylsp_format_document,
    pylsp_format_range,
)

here = Path(__file__).parent
fixtures_dir = here / "fixtures"


@pytest.fixture
def workspace(tmpdir):
    """Return a workspace."""
    return Workspace(uris.from_fs_path(str(tmpdir)), Mock())


@pytest.fixture
def config(workspace):
    """Return a config object."""
    cfg = Config(workspace.root_uri, {}, 0, {})
    cfg._plugin_settings = {
        "plugins": {"black": {"line_length": 88, "cache_config": False}}
    }
    return cfg


@pytest.fixture
def config_with_skip_options(workspace):
    """Return a config object."""
    cfg = Config(workspace.root_uri, {}, 0, {})
    cfg._plugin_settings = {
        "plugins": {
            "black": {
                "line_length": 88,
                "cache_config": False,
                "skip_string_normalization": True,
                "skip_magic_trailing_comma": True,
            }
        }
    }
    return cfg


@pytest.fixture
def unformatted_document(workspace):
    path = fixtures_dir / "unformatted.txt"
    uri = f"file:/{path}"
    return Document(uri, workspace)


@pytest.fixture
def unformatted_pyi_document(workspace):
    path = fixtures_dir / "unformatted.pyi"
    uri = f"file:/{path}"
    return Document(uri, workspace)


@pytest.fixture
def unformatted_crlf_document(workspace):
    path = fixtures_dir / "unformatted-crlf.py"
    uri = f"file:/{path}"
    with open(path, "r", newline="") as f:
        source = f.read()
    return Document(uri, workspace, source=source)


@pytest.fixture
def formatted_document(workspace):
    path = fixtures_dir / "formatted.txt"
    uri = f"file:/{path}"
    return Document(uri, workspace)


@pytest.fixture
def formatted_pyi_document(workspace):
    path = fixtures_dir / "formatted.pyi"
    uri = f"file:/{path}"
    return Document(uri, workspace)


@pytest.fixture
def formatted_crlf_document(workspace):
    path = fixtures_dir / "formatted-crlf.py"
    uri = f"file:/{path}"
    with open(path, "r", newline="") as f:
        source = f.read()
    return Document(uri, workspace, source=source)


@pytest.fixture
def invalid_document(workspace):
    path = fixtures_dir / "invalid.txt"
    uri = f"file:/{path}"
    return Document(uri, workspace)


@pytest.fixture
def config_document(workspace):
    path = fixtures_dir / "config" / "config.txt"
    uri = f"file:/{path}"
    return Document(uri, workspace)


@pytest.fixture
def unformatted_line_length(workspace):
    path = fixtures_dir / "unformatted-line-length.py"
    uri = f"file:/{path}"
    return Document(uri, workspace)


@pytest.fixture
def formatted_line_length(workspace):
    path = fixtures_dir / "formatted-line-length.py"
    uri = f"file:/{path}"
    return Document(uri, workspace)


def test_pylsp_format_document(config, unformatted_document, formatted_document):
    result = pylsp_format_document(config, unformatted_document)

    assert result == [
        {
            "range": {
                "start": {"line": 0, "character": 0},
                "end": {"line": 2, "character": 0},
            },
            "newText": formatted_document.source,
        }
    ]


def test_pyls_format_pyi_document(
    config, unformatted_pyi_document, formatted_pyi_document
):
    result = pylsp_format_document(config, unformatted_pyi_document)

    assert result == [
        {
            "range": {
                "start": {"line": 0, "character": 0},
                "end": {"line": 5, "character": 0},
            },
            "newText": formatted_pyi_document.source,
        }
    ]


def test_pylsp_format_document_unchanged(config, formatted_document):
    result = pylsp_format_document(config, formatted_document)

    assert result == []


def test_pyls_format_pyi_document_unchanged(config, formatted_pyi_document):
    result = pylsp_format_document(config, formatted_pyi_document)

    assert result == []


def test_pylsp_format_document_syntax_error(config, invalid_document):
    result = pylsp_format_document(config, invalid_document)

    assert result == []


def test_pylsp_format_document_with_config(config, config_document):
    result = pylsp_format_document(config, config_document)

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
def test_pylsp_format_range(config, unformatted_document, start, end, expected):
    range = {
        "start": {"line": start, "character": 0},
        "end": {"line": end, "character": 0},
    }

    result = pylsp_format_range(config, unformatted_document, range=range)

    assert result == [
        {
            "range": {
                "start": {"line": start, "character": 0},
                "end": {"line": end + 1, "character": 0},
            },
            "newText": expected,
        }
    ]


def test_pylsp_format_range_unchanged(config, formatted_document):
    range = {"start": {"line": 0, "character": 0}, "end": {"line": 1, "character": 0}}

    result = pylsp_format_range(config, formatted_document, range=range)

    assert result == []


def test_pylsp_format_range_syntax_error(config, invalid_document):
    range = {"start": {"line": 0, "character": 0}, "end": {"line": 1, "character": 0}}

    result = pylsp_format_range(config, invalid_document, range=range)

    assert result == []


def test_load_config(config):
    config = load_config(str(fixtures_dir / "config" / "example.py"), config)

    # TODO split into smaller tests
    assert config == {
        "line_length": 20,
        "target_version": set(),
        "pyi": True,
        "fast": True,
        "skip_magic_trailing_comma": True,
        "skip_string_normalization": True,
        "preview": True,
    }


def test_load_config_target_version(config):
    config = load_config(str(fixtures_dir / "target_version" / "example.py"), config)

    assert config["target_version"] == {black.TargetVersion.PY39}


def test_load_config_py36(config):
    config = load_config(str(fixtures_dir / "py36" / "example.py"), config)

    assert config["target_version"] == {
        black.TargetVersion.PY36,
        black.TargetVersion.PY37,
        black.TargetVersion.PY38,
        black.TargetVersion.PY39,
        black.TargetVersion.PY310,
    }


def test_load_config_defaults(config):
    config = load_config(str(fixtures_dir / "example.py"), config)

    assert config == {
        "line_length": 88,
        "target_version": set(),
        "pyi": False,
        "fast": False,
        "skip_magic_trailing_comma": False,
        "skip_string_normalization": False,
        "preview": False,
    }


def test_load_config_with_skip_options(config_with_skip_options):
    config = load_config(
        str(fixtures_dir / "skip_options" / "example.py"), config_with_skip_options
    )

    assert config == {
        "line_length": 88,
        "target_version": set(),
        "pyi": False,
        "fast": False,
        "skip_magic_trailing_comma": True,
        "skip_string_normalization": True,
        "preview": False,
    }


def test_entry_point():
    distribution = pkg_resources.get_distribution("python-lsp-black")
    entry_point = distribution.get_entry_info("pylsp", "pylsp_black")

    assert entry_point is not None

    module = entry_point.load()
    assert isinstance(module, types.ModuleType)


def test_pylsp_format_crlf_document(
    config, unformatted_crlf_document, formatted_crlf_document
):
    result = pylsp_format_document(config, unformatted_crlf_document)

    assert result == [
        {
            "range": {
                "start": {"line": 0, "character": 0},
                "end": {"line": 4, "character": 0},
            },
            "newText": formatted_crlf_document.source,
        }
    ]


def test_pylsp_format_line_length(
    config, unformatted_line_length, formatted_line_length
):
    config.update({"plugins": {"black": {"line_length": 79}}})
    result = pylsp_format_document(config, unformatted_line_length)

    assert result == [
        {
            "range": {
                "start": {"line": 0, "character": 0},
                "end": {"line": 3, "character": 0},
            },
            "newText": formatted_line_length.source,
        }
    ]


def test_cache_config(config, unformatted_document):
    # Cache should be off by default
    for _ in range(5):
        pylsp_format_document(config, unformatted_document)
    assert _load_config.cache_info().hits == 0

    # Enable cache
    config.update({"plugins": {"black": {"cache_config": True}}})

    # Cache should be working now
    for _ in range(5):
        pylsp_format_document(config, unformatted_document)
    assert _load_config.cache_info().hits == 4
