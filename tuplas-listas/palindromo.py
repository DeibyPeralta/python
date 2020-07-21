"""     Escribir un programa que pida al usuario una palabra y muestre por pantalla si es un palíndromo.        """

igual, aux = 0, 0
palabra = input("Ingrese la palabra que desea evaluar: ")
for ind in reversed(range(0, len(palabra))):
  if palabra[ind].lower() == palabra[aux].lower():
    igual += 1
  aux += 1
if len(palabra) == igual:
  print("El texto es palindromo!")
else:
  print("El texto no es palindromo!")