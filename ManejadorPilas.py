import numpy as np

class manejadorPilas(object):
    __tope1 = None
    __tope2 = None
    __tamanio = None
    __arreglo = None
    
    def __init__(self,tamanio = 5):
        self.__arreglo = np.empty(tamanio,dtype=int)
        self.__tamanio = tamanio
        self.__tope1 = -1
        self.__tope2 = tamanio
    
    def lleno(self):
        resultado = None
        if self.__tope1+1<self.__tope2:
            resultado = False
        else:
            resultado = True
        return resultado
    
    def vacio_pila1(self):
        resultado = None
        if self.__tope1 == -1:
            resultado = True
        else:
            resultado = False
        return resultado
    
    def vacio_pila2(self):
        resultado = None
        if self.__tope2 == self.__tamanio:
            resultado = True
        else:
            resultado = False
        return resultado
        
    
    def insertar_pila1(self, elemento):
        assert isinstance(elemento,int)
        val = None
        if not self.lleno():
            self.__tope1+=1
            self.__arreglo[self.__tope1] = elemento
            val = elemento
        else:
            val = 0
            print('ERROR: arreglo en memoria lleno!')
        return val
    
    def insertar_pila2(self,elemento):
        assert isinstance(elemento,int)
        val = None
        if not self.lleno():
            self.__tope2 -= 1
            self.__arreglo[self.__tope2] = elemento
            val = elemento
        else:
            val = 0
            print('ERROR: arreglo en memoria lleno!')
        return val
    
    def suprimir_pila1(self):
        valor = None
        if not self.vacio_pila1():
            valor = self.__arreglo[self.__tope1]
            self.__tope1-=1
        else:
            valor = 0
            print('ERROR: pila 1 vacia!')
        return valor
    
    def suprimir_pila2(self):
        valor = None
        if not self.vacio_pila2():
            valor = self.__arreglo[self.__tope2]
            self.__tope2 +=1
        else:
            valor = 0
            print('ERROR: pila 2 vacia!')
        return valor
    
    def mostrar_pila1(self):
        if not self.vacio_pila1():
            i = self.__tope1
            while i >= 0:
                print('Elemento: {}' .format(self.suprimir_pila1()))
                i-=1
        else:
            print('ERROR: pila 1 vacia!')
    
    def mostrar_pila2(self):
        if not self.vacio_pila2():
            i = self.__tope2
            while i <= self.__tamanio-1:
                print('Elemento: {}'.format(self.suprimir_pila2()))
                i+=1
        else:
            print('ERROR: pila 2 vacia!')
    



