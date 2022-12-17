def dividir_entrenamiento_testeo(datos, tasa_testeo):
    from sklearn.model_selection import train_test_split
    datos_train, datos_test = train_test_split(datos, test_size=tasa_testeo ) 
    return datos_train, datos_test


if __name__=='__main__':
    pass 