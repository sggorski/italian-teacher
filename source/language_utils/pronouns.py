from .nouns import *

# zaimek wskazujący bliski
def get_pronome_vicino(noun):
    if noun[0] in ('u','i','o','a','e'):
        return "quest'"
    elif noun[-1] == 'o':
        return "questo"
    elif noun[-1] == 'a':
        return "questa"
    elif noun[-1] == 'i':
        if noun in ("madri", "moglii", "colazioni", "carni", "tigri"):
            return "queste"
        return "questi"
    elif noun[-1] == 'e':
        return get_irregular_pronome_vicino(noun)
    else:
        return "questo"

# zaimek wskazujący bliski dla rzeczowników nieregularnych
def get_irregular_pronome_vicino(noun):
    if noun in ("parde", "nipote", "pane", "caffe", "te", "sale", "cameriere", "ingegnere",
                "insegnante", "giornale", "attore", "sapone", "cane", "fiore", "elefante",
                "leone", "pesce", "fiume", "mare", "sole", "latte"):
        return "questo"
    elif noun in ("madre", "moglie", "colazione", "carne", "tigre"):
        return "questa"
    else:
        return "queste"

# zaimek wskazujący daleki
def get_pronome_lontano(noun):
    if noun[0] in ('u','i','o','a','e'):
        return "quell'"
    elif noun[0] in ('x', 'z', 'y', 'j') or (noun[0] == 's' and noun[1] in ('t', 'p', 'c')) or (noun[0] == 'p' and noun[1] in ('n', 's')):
        return "quello"
    elif noun[-1] == 'o':
        return "quel"
    elif noun[-1] == 'a':
        return "quella"
    elif noun[-1] == 'i':
        if noun in ("madri", "moglii", "colazioni", "carni", "tigri"):
            return "quelle"
        return "quelli"
    elif noun[-1] == 'e':
        return get_irregular_pronome_lontano(noun)
    else:
        return "quel"

# zaimek wskazujący daleki dla rzeczowników nieregularnych
def get_irregular_pronome_lontano(noun):
    if noun in ("parde", "nipote", "pane", "caffe", "te", "sale", "cameriere", "ingegnere",
                "insegnante", "giornale", "attore", "sapone", "cane", "fiore", "elefante",
                "leone", "pesce", "fiume", "mare", "sole", "latte"):
        return "quel"
    elif noun in ("madre", "moglie", "colazione", "carne", "tigre"):
        return "quella"
    else:
        return "quelle"

# zaimki dzierżawcze
def get_possesive_pronoun(person, n, noun):
    noun_gender = define_gender(noun)
    if noun_gender == 'm_s':
        if n == 1:
            if person == 1:
                return "mio"
            elif person == 2:
                return "tuo"
            elif person == 3:
                return "suo"
        else:
            if person == 1:
                return "nostro"
            elif person == 2:
                return "vostro"
            elif person == 3:
                return "loro"
    elif noun_gender == 'f_s':
        if n == 1:
            if person == 1:
                return "mia"
            elif person == 2:
                return "tua"
            elif person == 3:
                return "sua"
        else:
            if person == 1:
                return "nostra"
            elif person == 2:
                return "vostra"
            elif person == 3:
                return "loro"
    elif noun_gender == 'm_p':
        if n == 1:
            if person == 1:
                return "miei"
            elif person == 2:
                return "tuoi"
            elif person == 3:
                return "suoi"
        else:
            if person == 1:
                return "nostri"
            elif person == 2:
                return "vostri"
            elif person == 3:
                return "loro"
    else:
        if n == 1:
            if person == 1:
                return "mie"
            elif person == 2:
                return "tue"
            elif person == 3:
                return "sue"
        else:
            if person == 1:
                return "nostre"
            elif person == 2:
                return "vostre"
            elif person == 3:
                return "loro"