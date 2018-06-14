from typing import NamedTuple

import black
from pyls import hookimpl


@hookimpl(hookwrapper=True)
def pyls_format_document(document):
    return format_document(document)


@hookimpl(hookwrapper=True)
def pyls_format_range(document, range):
    selection = Selection(start=range["start"]["line"], end=range["end"]["line"] + 1)
    return format_document(document, selection)


class Selection(NamedTuple):
    start: int
    end: int

    def to_range(self):
        return {
            "start": {"line": self.start, "character": 0},
            "end": {"line": self.end, "character": 0},
        }


def format_document(document, selection=None):
    outcome = yield

    result = outcome.get_result()

    if result:
        text = result[0]["newText"]
    else:
        text = document.source

    if selection:
        text = select_text(text, selection)
    else:
        selection = Selection(0, len(document.lines))

    try:
        formatted_text = format_text(text)
    except (ValueError, black.NothingChanged):
        return

    new_result = [{"range": selection.to_range(), "newText": formatted_text}]

    outcome.force_result(new_result)


def select_text(text, selection):
    lines = text.splitlines(True)
    return "".join(lines[selection.start : selection.end])


def format_text(text):
    return black.format_file_contents(text, line_length=88, fast=False)
