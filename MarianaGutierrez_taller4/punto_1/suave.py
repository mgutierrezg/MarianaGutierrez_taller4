import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import sys
#Funcion para caragar una imagen
n_pixel_kernell = sys.argv[2]
imagen = sys.argv[1]

def matriz_bn(imagen):
    imagen = Image.open("imagen.png")
    negra = imagen.convert('L')
    negra.save("bk.png")
    matriz = plt.imread("bk.png")
    return matriz 

matriz = matriz_bn(imagen)
M=(np.shape(matriz)[0])
N=(np.shape(matriz)[1])

def gauss(n_pixel_kernell):
    global M,N
    x = np.linspace(0.0,N-1,N)
    y = np.linspace(0.0,M-1,M)
    x, y = np.meshgrid(x,y)
    m = 0.0
    d= (x*x+y*y)**0.5
    formula = np.exp(-( (d-m)**2 / ( 2.0 * n_pixel_kernell**2 ) ) )
	
    return formula

def f_2d(mat):
    global M,N
    M=(np.shape(matriz)[0])
    N=(np.shape(matriz)[1])
    lista = np.zeros((M,N),dtype=np.complex)
    for k in range(M):
        for l in range(N):
             suma = 0.0
             for i in range(M):
                 for j in range(N):
                    expo = np.exp(-2j*np.pi*(float(k*i)/M + float(l*j)/N))
                    suma += mat[i,j]*expo
        lista[k,l] = suma/M/N

    return lista


def inversa2d(fourier):
    global M,N
    M=(np.shape(matriz)[0])
    N=(np.shape(matriz)[1])
    fourieri = np.zeros((M,N),dtype=float)
    for a in range(M):
        for b in range(N):
            suma = 0.0
            for i in range(M):
                for j in range(N):
                    x=(float(i*a)/M + float(j*b)/N) 
                    suma += fourier[i,j]*np.exp(2j*np.pi*x)
        fourieri[a,b] = (suma.real)

        return fourieri 


#Aca se mete n_pixel_kernell
n_pixel_kernell = 2
matriz = matriz_bn(imagen)
ft_imagen = f_2d(matriz)
gauss = gauss(n_pixel_kernell)
kernel = f_2d(gauss)
convol = kernel*ft_imagen
final = inversa2d(kernel*ft_imagen)
plt.imsave("suave.png", final[:,:],cmap= "gray")


