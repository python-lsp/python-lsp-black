# Eol chars accepted by the LSP protocol
EOL_CHARS = ["\r\n", "\r", "\n"]


def get_eol_chars(text):
    for eol_chars in EOL_CHARS:
        if text.find(eol_chars) > -1:
            break
    else:
        return None
    return eol_chars
