def buildCoder(shift):
    """
    Returns a dict that can apply a Caesar cipher to a letter.
    The cipher is defined by the shift value. Ignores non-letter characters
    like punctuation, numbers, and spaces.

    shift: 0 <= int < 26
    returns: dict
    """
    d = {}

    for i in range(len(string.ascii_lowercase)):
        s = (i + shift)  % 26
        c = string.ascii_lowercase[i]
        sc = string.ascii_lowercase[s]
        d[c] = sc
        d[c.upper()] = sc.upper()
 
    return d
