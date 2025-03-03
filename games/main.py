'''
Programa principal de games
'''

from Athlete import Athlete
from Sport import Sport
from Team import Team
from Game import Game
import game_logic as gl
import json

def main(archivo_torneo:str):
    '''
    Función principal de games
    '''

    if archivo_torneo != "":
        with(open(archivo_torneo,"r",encoding="utf-8")) as f:
            torneo = json.load(f)
    else:
        gl.create_gamefile()
        archivo_torneo = "torneo.json"
        with(open(archivo_torneo,"r",encoding="utf-8")) as f:
            torneo = json.load(f)
    

        # Jugar todos los juegos del torneo
    gl.play_game(torneo)
    #for juego in torneo:
     #   print(juego['score'])
    tablero = gl.scoring(torneo)
    gl.display_tablero(tablero)

if __name__ == "__main__":
    archivo_torneo = ""
    main(archivo_torneo)
 
    


