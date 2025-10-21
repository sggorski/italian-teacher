# czas teraźniejszy - presente
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

# odmiana czasowników nieregularnych w czasie teraźniejszym
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

# czas przeszły passato prossimo
def get_past_tense(verb, data):
    person = data[0]
    n = data[1]
    gender = data[2]

    participio = get_participio_passato(verb)

    if verb in ("essere", "uscire", "andare", "venire", "salire", "rimanere", "morire", "nascere",
                "scendere", "correre", "accendere", "crescere", "tornare", "visitare", "partire", "pulire"):
        modal = get_present_essere(person, n)
        if gender == 1 and n == 2:
            participio = participio[:-1] + 'i'
        elif gender == 2:
            if n == 1:
                participio = participio[:-1] + 'a'
            elif n == 2:
                participio = participio[:-1] + 'e'
    else:
        modal = get_present_avere(person, n)

    return modal + " " + participio

# forma przeszła głównego czasownika w passato prossimo w tym odmiana nieregularna
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

# czas przyszły futuro semplice
def get_future_tense(verb, data):
    person = data[0]
    n = data[1]

    if verb not in ("cercare", "pagare", "essere", "avere", "fare", "andare", "venire", "dare", "dire",
                    "rimanere", "vedere", "stare", "sapere"):
        if verb[-3] == 'a' or verb[-3] == 'e':
            if n == 1:
                if person == 1:
                    return verb[:-3] + "ero"
                elif person == 2:
                    return verb[:-3] + "erai"
                else:
                    return verb[:-3] + "era"
            elif n == 2:
                if person == 1:
                    return verb[:-3] + "eremo"
                elif person == 2:
                    return verb[:-3] + "erete"
                else:
                    return verb[:-3] + "eranno"
        elif verb[-3] == 'i':
            if n == 1:
                if person == 1:
                    return verb[:-3] + "iro"
                elif person == 2:
                    return verb[:-3] + "irai"
                else:
                    return verb[:-3] + "ira"
            elif n == 2:
                if person == 1:
                    return verb[:-3] + "iremo"
                elif person == 2:
                    return verb[:-3] + "irete"
                else:
                    return verb[:-3] + "iranno"
    else:
        return get_future_tense_irregular(verb, person, n)

# nieregularne formy przyszłe
def get_future_tense_irregular(verb, person, n):
    match verb:
        case "cercare": return get_future_cercare(person, n)
        case "pagare": return get_future_pagare(person, n)
        case "essere": return get_future_essere(person, n)
        case "avere": return get_future_avere(person, n)
        case "fare": return get_future_fare(person, n)
        case "andare": return get_future_andare(person, n)
        case "venire": return get_future_venire(person, n)
        case "dare": return get_future_dare(person, n)
        case "dire": return get_future_dire(person, n)
        case "rimanere": return get_future_rimanere(person, n)
        case "vedere": return get_future_vedere(person, n)
        case "stare": return get_future_stare(person, n)
        case "sapere": return get_future_sapere(person, n)

def get_future_cercare(person, n):
    if n == 1:
        if person == 1:
            return "cerchero"
        elif person == 2:
            return "cercherai"
        else:
            return "cerchera"
    elif n == 2:
        if person == 1:
            return "cercheremo"
        elif person == 2:
            return "cercherete"
        else:
            return "cercheranno"

def get_future_pagare(person, n):
    if n == 1:
        if person == 1:
            return "paghero"
        elif person == 2:
            return "pagherai"
        else:
            return "paghera"
    elif n == 2:
        if person == 1:
            return "pagheremo"
        elif person == 2:
            return "pagherete"
        else:
            return "pagheranno"

def get_future_essere(person, n):
    if n == 1:
        if person == 1:
            return "saro"
        elif person == 2:
            return "sarai"
        else:
            return "sara"
    elif n == 2:
        if person == 1:
            return "saremo"
        elif person == 2:
            return "sarete"
        else:
            return "saranno"

def get_future_avere(person, n):
    if n == 1:
        if person == 1:
            return "avro"
        elif person == 2:
            return "avrai"
        else:
            return "avra"
    elif n == 2:
        if person == 1:
            return "avremo"
        elif person == 2:
            return "avrete"
        else:
            return "avranno"

def get_future_fare(person, n):
    if n == 1:
        if person == 1:
            return "faro"
        elif person == 2:
            return "farai"
        else:
            return "fara"
    elif n == 2:
        if person == 1:
            return "faremo"
        elif person == 2:
            return "farete"
        else:
            return "faranno"

