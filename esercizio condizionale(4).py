# esercizio condizionale
# le condizionali sono cause nelle quali in caso in cui accada qualcosa, il comando procede in un determinato modo. l'esempio più classico è la calcolatrice
nomeInput = str (input ("inserisci il tuo nome\n"))
cognomeInput = str (input("inserisci il tuo conogme\n"))
print(f"salve {cognomeInput} {nomeInput}")
import math
Operazione = input("seleziona l'operazione da svolgere + - / * ^ rad (scrivi rad se vuoi usare la radice)\n")
if Operazione == "+":
    Num1 = float(input("inserisci il primo addendo\n"))
    Num2 = float(input("inserisci il secondo addendo\n"))
    print(f"la somma di {Num1} + {Num2} è: {Num1 + Num2}")
elif Operazione == "-":
    Num1 = float(input("inserisci un minuendo\n"))
    Num2 = float(input("inserisci il secondo sottraendo\n"))
    print(f"la sottrazione di {Num1} - {Num2} è: {Num1 - Num2}")
elif Operazione == "/":
    Num1 = float(input("inserisci il quoziente\n"))
    Num2 = float(input("inserisci il divisore\n"))
    if Num2 == 0:
        print("Errore")
    else:
        print(f"la divisione di {Num1} / {Num2} è: {Num1 / Num2}")
elif Operazione == ":":
    Num1 = float(input("inserisci il primo fattore\n"))
    Num2 = float(input("inserisci il secondo fattore\n"))
    print(f"la moltiplicazione di {Num1} * {Num2} è: {Num1 * Num2}")
elif Operazione == "^":
    Num1 = float(input("inserisci la base\n"))
    Num2 = float(input("inserisci l'esponente\n"))
    print(f"la potenza di {Num1} ^ {Num2} è: {Num1 ** Num2}")
elif Operazione == "rad":
    Num1 = float(input("inserisci il radicando\n"))
    Num2 = float(input("inserisci l'esponente della radice\n"))
    Ris = pow(Num1,1/Num2)
    print (f"la radice di {Num1} di {Num2} è: {Ris}")
else:
    print(f"scrivi l'operazione correttamente {nomeInput} {cognomeInput}")
