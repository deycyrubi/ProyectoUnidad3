"""
>>> numero = DistanciaEuclidea(2,2,4,4,)
>>> numero.CalDistancia()
>>> numero.getDistancia()
2.8284271247461903
"""

#Se declara la palabra reservada math para la resolución del problema
import math
#Se declara la clase la cual lleva por nombre el problema a resolver
class DistanciaEuclidea:

    """Se declaran los atributos de la clase DistanciaEuclidea de manera privada 
    los cuales indicarán las acciones o necesidades del objeto"""""
    __x1 = float(0)  #Se usa el elemento("__") para indicar que el atributo es privado
    __y1 = float(0)
    __x2 = float(0)
    __y2 = float(0)
    __distancia = float(0)
    __suma = float(0)

    #En esta sección realizamos el metodo constructor el cual será el que utilicen todos los demás métodos
    def __init__(self,x1,y1,x2,y2):  #def es para declarar un método y _init_es para definir al método constructor
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2

        self.CalDistancia() #Se usa la palabra reservada self seguida del atributo
        #para acceder a los atributos privados

    def CalDistancia(self):
        self.__distancia = math.sqrt((self.__x1 - self.__x2) ** 2 + (self.__y1 - self.__y2) ** 2)

    #Se usa get para que pueda mostrar el valor, puesto que  está declarado como privado
    def getDistancia(self):
        return self.__distancia


if __name__ == '__main__':
    import doctest
    doctest.testmod()