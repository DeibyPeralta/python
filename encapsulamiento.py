
class  encapsulamiento:
    __privado_atri="no se puede accedes fuera de la clase"

    def __privado_met(self):
        print("metodo, solo se accede dentro de la clase")

    def public_atri(self):
        return self.__privado_atri

    def public_met(self):
        return self.__privado_met()


e = encapsulamiento()     

si = e.public_atri()

print(si)