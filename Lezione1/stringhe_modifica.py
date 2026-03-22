# ESERCIZIO 5:
# Data la stringa nome = 'pinco pallino',
# modifica il terzo carattere. Cosa succede? Perchè? Gestiscilo.
# Crea una nuova stringa concatenando 'super' e nome,
# utilizzando tre metodi di concatenazione diversi e stampa i risultati ottenuti.

nome = 'pinco pallino'
#nome[2]='c'

try:
    nome[2]='c'
except TypeError:
    print("impossibile modificare l'elemento")

nome_esteso = 'super ' + nome
print(nome_esteso)

nome_esteso =f'super {nome}'
print(nome_esteso)

nome_esteso = "super {n}".format(n=nome)
print(nome_esteso)

#nome_esteso = "super " "pinco pallino"
#print(nome_esteso)