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