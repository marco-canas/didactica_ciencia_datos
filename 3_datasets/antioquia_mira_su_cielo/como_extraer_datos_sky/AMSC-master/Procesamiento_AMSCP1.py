#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Autor:Luisa Fernanda Buriticá Ruíz
# Fecha:22 junio de 2023
# Conctacto:fernanda.buritica@udea.edu.co
###############################################################################
# 1. LIBRERIAS
# 1.1 Librerías importadas
# 1.2 Modulos importados
from AMSC import resumen_estacion,resumen_estacion_andes,resumen_estacion_oriente,resumen_estacion_pb,resumen_estacion_sonson
###############################################################################
# 3. INFORMACIÓN DE ENTRADA

# 3.1 Direcciones de entrada y salida
path_in=r"/home/luisa/Descargas/Seminario_AMSC_20072023/AMSC-master/Entrada/"# Carpeta de entrada
path_out1=r"/home/luisa/Descargas/Seminario_AMSC_20072023/AMSC-master/Salida/"#Carpeta de salida
# 3.2 Carpeta
# 3.3 Vectores
columnas=["Tiempo Sistema","Outside Temperature","Wind Speed","Wind Direction","Outside Humidity",
          "Barometer","Rain Rate","UV","Solar Radiation"]
columnas_xlsx=[
    "Date",
    "Time",
    "Out_Temp",
    "Hi_Temp",
    "Low_Temp",
    "Out_Hum",
    "Dew_Pt",
    "Wind_Speed",
    "Wind_Dir",
    "Wind_Run",
    "Hi_Speed",
    "Hi_Dir",
    "Wind_Chill",
    "Head_Index",
    "THW_Index",
    "THSW_Index",
    "Bar",
    "Rain",
    "Rain_Rate",
    "Solar_Rad",
    "Solar_Energy"
    ]
columnas_CSV=['Timestamp','Outdoor Temperature', 'Wind Speed','Wind Direction','Outdoor Humidity',
              'Barometric Pressure','Rain']
###############################################################################
# 4. PROCESOS
#-----------------------------------------------------------------------------#

def Procesamiento_Datos_AMSC(Estacion):
    tipo1=["arboletes","caucasia","itm","santafe","turbo","yarumal"]
    if Estacion in tipo1:
        resumen_estacion(Estacion,path_in,columnas,path_out1)
    if Estacion in ["andes"]:
        resumen_estacion_andes(Estacion,path_in,columnas_xlsx,path_out1)
    if Estacion in ["oriente"]:
        print("Oriente")
        resumen_estacion_oriente(Estacion,path_in,columnas,path_out1)
    if Estacion in ["pb"]:
        print("Puerto Berrio")
        resumen_estacion_pb(Estacion,path_in,columnas_CSV,path_out1)
    if Estacion in ["sonson"]:
        resumen_estacion_sonson(Estacion,path_in,columnas,path_out1)

#Procesamiento_Datos_AMSC("arboletes")
Procesamiento_Datos_AMSC("caucasia")
#Procesamiento_Datos_AMSC("itm")
#Procesamiento_Datos_AMSC("santafe")
#Procesamiento_Datos_AMSC("turbo")
#Procesamiento_Datos_AMSC("yarumal")
#Procesamiento_Datos_AMSC("andes")
#Procesamiento_Datos_AMSC("oriente")
#Procesamiento_Datos_AMSC("pb")
#Procesamiento_Datos_AMSC("sonson")
############################## FIN CODIGO #####################################