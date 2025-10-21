# rodzajnik nieokreślony liczba pojedyncza
def get_articolo_undeterminativo_singular(noun):
    if noun[0] in ('x', 'z', 'y', 'j') or (noun[0] == 's' and noun[1] in ('t','p','c')) or (noun[0] == 'p' and noun[1] in ('n', 's')):
        return "uno"
    elif noun[-1] == 'a' and noun[0] in ('u','i','o','a','e'):
        return "un'"
    elif noun[-1] == 'a':
        return "una"
    else:
        return "un"

# rodzajnik nieokreślony liczba mnoga
def get_articolo_undeterminativo_plural(noun):
    if get_articolo_undeterminativo_singular(noun) == "uno":
        return "degli"
    elif get_articolo_undeterminativo_singular(noun) in ("una", "un'"):
        return "delle"
    elif get_articolo_undeterminativo_singular(noun) == "un" and noun[0] in ('u','i','o','a','e'):
        return "degli"
    else:
        return "dei"

# rodzajnik określony liczba pojedyncza
def get_articolo_determinativo_singular(noun):
    if noun[0] in ('x', 'z', 'y', 'j') or (noun[0] == 's' and noun[1] in ('t', 'p', 'c')) or (noun[0] == 'p' and noun[1] in ('n', 's')):
        return "lo"
    elif noun[0] in ('u','i','o','a','e'):
        return "l'"
    elif noun[-1] == 'a' or noun in ("madre", "moglie", "colazione", "carne", "tigre"):
        return "la"
    else:
        return "il"

# rodzajnik określony liczba mnoga
def get_articolo_determinativo_plural(noun):
    if get_articolo_determinativo_singular(noun) == "lo":
        return "gli"
    elif get_articolo_determinativo_singular(noun) == "la":
        return "le"
    elif get_articolo_determinativo_singular(noun) == "l'" and noun[-1] == 'o':
        return "gli"
    elif get_articolo_determinativo_singular(noun) == "l'" and noun[-1] == 'a':
        return "le"
    else:
        return "i"