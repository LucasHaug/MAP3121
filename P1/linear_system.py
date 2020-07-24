#!/usr/bin/env python3

import numpy as np
import sympy as sym
import decimal
from itertools import permutations

#################################################
### Context control
#################################################

# Number of significant digits
PRECSION = 2

# Round to nearest with ties going away from zero.
# See https://docs.python.org/3/library/decimal.html#rounding-modes
ROUNDING_MODE = decimal.ROUND_HALF_UP

#################################################
### Main Function
#################################################


def main():
    # Parameters
    decimal.getcontext().prec = PRECSION
    decimal.getcontext().rounding = ROUNDING_MODE
    print(decimal.getcontext())

    x_approx_array = [decimal.Decimal('1.1'), decimal.Decimal('1.8'), decimal.Decimal('2.7')]

    b_array = [decimal.Decimal('-1'), decimal.Decimal('1'), decimal.Decimal('6')]

    a_matrix = [[decimal.Decimal('3'), decimal.Decimal('-1'), decimal.Decimal('-1')],
                [decimal.Decimal('-1'), decimal.Decimal('3'), decimal.Decimal('-1')],
                [decimal.Decimal('-1'), decimal.Decimal('-1'), decimal.Decimal('3')]]

    calc_residue(x_approx_array, a_matrix, b_array, PRECSION)

    sassenfeld_criteria_iterative(a_matrix)


#################################################
### Methods functions
#################################################


def matrix_decomposition(a_matrix, precision):
    """
    Decompõe uma matrix A simétrica em três matrizes L, D e
    Lt, retornando as duas matrizes L e D.
    """

    decimal.getcontext().prec = precision
    decimal.getcontext().rounding = ROUNDING_MODE

    matrix_dimension = len(a_matrix)

    a_matrix_copy = np.copy(a_matrix)

    l_matrix = np.full((matrix_dimension, matrix_dimension), decimal.Decimal('0'))
    d_matrix = np.full((matrix_dimension, matrix_dimension), decimal.Decimal('0'))

    for f in range(0, matrix_dimension):
        # Generate L matrix
        for l in range(f, matrix_dimension):
            l_matrix[l][f] = a_matrix_copy[l][f] / a_matrix_copy[f][f]

        # Generate the new matrix A
        for c in range(0, matrix_dimension):
            for l in range(f + 1, matrix_dimension):
                a_matrix_copy[l][c] = a_matrix_copy[l][c] - l_matrix[l][f] * a_matrix_copy[f][c]

    # Generate D matrix
    for l in range(0, matrix_dimension):
        d_matrix[l][l] = a_matrix_copy[l][l]

    return l_matrix, d_matrix



def lu_decomposition(a_matrix, precision):
    """
    Decompõe uma matrix A simétrica em três matrizes L e
    U, retornando as duas matrizes
    """

    decimal.getcontext().prec = precision
    decimal.getcontext().rounding = ROUNDING_MODE

    matrix_dimension = len(a_matrix)

    a_matrix_copy = np.copy(a_matrix)

    l_matrix = np.full((matrix_dimension, matrix_dimension), decimal.Decimal('0'))
    u_matrix = np.full((matrix_dimension, matrix_dimension), decimal.Decimal('0'))

    for f in range(0, matrix_dimension):
        # Generate L matrix
        for l in range(f, matrix_dimension):
            l_matrix[l][f] = a_matrix_copy[l][f] / a_matrix_copy[f][f]

        # Generate the new matrix A
        for c in range(0, matrix_dimension):
            for l in range(f + 1, matrix_dimension):
                a_matrix_copy[l][c] = a_matrix_copy[l][c] - l_matrix[l][f] * a_matrix_copy[f][c]

    # Generate U matrix
    u_matrix = a_matrix_copy

    return l_matrix, u_matrix



