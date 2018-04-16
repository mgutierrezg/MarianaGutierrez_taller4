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
	global M, N
	M=(np.shape(mat)[0])
	N=(np.shape(mat)[1])
	lista =np.zeros((M,N), dtype= complex)
	for k in range(M):
		for l in range(N):
			suma = 0.0
			for i in range(M):
				for j in range(N):
					exponencial = np.exp(-2j*np.pi*(float(k*i)/M + float(l*j)/N))
					suma += mat[i, j]* exponencial
		        lista[l][k] = suma / M /N 
	return lista


def inversa_2d(fourier):
	global M, N 
        lista =np.zeros((M,N), dtype= float)
	for i in range(M):
		for j in range(N):
			suma = 0.0
			for k in range(M):
				for l in range(N):
					exponencial = np.exp(2j*np.pi*(float(k*i)/M + float(l*j)/N))
					suma += fourier[l][k] * exponencial
	  
		        lista[i,j]= (suma.real)
        return lista

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
        final = inversa_2d(convol)
        plt.imsave("altas.png", final[:,:],cmap= "gray")
    elif alto_bajo == "bajo":
        matriz = matriz_bn(imagen)
        ft_imagen = f_2d(matriz)
        baja = bajos(ft_imagen)
        gauss1 = gauss()
        kernel = f_2d(gauss1)
        convol = kernel*baja
        final = inversa_2d(convol)
        plt.imsave("bajas.png", final[:,:],cmap= "gray")
            
ejecuta(alto_bajo)
