# Este archivo .py es para las funciones asociadas al capítulo 10 de Geron

def obtener_datos_fashion_mnist():
    import tensorflow as tf 
    from tensorflow import keras
    fashion_mnist = keras.datasets.fashion_mnist
    (X_train_full, y_train_full), (X_test, y_test) = fashion_mnist.load_data()
    return (X_train_full, y_train_full), (X_test, y_test)


def graficar_datos():
    from sklearn.datasets import load_iris 
    X, y = load_iris(return_X_y = True) 
    X = X[:,(2,3)] 
    import matplotlib.pyplot as plt 
    ax = plt.gca() 
    ax.set(title = 'Visualización de datos de flores de iris', xlabel = 'Longitud del pétalo')
    ax.set_ylabel('ancho del pétalo')
    ax.axis( [ min(X[:, 0])-0.3, max(X[:,0])+0.3, min(X[:, 1])-0.3, max(X[:,1])+ 0.3 ]) 
    ax.plot(X[:, 0], X[:,1], 'o')
    ax.grid() 
    plt.savefig('Todo_el_dataset-iris.jpg')
     

if __name__=='__main__':
    pass 