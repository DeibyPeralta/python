"""     Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, 
Historia y Lengua) en una lista y la muestre por pantalla el mensaje Yo estudio <asignatura>, donde <asignatura> 
es cada una de las asignaturas de la lista.     """

materias = ['matematicas', 'fisica', 'quimica', 'historia', 'lengua']

for x in materias:
    print('yo estudio: {}'.format(x))