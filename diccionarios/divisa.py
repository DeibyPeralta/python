"""     Escribir un programa que guarde en una variable el diccionario {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}, 
pregunte al usuario por una divisa y muestre su símbolo o un mensaje de aviso si la divisa no está en el
diccionario.     """

datos = {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}

divisa = input("Divisa a buscar: ")

if divisa == 'Euro':
    print("Esta el Euro")
elif divisa == 'Dollar':
    print("Esta el dolar")
elif divisa == 'Yen':
    print("Esta el yen")
else:
    print("error")

    print(datos.get(divisa.title(), "La divisa no está."))

