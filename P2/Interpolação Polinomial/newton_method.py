#!/usr/bin/env python3

import numpy as np
import sympy as sym

#################################################
### Main Function
#################################################


def main():
    # Parameters
    x = sym.symbols('x')
    f_function = (1/2)**x

    x_to_calculate = 1/3
    x_values = [-2, -1, 1, 2]
    f_values = [4, 2, 0.5, 0.25]

    div_differences_matrix = divided_differences(x_values, f_values)

    print(f"Matrix de diferenças divididas: \n{div_differences_matrix}")

    result = solve(x_to_calculate, x_values, div_differences_matrix)

    result = sym.nsimplify(result)

    print(f"O resultado é de {result}")

    if 'f_function' in locals():
        error = error_calculation_with_f(x_to_calculate, x_values, div_differences_matrix, f_function)
    else:
        error = error_calculation(x_to_calculate, x_values, div_differences_matrix)


    print(f"Erro de {error}")



#################################################
### Methods functions
#################################################

def divided_differences(x_values, f_values):
    """
    Calcula o polinômio interpolador pelo método de Newton
    """

    max_order = len(x_values) - 1

    div_differences_matrix = np.zeros((max_order + 1, max_order + 1), dtype=float)

    for i in range(0, max_order + 1):
        div_differences_matrix[i][0] = f_values[i]

    for j in range(1, max_order + 1):
        for i in range(j, max_order + 1):
            div_differences_matrix[i][j] = ((div_differences_matrix[i][j - 1] - div_differences_matrix[i - 1][j - 1]) /
                                            (x_values[i] - x_values[i - j]))

    return div_differences_matrix



def solve(x_to_calculate, x_values, div_differences_matrix):
    x_sym = sym.symbols('x')

    # Get divided differences coefficients
    num_of_coefficients = len(div_differences_matrix)

    div_differences_diag = np.zeros(num_of_coefficients, dtype=float)

    for i in range(0, num_of_coefficients):
        div_differences_diag[i] = div_differences_matrix[i][i]

    # Get result
    result = div_differences_diag[0]
    polynomial = div_differences_diag[0]

    for i in range(1, num_of_coefficients):
        x_product = 1
        x_sym_product = 1

        for j in range(0, i):
            x_product *= (x_to_calculate - x_values[j])
            x_sym_product *= (x_sym - x_values[j])


        result += div_differences_diag[i] * x_product
        polynomial += div_differences_diag[i] * x_sym_product

    polynomial = sym.nsimplify(polynomial)
    polynomial = sym.simplify(polynomial)
    print(f'p({x_sym})={polynomial}')

    return result



def error_calculation(x_to_calculate, x_values, div_differences_matrix):
    """
    Cálculo do erro sem a função f.
    """

    x_product = div_differences_matrix[-1][-1]

    for i in range(0, len(x_values) - 1):
        x_product *= (x_to_calculate - x_values[i])

    error = x_product

    return error



def error_calculation_with_f(x_to_calculate, x_values, div_differences_matrix, f_function):
    """
    Cálculo do erro tendo a função f.
    """

    np1 = len(x_values)

    x = sym.symbols('x')
    f_np1_derivative = sym.diff(f_function, x, np1)
    f_np1_derivative = sym.lambdify(x, f_np1_derivative)

    max_f_np1_derivative = max(map(f_np1_derivative, x_values))

    x_product = max_f_np1_derivative

    for x in x_values:
        x_product *= (x_to_calculate - x)

    error = x_product / (np.math.factorial(np1))

    return error

#################################################
### Main Function Call
#################################################

if __name__ == "__main__":
    main()
