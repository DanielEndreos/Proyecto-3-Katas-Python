"""
10. Escribe una función que reciba una lista de números y calcule su promedio. Si la lista está vacía, lanza una excepción personalizada y maneja el error adecuadamente.
"""
def promedioCalc(listaInput: list):
    if len(listaInput) == 0:
        raise IndexError("La lista está vacía.")  
    else:
        return round(sum(listaInput)/len(listaInput),2)

listaDatos=[23,2,123,12,4,512,4123,12,3,512,4,123,123,2,232,3,232,3132,123]
print(promedioCalc(listaDatos))

listaDatos=[]
print(promedioCalc(listaDatos))