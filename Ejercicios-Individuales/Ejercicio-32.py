"""
32. Crea una función que tome un nombre completo y una lista de empleados, busque el nombre en la lista y devuelva el puesto del empleado si se encuentra; de lo contrario, devuelve un mensaje indicando que la persona no trabaja aquí.
"""

empleados = [
    {"nombre": "Ana Gómez"      , "puesto": "Gerente de Ventas"},
    {"nombre": "Carlos Ruiz"    , "puesto": "Técnico de Mantenimiento"},
    {"nombre": "Lucía Pérez"    , "puesto": "Administrativa"},
    {"nombre": "Dani Meco"      , "puesto": "Programador de Automatismos Industriales"},
    {"nombre": "Marta López"    , "puesto": "Responsable de Recursos Humanos"},
    {"nombre": "Jorge Torres"   , "puesto": "Diseñador Industrial"},
    {"nombre": "Laura Sánchez"  , "puesto": "Contable"},
    {"nombre": "Sergio Díaz"    , "puesto": "Ingeniero de Producción"},
    {"nombre": "Beatriz Romero" , "puesto": "Supervisora de Calidad"},
    {"nombre": "Raúl Navarro"   , "puesto": "Logística y Almacén"}
]

nombreCompleto = "Dani Meco"

def busqEmpleado(name:str, listaEmpl: list) -> str:
    return next((e for e in empleados if e["nombre"] == name), "El trabajador no trabaja aquí")

resultadoBusqueda = busqEmpleado("Dani Meco", empleados)

print(f"El trabajador {resultadoBusqueda['nombre']} trabaja aquí como {resultadoBusqueda['puesto']}.")
    
    
    