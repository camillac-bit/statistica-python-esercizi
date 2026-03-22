# ESERCIZIO 4:
# Data la tupla tl = (9,8,'pollo'),
# modifica il terzo elemento inserendo 7, gestisci l'eccezione.
# Data la tupla animali = (['gatto','topo'],'istrice','nottula'),
# modifica il primo elemento della lista contenuta nella tupla e stampa la tupla.
# Perchè non viene generata un'eccezione?

tl = (9,8,'pollo')
#tl[2] = 7

try:
    tl[2] = 7
except TypeError:
    print('Impossibile modificare la tupla: tipo immutabile')

animali = (['gatto','topo'],'istrice','nottula')
animali[0][0]='dugongo'

print(animali)