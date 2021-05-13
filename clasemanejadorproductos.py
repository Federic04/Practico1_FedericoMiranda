import csv
from claseproducto import producto
class manejadorproductos:
    __listaproductos=[]


    def __init__(self):
        self.__listaproductos=[]

    def cargarproductos(self):
        band=True
        archivo=open('Productos.csv')
        reader=csv.reader(archivo,delimiter=';')
        for fila in reader:
            if band==True:
                band=False
            else:
                cd=int(fila[0])
                des=fila[1].lower()
                p=int(fila[2])
                unproducto=producto(cd,des,p)
                self.__listaproductos.append(unproducto)

        archivo.close()
    def getproductos(self):
        return self.__listaproductos
    def ordenar(self):
        self.__listaproductos.sort()
