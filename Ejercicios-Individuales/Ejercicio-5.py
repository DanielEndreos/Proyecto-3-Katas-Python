"""
5. Escribe una función que tome una lista de números como parámetro y un valor opcional nota_aprobado (por defecto 5). La función debe calcular la media de los números en la lista y determinar si la media es mayor o igual que nota_aprobado. Si es así, el estado será "aprobado"; de lo contrario, "suspenso". La función debe devolver una tupla que contenga la media y el estado.
"""

def checkNotas(listaNotas: list, notaLimite: float) -> tuple:
    mediaNota = sum(listaNotas)/len(listaNotas)
    mediaNota = round(mediaNota,2)
    if mediaNota>=notaLimite:
        return (mediaNota,"Aprobado")
    else:
        return (mediaNota,"Suspendido")

notasLista = [7.5, 6.0, 9.0, 4.5, 8.0, 5.0, 10.0, 3.5, 6.5, 7.0, 2.0, 9.5, 8.5, 4.0, 5.5, 6.8, 7.2, 3.0, 9.8, 1.5]
notaAprobado = 5.0

resultado = checkNotas(notasLista, notaAprobado)
print (resultado)


notasLista = [2.5, 2.0, 2.0, 4.5, 8.0, 5.0, 6.0, 3.5, 6.5, 7.0, 2.0, 3.5, 8.5, 4.0, 5.5, 6.8, 7.2, 3.0, 9.8, 1.5]
notaAprobado = 5.0

resultado = checkNotas(notasLista, notaAprobado)
print (resultado)