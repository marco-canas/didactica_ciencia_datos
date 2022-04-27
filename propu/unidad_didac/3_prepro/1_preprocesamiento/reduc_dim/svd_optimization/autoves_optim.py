import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols

x, y = symbols('x y')
X = np.array([x, y]).reshape(-1, 1)
A = np.array([[2, -1],
              [-1, 2]])

X1 = np.linalg.eig(A)[1].T[0]
X2 = np.linalg.eig(A)[1].T[1]


forma = np.dot(X.T, np.dot(A, X))[0, 0]

def L(xx, yy):
    return float((forma.subs(x, xx)).subs(y, yy))


xx, yy = np.linspace(-3, 3, 20), np.linspace(-3, 3, 20)
x0s, y0s = np.meshgrid(xx, yy)
XX = np.c_[x0s.ravel(), y0s.ravel()]
z0s = np.array([L(XX[i][0], XX[i][1]) for i in range(len(XX))])
z0s = z0s.reshape(x0s.shape)



theta = np.linspace(0, 2 * np.pi)
xe = np.cos(theta)
ye = np.sin(theta)
X_circ = np.c_[xe, ye]
X_elip = np.dot(X_circ, A)
Z_elip = np.array([L(X_elip[i, 0], X_elip[i, 1]) for i in range(len(X_elip))])


plt.style.use("dark_background")
fig, ax = plt.subplots(1, subplot_kw={'projection':'3d'})

ax.grid(False)
ax.xaxis.pane.fill = False
ax.yaxis.pane.fill = False
ax.zaxis.pane.fill = False
ax.plot_surface(x0s, y0s, z0s, alpha=0.4)
ax.plot(X_elip[:, 0], X_elip[:, 1], np.zeros_like(X_elip[:, 0]))
ax.plot(X_elip[:, 0], X_elip[:, 1], Z_elip, color='blue', linewidth=2)
ax.plot([0, X1[0]], [0, X1[1]], [0,0], color='red')
ax.plot([0, X2[0]], [0, X2[1]], [0,0], color='red')
plt.show()
