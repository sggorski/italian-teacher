from source.language_utils import adjectives, articles, nouns, pronouns, verbs


# GŁÓWNA FUNKCJA DO TWORZENIA CAŁYCH ZDAŃ
def construct_sentence(data):
    sentence, subject_data = handle_subject(data)
    sentence += handle_verb(data, subject_data)
    sentence += handle_object(data)

    sentence = sentence.strip()
    sentence = sentence.capitalize()
    if data['sentence_type'] == "interrogative":
        sentence += '?'
    else:
        sentence += '.'

    return sentence

# funkcja obrabiająca odpowiednią formę rzeczownika z przymiotnikiem
def handle_subject(data):
    sentence = ""
    singular_1 = True

    if not data["subject_isPerson"]:
        noun = data["subject_noun"]

        if data["subject_number"] == "plural":
            singular_1 = False

        if data["subject_article"] == "definite":
            if singular_1:
                sentence += articles.get_articolo_determinativo_singular(noun) + " "
            else:
                sentence += articles.get_articolo_determinativo_plural(noun) + " "
        elif data["subject_article"] == "indefinite":
            if singular_1:
                sentence += articles.get_articolo_undeterminativo_singular(noun) + " "
            else:
                sentence += articles.get_articolo_undeterminativo_plural(noun) + " "

        if data["subject_number"] == "plural":
            noun = nouns.get_plural(noun)

        if "subject_demonstrative" in data.keys():
            if data["subject_demonstrative"] == "near":
                sentence += pronouns.get_pronome_vicino(noun) + " "
            elif data["subject_demonstrative"] == "far":
                sentence += pronouns.get_pronome_lontano(noun) + " "

        if "subject_possessive" in data.keys():
            if data["subject_possessive"] == "io":
                sentence += pronouns.get_possesive_pronoun(1, 1, noun) + " "
            elif data["subject_possessive"] == "tu":
                sentence += pronouns.get_possesive_pronoun(2, 1, noun) + " "
            elif data["subject_possessive"] in ("lui", "lei"):
                sentence += pronouns.get_possesive_pronoun(3, 1, noun) + " "
            elif data["subject_possessive"] == "noi":
                sentence += pronouns.get_possesive_pronoun(1, 2, noun) + " "
            elif data["subject_possessive"] == "voi":
                sentence += pronouns.get_possesive_pronoun(2, 2, noun) + " "
            elif data["subject_possessive"] == "loro":
                sentence += pronouns.get_possesive_pronoun(3, 2, noun) + " "

        sentence += noun + " "

        if "subject_adjective" in data.keys():
            if data["subject_adjective"] is not None:
                sentence += adjectives.get_adjective_in_correct_form(noun, data["subject_adjective"]) + " "

        noun_data = nouns.define_gender(noun)
        if noun_data == "m_s":
            subject_data = [3, 1, 1]
        elif noun_data == "m_p":
            subject_data = [3, 2, 1]
        elif noun_data == "f_s":
            subject_data = [3, 1, 2]
        else:
            subject_data = [3, 2, 2]

    else:
        subject_data = [int(data["subject_person_code"][0]), int(data["subject_person_code"][2]),
                        int(data["subject_person_code"][4])]
        if subject_data[0] == 1 and subject_data[1] == 1:
            sentence += "io "
        elif subject_data[0] == 2 and subject_data[1] == 1:
            sentence += "tu "
        elif subject_data[0] == 3 and subject_data[1] == 1 and subject_data[2] == 1:
            sentence += "lui "
        elif subject_data[0] == 3 and subject_data[1] == 1 and subject_data[2] == 2:
            sentence += "lei "
        elif subject_data[0] == 1 and subject_data[1] == 2:
            sentence += "noi "
        elif subject_data[0] == 2 and subject_data[1] == 2:
            sentence += "voi "
        elif subject_data[0] == 3 and subject_data[1] == 2:
            sentence += "loro "

    return sentence, subject_data

