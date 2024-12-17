

def obtener_datos():
    from sklearn.datasets import fetch_openml
    mnist = fetch_openml('mnist_784', version = 1, as_frame = False)
    X,y = mnist.data, mnist.target 
    return X,y

if __name__=='__main__':
    pass 