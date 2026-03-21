# ESERCIZIO 1:
# Data la lista:
# iron_man = ['Iron Man', 'Tony Stark', 'Marvel', 1963, 85]
# Scrivi espressioni per ottenere:
# - "Tony Stark"
# - 85 usando indice negativo
# - ['Marvel', 1963] usando slicing
# - gli ultimi 3 elementi


iron_man = ['Iron Man',
            'Tony Stark',
            'Marvel',
            1963,
            85]

print(iron_man[1])
print(iron_man[-1])
print(iron_man[-3:-1]) 
#print(iron_man[2:-1])
#print(iron_man[-3:4])
#print(iron_man[2:4])
print(iron_man[-3:])

