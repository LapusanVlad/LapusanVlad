# Cerinta 1
meniu = ['papanasi'] * 10 + ['ceafa'] * 3 + ["guias"] * 6
preturi = [["papanasi", 7], ["ceafa", 10], ["guias", 5]]
studenti = ["Liviu", "Ion", "George", "Ana", "Florica"]  # coada FIFO
comenzi = ["guias", "ceafa", "ceafa", "papanasi", "ceafa"]  # coada FIFO
tavi = ["tava"] * 7  # stiva LIFO
istoric_comenzi = []

# Servirea comenzilor
while studenti and comenzi and tavi:
    print(f"{studenti.pop(0)} a comandat {comenzi.pop(0)}.")
    tavi.pop()
    istoric_comenzi.append((studenti[0], comenzi[0])) if studenti and comenzi else None

# Afisarea istoricului comenzilor
print("\nIstoric comenzi:", istoric_comenzi)

# Cerinta 2
meniu = ['papanasi'] * 10 + ['ceafa'] * 3 + ['guias'] * 6
comenzi = ["guias", "ceafa", "ceafa", "papanasi", "ceafa"]
tavi_ramase = 10 - len(comenzi)  # Avem inițial 10 tăvi

# Afisarea rezultatelor
print(f"S-au comandat {comenzi.count('guias')} guias, {comenzi.count('ceafa')} ceafa, {comenzi.count('papanasi')} papanasi.")
print(f"Mai sunt {tavi_ramase} tavi.")
print(f"Mai este ceafa: {meniu.count('ceafa') > comenzi.count('ceafa')}.")
print(f"Mai sunt papanasi: {meniu.count('papanasi') > comenzi.count('papanasi')}.")
print(f"Mai sunt guias: {meniu.count('guias') > comenzi.count('guias')}.")

# Cerinta 3
preturi = [["papanasi", 7], ["ceafa", 10], ["guias", 5]]
comenzi = ["guias", "ceafa", "ceafa", "papanasi", "ceafa"]

# Calculul incasarilor si filtrarea produselor ieftine
incasari = sum(preț for produs, preț in preturi for c in comenzi if c == produs)
produse_ieftine = [p for p in preturi if p[1] <= 7]

# Afisare
print(f"Cantina a încasat: {incasari} lei.")
print(f"Produse care costă cel mult 7 lei: {produse_ieftine}")


