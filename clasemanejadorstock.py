import csv
from clasestock import stock
class manejadorstock:
    __listastock=[]

    def __init__(self):
        self.__listastock=[]


    def cargarstock(self):
        band=True
        archivo=open('Stock.csv')
        reader=csv.reader(archivo,delimiter=';')
        for fila in reader:
            if band==True:
                band=False
            else:
                cp=int(fila[0])
                cant=int(fila[1])
                unstock=stock(cp,cant)
                self.__listastock.append(unstock)
        archivo.close()
    def actulizarstock(self,cod_ing,cant_ing,t_transaccion):
         if t_transaccion=='c':
             for i in range(len(self.__listastock)):
                 if self.__listastock[i].getcodigo()==cod_ing:
                     self.__listastock[i]=self.__listastock[i]+cant_ing
         else:
             for i in range(len(self.__listastock)):
                 if self.__listastock[i].getcodigo()==cod_ing:
                     self.__listastock[i]=self.__listastock[i]-cant_ing


    def getstock(self):
       return self.__listastock





