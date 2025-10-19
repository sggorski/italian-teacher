# rzeczowniki
def get_nouns():
    nouns = ["parde", "madre", "genitori", "fratello", "sorella", "marito", "moglie", "bambino", "bambina", "figlio",
             "figlia", "zio", "zia", "nonno", "nonna", "nipote", "cibo", "colazione", "pranzo", "cena", "pane", "formaggio",
             "vino", "caffe", "latte", "te", "torta", "panino", "carne", "sale", "insalata", "frutta", "verdura", "piatto",
             "tavolo", "insegnante", "medico", "ingegnere", "cameriere", "commesso", "commessa", "segretario", "segretaria",
             "giornale", "congresso", "parlamento", "bandiera", "banca", "contanti", "soldi", "negozio", "mercato", "maglietta",
             "pantaloni", "scarpe", "borsa", "cappello", "cappotto", "vestito", "collana", "passatempi", "sport", "calcio",
             "pallavolo", "tennis", "spiaggia", "libro", "film", "attore", "attrice", "musica", "casa", "cucina", "bagno",
             "porta", "finestra", "scale", "letto", "orologio", "sapone", "specchio", "frigo", "macchina", "autobus",
             "bicicletta", "treno", "aeroplano", "barca", "ufficio", "fabbrica", "collega", "computer", "gatto", "cane",
             "pesce", "uccello", "cavallo", "leone", "tigre", "elefante", "orso", "natura", "albero", "fiore", "bosco",
             "fiume", "montagna", "lago", "mare", "terra", "cielo", "sole", "luna", "stella" "vento", "pioggia"
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

# czasowniki modalne
def get_modal_verbs():
    modal_verbs = ["volere", "dovere", "potere"]
    return modal_verbs

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