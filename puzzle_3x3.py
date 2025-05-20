"""PUZZLE 3x3"""

import random
import os


def validar_entrada(entrada):
    """Valida que el numero ingresado este dentro del rango"""
    if entrada > 0 and entrada < 9:
        return False
    return True


def buscar_elemento(buscado, matrix):
    """Busca la posicion en la matriz del numero ingresado"""
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


def calcular_dif(fil, col, matrix, const_fil, const_col):
    """Calcula la diferencia entre el numero ingresado y alguno de sus adyacentes"""
    dif = matrix[fil][col] - matrix[fil + const_fil][col + const_col]
    return dif


def condicion_victoria(matrix):
    """Compara la matriz en forma de lista, con la lista modelo"""
    condicion_final = [1, 2, 3, 4, 5, 6, 7, 8, 0]

    if matrix == condicion_final:
        return True

    else:
        return False


def es_resoluble(puzzle):
    """Verifica la cantidad de inversiones para confirmar que el puzzle se pueda resolver"""
    sin_cero = [n for n in puzzle if n != 0]
    inversiones = 0

    for i in enumerate(sin_cero):   # pylint: disable=consider-using-enumerate
        for j in range(i + 1, len(sin_cero)):
            if sin_cero[i] > sin_cero[j]:
                inversiones += 1

    return inversiones % 2 == 0


VALIDO = 1

numeros = list(range(9))

random.shuffle(numeros)

while es_resoluble(numeros) is False:
    random.shuffle(numeros)

matrixPuzzle = [numeros[:3], numeros[3:6], numeros[6:9]]


while condicion_victoria(numeros) is False:

    print("Presione S para salir.")

    if VALIDO == 0:
        print("¡No se puede mover ese valor!")

    filaCero, columnaCero = buscar_elemento(0, matrixPuzzle)

    for row in matrixPuzzle:
        print("      ", end="")
        for element in row:
            print(element, end="  ")
        print()

    valor = input("Ingrese un numero: ")

    if valor.lower() == 's':
        print("¡Adiós!")
        exit()

    valor = int(valor)

    while validar_entrada(valor) is True:
        print("¡Ingrese un numero válido!")
        valor = input("Ingrese un número: ")
        valor = int(valor)

    filaValor, columnaValor = buscar_elemento(valor, matrixPuzzle)

    DIFERENCIA = 0
    CONTADOR = 0

    while (DIFERENCIA != valor and CONTADOR < 4):
        if filaValor != 2:
            DIFERENCIA = calcular_dif(
                filaValor, columnaValor, matrixPuzzle, 1, 0)
            if DIFERENCIA == valor:
                break
            CONTADOR += 1

        if columnaValor != 2:
            DIFERENCIA = calcular_dif(
                filaValor, columnaValor, matrixPuzzle, 0, 1)
            if DIFERENCIA == valor:
                break
            CONTADOR += 1

        if filaValor != 0:
            DIFERENCIA = calcular_dif(
                filaValor, columnaValor, matrixPuzzle, -1, 0)
            if DIFERENCIA == valor:
                break
            CONTADOR += 1

        if columnaValor != 0:
            DIFERENCIA = calcular_dif(
                filaValor, columnaValor, matrixPuzzle, 0, -1)
            if DIFERENCIA == valor:
                break
            CONTADOR += 1

    if DIFERENCIA == valor:
        matrixPuzzle[filaCero][columnaCero] = valor
        matrixPuzzle[filaValor][columnaValor] = 0
        VALIDO = 1
        os.system('cls')

    else:
        VALIDO = 0
        os.system('cls')

    numeros = [elemento for fila in matrixPuzzle for elemento in fila]

os.system('cls')

print("""          ██████╗  █████╗ ███╗   ██╗ █████╗ ███████╗████████╗███████╗
         ██╔════╝ ██╔══██╗████╗  ██║██╔══██╗██╔════╝╚══██╔══╝██╔════╝
         ██║  ███╗███████║██╔██╗ ██║███████║███████╗   ██║   █████╗  
         ██║   ██║██╔══██║██║╚██╗██║██╔══██║╚════██║   ██║   ██╔══╝  
         ╚██████╔╝██║  ██║██║ ╚████║██║  ██║███████║   ██║   ███████╗
         ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝╚══════╝   ╚═╝   ╚══════╝""")

exit()
