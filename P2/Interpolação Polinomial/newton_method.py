#!/usr/bin/env python3

import numpy as np

#################################################
### Main Function
#################################################


def main():
    # Parameters
    x_to_calculate = 0
    x_values = [-1, 0, 2]
    f_values = [4, 1, -1]

    div_differences_matrix = divided_differences(x_values, f_values)

    print(f"Matrix de diferenças divididas: \n{div_differences_matrix}")

    result = solve(x_to_calculate, x_values, div_differences_matrix)

    print(f"O resultado é de {result}")



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
    # Get divided differences coefficients
    num_of_coefficients = len(div_differences_matrix)

    div_differences_diag = np.zeros(num_of_coefficients, dtype=float)

    for i in range(0, num_of_coefficients):
        div_differences_diag[i] = div_differences_matrix[i][i]

    # Get result
    result = div_differences_diag[0]

    for i in range(1, num_of_coefficients):
        x_product = 1

        for j in range(0, i):
            x_product *= (x_to_calculate - x_values[j])

        result += div_differences_diag[i] * x_product

    return result



def error_calculation(x_to_calculate, x_values, div_differences_matrix):
    """
    Cálculo do erro
    """

    num_of_devided_diffs = len(div_differences_matrix)

    x_product = div_differences_matrix[num_of_devided_diffs - 1][num_of_devided_diffs - 1]

    for x in x_values:
        x_product *= (x_to_calculate - x)

    error = x_product

    return error

#################################################
### Main Function Call
#################################################

if __name__ == "__main__":
    main()
