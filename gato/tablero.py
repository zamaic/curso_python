'''
tablero.py: Dibuja el tablero del juego del gato
'''
import random
import sys

def obtener_nombre():
    '''Obtiene el nombre del jugador desde los argumentos de la terminal'''
    if len(sys.argv) > 1:
        return sys.argv[1]
    return "Usuario"

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


def ia(simbolos: dict):
    '''
    IA mejorada para tratar de ganar o bloquear al jugador
    '''
    lista_combinaciones = [
        ['1','2','3'], ['4','5','6'], ['7','8','9'],
        ['1','4','7'], ['2','5','8'], ['3','6','9'],
        ['1','5','9'], ['3','5','7']
    ]
    
    # 1. Verificar si la IA puede ganar en el siguiente movimiento
    for combo in lista_combinaciones:
        valores = [simbolos[c] for c in combo]
        if valores.count('O') == 2 and valores.count('X') == 0:
            for c in combo:
                if simbolos[c] not in ['X', 'O']:
                    simbolos[c] = 'O'
                    return
    
    # 2. Bloquear al jugador si está a punto de ganar
    for combo in lista_combinaciones:
        valores = [simbolos[c] for c in combo]
        if valores.count('X') == 2 and valores.count('O') == 0:
            for c in combo:
                if simbolos[c] not in ['X', 'O']:
                    simbolos[c] = 'O'
                    return
    
    # 3. Si no hay jugadas críticas, hacer un movimiento aleatorio
    opciones = [c for c in simbolos if simbolos[c] not in ['X', 'O']]
    if opciones:
        simbolos[random.choice(opciones)] = 'O'

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
 
def juego(simbolos:dict):
    '''
    Juego del gato
    '''
    lista_combinaciones = [
        ['1','2','3'],
        ['4','5','6'],
        ['7','8','9'],
        ['1','4','7'],
        ['2','5','8'],
        ['3','6','9'],
        ['1','5','9'],
        ['3','5','7']
    ]

    en_juego = True
    dibuja_tablero(simbolos)
    movimientos = 0
    gana = None
    while en_juego:
        usuario(simbolos)
        dibuja_tablero(simbolos)
        movimientos += 1
        gana = checa_winner(simbolos,lista_combinaciones)
        if gana is not None:
            en_juego=False
            continue
        if movimientos >=9:
            en_juego = False
            continue
        ia(simbolos)
        dibuja_tablero(simbolos)
        movimientos += 1
        gana = checa_winner(simbolos,lista_combinaciones)
        if gana is not None:
            en_juego=False
            continue
        if movimientos >= 9:
            en_juego = False
            continue
    return gana
        


def checa_winner(simbolos:dict,combinaciones:list):
    '''Checa si hay un ganador'''
    for c in combinaciones:
        if simbolos[c[0]] == simbolos[c[1]] == simbolos[c[2]]:
            return simbolos[c[0]]
    return None

def actualiza_score(score:dict,ganador:str, nombre:str):
    '''Actualiza el score'''
    X = score["X"]
    O = score["O"]
    if ganador is not None:
        print(f'El ganador es {ganador}')
        if ganador == 'X':
            X["G"] += 1
            O["P"] += 1
        elif ganador == 'O':
            O["G"] += 1
            X["P"] += 1
        else:
            X["E"] += 1
            O["E"] += 1
    else:
        print('Empate')
        X["E"] += 1
        O["E"] += 1

def despliega_tablero(score: dict, nombre: str):
    '''Despliega el tablero de score con mejor formato'''
    ancho = max(len(nombre), len("Computadora"))  # Calcula el ancho máximo para alinear
    nombre_formateado = nombre.ljust(ancho)  # Ajusta el ancho con espacios
    computadora_formateada = "Computadora".ljust(ancho)

    print(f'''
    {nombre_formateado} X | G: {score["X"]["G"]} | P: {score["X"]["P"]} | E: {score["X"]["E"]}
    {computadora_formateada} O | G: {score["O"]["G"]} | P: {score["O"]["P"]} | E: {score["O"]["E"]}
''')


if __name__ == '__main__':
    numeros = [str(i) for i in range(1,10)]
    dsimbolos = {x:x for x in numeros}
    g = juego(dsimbolos)
    if g is not None:
        print(f'El ganador es: {g}')
    else:
        print('Empate')
    