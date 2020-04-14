#para utilizar una biblioteca, ésta se debe de importar
import math

x = math.cos(math.pi)

print(x)

#También se puede importar todas las funciones de las bibliotecas, de esta manera no se tiene que usar el prefijo
#de la biblioteca, que en el ejmplo anterior fue math
from math import *

x = cos(pi) #No se utiliza el prefijo math

print(x)

#Otra manera es importar sólo las funciones que se necesitan
from math import cos, pi

x = cos(pi)

print(x)
