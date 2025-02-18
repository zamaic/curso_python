'''
Programa principal del juego del ahorcado
'''

import funciones as fn
from random import choice
import string
import os
import unicodedata
import argparse


def main(archivo_texto:str,nombre_plantilla='plantilla'):
    '''
    Programa principal
    '''
    # Cargamos las plantillas
    plantillas = fn.carga_plantillas(nombre_plantilla)
    lista_oraciones = fn.carga_archivo_texto(archivo_texto)
    palabras = fn.obten_palabras(lista_oraciones)
    o = 5 
    p = choice(palabras)
    abecedario = {letra:letra for letra in string.ascii_lowercase}
    adivinadas = set()
    while o>1:
        fn.despliega_plantilla(plantillas,o)
        o = fn.adivinar_letra(abecedario,p,adivinadas,o)
        if p == ''.join([letra if letra in adivinadas else '_' for letra in p]):
            print('Ganaste')
            break
    fn.despliega_plantilla(plantillas,o)
    print(f"La palabra era {p}")

if __name__ == '__main__':
    parse = argparse.ArgumentParser(description='Juego del ahorcado')
    parser.add_argument('-a','--archivo', help='Archivo de texto con palabras', default= './datos/pg15532.txt')
    args = parser.parse_args()
    archivo = args.archivo
    if os.stat(archivo) == False:
        print('El archivo {archivo} no existe')
        exit()
    main(archivo)