def get_future_andare(person, n):
    if n == 1:
        if person == 1:
            return "andro"
        elif person == 2:
            return "andrai"
        else:
            return "andra"
    elif n == 2:
        if person == 1:
            return "andremo"
        elif person == 2:
            return "andrete"
        else:
            return "andranno"

def get_future_venire(person, n):
    if n == 1:
        if person == 1:
            return "verro"
        elif person == 2:
            return "verrai"
        else:
            return "verra"
    elif n == 2:
        if person == 1:
            return "verremo"
        elif person == 2:
            return "verrete"
        else:
            return "verranno"

def get_future_dare(person, n):
    if n == 1:
        if person == 1:
            return "daro"
        elif person == 2:
            return "darai"
        else:
            return "dara"
    elif n == 2:
        if person == 1:
            return "daremo"
        elif person == 2:
            return "darete"
        else:
            return "daranno"

def get_future_dire(person, n):
    if n == 1:
        if person == 1:
            return "diro"
        elif person == 2:
            return "dirai"
        else:
            return "dira"
    elif n == 2:
        if person == 1:
            return "diremo"
        elif person == 2:
            return "direte"
        else:
            return "diranno"

def get_future_rimanere(person, n):
    if n == 1:
        if person == 1:
            return "rimarro"
        elif person == 2:
            return "rimarrai"
        else:
            return "rimarra"
    elif n == 2:
        if person == 1:
            return "rimarremo"
        elif person == 2:
            return "rimarrete"
        else:
            return "rimarranno"

def get_future_vedere(person, n):
    if n == 1:
        if person == 1:
            return "vedro"
        elif person == 2:
            return "vedrai"
        else:
            return "vedra"
    elif n == 2:
        if person == 1:
            return "vedremo"
        elif person == 2:
            return "vedrete"
        else:
            return "vedranno"

def get_future_stare(person, n):
    if n == 1:
        if person == 1:
            return "staro"
        elif person == 2:
            return "starai"
        else:
            return "stara"
    elif n == 2:
        if person == 1:
            return "staremo"
        elif person == 2:
            return "starete"
        else:
            return "staranno"

def get_future_sapere(person, n):
    if n == 1:
        if person == 1:
            return "sapro"
        elif person == 2:
            return "saprai"
        else:
            return "sapra"
    elif n == 2:
        if person == 1:
            return "sapremo"
        elif person == 2:
            return "saprete"
        else:
            return "sapranno"

# tryb przypuszczający prosty - czas teraźniejszy
def get_condizionale_simplice(verb, data):
    person = data[0]
    n = data[1]

    if verb not in ("essere", "avere", "fare", "stare", "dare", "andare", "vivere", "vedere", "venire",
                    "bere", "rimanere", "sapere"):
        if verb[-3] == 'a' or verb[-1] == 'e':
            if n == 1:
                if person == 1:
                    return verb[:-3] + "erei"
                elif person == 2:
                    return verb[:-3] + "eresti"
                else:
                    return verb[:-3] + "erebbe"
            elif n == 2:
                if person == 1:
                    return verb[:-3] + "eremmo"
                elif person == 2:
                    return verb[:-3] + "ereste"
                else:
                    return verb[:-3] + "erebbero"
        elif verb[-3] == 'i':
            if n == 1:
                if person == 1:
                    return verb[:-3] + "irei"
                elif person == 2:
                    return verb[:-3] + "iresti"
                else:
                    return verb[:-3] + "irebbe"
            elif n == 2:
                if person == 1:
                    return verb[:-3] + "iremmo"
                elif person == 2:
                    return verb[:-3] + "ireste"
                else:
                    return verb[:-3] + "irebbero"
    else:
        return get_condizionale_irregular(verb, person, n)

# tryb przypuszczający teraźniejszy - odmiana nieregularna
def get_condizionale_irregular(verb, person, n):
    match verb:
        case "essere": return get_condizionale_essere(person, n)
        case "avere": return get_condizionale_avere(person, n)
        case "fare": return get_condizionale_fare(person, n)
        case "andare": return get_condizionale_andare(person, n)
        case "venire": return get_condizionale_venire(person, n)
        case "vivere": return get_condizionale_vivere(person, n)
        case "dare": return get_condizionale_dare(person, n)
        case "rimanere": return get_condizionale_rimanere(person, n)
        case "vedere": return get_condizionale_vedere(person, n)
        case "stare": return get_condizionale_stare(person, n)
        case "sapere": return get_condizionale_sapere(person, n)
        case "bere": return get_condizionale_bere(person, n)

