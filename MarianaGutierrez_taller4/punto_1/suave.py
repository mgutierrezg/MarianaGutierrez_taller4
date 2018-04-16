import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
#Funcion para caragar una imagen

def matriz_bn():
    imagen = Image.open("imagen.png")
    negra = imagen.convert('L')
    negra.save("imagen.png")
    matriz = plt.imread("imagen.png")
    return matriz 

matriz = matriz_bn()
print matriz

def fourier2d(matriz):
    m = (np.shape(matriz)[0])
    n = (np.shape(matriz)[1])
    lista = np.zeros((m,n), dtype = np.complex)
    M = range(m)
    N = range(n)
    for k in M:
        for l in N:
             suma = 0.0
             for i in M:
                 for j in N:
                        x = ((float(k*i)/m) + (float(l*j)/n))
                        suma += matriz[i,j]*np.exp(-2*l*np.pi*x)
        lista[k,l] = suma

    return lista
print fourier2d(matriz)

def inversa2d(fourier):
    m = (np.shape(fourier)[0])
    n = (np.shape(fourier)[1])
    listai = np.zeros((m,n), dtype = np.complex)
    M = range(m)
    N = range(n)
    for i in M:
        for j in N:
             suma = 0.0
             for k in M:
                 for l in N:
                        x = ((float(k*i)/m) + (float(l*j)/n))
                        suma += fourier[i,j]*np.exp(2*l*np.pi*x)
        listai[i,j] = suma

    return listai
ft = fourier2d(matriz)
print inversa2d(ft)




