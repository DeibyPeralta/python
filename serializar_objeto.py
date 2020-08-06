
import pickle #libreria para serializar

class vehiculo():

    def __init__(self, marca, modelo):
        self.marca=marca
        self.modelo=modelo
        self.enmarcha=False
        self.acelera=False
        self.frena=False

    def arrancar(self):
        self.enmarcha=True
    
    def acelera(self):
        self.acelera=True

    def frena(self):
        self.frena=True
    
    def estado(self):
        print("marca: ", self.marca)

coche1 = vehiculo("marca25", "modelo25")
coche2 = vehiculo("marca26", "modelo26")
coche3 = vehiculo("marca27", "modelo27")

coches = [coche1, coche2, coche3]

"""
fichero = open("coches_binarios", "wb")

# info volcar, name fichero a volcar in memory
pickle.dump(coches,fichero)

fichero.close()
del(fichero)        """


ficheroOpen = open("coches_binarios", "rb")
misCoches=pickle.load(ficheroOpen)

ficheroOpen.close()

for c in misCoches:
    print(c.estado())