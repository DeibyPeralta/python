""" Escribir un programa que muestre el eco de todo lo que el usuario introduzca hasta que el usuario escriba 
“salir” que terminará.    """

def salida():
    salir = False

    while salir == False:
        text = input("Digite algo: ")

        if text == "salir":
            salir = True
        else:
            salir = False

salida()   