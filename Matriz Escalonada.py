import numpy as np

def eliminar_gauss(A, tolerancia=1e-10):
    """
    Convierte la matriz A a su forma escalonada reducida (Gauss-Jordan).
    Los valores cercanos a cero se ajustan a cero (según un umbral de tolerancia).
    """
    filas, columnas = A.shape
    fila_pivote = 0

    # Fase de eliminación hacia adelante (reducción)
    for columna in range(columnas):
        if fila_pivote >= filas:
            break

        # Encontrar un pivote no nulo
        if A[fila_pivote, columna] == 0:
            continue

        # Hacer que A[fila_pivote, columna] sea 1
        A[fila_pivote] = A[fila_pivote] / A[fila_pivote, columna]

        # Hacer ceros debajo del pivote
        for i in range(fila_pivote + 1, filas):
            if A[i, columna] != 0:
                factor = A[i, columna]
                A[i] = A[i] - factor * A[fila_pivote]

        # Avanzar a la siguiente fila y columna
        fila_pivote += 1

    # Fase de reducción hacia atrás (eliminación de los elementos sobre los pivotes)
    for fila in range(filas-1, -1, -1):  # Recorremos desde la última fila hacia arriba
        for columna in range(columnas-1, -1, -1):  # Recorremos desde la última columna hacia la primera
            if A[fila, columna] == 1:
                # Hacer ceros sobre los pivotes
                for i in range(fila-1, -1, -1):
                    if A[i, columna] != 0:
                        factor = A[i, columna]
                        A[i] = A[i] - factor * A[fila]

    # Aplicamos el umbral de tolerancia para hacer ceros exactos
    A[np.abs(A) < tolerancia] = 0.0

    return A

def imprimir_matriz(A):
    """
    Imprime la matriz de manera más legible.
    """
    filas, columnas = A.shape
    for i in range(filas):
        print(" ".join([f"{A[i,j]:.2f}" for j in range(columnas)]))

# Ejemplo de uso
if __name__ == "__main__":
    # Solicitar el número de filas y columnas de la matriz
    filas = int(input("Ingrese el número de filas de la matriz (máximo 10): "))
    columnas = int(input("Ingrese el número de columnas de la matriz (máximo 10): "))

    # Verificar que las dimensiones no excedan 10x10
    if filas > 10 or columnas > 10:
        print("Error: Las dimensiones de la matriz deben ser 10x10 como máximo.")
    else:
        # Crear la matriz vacía
        A = np.zeros((filas, columnas), dtype=float)

        # Solicitar los valores de la matriz al usuario
        print("Ingrese los elementos de la matriz (cada fila en una sola línea):")
        for i in range(filas):
            for j in range(columnas):
                A[i, j] = float(input(f"Elemento [{i+1}, {j+1}]: "))

        print("\nMatriz original:")
        imprimir_matriz(A)

        # Convertir la matriz a escalonada reducida
        A_escalonada_reducida = eliminar_gauss(A)

        print("\nMatriz escalonada reducida (Gauss-Jordan):")
        imprimir_matriz(A_escalonada_reducida)