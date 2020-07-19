
class Fabrica:
    def __init__(self, marca, nombre, precio, descripcion):
        self.marca = marca
        self.nombre = nombre
        self.precio = precio
        self.descripcion = descripcion
# Auto = Fabrica('Ford11', 'Ranger11', 'camioneta11', '4*411', '4')        

    def __str__(self):
        return """
            Marca\t{}
            Nombre\t{}
            Precio\t{}
            Descripcion\t{}""".format(self.marca, self.nombre, self.precio, self.descripcion)

class Auto(Fabrica):# hereda de la clase Fabrica
    pass

class Deportivo(Fabrica):# hereda de fabrica
    ruedas = ""
    distribuidor = ""

    def __str__(self):
        return """
            Marca\t\t{}
            Nombre\t\t{}
            Precio\t\t{}
            Descripcion\t\t{}
            ruedas\t\t{}
            Distribuidor\t{}""".format(self.marca, self.nombre, self.precio, self.descripcion, self.ruedas, self.distribuidor)

class Accesorio(Fabrica):
    autor = ""
    fabricante = ""

    def __str__(self):
        return """
            Marca\t\t{}
            Nombre\t\t{}
            Precio\t\t{}
            Descripcion\t\t{}
            autor\t\t{}
            fabricante\t\t{}""".format(self.marca, self.nombre, self.precio, self.descripcion, self.autor, self.fabricante)

a = Auto('ford21', 'ranger21', 1.00021, 'camion21')

deportivo = Deportivo('volkswage36', 'vento36', 4.0036, 'el mejor36')
deportivo.ruedas = 3
deportivo.distribuidor = 'distribuidor 38'

accesorio = Accesorio('flat 56', 'luces de neon 56', 10.000, 'iluminacion 56')
accesorio.autor = 'yo 57'
accesorio.fabricante = 'yoooo 58'

fabrica = [accesorio, deportivo]
fabrica.append(a)

for x in fabrica:
    print(x, '\n')

for x in fabrica:
    if( isinstance(x, Auto) ):# isinstance lo toma de forma disitnta cada uno
        print("Auto: ",x.marca, x.nombre,"\n")
    elif( isinstance(x, Deportivo) ):
        print("deportivo: ", x.marca, x.ruedas,"\n")
    elif( isinstance(x, Accesorio) ):
        print("Accesorio: ", x.marca, x.nombre, x.fabricante,"\n")


"""     aca inicia el polimorfismo      """

def Descuento_accesorio(t, descuento):
    t.precio = t.precio - (t.precio/100 * descuento)

Descuento_accesorio(accesorio, 10)

print(float(accesorio.precio))


import copy     # copia del obj
copia_deportivo = copy.copy(accesorio)

print(copia_deportivo)

descuento = 10
a.precio = a.precio - (a.precio/100 * descuento)

a.precio