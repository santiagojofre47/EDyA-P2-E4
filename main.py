from ManejadorPilas import manejadorPilas

#test del manejo de dos pilas
if __name__ == '__main__':
    x1 = 1
    x2 = 4
    x3 = 5
    x4 = 6
    objManejador = manejadorPilas()
    objManejador.insertar_pila1(x1)
    objManejador.insertar_pila2(x2)
    objManejador.insertar_pila2(x3)
    objManejador.insertar_pila2(x4)
    objManejador.insertar_pila2(x4+1)
    objManejador.insertar_pila2(x4+2)#Este ultimo elemento no se insertará ya que el arreglo en memoria estará lleno
    objManejador.mostrar_pila1()
    objManejador.mostrar_pila2()