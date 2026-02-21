def crearListaDeNotas(numeroDeNotas):
    notas=[]
    for _ in range(numeroDeNotas):
      nota=random.randint(1,5)
      notas.append(nota)
    return notas