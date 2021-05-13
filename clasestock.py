
class stock:
    __cod_p=0
    __cantidad=0


    def __init__(self,c_p=0,cant=0):
        self.__cod_p=c_p
        self.__cantidad=cant
    def getcodigo(self):
        return self.__cod_p
    def getcantidad(self):
        return self.__cantidad
    def __add__(self, escalar):
        return stock(self.__cod_p,self.__cantidad+escalar)

    def __sub__(self, escalar):
        return stock(self.__cod_p,self.__cantidad-escalar)


