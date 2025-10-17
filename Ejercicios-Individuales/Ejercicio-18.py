"""
18. Escribe un programa en Python que cree una lista de diccionarios con información de estudiantes (nombre, edad, calificación) y use filter para extraer a los estudiantes con una calificación mayor o igual a 90.
"""
estudiantes = [
    {"nombre": "Dani", "edad": 20, "calificacion": 85},
    {"nombre": "Lucía", "edad": 22, "calificacion": 91},
    {"nombre": "Carlos", "edad": 19, "calificacion": 74},
    {"nombre": "Ana", "edad": 21, "calificacion": 95},
    {"nombre": "Marta", "edad": 23, "calificacion": 90}
]

estudiantesCalificados = list(filter(lambda a: a["calificacion"] >= 90, estudiantes))

print (estudiantesCalificados)