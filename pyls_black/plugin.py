import black
from pyls import hookimpl


@hookimpl
def pyls_format_document(document):
    return format_document(document)


@hookimpl
def pyls_format_range(document, range):
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

    try:
        formatted_text = format_text(text)
    except (ValueError, black.NothingChanged):
        return []

    return [{"range": range, "newText": formatted_text}]


def format_text(text):
    return black.format_file_contents(text, line_length=88, fast=False)
