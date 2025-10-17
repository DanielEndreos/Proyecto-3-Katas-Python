"""
39. Escribe una función que tome dos parámetros: figura (una cadena que puede ser "rectangulo", "circulo" o "triangulo") y datos (una tupla con los datos necesarios para calcular el área de la figura).
"""

import math

def calculoFigura(figura: str, **kwargs):
    if figura == "rectangulo":
        return print(f"El área del rectángulo es base*altura, {kwargs["base"]}x{kwargs["altura"]}={kwargs["base"]*kwargs["altura"]}.")
    elif figura == "circulo":
        return print(f"El área del círculo es π*r², {math.pi:.2f}x{kwargs["radio"]}²={math.pi*(kwargs["radio"]**2):.2f}.")
    elif figura == "triangulo":
        return print(f"El área del triángulo es (base*altura)/2, ({kwargs['base']}×{kwargs['altura']})/2 = {(kwargs['base'] * kwargs['altura'])/2}.")
#-----------Parametrización
argItem2 = {"base": 5, "altura": 10, "radio": 20,}

#----------Selección Opción ---------------
function = "triangulo"  #circulo , triangulo, rectangulo
    
#------ LLamada función -------------------
prueba = calculoFigura(function.lower(), **argItem2 )
