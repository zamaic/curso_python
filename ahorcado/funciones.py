'''
Funciones auxiliares del juego del ahorcado
'''
import string
import unicodedata
from random import choice
 
def carga_archivo_texto(archivo:str)->list:
    '''
    Carga un archivo de texto y devuelve una lista ocn las palabras del archivo
    '''
    with open(archivo,'r', encoding='utf-8') as file:
        oraciones=file.readlines()
    return oraciones
 
def carga_plantillas(nombre_plantilla:str)->dict:
    '''Carga las plantillas del juego a partir de un archivo de texto'''
    plantillas={}
    for i in range(6):
        plantillas[i]=carga_archivo_texto(f'./plantillas/{nombre_plantilla}-{i}.txt')
    return plantillas
 
def despliega_plantilla(diccionario:dict, nivel:int):
    '''Despliega una plantilla del juego'''
    if nivel>=0 and nivel<=5:
        template=diccionario[nivel]
        for renglon in template:
            print(renglon)
 
def obten_palabras(lista:list)->list:
    '''
    Obtiene las palabras de un texto
    '''
    texto = ' '.join(lista[120:])
    palabras = texto.split()
    # convertimos a minusculas
    minusculas = [palabra.lower() for palabra in palabras]
    set_palabras = set(minusculas)
    # removemos signos de puntuación y caracteres especiales
    set_palabras = {palabra.strip(string.punctuation) for palabra in set_palabras}
    # removemos números, paréntesis, corchetes y otros caracteres
    set_palabras = {palabra for palabra in set_palabras if palabra.isalpha()}
    # removemos acentos
    set_palabras = {unicodedata.normalize('NFKD', palabra).encode('ascii', 'ignore').decode('ascii') for palabra in set_palabras}
    return list(set_palabras)
 
def adivina_letra(abc:dict, palabra:str, letras_adivinadas:set, turnos:int):
    '''
    Adivina una letra de una palabra
    '''
    palabra_oculta = ""
    for letra in palabra:
        if letra in letras_adivinadas:
            palabra_oculta += letra
        else:
            palabra_oculta += "_"
    print(f'Tienes {turnos} oportunidades de fallar')
    abcd=' '.join(abc.values())
    print(f'El abecedario es: {abcd}')
    print(f'La palabra es: {palabra_oculta}')
    letra = input('Ingresa una letra: ')
    letra = letra.lower()
    if letra in abc:
        if abc[letra] == "*":
            print('Ya adivinaste esa letra')
        else:
            abc[letra]= "*"
            if letra in palabra:
                letras_adivinadas.add(letra)
            else:
                turnos -= 1
    return turnos
 
if __name__=='__main__':
    plantillas = carga_plantillas('plantilla')
    despliega_plantilla(plantillas, 5)
    lista_oraciones = carga_archivo_texto('./datos/pg15532.txt')
    lista_palabras = obten_palabras(lista_oraciones)
    print(len(lista_palabras))
    p = choice(lista_palabras)
    print(p)
    abcdario = {letra:letra for letra in string.ascii_lowercase}
    adivinadas = set()
    t = 5 # oportunidades
    t=adivina_letra(abcdario, p, adivinadas, t)
    t=adivina_letra(abcdario, p, adivinadas, t)
    print(t)
 
'''Programa principal del juego del ahorcado'''
 
import os
import string
import unicodedata
import argparse
from random import choice
import funciones as fn
 
def main(archivo_texto:str, nombre_plantilla='plantilla'):
    '''Programa principal'''
    #cargamos las plantillas
    plantillas=fn.carga_plantillas(nombre_plantilla)
    lista_oraciones=fn.carga_archivo_texto(archivo_texto)
    palabras=fn.obten_palabras(lista_oraciones)
    o = 5 #oportunidades
    p = choice(palabras)
    abcdario={letra:letra for letra in string.ascii_lowercase}
    adivinadas=set()
    while o > 0:
        fn.despliega_plantilla(plantillas, o)
        o=fn.adivina_letra(abcdario, p, adivinadas, o)
        if p== ''.join([letra if letra in adivinadas else '_' for letra in p]):
            print('¡Felicidades, adivinaste la palabra!')
            break
    fn.despliega_plantilla(plantillas,o)
    print(f"La palabra era: {p}")
 
if __name__=='__main__':
    parser=argparse.ArgumentParser(description='Juego del ahorcado')
    parser.add_argument('-a','--archivo', help='Archivo de texto con palabras', default='./datos/pg15532.txt')
    args=parser.parse_args()
    archivo=args.archivo
    if os.stat(archivo)==False:
        print(f'El archivo "{archivo}" no existe')
        exit()
    main(archivo)
 