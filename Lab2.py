import string

text = 'Eurodeputata Diana Șoșoacă Își Depune, Joi, Candidatura Pentru alegerile parlamentare pentru un mandat de senatoare'
jumatate = len(text) // 2

prima_jumatate = text[:jumatate].upper().strip()

a_doua_jumatate = text[jumatate:][::-1]
a_doua_jumatate = a_doua_jumatate.capitalize()

a_doua_jumatate = a_doua_jumatate.translate(str.maketrans('', '', string.punctuation))

rezultat_final = prima_jumatate + a_doua_jumatate

print("Rezultatul final:", rezultat_final)