
""" Escribir un programa en el que se pregunte al usuario por una frase y una letra, y muestre por pantalla el 
número de veces que aparece la letra en la frase. """

frase = input("Digite una frase: ")
letra = input("Introduce una letra: ")
contador = 0
for i in frase:
    if i == letra:
        contador += 1
print("la letra {} esta {} veces".format(letra, contador))
