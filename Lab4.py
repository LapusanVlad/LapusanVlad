# 1. Lista de cuvinte și alegerea cuvântului la întâmplare
import random
cuvinte = ["python", "programare", "calculator", "date", "algoritm"]
cuvant_de_ghicit = random.choice(cuvinte)
progres = ["_" for _ in cuvant_de_ghicit]

# 2. Inițializarea numărului de încercări
incercari_ramase = 6
litere_incercate = []

print("Bine ati venit la jocul Spanzuratoarea!")
print("Cuvantul de ghicit este","" .join(progres))
print(f"Incercari ramase {incercari_ramase}")

while incercari_ramase > 0 and "_" in progres:
    litera = input("Introduceti o litera: ").lower()

    if len(litera) != 1 or not litera.isalpha():
        print("Introduceti o singura litera din alfabet.")
        continue

    if litera in cuvant_de_ghicit:
        progres = [litera if cuvant_de_ghicit[i] == litera else progres[i] for i in range(len(cuvant_de_ghicit))]

    else:
        incercari_ramase -= 1


    print("Cuvantul de ghicit este: ","".join(progres))
    print(f"Incercari ramase {incercari_ramase}")



print("Felicitari! Ai ghicit cuvantul:" if "_" not in progres else "Ai pierdut! Cuvantul era:", cuvant_de_ghicit)