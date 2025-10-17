"""
11. Escribe un programa que pida al usuario que introduzca su edad. Si el usuario ingresa un valor no numérico o un valor fuera del rango esperado (por ejemplo, menor que 0 o mayor que 120), maneja las excepciones adecuadamente.
"""

try:
    edadUsuario = int(input("Introduce tu edad:"))
except TypeError as e:
    print(f"Error: Tipo de dato no compatible: {e}")
except ValueError as e:
    print(f"Error: El valor no corresponde: {e}")
except:
    print("Ocurrió un error inesperado")
else:
    if not (0 <= edadUsuario <= 120):
        raise ValueError("El valor introducido está fuera de los limites (Mín: 0 , Máx: 120)")
    else:
        print("El valor introducido es correcto.")