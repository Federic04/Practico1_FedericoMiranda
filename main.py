from clasemanejadorproductos import manejadorproductos
from clasemanejadorstock import manejadorstock
if __name__ == '__main__':
    manejadorproductos1=manejadorproductos()
    manejadorproductos1.cargarproductos()
    manejadorstock1=manejadorstock()
    manejadorstock1.cargarstock()
    cod_ing=int(input('\ningrese un codigo de producto:'))
    cant_ing=int(input('\ningrese cantidad de productos:'))
    t=input('\ningrese tipo de tansaccion ( (c-Compra, v-Venta):')
    manejadorstock1.actulizarstock(cod_ing,cant_ing,t)
    productos=manejadorproductos1.getproductos()
    print()
    for i in range (len(productos)):
        productos[i].mostrarcantidad(manejadorstock1)
    print()
    manejadorproductos1.ordenar()
    for  i in range (len(productos)):
        productos[i].mostrarlistado(manejadorstock1)




