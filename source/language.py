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
    verbs = ["essere", "avere", "fare", "dire", "capire", "sapere", "spiegare", "uscire", "andare", "venire",
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
        elif noun in ("madre", "moglie", "colazione", "carne", "tigre"):
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

def get_present_tense(verb, data):
    person = data[0]
    n = data[1]

    if verb not in ("essere", "avere", "fare", "dire", "sapere", "andare", "venire",
                    "bere", "rimanere", "tradurre", "dare", "uscire"):
        if verb[-3] == 'a':
            if n == 1:
                if person == 1:
                    return verb[:-3] + "o"
                elif person == 2:
                    return verb[:-3] + "i"
                else:
                    return verb[:-3] + "a"
            elif n == 2:
                if person == 1:
                    return verb[:-3] + "iamo"
                elif person == 2:
                    return verb[:-3] + "ate"
                else:
                    return verb[:-3] + "ano"
        elif verb[-3] == 'e':
            if n == 1:
                if person == 1:
                    return verb[:-3] + "o"
                elif person == 2:
                    return verb[:-3] + "i"
                else:
                    return verb[:-3] + "e"
            elif n == 2:
                if person == 1:
                    return verb[:-3] + "iamo"
                elif person == 2:
                    return verb[:-3] + "ete"
                else:
                    return verb[:-3] + "ono"
        elif verb in ("capire", "preferire", "finire"):
            if n == 1:
                if person == 1:
                    return verb[:-3] + "isco"
                elif person == 2:
                    return verb[:-3] + "isci"
                else:
                    return verb[:-3] + "isce"
            elif n == 2:
                if person == 1:
                    return verb[:-3] + "iamo"
                elif person == 2:
                    return verb[:-3] + "ite"
                else:
                    return verb[:-3] + "iscono"
        elif verb[-3] == 'i':
            if n == 1:
                if person == 1:
                    return verb[:-3] + "o"
                elif person == 2:
                    return verb[:-3] + "i"
                else:
                    return verb[:-3] + "e"
            elif n == 2:
                if person == 1:
                    return verb[:-3] + "iamo"
                elif person == 2:
                    return verb[:-3] + "ite"
                else:
                    return verb[:-3] + "ono"
    else:
        return get_present_tense_irregular(verb, person, n)

def get_present_tense_irregular(verb, person, n):
    match verb:
        case "essere": return get_present_essere(person, n)
        case "avere": return get_present_avere(person, n)
        case "fare": return get_present_fare(person, n)
        case "dire": return get_present_dire(person, n)
        case "sapere": return get_present_sapere(person, n)
        case "uscire": return get_present_uscire(person, n)
        case "andare": return get_present_andare(person, n)
        case "venire": return get_present_venire(person, n)
        case "bere": return get_present_bere(person, n)
        case "rimanere": return get_present_rimanere(person, n)
        case "tradurre": return get_present_tradurre(person, n)

def get_present_essere(person, n):
    if n == 1:
        if person == 1:
            return "sono"
        elif person == 2:
            return "sei"
        else:
            return "e"
    elif n == 2:
        if person == 1:
            return "siamo"
        elif person == 2:
            return "siete"
        else:
            return "sono"

def get_present_avere(person, n):
    if n == 1:
        if person == 1:
            return "ho"
        elif person == 2:
            return "hai"
        else:
            return "ha"
    elif n == 2:
        if person == 1:
            return "abbiamo"
        elif person == 2:
            return "avete"
        else:
            return "hanno"

def get_present_fare(person, n):
    if n == 1:
        if person == 1:
            return "faccio"
        elif person == 2:
            return "fai"
        else:
            return "fa"
    elif n == 2:
        if person == 1:
            return "facciamo"
        elif person == 2:
            return "fate"
        else:
            return "fanno"

def get_present_dire(person, n):
    if n == 1:
        if person == 1:
            return "dico"
        elif person == 2:
            return "dici"
        else:
            return "dice"
    elif n == 2:
        if person == 1:
            return "diciamo"
        elif person == 2:
            return "dite"
        else:
            return "dicono"

def get_present_sapere(person, n):
    if n == 1:
        if person == 1:
            return "so"
        elif person == 2:
            return "sai"
        else:
            return "sa"
    elif n == 2:
        if person == 1:
            return "sappiamo"
        elif person == 2:
            return "sapete"
        else:
            return "sanno"

def get_present_uscire(person, n):
    if n == 1:
        if person == 1:
            return "esco"
        elif person == 2:
            return "esci"
        else:
            return "esce"
    elif n == 2:
        if person == 1:
            return "usciamo"
        elif person == 2:
            return "uscite"
        else:
            return "escono"

def get_present_andare(person, n):
    if n == 1:
        if person == 1:
            return "vado"
        elif person == 2:
            return "vai"
        else:
            return "va"
    elif n == 2:
        if person == 1:
            return "andiamo"
        elif person == 2:
            return "andate"
        else:
            return "vanno"

def get_present_venire(person, n):
    if n == 1:
        if person == 1:
            return "vengo"
        elif person == 2:
            return "vieni"
        else:
            return "viene"
    elif n == 2:
        if person == 1:
            return "veniamo"
        elif person == 2:
            return "venite"
        else:
            return "vengono"

def get_present_bere(person, n):
    if n == 1:
        if person == 1:
            return "bevo"
        elif person == 2:
            return "bevi"
        else:
            return "beve"
    elif n == 2:
        if person == 1:
            return "beviamo"
        elif person == 2:
            return "bevete"
        else:
            return "bevono"

def get_present_rimanere(person, n):
    if n == 1:
        if person == 1:
            return "rimango"
        elif person == 2:
            return "rimani"
        else:
            return "rimane"
    elif n == 2:
        if person == 1:
            return "rimaniamo"
        elif person == 2:
            return "rimanete"
        else:
            return "rimangono"

def get_present_tradurre(person, n):
    if n == 1:
        if person == 1:
            return "traduco"
        elif person == 2:
            return "traduci"
        else:
            return "traduce"
    elif n == 2:
        if person == 1:
            return "traduciamo"
        elif person == 2:
            return "traducete"
        else:
            return "traducono"

def get_past_tense(verb, data):
    person = data[0]
    n = data[1]
    gender = data[2]

    participio = get_participio_passato(verb)

    if verb in ("essere", "uscire", "andare", "venire", "salire", "rimanere", "morire", "nascere",
                "scendere", "correre", "accendere", "crescere", "tornare", "visitare", "partire", "pulire"):
        modal = get_present_essere(person, n)
        if gender == 2:
            participio = participio[:-1] + 'a'
    else:
        modal = get_present_avere(person, n)

    return modal + " " + participio

def get_participio_passato(verb):
    irregolari = {
        "essere": "stato",
        "fare": "fatto",
        "dire": "detto",
        "leggere": "letto",
        "scrivere": "scritto",
        "rompere": "rotto",
        "cuocere": "cotto",
        "tradurre": "tradotto",
        "mettere": "messo",
        "aprire": "aperto",
        "morire": "morto",
        "nascere": "nato",
        "prendere": "preso",
        "accendere": "acceso",
        "perdere": "perso",
        "correre": "corso",
        "vedere": "visto",
        "chiedere": "chiesto",
        "rispondere": "risposto",
        "chiudere": "chiuso",
        "venire": "venuto",
        "vincere": "vinto",
        "vivere": "vissuto",
        "bere": "bevuto",
    }

    if verb in irregolari.keys():
        return irregolari[verb]
    elif verb[-3] == 'a':
        return verb[:-3] + "ato"
    elif verb[-3] == 'e':
        return verb[:-3] + "uto"
    elif verb[-3] == 'i':
        return verb[:-3] + "ito"
