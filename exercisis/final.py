""" Una panadería vende barras de pan a 3.49€ cada una. El pan que no es el día tiene un descuento del 60%. Escribir 
un programa que comience leyendo el número de barras vendidas que no son del día. Después el programa debe mostrar el 
precio habitual de una barra de pan, el descuento que se le hace por no ser fresca y el coste final total. """


pan = 3.49
descuento = (pan * 100)/60

vendidasNo = input("Barras vendidas que no son del dia: ")

precio_normal = vendidasNo * pan
print("Precio normal: {}".format(precio_normal))

precio_descuento = (precio_normal * 100) / 40
print("Precio descuento: {}".format(precio_descuento))

precio_final = (precio_normal * 100) / 60
print("Precio final: {}".format(precio_final))