def get_condizionale_essere(person, n):
    if n == 1:
        if person == 1:
            return "sarei"
        elif person == 2:
            return "saresti"
        else:
            return "sarebbe"
    elif n == 2:
        if person == 1:
            return "saremmo"
        elif person == 2:
            return "sareste"
        else:
            return "sarebbero"

def get_condizionale_avere(person, n):
    if n == 1:
        if person == 1:
            return "avrei"
        elif person == 2:
            return "avresti"
        else:
            return "avrebbe"
    elif n == 2:
        if person == 1:
            return "avremmo"
        elif person == 2:
            return "avreste"
        else:
            return "avrebbero"

def get_condizionale_fare(person, n):
    if n == 1:
        if person == 1:
            return "farei"
        elif person == 2:
            return "faresti"
        else:
            return "farebbe"
    elif n == 2:
        if person == 1:
            return "faremmo"
        elif person == 2:
            return "fareste"
        else:
            return "farebbero"

def get_condizionale_andare(person, n):
    if n == 1:
        if person == 1:
            return "andrei"
        elif person == 2:
            return "andresti"
        else:
            return "andrebbe"
    elif n == 2:
        if person == 1:
            return "andremmo"
        elif person == 2:
            return "andreste"
        else:
            return "andrebbero"

def get_condizionale_venire(person, n):
    if n == 1:
        if person == 1:
            return "verrei"
        elif person == 2:
            return "verresti"
        else:
            return "verrebbe"
    elif n == 2:
        if person == 1:
            return "verremmo"
        elif person == 2:
            return "verreste"
        else:
            return "verrebbero"

def get_condizionale_vivere(person, n):
    if n == 1:
        if person == 1:
            return "vivrei"
        elif person == 2:
            return "vivresti"
        else:
            return "vivrebbe"
    elif n == 2:
        if person == 1:
            return "vivremmo"
        elif person == 2:
            return "vivreste"
        else:
            return "vivrebbero"

def get_condizionale_vedere(person, n):
    if n == 1:
        if person == 1:
            return "vedrei"
        elif person == 2:
            return "vedresti"
        else:
            return "vedrebbe"
    elif n == 2:
        if person == 1:
            return "vedremmo"
        elif person == 2:
            return "vedreste"
        else:
            return "vedrebbero"

def get_condizionale_dare(person, n):
    if n == 1:
        if person == 1:
            return "darei"
        elif person == 2:
            return "daresti"
        else:
            return "darebbe"
    elif n == 2:
        if person == 1:
            return "daremmo"
        elif person == 2:
            return "dareste"
        else:
            return "darebbero"

def get_condizionale_rimanere(person, n):
    if n == 1:
        if person == 1:
            return "rimarrei"
        elif person == 2:
            return "rimarresti"
        else:
            return "rimarrebbe"
    elif n == 2:
        if person == 1:
            return "rimarremmo"
        elif person == 2:
            return "rimarreste"
        else:
            return "rimarrebbero"

def get_condizionale_stare(person, n):
    if n == 1:
        if person == 1:
            return "starei"
        elif person == 2:
            return "staresti"
        else:
            return "starebbe"
    elif n == 2:
        if person == 1:
            return "staremmo"
        elif person == 2:
            return "stareste"
        else:
            return "starebbero"

def get_condizionale_sapere(person, n):
    if n == 1:
        if person == 1:
            return "saprei"
        elif person == 2:
            return "sapresti"
        else:
            return "saprebbe"
    elif n == 2:
        if person == 1:
            return "sapremmo"
        elif person == 2:
            return "sapreste"
        else:
            return "saprebbero"

def get_condizionale_bere(person, n):
    if n == 1:
        if person == 1:
            return "berrei"
        elif person == 2:
            return "berresti"
        else:
            return "berrebbe"
    elif n == 2:
        if person == 1:
            return "berremmo"
        elif person == 2:
            return "berreste"
        else:
            return "berrebbero"

# tryb przypuszczający złożony - czasy przeszłe
def get_condizionale_composto(verb, data):
    person = data[0]
    n = data[1]
    gender = data[2]

    participio = get_participio_passato(verb)

    if verb in ("essere", "uscire", "andare", "venire", "salire", "rimanere", "morire", "nascere",
                "scendere", "correre", "accendere", "crescere", "tornare", "visitare", "partire", "pulire"):
        modal = get_condizionale_essere(person, n)
        if gender == 1 and n == 2:
            participio = participio[:-1] + 'i'
        elif gender == 2 and n == 1:
            participio = participio[:-1] + 'a'
        elif gender == 2 and n == 2:
            participio = participio[:-1] + 'e'
    else:
        modal = get_condizionale_avere(person, n)

    return modal + " " + participio

