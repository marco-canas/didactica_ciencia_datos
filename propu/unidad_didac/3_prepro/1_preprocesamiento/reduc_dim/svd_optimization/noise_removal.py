# Un hecho interesante sobre la reducción dimensional, es que a menudo reduce la cantidad de ruido en los datos.
# Por ejemplo, una imagen con algún monto de ruido puede ser reconstruida con el SVD truncado.

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

img = mpimg.imread('lena.png')
img.shape

img = img[:, :, 1] # solo en verde
plt.imshow(img)

noise = np.zeros_like(img)
img_copy = img.copy()
img_copy[100:104, :250] = 0.2 * np.random.rand(4, 250)
plt.imshow(img_copy)
u, s, vh = np.linalg.svd(img_copy)
u.shape
s.shape
vh.shape

k = 20
img_whited = u[:, :k] @ np.diag(s[:k]) @ vh[:k, :]
plt.imshow(img_whited)

def condi(i,j):
    return 1 * (np.abs(i - j) <= 50)

diag_noise = np.array([[0.1 * condi(i,j) for j in range(512)] for i in range(512)])
new_img_copy = img.copy()
new_img_copy += diag_noise
plt.imshow(new_img_copy)

u, s, vh = np.linalg.svd(new_img_copy)
k = 15
img_whited = u[:, :k] @ np.diag(s[:k]) @ vh[:k, :]
plt.imshow(img_whited)


# Preprocesamiento y limpieza de atributos en ML
PCA es usado en principio para reducción dimensional. Luego se buscará normalizar la nueva representación de los datos, de tal manera
que la varianza en cada dirección transformada sea la misma.

Sea $V _{k } $ de orden $d\times k$ la matriz cuyas columnas son los $k$ vectores o direcciones principales obtenidas con PCA.
1) Halle la representación $k$-dimensional de los datos, así $U _{k } = D V _{k } $.

2) Divida cada columna de $U _{k } $ por su desviación estándar (proceso conocido como whitening).

Algoritmos como SGD trabajan mejor luego de el Preprocesamiento que se acaba de describir.

En aprendizaje no supervisado se pude usar el preprocesamiento descrito para detectar datos atípicos.
La práctica de los pasos anteriores, hace que se incremente la distancia absoluta de los datos atípicos hasta
la media en las direcciones de baja varianza, permitiendo descrubir datos atípicos no obvios.

import numpy as np
import matplotlib.pyplot as plt

data = np.c_[9 * np.random.randn(100, 1), 3 * np.random.randn(100, 1), 1 * np.random.randn(100, 1)]
data[95:, 2] = [5,6, -5, -6, 5]
data[90:, :]

fig, ax = plt.subplots(subplot_kw={"projection":"3d"})
plt.plot(data[:, 0], data[:, 1], data[:, 2], 'o')

data_meaned = data - data.mean(axis=0)
u, s, vh = np.linalg.svd(data_meaned)
data_tr = u[:, :2] @ np.diag(s[:2]) @ vh[:2, :]
fig, ax = plt.subplots(subplot_kw={"projection":"3d"})
plt.plot(data_tr[:, 0], data_tr[:, 1], data_tr[:, 2], 'o')

data_whited = data_tr / data_tr.std(axis=0)

fig, ax = plt.subplots(subplot_kw={"projection":"3d"})
plt.plot(data_whited[:, 0], data_whited[:, 1], data_whited[:, 2], 'o')

def maha(X):
    X_meaned = (X - data.mean(axis=0)).reshape(1, -1)
    C = np.cov(data.T)
    return np.dot(X_meaned, np.dot(np.linalg.inv(C), X_meaned.T))[0]

mahas = [maha(X) for X in data]
plt.plot(mahas)
