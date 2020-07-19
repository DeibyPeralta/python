class fabrica:
    def __init__(self, tiempo, nombre, ruedas):
        self.tiempo = tiempo
        self.nombre = nombre
        self.ruedas = ruedas
        print("se creo el auto", self.nombre)

    def __str__(self):
        return "{}({})".format(self.nombre, self.tiempo)


class listado: # 
    autos = []# lista que contiene lso datos

    def __init__(self,autos=[]):  # constructor
        self.autos = autos

    def agregar(self, obj):
        self.autos.append(obj) # agrego obj

    def mirar(self):
        for obj in self.autos:
            print(obj)


a = fabrica(20, "automovil",4)

# clase listado
l = listado([a])
l.mirar()

l.agregar(fabrica(123,"segundo",4))

l.mirar()
