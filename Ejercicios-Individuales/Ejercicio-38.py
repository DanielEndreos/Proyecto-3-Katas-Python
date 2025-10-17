"""
38. Escribe un programa que determine qué calificación en texto tiene un alumno según su calificación numérica.
        Reglas:
                0 - 69: insuficiente
                70 - 79: bien
                80 - 89: muy bien
                90 - 100: excelente
"""

try:
    calificacionAlumno = int(input("Que nota ha sacado el alumno?"))
except ValueError as e:
    print(f"El formato no es correcto: {e} ")
else:
    if 0 <= calificacionAlumno <= 69:
        print("Insuficiente")
    elif 70 <= calificacionAlumno <= 79:
        print("Bien")
    elif 80 <= calificacionAlumno <= 89:
        print("Muy bien")
    elif 90 <= calificacionAlumno <= 100:
        print("Excelente")
