# rzeczowniki
def get_nouns():
    nouns = ["parde", "madre", "genitori", "fratello", "sorella", "marito", "moglie", "bambino", "bambina", "figlio",
             "figlia", "zio", "zia", "nonno", "nonna", "nipote", "cibo", "colazione", "pranzo", "cena", "pane", "formaggio",
             "vino", "caffe", "latte", "te", "torta", "panino", "carne", "sale", "insalata", "frutta", "verdura", "piatto",
             "tavolo", "insegnante", "medico", "ingegnere", "cameriere", "commesso", "commessa", "segretario", "segretaria",
             "giornale", "congresso", "parlamento", "bandiera", "banca", "contanti", "soldi", "negozio", "mercato", "maglietta",
             "pantaloni", "scarpe", "borsa", "cappello", "cappotto", "vestito", "collana", "passatempi", "sport", "calcio",
             "pallavolo", "tennis", "spiaggia", "libro", "film", "attore", "attrice", "musica", "casa", "cucina", "bagno",
             "porta", "finestra", "scala", "letto", "orologio", "sapone", "specchio", "frigo", "macchina", "autobus",
             "bicicletta", "treno", "aeroplano", "barca", "ufficio", "fabbrica", "collega", "computer", "gatto", "cane",
             "pesce", "uccello", "cavallo", "leone", "tigre", "elefante", "orso", "natura", "albero", "fiore", "bosco",
             "fiume", "montagna", "lago", "mare", "terra", "cielo", "sole", "luna", "stella", "vento", "pioggia"
    ]
    return nouns

# przymiotniki
def get_adjectives():
    adjectives = ["grande", "piccolo", "lungo", "corto", "buono", "cattivo", "freddo", "caldo", "bello", "bravo", "brutto",
                  "caro", "giovane", "vecchio", "nuovo", "stesso", "vero", "largo", "stretto", "alto", "basso", "pesante",
                  "leggero", "vicino", "lontano", "fantastico", "terribile", "tiepido", "morbido", "duro", "gentile", "aperto",
                  "chiuso", "divertente", "comico", "felice", "contento", "triste", "pazzo", "rapido", "lento", "facile",
                  "difficile", "importante", "inutile", "utile", "rosso", "verde", "bianco", "rosso", "verde", "bianco",
                  "nero", "giallo", "merrone", "arancione", "rosa", "viola", "blu", "rotondo", "quadrato", "sferico",
                  "soleggiato", "nuvoloso", "dolce", "salato", "aspro", "acerbo", "acido", "amaro", "pericoloso", "interessante",
                  "noioso", "forte", "debole", "malato", "ricco", "povero", "ordinato", "carino", "grasso", "magro", "elegante",
                  "altro", "primo", "dritto", "possibile", "generale", "presente", "maggiore", "minore", "naturale", "italiano",
                  "francese", "polaccho", "americano", "tedesco", "russo", "economico", "unico", "diverso", "reale"]
    return adjectives

# czasowniki
def get_verbs():
    verbs = ["essere", "avere", "fare", "dire", "capire", "sapere", "spiengare", "uscire", "andare", "venire",
             "preferire", "bere", "salire", "rimanere", "morire", "finire", "vedere", "leggere", "nascere",
             "chiedere", "rispondere", "conoscere", "mettere", "aprire", "perdere", "vivere", "cuocere",
             "scendere", "scrivere", "prendere", "rompere", "correre", "vincere", "tradurre", "chiudere",
             "accendere", "crescere", "spingere", "chiamare", "scusare", "mancare", "interessare", "sembrare",
             "amare", "odiare", "mangiare", "ascoltare", "parlare", "ordinare", "cercare", "pensare",
             "incontrare", "portare", "toccare", "guardare", "tornare", "trovare", "dare", "abitare",
             "sperare", "aspettare", "pranzare", "cenare", "telefonare", "comprare", "pagare", "entrare",
             "lavorare", "studiare", "mandare", "uscire", "lasciare", "salutare", "usare", "visitare",
             "camminare", "iniziare", "imparare", "cambiare", "guadagnare", "tirare", "invitare", "diventare",
             "giocare", "credere", "vendere", "ripetere", "godere", "dormire", "servire", "pregare", "partire", "pulire"]
    return verbs

# liczba mnoga
def get_plural(noun):
    if noun in ("caffe", "te"):
        return noun
    elif noun[-1] == 'o':
        return noun[:-1] + 'i'
    elif noun[-1] == 'a':
        return noun[:-1] + 'e'
    elif noun[-1] == 'e':
        return noun[:-1] + 'i'
    else:
        return noun

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
    elif noun[-1] == 'a':
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

# zaimek wskazujący bliski
def get_pronome_vicino(noun):
    if noun[0] in ('u','i','o','a','e'):
        return "quest'"
    elif noun[-1] == 'o':
        return "questo"
    elif noun[-1] == 'a':
        return "questa"
    elif noun[-1] == 'i':
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
    elif noun in ("madre", "moglie", "colazione", "cena", "carne", "tigre"):
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
    elif noun in ("madre", "moglie", "colazione", "cena", "carne", "tigre"):
        return "quella"
    else:
        return "quelle"

def define_gender(noun):
    if noun[-1] == 'o':
        return "m_s"
    elif noun[-1] == 'a':
        return "f_s"
    elif noun[-1] == 'i':
        return "m_p"
    elif noun[-1] == 'e':
        if noun in ("parde", "nipote", "pane", "caffe", "te", "sale", "cameriere", "ingegnere",
                "insegnante", "giornale", "attore", "sapone", "cane", "fiore", "elefante",
                "leone", "pesce", "fiume", "mare", "sole", "latte"):
            return "m_s"
        elif noun in ("madre", "moglie", "colazione", "cena", "carne", "tigre"):
            return "f_s"
        else:
            return "f_p"
    else:
        return "m_s"

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