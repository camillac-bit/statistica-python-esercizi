# ESERCIZIO 3:
# Data la lista names = ['Thor', 'Batman', 'Iron Man']
# ordinare la lista in ordine lessicografico e stampare la lista.
# In seguito ordinare la lista in ordine non crescente rispetto alla lunghezza
# delle stringhe contenute in essa. Stampare nuovamente la lista.


names = ['Thor', 'Batman', 'Iron Man']

#names.sort() restituisce None

names.sort()
print(names)

names.sort(key=lambda n : len(n), reverse=True)
# in realtà si poteva mettere direttamente key=len
print(names)