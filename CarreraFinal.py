import os
from random import randint, uniform 

acumulado = 0
acumulado2 = 0
i = 0
op = 0
valor = 0

def proceso():
    casillas = []
    print("Por Favor, Ingrese el numero de jugadores minimo 2 maximo 5: ")
    jug = int(input())
    if jug < 2 or jug > 5:
        print("Digite un numero de jugadores (2-5)")
        print(":::::::::::::::::::::::::::::::PRESIONE ENTER PARA CONTINUAR:::::::::::::::::::::::::::::")
        input()
        return
    for i in range(1,jug+1):
        Datos = 0
        casillas.append(Datos)
    i=0

    while casillas[i] <= valor:
        os.system("cls")
        dado1 = randint(1,6)
        dado2 = randint(1,6)
        print("Jugador ",i+1, "Sacao: ", dado1, "y ", dado2)
        casillas[i] = casillas[i] + dado1 + dado2
        print("Jugador ",i+1," Acomulado de: ", casillas[i])
        print("Resultados Totales: ", casillas)
        input("Presiona enter para el turno del siguiente jugador")
        if casillas[i] >= valor:
            print("El Jugador ", i+1, "Gano")
            input()
            break
        i = i+1
        if i== jug:
            i=0

while op !=4:
    os.system("cls")
    print(":::::::::::::::::::::::::::::::CARRERA DE DADOS:::::::::::::::::::::::::::::")
    print("Por Favor, Ingrese un numero del 1-3 para comenzar el juego: ")
    print("[1] Nivel Basico De 50 Puntos")
    print("[2] Nivel Medio De 70 Puntos")
    print("[3] Nivel Medio De 100 Puntos")
    print("[4] Salir")
    op = int(input())

    if op == 1:
        print("Nivel Basico De 50 Puntos")
        print("::::::::::::::::::::::::")
        valor = 50
        proceso()
    elif op == 2:
        print("Nivel Medio De 70 Puntos")
        print("::::::::::::::::::::::::")
        valor = 70 
        proceso()
    elif op == 3:
        print("Nivel Avanzado De 100 Puntos")
        print("::::::::::::::::::::::::")
        valor = 100 
        proceso()
    elif op == 4:
        print(":::::::::::::::::::::::::::::::Gracias por jugar:::::::::::::::::::::::::::::")
        print("::::::::::::::::::::::::::Realizado por: Stiven Gómez::::::::::::::::::::::::")
        exit  
    else:
        print(":::::::::::::::::::::::::::::::EL NUMERO QUE INGRESO ES INVALIDO:::::::::::::::::::::::::::::")
        print(":::::::::::::::::::::::::::::::PRESIONE ENTER PARA CONTINUAR:::::::::::::::::::::::::::::")
        input()