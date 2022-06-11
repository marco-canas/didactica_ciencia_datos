# SEGURIDAD DE PUENTES Abajóse muestran los resultados  
# de un reporte del 2007 de la condición de los puentes
# de carreteras en E.U. Cada puente se clasificó como 
# seguro, en necesidad de reparación o debe reemplazarse. 
# Complete la tabla.
# con control 1 hacemos que el texto se vuelva un comentario

"""
Optra manera de comentarizar es con el uso de las tres comillas
SEGURIDAD DE PUENTES Abajóse muestran los resultados  
de un reporte del 2007 de la condición de los puentes
de carreteras en E.U. Cada puente se clasificó como 
seguro, en necesidad de reparación o debe reemplazarse. 
Complete la tabla.
con control 1 hacemos que el texto se vuelva un comentario
"""
# print(':'*30)
# print('Aplicación de seguridad de puentes')
# n_puentes_seguros = 445_396
# n_puestes_no_repararse = 72_033
# n_puestes_seguros_reemplazarse = 80_447
# n_total_puentes = n_puentes_seguros
# +n_puestes_no_repararse+n_puestes_seguros_reemplazarse
# print()
# print('El número total de puestes en 2007', n_total_puentes)

# Cada tren del metro de la Ciudad de México tiene 9 vagones, 
# cada uno con 8 puertas y cada una de dos hojas corredizas. 
# Si se desea cambiar las hojas de los 120 trenes existentes 
# en la ciudad, ¿cuántas hojas se van a cambiar?

# print()
# print(':'*30)
# vagones=9
# puertas=8
# hojas=2
# trenes = 120
# hojas_a_cambiar = vagones*puertas*hojas*trenes
# print('El número de hojas a cambiar es: ', hojas_a_cambiar)
# print(f'El número total de Hojas a Cambiar es: {hojas_a_cambiar:,.0f}')


# En un camión de transporte de gaseosas caben 20 cajas. 
# Cada una con 35 canastas y cada canasta con 30 gaseosas.
# a.	¿Cuántas gaseosas puede llevar un camión completamente cargado?
# b.	Si tienen 1 186 500 gaseosas para transportar, 
# ¿Cuántos camiones se requieren? 
# ¿Cuántas gaseosas llevaría el camión que no está completamente cargado?

# print()
# print(':'*30)

# cajas_x_camion = 20
# canastas_x_caja = 35
# gaseosas_x_caja = 30
# total_gas_x_camion = cajas_x_camion*canastas_x_caja*gaseosas_x_caja 



# print('a. Un camión puede llevar ', total_gas_x_camion, 'gaseosas') 

# print('b. se necesitan', 1186500//total_gas_x_camion, 'mas un camión con'
#       ,186500%total_gas_x_camion, 'gaseosas')

# print(5758//73)
# print('El residuo de las gaseosas es:', 5758%73)

# print()
# print(':'*30)


# # DIVISIÓN CELULAR Después de 1 hora, 
# # una célula se ha dividido para formar otra célula. 
# # En otra hora, estas dos células se han dividido por 
# # lo que existen cuatro células. En otra hora, estas 
# # cuatro células se dividen por lo que existen ocho.
# # ¿Cuántas células existen al final de la cuarta hora?


# def n_celulas(t):
#     print('El número de células después de la hora', t, 'es: ', 2**t)
    
# n_celulas(4)

# print(pow(2,4)) 


# Después de t años, el saldo A en una cuenta con capital inicial P 
# y tasa anual de interés r (en forma decimal) está dado por las 
# fórmulas siguientes.
# Se invierte un total de $12 000 a una tasa anual de interés de 9%. 
# Encuentre el saldo después de 5 años si se capitaliza
# a.	Trimestralmente.
# b.	Mensualmente.
# c.	Continuamente

# p = 12_000 # valor inicial en USA
# r = 0.09 # tasa efectiva anual en decimal 
# t = 5    # tiempo en años


# #parte a. Interés trimestral
# n = 3 # interés trimestral

# A = p*pow(1+r/n, n*t)
# print('El total que se capitaliza trimestralmente es', A)

# #parte b. 
# n = 12 # interés mensual

# A = p*pow(1+r/n, n*t)
# print('El total que se capitaliza mensualmente es',round(A,2)) 

# import math as m

# print(m.exp(1)) 

# A = p*m.exp(r*t)

# print('El total que se capitaliza continuamente es',round(A,2)) 

#%%

# import numpy as np 

# print(np.sqrt(4))

# print(np.exp(1))

# import math as m 

# print(m.exp(1))

# # calcule el volumen de un cilindro
# r = 1
# h = 1
# v = np.pi*r**2*h
# print(v)
#%%

# print('ilustracion de la instrucción dir')

# print('ella permite saber las propiedades y métodos de una variable')
#%%

# nombre = 'Marco'

# #print(dir(nombre)) 

# nombre_nuevo = nombre.upper()
# print(nombre_nuevo) 

# nombre_nuevo = nombre.lower()
# print(nombre_nuevo) 

# nombre_nuevo = nombre.replace('M', 'N')
# print(nombre_nuevo)

# nombre_nuevo = nombre.count('c')
# print(nombre_nuevo)

# nombre_nuevo = nombre.startswith('N')
# print(nombre_nuevo)

#%%

# help(pow)

# print('varias formas de unir texto')
# segundo_nombre = 'julio'
# print(f'unimos Marco con {segundo_nombre}')
# b = str(5)
# print(b)

#%%

# c = 0.5

# print(f'expresar en forma porcentual {c:0.2%}')

# print(f'expresar en forma porcentual {c:,.2f}')

#%%


print(input('numero de puentes seguros: '))

