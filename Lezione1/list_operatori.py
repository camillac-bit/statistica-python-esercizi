# ESERCIZIO 2:
# Data la lista names = ['Batman', 'Iron Man', 'Thor']
# verifica se 'Thor' è presente e se 'Hulk' è presente.
# In seguito elimina il secondo elemento della lista
# e successivamente stampa il nuovo secondo elemento della lista.
# Cosa succede se si moltiplica la lista uno =[1] per 42? 
# Stampa il risutato di questa operazione e la lunghezza della nuova lista creata.

names = ['Batman',
         'Iron Man',
         'Thor']

print(f"Thor: {'Thor' in names}")
print("Hulk:",'Hulk' in names)

del names[1]
print(names[1])

uno = [1]
prova = uno * 42
print(f"Lista: {prova}\nLunghezza: {len(prova)}")