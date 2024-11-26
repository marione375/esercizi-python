import random
#questa funzione seleziona il numero ed il seme delle carte che possano essere date
numero1 = random.randint (1,10)
numero2 = random.randint (1,10)
seme1 = random.randint (1,4)
seme2 = random.randint (1,4)
def calcolocarte():
    if numero1 == 10:
        numero1 = "Re"
    elif numero1 == 9:
        numero1 = "Donna"
    elif numero1 == 8:
        numero1 = "Jack"
    if seme1 == 1:
        seme1 = "Cuori"
    elif seme1 == 2:
        seme1 = "Quadri"
    elif seme1 == 3:
        seme1 = "Picche"
    else:
        seme1 = "Fiori"
    if numero2 == 10:
        numero2 = "Re"
    elif numero2 == 9:
        numero2 = "Donna"
    elif numero2 == 8:
        numero2 = "Jack"
    if seme2 == 1:
        seme2 = "Cuori"
    elif seme2 == 2:
        seme2 = "Quadri"
    elif seme2 == 3:
        seme2 = "Picche"
    else:
        seme2 = "Fiori"
carta1 = f"{numero1} di {seme1}"
carta2 = f"{numero2} di {seme2}"
if carta1 != carta2:

    print(f"il dealer ti ha dato due carte:\n {carta1} e {carta2}")

