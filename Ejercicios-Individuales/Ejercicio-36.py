"""
36. Crea una función llamada procesar_texto
        Procesa un texto según la opción especificada: contar_palabras, reemplazar_palabras o eliminar_palabra.
        Código a seguir:

            Crear una función contar_palabras que cuente el número de veces que aparece cada palabra en el texto y devuelva un diccionario.
            Crear una función reemplazar_palabras para sustituir una palabra_original por una palabra_nueva en el texto y devolver el texto modificado.
            Crear una función eliminar_palabra que elimine una palabra del texto y devuelva el texto sin ella.
            Crear la función procesar_texto que reciba un texto, una opción ("contar", "reemplazar", "eliminar") y un número variable de argumentos según la opción elegida.

        Caso de uso:
            Verificar el funcionamiento completo de procesar_texto.
"""

#---------Función: Contar Palabras-----------------
def contar_palabras(texto: str) -> dict:
    textoSeparado = texto.lower().replace(".","").replace(",","").split(" ")
    registro = {}

    for palabra in textoSeparado:
        registro[palabra] = registro.get(palabra, 0) + 1 
    return print(registro)

#---------Función: Reemplazar Palabras-------------
def reemplazar_palabras(texto: str, palabraOut: str, palabraIn: str) -> str:
    textoSeparado = texto.lower().replace(".","").replace(",","").split(" ")
    lista = []

    for palabra in textoSeparado:
        if (palabra == palabraOut):
            lista.append(palabraIn)
        else: 
            lista.append(palabra)
    
    return print(" ".join(lista))

#---------Función: Eliminar Palabras --------------
def eliminar_palabra(texto: str, palabraOut: str) -> str:
    textoSeparado = texto.lower().replace(".","").replace(",","").split(" ")
    lista = []

    for palabra in textoSeparado:
        if (palabra != palabraOut):
            lista.append(palabra)
    
    return print(" ".join(lista))

#---------Función: Procesar Texto -----------------
def procesar_texto(texto: str, funcion: str, *args):

    if funcion == "contar":
        return contar_palabras(texto)
    elif funcion == "reemplazar":
        return reemplazar_palabras(texto, args[0], args[1])
    elif funcion == "eliminar":
        return eliminar_palabra(texto, args[0])
    else:
        print(f"La función {funcion} no existe, utiliza 'contar', 'reemplazar' o 'eliminar'")
    return
    
#----------Selección Opción ---------------
function = "eliminar"
    
#------ Parametrización Opciones ----------
if function == "reemplazar":
    argItem = ("nada", "algo")

elif function == "eliminar":
    argItem = ("nada",) #hace falta la coma...

#------ LLamada función -------------------
prueba = procesar_texto("Nada es nada si no haces nada.", function, *argItem )