def solve_linear_system(a_matrix, b_array, precision):
    """
    Soluciona um sistema Ax = b, onde A é uma matrix simétrica.

    Para a resolução do sistema, é feita a decomposição de A para L*D*Lt.

    É feita a divisão do problema em três sistemas menores:
    L * y = b
    D * z = y
    Lt * x = z
    """

    decimal.getcontext().prec = precision
    decimal.getcontext().rounding = ROUNDING_MODE

    matrix_dimension = len(a_matrix)

    l_matrix, d_matrix = matrix_decomposition(a_matrix, precision)

    # First system solution -> L * y = b
    y_array = np.full(matrix_dimension, decimal.Decimal('0'))

    y_array[0] = b_array[0]

    for l in range(1, matrix_dimension):
        y_array[l] = b_array[l]

        for m in range(0, l):
            y_array[l] = y_array[l] - y_array[m] * l_matrix[l][m]

    # Second system solution -> D * z = y
    z_array = np.full(matrix_dimension, decimal.Decimal('0'))

    for l in range(0, matrix_dimension):
        z_array[l] = y_array[l] / d_matrix[l][l]

    # Third system solution -> Lt * x = z
    x_array = np.full(matrix_dimension, decimal.Decimal('0'))

    x_array[-1] = z_array[-1]

    for l in range(matrix_dimension - 2, -1, -1):
        x_array[l] = z_array[l]

        for m in range(matrix_dimension - 1, l, -1):
            x_array[l] = x_array[l] - x_array[m] * np.transpose(l_matrix)[l][m]

    return x_array


def calc_residue(x_approx_array, a_matrix, b_array, precision):
    """
    Calcula o resíduo.
    """

    residue_precision = precision * 2

    decimal.getcontext().prec = residue_precision
    decimal.getcontext().rounding = ROUNDING_MODE

    num_of_xs = len(x_approx_array)

    residue = np.full(num_of_xs, decimal.Decimal('0'))

    b_approx_array = np.dot(a_matrix, x_approx_array)

    residue = b_array - b_approx_array

    print(f"Resíduo:\n{residue}")

    correction_array = solve_linear_system(a_matrix, residue, residue_precision)

    print(f"Correção:\n{correction_array}")



def sassenfeld_criteria(a_matrix, print_betas):
    matrix_dimension = len(a_matrix)

    β_array = np.full(matrix_dimension, 1, dtype=float)

    for i in range(0, matrix_dimension):
        β_array[i] *= 1 / abs(float(a_matrix[i][i]))

        next_elements_sum = 0

        for j in range(i + 1, matrix_dimension):
            next_elements_sum += abs(float(a_matrix[i][j]))

        prev_elements_sum = 0

        for j in range(0, i):
            prev_elements_sum += (β_array[j] * abs(float(a_matrix[i][j])))

        β_array[i] *= (prev_elements_sum + next_elements_sum)

    βmax = max(β_array)

    if (print_betas == True):
        for i in range(0, matrix_dimension):
            print(f"β{i + 1} = {sym.nsimplify(β_array[i])}\n")

        print(f"βmax = {βmax}")

    return βmax



def sassenfeld_criteria_iterative(a_matrix):
    matrix_dimension = len(a_matrix)

    perm = list(permutations(list(range(0, matrix_dimension))))
    num_of_perms = len(perm)

    a_matrix_perm = np.copy(a_matrix)

    β_max_array = []

    for i in range(num_of_perms):
        for j in range(num_of_perms):
            for k in range(matrix_dimension):
                for l in range(matrix_dimension):
                    a_matrix_perm[k][l] = a_matrix[perm[i][k]][perm[j][l]]

            βmax = sassenfeld_criteria(a_matrix_perm, False)

            if (βmax < 1):
                print(f"Matriz permutada: \n{a_matrix_perm}")

                print(f"βmax = {sym.nsimplify(βmax)}")

                β_max_array.append(βmax)

    if (β_max_array == []):
        print(f"A matriz não satisfaz o critério de Sassenfeld")
    else:
        best_βmax = min(β_max_array)
        print(f"Melhor βmax = {sym.nsimplify(best_βmax)}")

        return best_βmax



#################################################
### Main Function Call
#################################################

if __name__ == "__main__":
    main()
