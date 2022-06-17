
import numpy as np 
print(np.exp(2)) 

#%%

# Tuplas

a = (1,3,5)
print(a)

print(len(a))
print(a[0]) 
print(a[-1])

b = ('marco', 'julio', 'canas', 'campillo')
print(b[1])
print(type(b))
print(type(b[2]))
#%%
# Listas en python

lista1 = ['marco', 23, 19, 31, True, False]
print(lista1)
lista1[0] = 513
print(lista1)
print(dir(lista1)) 
# así puedo ver los métodos y atributos asociados al tipo lista
lista1.append(3.14)
print(lista1)


#%%

# Conversión de tipos

print(list(a)) 
print('marco' in lista1)

#%%

print(list(range(5))) # range permite crear secuencias de números enteros
print(tuple(range(13,5,-1)))

print(list(range(0,20,2)))

