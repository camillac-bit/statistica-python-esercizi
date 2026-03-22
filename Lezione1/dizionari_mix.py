# ESERCIZIO 6:
# Dato il dizionario d = {"nome": "E****", "età": 32},
# stampare se è possibile d["città"].
# Cosa resistuisce "nome" in d? E 23 in d? Stampare i valori restituiti.
# Aggiungere una nuova coppia chiave-valore "hobby": ['palestra','animali','pokemon'].
# Modificare la lista in corrsipondenza della chiave "hobby" aggiungendo 'labubu'.
# Modificare l'età e stampare il dizionario con le modifiche apportate.
# Aggiungere la coppia chiave-valore: ['altezza'] = 1.58, cosa succede? Perchè? Gestire l'errore.
# Eliminare la chiave "età" e il valore associato e stampare nuovamente d.

d = {"nome": "E****", "età": 32}

try:
    print(d['citta'])
except KeyError:
    print("Impossibile recuperare il valore associato a 'città': chiave insesistente.")


print("nome" in d)
print(23 in d)

d["hobby"] = ['palestra','animali','pokemon']
d["hobby"].append('labubu')

d["età"] = 23

print(d)

try:
    d[['altezza']]=1.58
except TypeError:
    print("Impossibile aggiungere una chiave come lista: le chiavi devono essere immutabili.")

del d["età"]
print(d)