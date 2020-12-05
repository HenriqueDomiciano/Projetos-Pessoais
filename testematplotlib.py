from matplotlib import pyplot
import numpy as np

x= np.linspace(0, 20 , 1000)
y1= np.sin(x)
y2= np.cos(x)
y3= (y1+y2)**2
y4=(np.e)**(-x)


pyplot.title("grafico")
pyplot.xlabel("x")
pyplot.ylabel("y")


pyplot.plot(x,y1,label="hiperbolico")
pyplot.plot(x,y2,label="normal")
pyplot.plot(x,y3,label="soma ao quadrado")
pyplot.plot(x,y4,label='e**-x')
pyplot.legend(loc="upper right")
pyplot.show()
