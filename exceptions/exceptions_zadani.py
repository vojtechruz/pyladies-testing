# Ukol: Zmen funkci tah_hrace tak, aby se zeptala znovu, pokud uzivatel nezada cele cislo.
# Napoveda: Jaka vyjimka vyskoci, pokud int(cislo_policka) nedokaze prevest vstup na cele cislo? Co se s tim da delat?

def tah_hrace(herni_pole):
    while True:
        cislo_policka = input("Zadej cislo policka 0-19: ")
        cislo_policka = int(cislo_policka)
        if cislo_policka < 0 or cislo_policka > 19:
            print("Prosim zadej cislo v rozmezi 0-19.")
        elif herni_pole[cislo_policka] != "-":
            print("Policko {} je obsazene, vyber prosim jine.".format(cislo_policka))
        else:
            return tah(herni_pole, cislo_policka, "x")

def tah(herni_pole, cislo_policka, symbol):
    return herni_pole[:cislo_policka] + symbol + herni_pole[cislo_policka + 1:]

print(tah_hrace("--------------------"))