def applyCoder(text, coder):
    """
    Applies the coder to the text. Returns the encoded text.

    text: string
    coder: dict with mappings of characters to shifted characters
    returns: text after mapping coder chars to original text
    """
    result = ''

    for c in text:
        if c in string.punctuation or c == ' ' or c.isdigit():
            result += c
        else:
            result += coder[c]

    return result
