def profesor(estudiantes=None):
    if estudiantes is None:
        print("debes escribir algo")


profesor("asd")
"""
try:
    numero = float(input("escribe un numero: "))
    10/numero
except TypeError:
    print("esto es una cadena")
except ValueError:
    print("esto es un numero")
except ZeroDivisionError:
    print("no se puede dividir por cero")
except Exception as x:
    print(type(x).__name__)     """


"""
try:
    variable = float(input('ingresa un float o int: '))
    a = 2
    print("resultado: ", a*variable)
except:
    print("no ingresate un float")      """

"""
dato = False
while(dato == False):
    try:
        variable = float(input('ingresa un float o int: '))
        a = 2
        print("resultado: ", a*variable)
        dato = True
    except:
        print("no ingresate un float")      
        dato = False        """

"""
while(True):
    try:
        variable = float(input('ingresa un float o int: '))
        a = 2
        print("resultado: ", a*variable)
    except:
        print("no ingresate un float")      
    else:
        print("todo salio bien")
        break
    finally:
        print("ya termino todo")        """