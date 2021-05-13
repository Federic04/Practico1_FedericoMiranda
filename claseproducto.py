class producto:
    __cod=0
    __descripcion=''
    __precio_u=0


    def __init__(self,cd=0,des='',p=0):
        self.__cod=cd
        self.__descripcion=des
        self.__precio_u=p
    def getdescripcion(self):
        return self.__descripcion
    def mostrarcantidad(self,manejadorstock1):
        stocks=manejadorstock1.getstock()
        c_u=0
        for i in range(len(stocks)):
            if self.__cod==stocks[i].getcodigo():
                c_u=stocks[i].getcantidad()
        print('cantidad de stock del producto {} es:{}'.format(self.__cod,c_u))


    def __lt__(self, otradescripcion):
        if(self.__descripcion<otradescripcion.getdescripcion()):
            return True
        else:
            return False
    def mostrarlistado(self,manejadorstock1):
        stocks=manejadorstock1.getstock()
        for i in range (len(stocks)):
            if stocks[i].getcodigo()==self.__cod:
                if stocks[i].getcantidad()<10:
                    print('Descripcion:{}    Cantidad en stock:{}'.format(self.__descripcion,stocks[i].getcantidad()))


