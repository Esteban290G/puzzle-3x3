"""codigo de practica"""

import random
import os


def validarEntrada(valor):
    if valor > 0 and valor < 9:
        return False
    return True


def buscarElemento(buscado, matrix):

    fil = -1
    col = -1

    for i, fila in enumerate(matrix):
        for j, elemento in enumerate(fila):
            if buscado == elemento:
                fil = i
                col = j
                break
        if col != -1:
            break

    return (fil, col)


def calcularDif(fil, col, matrix, constFil, constCol):
    dif = matrix[fil][col] - matrix[fil + constFil][col + constCol]
    return dif


def condicionVictoria(matrix):
    condicionFinal = [1, 2, 3, 4, 5, 6, 7, 8, 0]

    if matrix == condicionFinal:
        return True

    else:
        return False


def esResoluble(puzzle):
    sinCero = [n for n in puzzle if n != 0]
    inversiones = 0

    for i in range(len(sinCero)):
        for j in range(i + 1, len(sinCero)):
            if sinCero[i] > sinCero[j]:
                inversiones += 1

    return inversiones % 2 == 0


valido = 1

numeros = list(range(9))

random.shuffle(numeros)

while esResoluble(numeros) is False:
    random.shuffle(numeros)

matrixPuzzle = [numeros[:3], numeros[3:6], numeros[6:9]]


while condicionVictoria(numeros) is False:

    print("Presione S para salir.")

    if valido == 0:
        print("¡No se puede mover ese valor!")

    filaCero, columnaCero = buscarElemento(0, matrixPuzzle)

    for row in matrixPuzzle:
        print("      ", end="")
        for element in row:
            print(element, end="  ")
        print()

    valor = input("Ingrese un numero: ")

    if valor.lower() == 's':
        print("¡Adiós!")
        break

    valor = int(valor)

    while validarEntrada(valor) is True:
        print("¡Ingrese un numero válido!")
        valor = input("Ingrese un número: ")
        valor = int(valor)

    filaValor, columnaValor = buscarElemento(valor, matrixPuzzle)

    diferencia = 0
    contador = 0

    while (diferencia != valor and contador < 4):
        if filaValor != 2:
            diferencia = calcularDif(
                filaValor, columnaValor, matrixPuzzle, 1, 0)
            if diferencia == valor:
                break
            contador += 1

        if columnaValor != 2:
            diferencia = calcularDif(
                filaValor, columnaValor, matrixPuzzle, 0, 1)
            if diferencia == valor:
                break
            contador += 1

        if filaValor != 0:
            diferencia = calcularDif(
                filaValor, columnaValor, matrixPuzzle, -1, 0)
            if diferencia == valor:
                break
            contador += 1

        if columnaValor != 0:
            diferencia = calcularDif(
                filaValor, columnaValor, matrixPuzzle, 0, -1)
            if diferencia == valor:
                break
            contador += 1

    if diferencia == valor:
        matrixPuzzle[filaCero][columnaCero] = valor
        matrixPuzzle[filaValor][columnaValor] = 0
        valido = 1
        os.system('cls')

    else:
        valido = 0
        os.system('cls')

    numeros = [elemento for fila in matrixPuzzle for elemento in fila]

os.system('cls')


if condicionVictoria is True:
    print(""" 
         ██████╗  █████╗ ███╗   ██╗ █████╗ ███████╗████████╗███████╗
        ██╔════╝ ██╔══██╗████╗  ██║██╔══██╗██╔════╝╚══██╔══╝██╔════╝
        ██║  ███╗███████║██╔██╗ ██║███████║███████╗   ██║   █████╗  
        ██║   ██║██╔══██║██║╚██╗██║██╔══██║╚════██║   ██║   ██╔══╝  
        ╚██████╔╝██║  ██║██║ ╚████║██║  ██║███████║   ██║   ███████╗
        ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝╚══════╝   ╚═╝   ╚══════╝
                                                                """)
else:
    print("¡Adiós!")
exit()
