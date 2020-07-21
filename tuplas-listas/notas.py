""" Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, 
Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado en cada asignatura, y después las 
muestre por pantalla con el mensaje En <asignatura> has sacado <nota> donde <asignatura> es cada una des las
asignaturas de la lista y <nota> cada una de las correspondientes notas introducidas por el usuario.        """

materias = ['matematicas', 'fisica', 'quimica', 'historia', 'lengua']
notas = []

for x in materias:
    nota = float(int(input("Digite la nota: ")))
    notas.append(nota)

for i in range(len(materias)):
    print("En {} saco {}".format(materias[i], notas[i]))


