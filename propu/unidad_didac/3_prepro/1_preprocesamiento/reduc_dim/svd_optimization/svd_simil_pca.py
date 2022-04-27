import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
#
# SVD
# Encuentra subespacio k-dimensional tal que proyectar los datos
# sobre dicho subespacio maximiza la suma de cuadrados de distancias
# al origen
#
# PCA
# Intenta preservar la suma de cuadrados de distancias al promedio de datos.

# def
def datos3d(n):
    np.random.seed(42)
    xs = 9 * np.random.randn(n) + 9
    ys = 3 * np.random.randn(n) + 3
    zs = xs + ys + 12 + 3 * np.array([np.random.randn() for _ in range(len(xs))])
    return np.c_[xs, ys, zs]

def dibuja_ejes():
    ax.plot([0, 20], [0, 0], [0, 0], 'y')
    ax.plot([0, 0], [0, 20], [0, 0], 'y')
    ax.plot([0, 0], [0, 0], [0, 20], 'y')

def dibuja_plano(a, b, c):
    xs = np.linspace(-20, 20, 20)
    ys = np.linspace(-20, 20, 20)
    x0s, y0s = np.meshgrid(xs, ys)
    z0s = (-a/c) * x0s + (-b/c) * y0s
    ax.plot_surface(x0s, y0s, z0s, alpha=0.4)

def matriz_proy(a, b, c):
    u = np.array([a, b, c]).reshape(-1, 1)
    return np.eye(3) - (1/(np.dot(u.T, u))) * np.dot(u, u.T)

plt.style.use("dark_background")
fig, ax = plt.subplots(subplot_kw={"projection":"3d"})
Data = datos3d(30)
Data_p = np.dot(Data, matriz_proy(-1, 1, 1))
ax.plot(Data[:, 0], Data[:, 1], Data[:, 2], 'o')
ax.plot(Data_p[:, 0], Data_p[:, 1], Data_p[:, 2], 'bo')
ax.grid(False)
ax.xaxis.pane.fill = False
ax.yaxis.pane.fill = False
ax.zaxis.pane.fill = False
ax.axis([-20, 20, -20, 20])
ax.set_xticks([])
ax.set_yticks([])
ax.set_zticks([])
dibuja_ejes()
dibuja_plano(-1, 1, 1)

plt.show()
