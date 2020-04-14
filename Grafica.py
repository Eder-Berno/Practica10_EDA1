#Esta línea se ocupa para que las gráficas que se generen queden embedidas dentro de la página
%pylab inline

#importando las bibliotecas
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

#Datos de entrada
x = linscape(0,5,20) #Generando 10 puntos entre 0 y 5

fig, ax = plt.subplots(facecolor='w', edgecolor='k')
ax.plot(x, sin(x), maker="o", color="r", linestyle="None")

ax.grid(True)
ax.set_xlabel('X') #Etiqueta el eje x
ax.set_ylabel('Y') #Etiqueta el eje y
ax.grid(True)
ax.legend(["y = x**2"])

plt.tittle('Puntos')
plt.show()

fig.savefig("Gráfica.png") #Guardando la gráfica
