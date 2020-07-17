"""       if
print('programa de notas')

def evaluacion(nota):
    valoracion="aprovado"
    if nota < 5:
        valoracion='suspendido'
    else:
        valoracion='aprovo'
    return valoracion

dato = input('ingrese la nota: ')
print(evaluacion(int(dato)))       """




"""         for
# recorro una lista
for i in ["primavera", "otoño"]:     #[1,2,3]: 
    print('hola: ' + str(i)) # ,end=''       # sin salto de linea

# imprime tantas veces como caracteres
for i in "prueba":
    print("hola: " + i)


# validar correo
email = False
for i in "correo@gmail.com":
    if(i=="@"):     
        email = True

print("email is " + str(email))     """

"""
iteracion = 0
while iteracion <= 3:
    iteracion += 1
    print("text: ", str(iteracion))     """

for i in range(5,20,3): # 5 -- 9 of 3 in 3
    print(i)