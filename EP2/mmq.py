#!/usr/bin/env python3

import numpy as np

#################################################
### Functions Definitions
#################################################

def generate_linear_system(f_array, g_matrix):
    """
    Dado f(x) = a0 * g0(x) + a1 * g1(x) + ... + ak * gk(x)

    Retorna a matriz A e b do sistema normal A * x = b, gerados
    a partir de f(x) e os vetores g.
    """

    num_of_coeficients = len(g_matrix)

    a_matrix = np.zeros((num_of_coeficients, num_of_coeficients), dtype=float)
    b_array = np.zeros(num_of_coeficients, dtype=float)

    for k in range(0, num_of_coeficients):
        b_array[k] = np.inner(f_array, g_matrix[k])

    for i in range(0, num_of_coeficients):
        for j in range(i, num_of_coeficients):
            inner_product = np.inner(g_matrix[i], g_matrix[j])
            a_matrix[i][j] = inner_product

            if i != j:
                a_matrix[j][i] = inner_product

    return a_matrix, b_array



def matrix_decomposition(a_matrix):
    """
    Decompõe uma matrix A simétrica em três matrizes L, D e
    Lt, retornando as duas matrizes L e D.

    Aviso: A matriz A é mudada dentro da função.
    """

    matrix_dimension = len(a_matrix)

    l_matrix = np.zeros((matrix_dimension, matrix_dimension), dtype=float)
    d_matrix = np.zeros((matrix_dimension, matrix_dimension), dtype=float)

    for f in range(0, matrix_dimension):
        # Generate L matrix
        for l in range(f, matrix_dimension):
            l_matrix[l][f] = a_matrix[l][f] / a_matrix[f][f]

        # Generate the new matrix A
        for c in range(0, matrix_dimension):
            for l in range(f + 1, matrix_dimension):
                a_matrix[l][c] = a_matrix[l][c] - l_matrix[l][f] * a_matrix[f][c]

    # Generate D matrix
    for l in range(0, matrix_dimension):
        d_matrix[l][l] = a_matrix[l][l]

    return l_matrix, d_matrix



def solve_linear_system(a_matrix, b_array):
    """
    Soluciona um sistema Ax = b, onde A é uma matrix simétrica.

    Para a resolução do sistema, é feita a decomposição de A para L*D*Lt.

    É feita a divisão do problema em três sistemas menores:
    L * y = b
    D * z = y
    Lt * x = z
    """

    matrix_dimension = len(a_matrix)

    l_matrix, d_matrix = matrix_decomposition(a_matrix)

    # First system solution -> L * y = b
    y_array = np.zeros(matrix_dimension, dtype=float)

    y_array[0] = b_array[0]

    for l in range(1, matrix_dimension):
        y_array[l] = b_array[l]

        for m in range(0, l):
            y_array[l] = y_array[l] - y_array[m] * l_matrix[l][m]

    # Second system solution -> D * z = y
    z_array = np.zeros(matrix_dimension, dtype=float)

    for l in range(0, matrix_dimension):
        z_array[l] = y_array[l] / d_matrix[l][l]

    # Third system solution -> Lt * x = z
    x_array = np.zeros(matrix_dimension, dtype=float)

    x_array[-1] = z_array[-1]

    for l in range(matrix_dimension - 2, -1, -1):
        x_array[l] = z_array[l]

        for m in range(matrix_dimension - 1, l, -1):
            x_array[l] = x_array[l] - x_array[m] * np.transpose(l_matrix)[l][m]

    return x_array



def f_approximation(g_matrix, coeficients_array):
    """
    Retorna um vetor para o valor aproximado de f, dados os coeficientes ak.
    """

    num_of_xs = len(g_matrix[0])
    num_of_coeficients = len(g_matrix)

    f_approx_array = np.zeros(num_of_xs, dtype=float)

    for i in range(0, num_of_xs):
        approx_sum = 0

        for k in range(0, num_of_coeficients):
            approx_sum += coeficients_array[k] * g_matrix[k][i]

        f_approx_array[i] = approx_sum

    return f_approx_array



def squared_error_calculation(f_array, g_matrix, coeficients_array):
    """
    Cálculo discreto do erro quadrático.
    """

    num_of_xs = len(f_array)

    f_approx_array = f_approximation(g_matrix, coeficients_array)

    error_sum = 0

    for i in range(0, num_of_xs):
        error_sum += ((f_array[i] - f_approx_array[i])**2)

    error_sum /= num_of_xs

    error = np.sqrt(error_sum)

    return error
