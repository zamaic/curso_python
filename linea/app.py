# cálculo de coordenadas de líneas
import funcioness
import argparse



def main(m:float,b:float):

    '''
    Funciòn principal que calcula las coorodenadas de una linea recta 
    Recibimos m y b
    Regresa: nada...
    '''
   
    X = [x/10.0 for x in range(10,110,5)]
    Y = [funcioness.calcular_y(x,m,b) for x in X]
    coordenadas_flotantes = list(zip(X,Y))
    print("Flotantes: ")
    print(coordenadas_flotantes)
    funcioness.graficar_linea(X,Y,m,b)
  

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-m', type=float,help='Pendiente de la linea',default = 2.0)
    parser.add_argument('-b', type=float,help='Ordenada de la linea',default = 3.0)
    args = parser.parse_args()
    main(args.m,args.b)