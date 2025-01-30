'''
tablero.py: Dibuja el tablero del juego del gato
'''

import random

def dibuja_tablero(simbolos:dict):
    '''
    Dibuja el tablero del juego del gato
    '''

    print(f'''
    {simbolos['1']} | {simbolos['2']} | {simbolos['3']}
    ---------
    {simbolos['4']} | {simbolos['5']} | {simbolos['6']}
    ---------
    {simbolos['7']} | {simbolos['8']} | {simbolos['9']}
    ''')

def ia(simbolos:dict):
    '''
    Juega la máquina
    '''
    ocupado = True
    while ocupado == True:
        x = random.choice(list(simbolos.keys()))
        if simbolos[x]  not in ['X','O']:
            simbolos[x]='O'
            ocupado = False


def usuario(simbolos:dict):
    '''
    Juega el usuario
    '''
    lista_numeros = [str(i) for i in range(1,10)]
    ocupado = True
    while ocupado is True:
        x = input('Ingresa el número de la casilla: ')
        if x in lista_numeros:
            if simbolos[x] not in ['X','O']:
                simbolos[x] = 'X'
                ocupado = False
            else:
                print('Casilla ocupada')
        else:
            print('Número incorrecto')
 
if __name__ == '__main__':
    numeros = [str(i) for i in range(1,10)]
    dsimbolos = {x:x for x in numeros}
    dibuja_tablero(dsimbolos)
    ia(dsimbolos)
    dibuja_tablero(dsimbolos)
    usuario(dsimbolos)
    dibuja_tablero(dsimbolos)
    '''
    x = random.choice(numeros)
    numeros.remove(x)
    dsimbolos[x] = 'X'
    dibuja_tablero(dsimbolos)
    o = random.choice(numeros)
    numeros.remove(o)
    dsimbolos[o] = 'O'
    dibuja_tablero(dsimbolos)
    print(numeros)
    '''