"""
40. Escribe un programa en Python que utilice condicionales para determinar el monto final de una compra en una tienda en línea, después de aplicar un descuento. El programa debe:
    a. Solicitar al usuario el precio original de un artículo.
    b. Preguntar si tiene un cupón de descuento (respuesta sí o no).
    c. Si la respuesta es sí, solicitar el valor del cupón de descuento.
    d. Aplicar el descuento al precio original, siempre que el valor del cupón sea válido (mayor a cero).
    e. Mostrar el precio final de la compra, considerando o no el descuento.
    f. Usar estructuras de control de flujo (if, elif, else) para llevar a cabo las acciones.
"""

#A. Preguntas
precioArticulo = float(input("Por favor, introduce el precio del artículo:"))
cuponDescuento = str(input("Tienes un cupón descuento? y/n"))
if cuponDescuento == "y":
    valorDescuento = int(input("Que % de descuento tiene el cupón?"))
    if valorDescuento > 0:
        precioArticulo = precioArticulo - (precioArticulo*(valorDescuento/100))

if cuponDescuento == "y":
    print(f"El precio total de la compra asciende a {precioArticulo:.2f}, se ha aplicado un descuento del {valorDescuento}%.")
else:
    print(f"El precio total de la compra asciende a {precioArticulo:.2f}")