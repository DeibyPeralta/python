# solo existe en python

class primera:
    def __init__(self):
        print("clase padre")

    def metodo_1(self):
        print("metodo padre")

class segunda:
    def __init__(self):
        print("clase hija")

    def metodo_2(self):
        print("metodo hijo")

class tercera(segunda, primera):
    def metodo_3(self):
        print("metodo hereda 3")

herencia_multiple = tercera()# hereda derecha a izquierda
print(herencia_multiple)

print(herencia_multiple.metodo_1() )
print(herencia_multiple.metodo_2() )