
import pickle

class Persona:

    def __init__(self, nombre, genero, edad):
        self.nombre=nombre
        self.genero=genero
        self.edad=edad
        print("nombre: ", self.nombre)

    def __str__(self):
        return "{} {} {}".format(self.nombre, self.genero, self.edad)

class ListaPersona:

    personas=[]

#   constructor
    def __init__(self):
        listdePersonas=open("ficheroExterno", "ab+")
        listdePersonas.seek(0)# cursor position 0

        try:
            self.personas=pickle.load(listdePersonas)
            print("Se cargaron del fichero externo")
        except:
            print("Fichero vacio")
        finally:
            listdePersonas.close()
            del(listdePersonas)
#   constructor       

    def agregarPersona(self, p):
        self.personas.append(p)
        self.guardarFicheroExterno()

    def mostrarPersona(self):
        for p in self.personas:
            print(p)

    def guardarFicheroExterno(self):
        listdePersonas=open("ficheroExterno", "wb")
        pickle.dump(self.personas, listdePersonas)
        listdePersonas.close()
        del(listdePersonas)

    def mostrarInfoFichero(self):
        print("info del fichero")
        for p in self.personas:
            print(p)

miLista=ListaPersona()# constructor

p = Persona("sandra", "femenino", 69)
miLista.agregarPersona(p)

miLista.mostrarInfoFichero()