""" devuelve 1 en 1     """

def generaPares(limite):

    num = 1

    while num < limite:
        yield num*2
        num += 1

objIterable=generaPares(10)

print(next(objIterable))

print("msa codigo ....")

print(next(objIterable))

print("msa codigo ....")


"""
for i in objIterable:
    print(i)    """


#   son el mismo algoritmo pero yield es generador

"""
def generaPares(limite):
    num = 1

    miLista=[]

    while num < limite:
        miLista.append(num*2)
        num += 1

    return miLista

print(generaPares(10))  """