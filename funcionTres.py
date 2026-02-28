#Crear una función que calcula el promedio de una lista de notas
def calcular_promedio_notas(notas):
    #extaer los elementos de una lista (recorrer la lista)
    acumulador=0
    for nota in notas:
        acumulador+=nota
    return(acumulador/len(notas))

