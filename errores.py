
"""
try:
    variable = float(input('ingresa un float o int: '))
    a = 2
    print("resultado: ", a*variable)
except:
    print("no ingresate un float")      """

dato = False
while(dato == False):
    try:
        variable = float(input('ingresa un float o int: '))
        a = 2
        print("resultado: ", a*variable)
        dato = True
    except:
        print("no ingresate un float")      
        dato = False