# __init__   crea el obj
#  hace referercai al propio objeto, diferencia class y met
class Auto:
    rojo = False

    def __init__(self, puertas=None, color=None): #no es obligatorio mandarle datos
        self.puertas = puertas
        self.color = color

        if puertas is not None and color is not None:
            print("se cro una uto con puertas {}, y color {}".format(puertas, color))
    def Fabricar(self):
        self.rojo = True

    def confirmar_fabricacion(self):
        if (self.rojo):
            print("auto rojo")
        else:
            print("aun no esta coloreado")

a = Auto("2", "rojo")# line 10 validation
a.confirmar_fabricacion()
a.Fabricar()
a.confirmar_fabricacion()
#print(a.rojo)

"""
class Estudiantes:  #creo clase
    pass

Estudiantes = Estudiantes() # instancio el objeto

print(type(Estudiantes))        """


"""
class Auto:
    pass

consecionario = Auto()

consecionario.color = "rojo"
consecionario.puerta = "muchas"

print("mi auto es de color: ", consecionario.color) """