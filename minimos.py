import numpy as np
import matplotlib.pyplot as plt


#Creación de arreglos
x = np.array([1,2,3,4,5,6,7,9])
y = np.array([4,5,6,7,8,9,10,11])


#Parámetros del Kernel
N = len(x)
sx = sum(x)
sx2 = sum(x**2)

#Construcción de Kernel
matriz = [
    [N,sx],
    [sx,sx2]
    ]


matriz = np.matrix(matriz)

#creación de vector de datos
sy = sum(y)
sxy = sum(x*y)
m2 = [sy,sxy]
m2 = np.matrix(m2)

#Inversión de matriz
minv = np.linalg.inv(matriz)

#Obtención de coeficientes
coef = minv*m2.T
coef = np.array(coef)
print(coef)

#ecuación de la recta
y2 = coef[1]*x + coef[0]

#gráficado 
plt.plot(x,y,'ro')
plt.title('Minímos cuadrados')
plt.xlabel('x')
plt.ylabel('y')
plt.plot(x,y2)
plt.show()

