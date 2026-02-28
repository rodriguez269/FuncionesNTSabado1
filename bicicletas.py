#crear una funcion en python para crear una lista de n estudiantes que son diccionarios


#crear una lista de 20 notas asociadas a la eficiencia
#crear una lista de 20 notas asociadas al parecido
#crear una lista de 20 notas asociadas a la estabilidad
#crear una rutina para obtener el promedio de esas notas
#crear una rutina para calcular el ganador

from funcionUno import crear_lista_estudiantes
from funcionDos import crear_lista_notas
from funcionTres import calcular_promedio_notas
from funcionCuatro import evaluar_bicicleta




#Paso 1 creo el equipo
equipoUno=crear_lista_estudiantes(4)

#Paso 2 Evaluar los componenetes EF,ES,P de la bicicleta
notasEficiencia=crear_lista_notas(50)
notasEstabilidad=crear_lista_notas(50)
notasParecido=crear_lista_notas(50)

#Paso 3 calcular la nota promedio de cada componente
eficiencia=calcular_promedio_notas(notasEficiencia)
estabilidad=calcular_promedio_notas(notasEstabilidad)
parecido=calcular_promedio_notas(notasParecido)

#Paso 4 evaluo la bicicleta
evalucionFinal=evaluar_bicicleta(eficiencia,estabilidad,parecido)

#Paso 5 muestro el resultado
print(f"El resultado del equipo 1 fue:  {evalucionFinal}")