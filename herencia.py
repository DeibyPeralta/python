
class Fabrica:
    def __init__(self, marca, nombre, precio, descripcion, ruedas=None, distribuidor=None):
        self.marca = marca
        self.nombre = nombre
        self.precio = precio
        self.descripcion = descripcion
        self.ruedas = ruedas
        self.distribuidor = distribuidor
# Auto = Fabrica('Ford11', 'Ranger11', 'camioneta11', '4*411', '4')        

    def __str__(self):
        return """
            Marca\t{}
            Nombre\t{}
            Precio\t{}
            Descripcion\t{}""".format(self.marca, self.nombre, self.precio, self.descripcion)

class Auto(Fabrica):# hereda de la clase Fabrica
    pass
a = Auto('ford21', 'ranger21', 1.00021, 'camion21')
print(a)


class Deportivo(Fabrica):
    ruedas = ""
    distribuidor = ""

    def __str__(self):
        return """
            Marca\t\t{}
            Nombre\t\t{}
            Precio\t\t{}
            Descripcion\t\t{}
            Distribuidor\t{}""".format(self.marca, self.nombre, self.precio, self.descripcion, self.distribuidor)

deportivo = Deportivo('volkswage36', 'vento36', 4.0036, 'el mejor36')
deportivo.ruedas = 3
deportivo.distribuidor = 'distribuidor 38'

print(deportivo)