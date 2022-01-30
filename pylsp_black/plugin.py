import logging
import os
from pathlib import Path
from typing import Dict, Optional

import black
import toml
from pylsp import hookimpl

logger = logging.getLogger(__name__)

GLOBAL_CONFIG: Optional[Path] = None
try:
    if os.name == "nt":
        GLOBAL_CONFIG = Path.home() / ".black"
    elif "XDG_CONFIG_HOME" in os.environ:
        GLOBAL_CONFIG = Path(os.environ["XDG_CONFIG_HOME"]) / "black"
    else:
        GLOBAL_CONFIG = Path.home() / ".config" / "black"
except Exception as e:
    logger.error("Error determining black global config file path: %s", e)
else:
    if GLOBAL_CONFIG is not None and GLOBAL_CONFIG.exists():
        logger.info("Found black global config file at %s", GLOBAL_CONFIG)


@hookimpl(tryfirst=True)
def pylsp_format_document(document):
    return format_document(document)


@hookimpl(tryfirst=True)
def pylsp_format_range(document, range):
    range["start"]["character"] = 0
    range["end"]["line"] += 1
    range["end"]["character"] = 0
    return format_document(document, range)


def format_document(document, range=None):
    if range:
        start = range["start"]["line"]
        end = range["end"]["line"]
        text = "".join(document.lines[start:end])
    else:
        text = document.source
        range = {
            "start": {"line": 0, "character": 0},
            "end": {"line": len(document.lines), "character": 0},
        }

    config = load_config(document.path)

    try:
        formatted_text = format_text(text=text, config=config)
    except black.NothingChanged:
        # raised when the file is already formatted correctly
        return []

    return [{"range": range, "newText": formatted_text}]


def format_text(*, text, config):
    mode = black.FileMode(
        target_versions=config["target_version"],
        line_length=config["line_length"],
        is_pyi=config["pyi"],
        string_normalization=not config["skip_string_normalization"],
    )
    try:
        # will raise black.NothingChanged, we want to bubble that exception up
        return black.format_file_contents(text, fast=config["fast"], mode=mode)
    except (
        # raised when the file has syntax errors
        ValueError,
        # raised when the file being formatted has an indentation error
        IndentationError,
        # raised when black produces invalid Python code or formats the file
        # differently on the second pass
        AssertionError,
    ) as e:
        # errors will show on lsp stderr stream
        logger.error("Error formatting with black: %s", e)
        raise black.NothingChanged from e


def load_config(filename: str) -> Dict:
    defaults = {
        "line_length": 88,
        "fast": False,
        "pyi": filename.endswith(".pyi"),
        "skip_string_normalization": False,
        "target_version": set(),
    }

    root = black.find_project_root((filename,))

    # Black 22.1.0+ returns a tuple
    if isinstance(root, tuple):
        pyproject_filename = root[0] / "pyproject.toml"
    else:
        pyproject_filename = root / "pyproject.toml"

    if not pyproject_filename.is_file():
        if GLOBAL_CONFIG is not None and GLOBAL_CONFIG.exists():
            pyproject_filename = GLOBAL_CONFIG
            logger.info("Using global black config at %s", pyproject_filename)
        else:
            logger.info("Using defaults: %r", defaults)
            return defaults

    try:
        pyproject_toml = toml.load(str(pyproject_filename))
    except (toml.TomlDecodeError, OSError):
        logger.warning(
            "Error decoding pyproject.toml, using defaults: %r",
            defaults,
        )
        return defaults

    file_config = pyproject_toml.get("tool", {}).get("black", {})
    file_config = {
        key.replace("--", "").replace("-", "_"): value
        for key, value in file_config.items()
    }

    config = {
        key: file_config.get(key, default_value)
        for key, default_value in defaults.items()
    }

    if file_config.get("target_version"):
        target_version = set(
            black.TargetVersion[x.upper()] for x in file_config["target_version"]
        )
    elif file_config.get("py36"):
        target_version = {
            black.TargetVersion.PY36,
            black.TargetVersion.PY37,
            black.TargetVersion.PY38,
            black.TargetVersion.PY39,
        }
    else:
        target_version = set()

    config["target_version"] = target_version

    logger.info("Using config from %s: %r", pyproject_filename, config)

    return config
