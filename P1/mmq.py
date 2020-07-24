#!/usr/bin/env python3

import numpy as np
import sympy as sym
import decimal

import linear_system as linsys

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

    values_array = [decimal.Decimal('1'), decimal.Decimal('2'), decimal.Decimal('3'), decimal.Decimal('1'), decimal.Decimal('2'), decimal.Decimal('1')]

    coef_matrix = [[decimal.Decimal('1'), decimal.Decimal('0'), decimal.Decimal('0')],
                   [decimal.Decimal('0'), decimal.Decimal('1'), decimal.Decimal('0')],
                   [decimal.Decimal('0'), decimal.Decimal('0'), decimal.Decimal('1')],
                   [decimal.Decimal('-1'), decimal.Decimal('1'), decimal.Decimal('0')],
                   [decimal.Decimal('0'), decimal.Decimal('-1'), decimal.Decimal('1')],
                   [decimal.Decimal('-1'), decimal.Decimal('0'), decimal.Decimal('1')]]

    coef_matrix = np.transpose(coef_matrix)

    g_matrix, f_array = generate_linear_system(values_array, coef_matrix)

    print(f"\nMatriz G: \n{g_matrix} \n\nMatriz F: \n{f_array}")

    x_array = linsys.solve_linear_system(g_matrix, f_array, PRECSION)

    print(f"\nResposta X: \n{x_array}")



#################################################
### Methods functions
#################################################



def dot_product(u_vector, v_vector):
    """
    Calcula o produto interno de dois vetores u e v.
    """

    decimal.getcontext().prec = PRECSION
    decimal.getcontext().rounding = ROUNDING_MODE

    result = 0

    for i in range(0, len(u_vector)):
        result += u_vector[i] * v_vector[i]

    return result



def generate_linear_system(f_array, g_matrix):
    """
    Dado f(x) = a0 * g0(x) + a1 * g1(x) + ... + ak * gk(x)

    Retorna a matriz A e b do sistema normal A * x = b, gerados
    a partir de f(x) e os vetores g.
    """

    decimal.getcontext().prec = PRECSION
    decimal.getcontext().rounding = ROUNDING_MODE

    num_of_coeficients = len(g_matrix)

    a_matrix = np.full((num_of_coeficients, num_of_coeficients), decimal.Decimal('0'))
    b_array = np.full(num_of_coeficients, decimal.Decimal('0'))

    for k in range(0, num_of_coeficients):
        b_array[k] = dot_product(f_array, g_matrix[k])

    for i in range(0, num_of_coeficients):
        for j in range(i, num_of_coeficients):
            inner_product = dot_product(g_matrix[i], g_matrix[j])
            a_matrix[i][j] = inner_product

            if i != j:
                a_matrix[j][i] = inner_product

    return a_matrix, b_array



def f_approximation(g_matrix, coeficients_array):
    """
    Retorna um vetor para o valor aproximado de f, dados os coeficientes ak.
    """

    decimal.getcontext().prec = PRECSION
    decimal.getcontext().rounding = ROUNDING_MODE

    num_of_xs = len(g_matrix[0])
    num_of_coeficients = len(g_matrix)

    f_approx_array = np.full(num_of_xs, decimal.Decimal('0'))

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

    decimal.getcontext().prec = PRECSION
    decimal.getcontext().rounding = ROUNDING_MODE

    num_of_xs = len(f_array)

    f_approx_array = f_approximation(g_matrix, coeficients_array)

    error_sum = 0

    for i in range(0, num_of_xs):
        error_sum += ((f_array[i] - f_approx_array[i])**2)

    error_sum /= num_of_xs

    error = np.sqrt(error_sum)

    return error



#################################################
### Main Function Call
#################################################

if __name__ == "__main__":
    main()
