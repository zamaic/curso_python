'''
Programa principal de games
'''

from Athlete import Athlete
from Sport import Sport
from Team import Team
from Game import Game
import json

def main(archivo_torneo:str):
    '''
    Función principal de games
    '''

    if archivo_torneo != "":
        with(open(archivo_torneo,"r",encoding="utf-8")) as f:
            torneo = json.load(archivo_torneo)
    else:
        players_mexico = ['Chicharito','Chucky','Ochoa','Tecatito,','Guardado','Herrera','Layun','Moreno','Araujo','Oribe','Jimenez']
        players_espania = ['Casillas','Ramos','Pique','Iniesta','Silva','Isco','Busquets','Costa','Moreta','Asensio']
        players_brasil = ['Neymar', 'Coutinho', 'Marcelo', 'Casemiro', 'Alisson', 'Jesus', 'Silva', 'Firmino', 'Danilo']
        players_argentina = ['Messi', 'Aguero', 'Di Maria', 'Mascherano', 'Higuain', 'Dybala', 'Otamendi', 'Romero', 'Mascherano', 'Rojo', 'Bsnega', 'Caballero']
        lista_mexico = [Athlete(x) for x in players_mexico]
        lista_espania = [Athlete(x) for x in players_espania]
        lista_brasil = [Athlete(x) for x in players_brasil]
        lista_argentina = [Athlete(x) for x in players_argentina]
        soccer = Sport("Soccer",11,"FIFA")
        mexico = Team("Mexico",soccer,lista_mexico)
        espania = Team("España",soccer,lista_espania)
        brasil = Team("Brasil",soccer,lista_brasil)
        argentina = Team("Argentina",soccer,lista_argentina)
        equipos = [mexico,espania,brasil,argentina]

        d = {}
        for local in equipos:
            for visitante in equipos:
                if local != visitante:
                    juego  = Game(local,visitante)
                    partido = f'{local} - {visitante}'
                    partido_2 = f'{visitante} - {local}'
                    if partido_2 not in d:
                        d[partido] = juego.to_json()

        torneo = list(d.values())
        #juego = Game(mexico,espania)
        #torneo = [juego.to_json()]
        archivo_torneo = "torneo.json"
        with(open(archivo_torneo,"w",encoding="utf-8")) as f:
            json.dump(torneo,f,ensure_ascii=False,indent=4)
        print(f"Se escribió archivo '{archivo_torneo}' satisfactoriamente")
    
        # Jugar todos los juegos del torneo
    for juego in torneo:
        A = Team(juego['A']['name'], Sport(juego['A']['sport']['name'], juego['A']['sport']['players'], juego['A']['sport']['league']), [Athlete(x['name']) for x in juego['A']['players']])
        B = Team(juego['B']['name'], Sport(juego['B']['sport']['name'], juego['B']['sport']['players'], juego['B']['sport']['league']), [Athlete(x['name']) for x in juego['B']['players']])
        game = Game(A, B)
        game.play()
        print(game)
        print("----------------")

if __name__ == "__main__":
    archivo_torneo = ""
    main(archivo_torneo)
 
    


