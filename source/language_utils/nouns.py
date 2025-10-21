# liczba mnoga
def get_plural(noun):
    if noun in ("caffe", "te"):
        return noun
    if noun == "moglie":
        return "mogli"
    elif noun[-1] == 'o':
        return noun[:-1] + 'i'
    elif noun[-1] == 'a':
        return noun[:-1] + 'e'
    elif noun[-1] == 'e':
        return noun[:-1] + 'i'
    else:
        return noun

# metoda określająca liczbę i rodzaj rzeczownika
def define_gender(noun):
    if noun[-1] == 'o':
        return "m_s"
    elif noun[-1] == 'a':
        return "f_s"
    elif noun[-1] == 'i':
        if noun in ("madri", "moglii", "colazioni", "carni", "tigri"):
            return "f_p"
        else:
            return "m_p"
    elif noun[-1] == 'e':
        if noun in ("padre", "nipote", "pane", "caffe", "te", "sale", "cameriere", "ingegnere",
                "insegnante", "giornale", "attore", "sapone", "cane", "fiore", "elefante",
                "leone", "pesce", "fiume", "mare", "sole", "latte"):
            return "m_s"
        elif noun in ("madre", "moglie", "colazione", "carne", "tigre"):
            return "f_s"
        else:
            return "f_p"
    else:
        return "m_s"