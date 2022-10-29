# Este archivo .py es para las funciones asociadas al capítulo 10 de Geron

def obtener_datos_fashion_mnist():
    import tensorflow as tf 
    from tensorflow import keras
    fashion_mnist = keras.datasets.fashion_mnist
    (X_train_full, y_train_full), (X_test, y_test) = fashion_mnist.load_data()
    return (X_train_full, y_train_full), (X_test, y_test)


if __name__=='__main__':
    pass 