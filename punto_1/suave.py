import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
#Funcion para caragar una imagen

def imagen_matriz(imagen):
    matriz = plt.imread(imagen)
    return matriz

matriz = imagen_matriz("index.png")
#Para crear un kernell, vamos a usar el gausiano con exp(-0.5*x al cuadrado)


def funcion(x):
    funcion = np.exp(-0.05*x**2)
    return funcion


#Integral con trapecio
def integra(f,a,b,N):
    h = (b-a)/(N-1)
    resultado = 0.0
    for i in range(N):
        x = a + i *h
        resultado += 0.5*(f(x)+f(x+h))*h
    return resultado

def genera_kernell1D(n_pixel_kernell):
    x= np.linspace(-10,10,n_pixel_kernell)
    integral = integra(funcion,-10,10,n_pixel_kernell)
    func = funcion(x)
    func = func/integral
    tfunc = np.transpose(func)
    kernel = func*tfunc
    return kernell




