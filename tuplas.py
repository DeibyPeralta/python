#duplas no se pueden modificar

dupla = ("borrar", 1, 2, 3, 'cuatro')
miLista = list(dupla)
print(miLista[0])
#print(dupla[4])

#   se pueden pasar de listas a duplas y viseversa

lista = ["uno", 2, 3, 'cuatro']
miDupla=tuple(lista)
print(miDupla)

print("uno" in miDupla) #   True si esta, False si no
print(miDupla.count(3)) #   cuantas veces esta 3
print(len(miDupla))     #   cuantas datos tiene


#       duplas unitarias --- solo un dato
tuplaUnitaria=(3,)
print(len(tuplaUnitaria))

#       Empaquetar tuplas
tupla=("julio", 2, 1993)
mes, dia, año=tupla

print(mes)
print(dia)
print(año)