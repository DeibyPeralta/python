# el * indica numero indeterminado de elementos en forma de tuplas

def devuelve_ciudades(*ciudades):
    for i in ciudades:
     #   for subI in i:
            yield from i #yield omite doble for
# me da m xq me da el 1 elemento y luego la 1 letra
ciudades_devuelta = devuelve_ciudades('madrid', 'barceloa', 'bilbao')

print(next(ciudades_devuelta))
