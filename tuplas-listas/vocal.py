""" Escribir un programa que pida al usuario una palabra y muestre por pantalla el número de veces que contiene
cada vocal. """

palabra = input("Digite una palabra: ")
vocales = ['a', 'e', 'i', '0', 'u']

for v in vocales:
    contador = 0
    for p in palabra:
        if p == v: 
            contador +=1
    print("la {} esta {} veces".format(v, contador))
