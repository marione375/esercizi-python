#ecco l'esercizio input
#con l'imput posso ricevere i segnali della tastira, così che la macchina può (leggere) ciò che gli scriviamo, può leggere del testo
nome=input("Scriva il suo nome\n")
cognome=input("scrivi il tuo cognome\n")
#può anche ricevere i numeri
iban=input("se mi scrivi il numero della carta di credito sarei felice\n")
print(f"Signor {cognome} {nome} abbiamo prelevato i contanti dalla sua carta di credito\n arrivederci :P")
print(f"Il saldo della sua carta ({iban}) è 0")
#può essere utilizzato per fare delle operazioni basilare
print("facciamo un addizzione\n")
Num1 = float(input("inserisci il primo addendo\n"))
Num2 = float(input("inserisci il secondo addendo\n"))
print(f"la somma di {Num1} + {Num2} è: {Num1 + Num2}\n")
#può essere usato per tutti i tipi di operazioni.
