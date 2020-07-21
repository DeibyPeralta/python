""" Escribir un programa que pregunte al usuario los números ganadores de la lotería primitiva, los almacene 
en una lista y los muestre por pantalla ordenados de menor a mayor. """

num = []

x = int(input("Cuantos numero registrara? "))

while x != 0:
    numero = int(input("Numero loteria: "))
    num.append(numero)

    if x != 0:
        x = x-1

ordenados = sorted(num)
print("numero: {}".format(ordenados))

