def crear_lista_estudiantes(numeroEstudiantes):
    estudiantes=[]
    for _ in range(numeroEstudiantes):
        estudiante={}
        estudiante["id"]=input("Ingrese el ID del estudiante: ")
        estudiante["nombres"]=input("Ingrese el nombre del estudiante: ")
        estudiante["documento"]=input("Ingrese el documento: ")
        estudiante["semestre"]=input("Ingresa el semestre: ")
        estudiantes.append(estudiante)
    return estudiantes

crear_lista_estudiantes(5)

 
