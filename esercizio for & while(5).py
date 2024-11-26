import time
#while è una ripetizione finchè la condizione è vera
#il for invece ripete l'attività finchè la condizione si verifica
x = int(input("inserisci un numero\n"))
passaggi = 0
#divide finchè il numero non diventa dispari
if x == 0:
    print("non te lo farò")
else:
    while x%2 == 0:
        x= x/2
        print(x)
y = 5
for i in range(6):
    print("disistallamento della cartella win32 in ", y)
    time.sleep(1)
    y-=1
