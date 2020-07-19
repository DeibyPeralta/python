""" Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10 veces.    """

name = input("nombre: ")

for i in range(10):
    print("nombre: {} ves {}".format(name, i))