#Crear una lista de 500 notas (1,5)
#Mock

import random
notas=[] 
for i in range(5):
    nota=random.randint(1,5)
    #Llenar una lista
    notas.append(nota)

#Manipulando listas con Python
notas.insert(1,80)
notas.remove(80)
notas.pop(0)
notas.sort(reverse=True)
notas.clear()
print(notas)