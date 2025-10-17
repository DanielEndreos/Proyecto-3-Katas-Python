"""
37. Genera un programa que nos indique si es de noche, de día o de tarde según la hora proporcionada por el usuario.
"""

hora = str(input("Introduce la hora en formato String hh:mm:ss:"))

hora = hora.split(":") #Separamos la hora en Horas, minutos y segundos

horaInt = int(hora[0]) #Cogemos el apartado horas y lo convertimos a Int

if (horaInt >= 6 and horaInt<=12):
    print("Es por la mañana")
elif (horaInt >= 13 and horaInt<=20):
    print("Es por la tarde")
elif (horaInt >= 21 or horaInt<=5):
    print("Es por la noche")