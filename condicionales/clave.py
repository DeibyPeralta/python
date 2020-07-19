""" Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por 
la contraseña e imprima por pantalla si la contraseña introducida por el usuario coincide con la guardada en la 
variable sin tener en cuenta mayúsculas y minúsculas.   """

import os
import time
clave = "1234"

dato = False
while (dato == False):
    time.sleep(1)
    os.system("cls")
    password = input("Digite la clave: ")

    if password == clave:
        print("Contraseña correcta")
        dato = True
    else:
        print("Contraseña mala")
        dato = False