# funkcja obrabiająca odpowiednią formę czasownika
def handle_verb(data, subject_data):
    sentence = ""

    verb = data["verb"]
    if data['sentence_type'] == "negative":
        sentence += "non "

    if data["tense_type"] == "present" and data['sentence_type'] == "negative" and data["mood_type"] == "imperative":
        sentence += verb + " "
    elif data["tense_type"] == "present":
        if data["mood_type"] == "imperative":
            sentence += verbs.get_imperativo(verb, subject_data) + " "
        elif data["mood_type"] == "indicative":
            sentence += verbs.get_present_tense(verb, subject_data) + " "
        else:
            sentence += verbs.get_condizionale_simplice(verb, subject_data) + " "
    elif data["tense_type"] == "past":
        if data["mood_type"] == "indicative":
            sentence += verbs.get_past_tense(verb, subject_data) + " "
        else:
            sentence += verbs.get_condizionale_composto(verb, subject_data) + " "
    else:
        sentence += verbs.get_future_tense(verb, subject_data) + " "

    return sentence

# funkcja obrabiająca odpowiednią formę "całej reszty zdania" - object
def handle_object(data):
    singular_1 = True
    sentence = ""

    if not data["object_isPerson"]:
        noun = data["object_noun"]

        if data["object_number"] == "plural":
            singular_1 = False

        if data["object_article"] == "definite":
            if singular_1:
                sentence += articles.get_articolo_determinativo_singular(noun) + " "
            else:
                sentence += articles.get_articolo_determinativo_plural(noun) + " "
        elif data["object_article"] == "indefinite":
            if singular_1:
                sentence += articles.get_articolo_undeterminativo_singular(noun) + " "
            else:
                sentence += articles.get_articolo_undeterminativo_plural(noun) + " "

        if data["object_number"] == "plural":
            noun = nouns.get_plural(noun)

        if "object_demonstrative" in data.keys():
            if data["object_demonstrative"] == "near":
                sentence += pronouns.get_pronome_vicino(noun) + " "
            elif data["object_demonstrative"] == "far":
                sentence += pronouns.get_pronome_lontano(noun) + " "

        if "object_possessive" in data.keys():
            if data["object_possessive"] == "io":
                sentence += pronouns.get_possesive_pronoun(1, 1, noun) + " "
            elif data["object_possessive"] == "tu":
                sentence += pronouns.get_possesive_pronoun(2, 1, noun) + " "
            elif data["object_possessive"] in ("lui", "lei"):
                sentence += pronouns.get_possesive_pronoun(3, 1, noun) + " "
            elif data["object_possessive"] == "noi":
                sentence += pronouns.get_possesive_pronoun(1, 2, noun) + " "
            elif data["object_possessive"] == "voi":
                sentence += pronouns.get_possesive_pronoun(2, 2, noun) + " "
            elif data["object_possessive"] == "loro":
                sentence += pronouns.get_possesive_pronoun(3, 2, noun) + " "

        sentence += noun + " "

        if "object_adjective" in data.keys():
            if data["object_adjective"] is not None:
                sentence += adjectives.get_adjective_in_correct_form(noun, data["object_adjective"]) + " "

    else:
        object_data = [int(data["object_person_code"][0]), int(data["object_person_code"][2]),
                        int(data["object_person_code"][4])]
        if object_data[0] == 1 and object_data[1] == 1:
            sentence += "mi "
        elif object_data[0] == 2 and object_data[1] == 1:
            sentence += "ti "
        elif object_data[0] == 3 and object_data[1] == 1 and object_data[2] == 1:
            sentence += "lo "
        elif object_data[0] == 3 and object_data[1] == 1 and object_data[2] == 2:
            sentence += "la "
        elif object_data[0] == 1 and object_data[1] == 2:
            sentence += "ci "
        elif object_data[0] == 2 and object_data[1] == 2:
            sentence += "vi "
        elif object_data[0] == 3 and object_data[1] == 2:
            sentence += "li "

    return sentence
