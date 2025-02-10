'''
Este archivo es el punto de entrada de la aplicación
'''
import tablero

def main():
    '''
    Función principal
    '''
    nombre = tablero.obtener_nombre()
    X = {"G":0,"P":0,"E":0}
    O = {"G":0,"P":0,"E":0}
    score = {"X":X,"O":O}
    numeros = [str(i) for i in range(1,10)]   
    corriendo = True
    while corriendo:
        dsimbolos = {x:x for x in numeros}
        g = tablero.juego(dsimbolos)
        tablero.actualiza_score(score,g,nombre)
        tablero.despliega_tablero(score,nombre)
        seguir = input('¿Gustas seguir jugando? (s/n): ')
        if seguir.lower() == 'n':
            corriendo = False
    

if __name__ == '__main__':
    main()