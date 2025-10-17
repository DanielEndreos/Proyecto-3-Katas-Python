"""
8. Escribe un programa que pida al usuario dos números e intente dividirlos. Si el usuario ingresa un valor no numérico o intenta dividir por cero, maneja esas excepciones de manera adecuada y muestra un mensaje indicando si la división fue exitosa o no.
"""
try:
    numA = float(input("Introduce el primer número:"))
    numB = float(input("Introduce el segundo número:"))
    resultado = numA / numB
except ZeroDivisionError as e:
    print("Error: División por cero: ", e)
except ValueError as e:
    print("Error: Tipo de dato no compatible: ", e)
except Exception as e:
    print("Ocurrió un error inesperado: ", e)
else:
    print(f"El resultado ha sido: {resultado:.2f}")
finally:
    print("Finalizando el proceso...")
