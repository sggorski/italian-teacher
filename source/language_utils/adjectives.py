from source.language_utils import nouns

# poprawna forma przymiotnika
def get_adjective_in_correct_form(noun, adjective):
    noun_gender = nouns.define_gender(noun)
    if noun_gender == "m_s":
        if adjective[-1] == 'o' or adjective[-1] == 'e':
            return adjective
        else: return adjective[:-1] + 'o'
    elif noun_gender == "f_s":
        if adjective[-1] == 'a' or adjective[-1] == 'e':
            return adjective
        else: return adjective[:-1] + 'a'
    elif noun_gender == "m_p":
        return adjective[:-1] + 'i'
    else:
        if adjective[-1] == 'a' or adjective[-1] == 'o':
            return adjective[:-1] + 'e'
        else: return adjective[:-1] + 'i'