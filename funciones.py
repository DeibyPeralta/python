"""
def suma():
    uno=1
    dos=2
    print(uno + dos)

#   suma()

def sumaRecive(uno, dos):
    print(uno + dos)

#   sumaRecive(1,3)

def sumaReturn(uno, dos):
    resultado = uno + dos
    return resultado

resultado_sumaReturn=sumaReturn(2,4)
print(resultado_sumaReturn)
"""
def tabla():
    global texto = 'texto' # hago una variable global
    for x in range(10):
        print("7 * {} = {}".format(x,x*7))

print(tabla())