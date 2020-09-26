import numpy as np
import matplotlib.pyplot as plt

def derivacion():
    fx = lambda x : x**2 -5*x +8
    x = np.linspace(-50,50,100)
    aa = fx(x)
    plt.plot(x,aa,color='red')
    plt.savefig('derivacion.png')
    plt.title('Grafica de derivacion')
    plt.xlabel('Jhonathan Jovanny Contreras Tzintzun')
    plt.show()

def integracion():
    gx = lambda x : (x**3 / 3) - 2*x + 8*x
    x = np.linspace(-50,50,100)
    bb = gx(x)
    plt.plot(x,bb,color='green')
    plt.savefig('Integracion.png')
    plt.title('Grafica de integracion')
    plt.xlabel('Jhonathan Jovanny Contreras Tzintzun')
    plt.show()

def comprobacion():
    gx = lambda x : x**2 -5*x +8
    x = np.linspace(-50,50,100)
    bb = gx(x)
    plt.plot(x,bb,color='yellow')
    plt.savefig('comprobacion.png')
    plt.title('Grafica de comprobacion')
    plt.xlabel('Jhonathan Jovanny Contreras Tzintzun')
    plt.show()

derivacion()
integracion()
comprobacion()