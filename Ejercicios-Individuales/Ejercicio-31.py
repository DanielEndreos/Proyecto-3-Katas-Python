"""
31. Crea una función que solicite al usuario ingresar una lista de nombres y luego un nombre para buscar en esa lista. Si el nombre está en la lista, imprime un mensaje indicando que fue encontrado; de lo contrario, lanza una excepción.
"""

def defineAndFind() -> str:

    listaUsers = []
    nameUser = ""

    while nameUser.lower() != "fin":
        try:
            nameUser =  str(input("Buenos días, inserta nombres y termina con la palabra 'fin':"))
        except ValueError as e:
            print("Error: Tipo de dato no compatible: ", e)
        except Exception as e:
            print("Ocurrió un error inesperado: ", e)
        else:
            if ((nameUser.lower() != "fin") and (nameUser != "") and (nameUser.isalpha()) ):
                listaUsers.append(nameUser.lower().capitalize())

    nameFilter = str(input("Introduce el nombre a buscar: "))
    print("Los usuarios introducidos son: ", listaUsers)
    if nameFilter.lower().capitalize() in listaUsers:
        return f"El nombre '{nameFilter.capitalize()}' está en la lista."
    else:
        return f"El nombre '{nameFilter.capitalize()}' no está en la lista."

prueba = defineAndFind()
print(prueba)




