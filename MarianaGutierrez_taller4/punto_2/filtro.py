import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import sys

#Funcion para caragar una imagen
alto_bajo = sys.argv[2]
imagen = sys.argv[1]

def matriz_bn(imagen):
    imagen = Image.open(imagen)
    negra = imagen.convert('L')
    negra.save("bk.png")
    matriz = plt.imread("bk.png")
    return matriz 

matriz = matriz_bn(imagen)
M=(np.shape(matriz)[0])
N=(np.shape(matriz)[1])

def gauss():
    global M,N
    x = np.linspace(0.0,N-1,N)
    y = np.linspace(0.0,M-1,M)
    x, y = np.meshgrid(x,y)
    sigma = 1.0
    m = 0.0
    d= (x*x+y*y)**0.5
    formula = np.exp(-( (d-m)**2 / ( 2.0 * sigma**2.0 ) ) )
	
    return formula

def f_2d(mat):
    global M,N

    M=(np.shape(mat)[0])
    N=(np.shape(mat)[1])
	
    lista= np.zeros((M,N), dtype=complex)
	
    for i in range (M):

        for j in range(N):
	    suma=0.0
	    for a in range(M):
		for b in range(N):
		    x=((float(i*a)/M)+ (float(j*b)/N))
		    suma += mat[a,b]*np.exp(-2j*np.pi*x)
				
	lista[i,j]=suma/M/N
    return lista

def inversa2d(mat):
    global M,N
    M=(np.shape(mat)[0])
    N=(np.shape(mat)[1])
    fourieri = np.zeros((M,N),dtype=float)
    for a in range(M):
        for b in range(N):
            suma = 0.0
            for i in range(M):
                for j in range(N):
                    x=(float(i*a)/M + float(j*b)/N) 
                    suma += mat[i,j]*np.exp(2j*np.pi*x)
        fourieri[a,b] = (suma.real)

        return fourieri 


def altos(mat):
    global M,N
    M=(np.shape(mat)[0])
    N=(np.shape(mat)[1])
    for i in range(M):
        for j in range(N):
            if (mat[i][j] <0.03):
                mat[i][j] = 0
        return mat[i][j]
def bajos(mat):
    global M,N
    M=(np.shape(mat)[0])
    N=(np.shape(mat)[1])
    for i in range(M):
        for j in range(N):
            if (mat[i][j] >0.03):
                mat[i][j] = 0
        return mat[i][j]


def ejecuta(alto_bajo):
    if alto_bajo == "alto":
        matriz = matriz_bn(imagen)
        ft_imagen = f_2d(matriz)
        alta = altos(ft_imagen)
        gauss1 = gauss()
        kernel = f_2d(gauss1)
        convol = kernel*alta
        final = inversa2d(convol)
        plt.imsave("altas.png", final[:,:],cmap= "gray")
    elif alto_bajo == "bajo":
        matriz = matriz_bn(imagen)
        ft_imagen = f_2d(matriz)
        baja = bajos(ft_imagen)
        gauss1 = gauss()
        kernel = f_2d(gauss1)
        convol = kernel*baja
        final = inversa2d(convol)
        plt.imsave("bajas.png", final[:,:],cmap= "gray")
            
ejecuta(alto_bajo)