# tryb rozkazujący
def get_imperativo(verb, data):
    person = data[0]
    n = data[1]

    if verb not in ("essere", "avere", "fare", "stare", "sapere", "andare", "dare", "dire"):
        if verb[-3] == 'a':
            if n == 1:
                if person == 2:
                    return verb[:-3] + "a"
                else:
                    return verb[:-3] + "i"
            elif n == 2:
                if person == 1:
                    return verb[:-3] + "iamo"
                elif person == 2:
                    return verb[:-3] + "ate"
                else:
                    return verb[:-3] + "ano"
        elif verb[-3] == 'e':
            if n == 1:
                if person == 2:
                    return verb[:-3] + "i"
                else:
                    return verb[:-3] + "a"
            elif n == 2:
                if person == 1:
                    return verb[:-3] + "iamo"
                elif person == 2:
                    return verb[:-3] + "ete"
                else:
                    return verb[:-3] + "ono"
        elif verb in ("capire", "preferire", "finire"):
            if n == 1:
                if person == 2:
                    return verb[:-3] + "isci"
                else:
                    return verb[:-3] + "isca"
            elif n == 2:
                if person == 1:
                    return verb[:-3] + "iamo"
                elif person == 2:
                    return verb[:-3] + "ite"
                else:
                    return verb[:-3] + "iscono"
        elif verb[-3] == 'i':
            if n == 1:
                if person == 2:
                    return verb[:-3] + "i"
                else:
                    return verb[:-3] + "a"
            elif n == 2:
                if person == 1:
                    return verb[:-3] + "iamo"
                elif person == 2:
                    return verb[:-3] + "ite"
                else:
                    return verb[:-3] + "ono"
    else:
        return get_imperativo_irregular(verb, person, n)

# tryb rozkazujący - odmiana nieregularna
def get_imperativo_irregular(verb, person, n):
    match verb:
        case "essere": return get_imperativo_essere(person, n)
        case "avere": return get_imperativo_avere(person, n)
        case "fare": return get_imperativo_fare(person, n)
        case "andare": return get_imperativo_andare(person, n)
        case "dare": return get_imperativo_dare(person, n)
        case "dire": return get_imperativo_dire(person, n)
        case "sapere": return get_imperativo_sapere(person, n)
        case "stare": return get_imperativo_stare(person, n)

def get_imperativo_essere(person, n):
    if n == 1:
        if person == 2:
            return "sii"
        else:
            return "sia"
    elif n == 2:
        if person == 1:
            return "siamo"
        elif person == 2:
            return "siete"
        else:
            return "siano"

def get_imperativo_avere(person, n):
    if n == 1:
        if person == 2:
            return "abbi"
        else:
            return "abbia"
    elif n == 2:
        if person == 1:
            return "abbiamo"
        elif person == 2:
            return "abbiate"
        else:
            return "abbiano"

def get_imperativo_sapere(person, n):
    if n == 1:
        if person == 2:
            return "sappi"
        else:
            return "sappia"
    elif n == 2:
        if person == 1:
            return "sappiamo"
        elif person == 2:
            return "sappiate"
        else:
            return "sappiano"

def get_imperativo_andare(person, n):
    if n == 1:
        if person == 2:
            return "va"
        else:
            return "vada"
    elif n == 2:
        if person == 1:
            return "andiamo"
        elif person == 2:
            return "andate"
        else:
            return "vadano"

def get_imperativo_fare(person, n):
    if n == 1:
        if person == 2:
            return "fa"
        else:
            return "faccia"
    elif n == 2:
        if person == 1:
            return "facciamo"
        elif person == 2:
            return "fate"
        else:
            return "facciano"

def get_imperativo_dare(person, n):
    if n == 1:
        if person == 2:
            return "da"
        else:
            return "dia"
    elif n == 2:
        if person == 1:
            return "diamo"
        elif person == 2:
            return "date"
        else:
            return "diano"

def get_imperativo_dire(person, n):
    if n == 1:
        if person == 2:
            return "di"
        else:
            return "dica"
    elif n == 2:
        if person == 1:
            return "diciamo"
        elif person == 2:
            return "dite"
        else:
            return "dicano"

def get_imperativo_stare(person, n):
    if n == 1:
        if person == 2:
            return "sta"
        else:
            return "stia"
    elif n == 2:
        if person == 1:
            return "stiamo"
        elif person == 2:
            return "state"
        else:
            return "stiano"

