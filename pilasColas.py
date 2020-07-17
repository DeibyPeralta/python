
"""         pilas       """
pila =  [4,3,2,1]

pila.append(5)
"""print(pila)

pila.append(6)
print(pila)

pila.append(122)
print(pila)     """

#eliminado = pila.pop()
#print(eliminado) # elimina


"""         colas           """
from collections import deque # importo libreria colas

colas = deque(["primero", "segundo", "tercero"])
print(colas)

eliminado = colas.pop() # elimino

print(colas)
print(eliminado)