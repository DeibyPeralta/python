
import pickle

#   escribo en el codigo binario
"""
lista_nombres=["pedro", "ana" , "maria" , "isabel"]
fichero_binario=open("lista_binario", "wb")# write binaria
pickle.dump(lista_nombres, fichero_binario)# info volcar, name fichero a volcar in memory
fichero_binario.close()
del (fichero_binario)# delete of memory """

#   leo datos del fichero binario
binario=open("lista_binario", "rb")# read binaria
lista=pickle.load(binario)
binario.close()
print(lista)