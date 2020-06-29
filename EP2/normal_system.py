#!/usr/bin/env python3

import numpy as np

#################################################
### Functions Definitions
#################################################

def generate(g_matrix, f):
    """
    Dado f(x) = a0 * g0(x) + a1 * g1(x) + ... + ak * gk(x)

    Retorna a matriz A e b do sistema normal A * x = b, gerados
    a partir de f(x) e os vetores g.
    """

    num_of_coeficients = len(f)

    A = np.zeros((num_of_coeficients, num_of_coeficients), dtype=float)
    b = np.zeros(num_of_coeficients, dtype=float)

    for k in range(0, num_of_coeficients):
        b[k] = np.inner(f, g_matrix[k])

    for i in range(0, num_of_coeficients):
        for j in range(i, num_of_coeficients):
            inner_product = np.inner(g_matrix[i], g_matrix[j])
            A[i][j] = inner_product

            if i != j:
                A[j][i] = inner_product

    return A, b



def matrix_decomposition(A):
    """
    Decompõe uma matrix A simétrica em três matrizes L, D e
    Lt, retornando apenas dois vetores que representam as
    matrizes L e D.
    """

    matrix_dimension = len(A[0])

    L = np.zeros((matrix_dimension, matrix_dimension), dtype=float)
    D = np.zeros((matrix_dimension, matrix_dimension), dtype=float)

    # math

    return L, D




def solve(A, b):
    """
    Soluciona um sistema Ax = b, onde A é uma matrix simétrica.

    Para a resolução do sistema, é feita a decomposição de A para L*D*Lt.

    É feita a divisão do problema em três sistemas menores:
    L * y = b
    D * z = y
    Lt * x = z
    """

    dimension = len(b[0])

    x_array = np.zeros(dimension, dtype=float)

    # math

    return x_array
