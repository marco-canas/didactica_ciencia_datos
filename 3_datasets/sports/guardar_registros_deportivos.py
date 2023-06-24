import csv
import datetime

def solicitar_medicion():
    fecha = datetime.date.today().strftime("%d/%m/%Y")
    kilometraje = float(input("entre la distancia recorrida en kilometros: "))
    tiempo = float(input("entre el tiempo empleado en minutos: "))
    velocidad_promedio = kilometraje/(tiempo/60)
    velocidad_maxima = float(input("entre velocidad máxima: "))
    medicion = [fecha, kilometraje, tiempo, velocidad_promedio, velocidad_maxima]
    return medicion

def agregar_medicion(medicion):
    with open('registro.csv', "a", newline = "") as archivo_csv:
        writer = csv.writer(archivo_csv)
        writer.writerow(medicion)
    print("Infromación agregada al archivo correctamente")    

def main():
    print("Bienvenido al registro diario de mediciones de un deportista")
    while True:
        opcion = input("Desea agregar una medición o no (s/n): ")
        if opcion.lower() == 's':
            medicion = solicitar_medicion()
            agregar_medicion(medicion)
        else:
            break
            


if __name__ == "__main__":
    main() 
