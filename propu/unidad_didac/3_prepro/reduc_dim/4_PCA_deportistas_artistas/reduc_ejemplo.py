from deportistas_y_artistas import *
import numpy as np
import re
import pandas as pd
import nltk
from nltk.tokenize import WordPunctTokenizer
nltk.download('stopwords')
from nltk.corpus import stopwords
from collections import Counter


personajes = [eric_clapton, amy_winehouse, ruben_blades,
              juan_cuadrado, maria_sharapova, kevin_durant]


def todo(personaje):
    cadenas = WordPunctTokenizer().tokenize(personaje)

    depurado=[]
    for token in cadenas:
        token = token.lower()
        # remove any value that are not alphabetical
        new_token = re.sub(r'[^a-zA-Z]+', '', token)
        # remove empty value and single character value
        if new_token != "" and len(new_token) >= 2:
            vowels=len([v for v in new_token if v in "aeiou"])
            if vowels != 0: # remove line that only contains consonants
                depurado.append(new_token)


    # Get the list of stop words
    stop_words = stopwords.words('english')
    # add new stopwords to the list
    stop_words.extend(["could","though","would","also","many",'much'])
    # Remove the stopwords from the list of tokens
    tokens = [x for x in depurado if x not in stop_words]

    return tokens

def todo_dic(personaje):
    tokens = todo(personaje)
    return dict(Counter(tokens))

def diccionario_compartido(personajes):
    palabras = []
    for personaje in personajes:
        for palabra, frecuencia in Counter(todo(personaje)).most_common(30):
            palabras.append(palabra)
    return palabras

dic_compartido = diccionario_compartido(personajes)

def personaje_a_vector(personaje, dic_compartido):
    valores = []
    for palabra in dic_compartido:
        if palabra in todo(personaje):
            valores.append(todo_dic(personaje)[palabra])
        else:
            valores.append(0)
    return np.array(valores).reshape(1, -1)

data_np = np.r_[personaje_a_vector(juan_cuadrado, dic_compartido),
             personaje_a_vector(kevin_durant, dic_compartido),
             personaje_a_vector(maria_sharapova, dic_compartido),
             personaje_a_vector(ruben_blades, dic_compartido),
             personaje_a_vector(eric_clapton, dic_compartido),
             personaje_a_vector(amy_winehouse, dic_compartido)]

data = pd.DataFrame(data_np, columns=dic_compartido)
print(data.head(6))

print(len(dic_compartido))
print("")
print(len(data))
