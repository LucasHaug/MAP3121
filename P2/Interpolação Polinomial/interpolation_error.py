#!/usr/bin/env python3

import numpy as np

#################################################
### Change for each problem
#################################################

def f_derivative(x, y, derivative_order):
    """
    Derivada de f em relacao a x, ao se derivar
    uma parcela que tenha, não se pode "eliminar"
    o y.
    """

    if (derivative_order == 1):
        result = y - x**2 + 1 - 2 * x
    elif (derivative_order == 2):
        result = y - x**2 - 1 - 2 * x
    elif (derivative_order == 3):
        result = y - x**2 - 1 - 2 * x
    else:
        result = 0

    return result


#################################################
### Main Function
#################################################


def main():
    # Functions
    f_function = lambda x: (0.5)**x
    f_approx = lambda x: -x**3/16 + 7*x**2/24 - 11*x/16 + 23/24
    f_np1_derivative = lambda x: x

    # Parameters
    step = 0.2
    x0 = 0
    xn = 2
    x_value = 0.25
    polynomial_order = 4

    exact_error(x_value, f_function, f_approx)
    max_error(polynomial_order, step, x0, xn, f_np1_derivative)


#################################################
### Methods functions
#################################################

def exact_error(x_value, f_function, f_approx):
    """
    Cálculo do erro exato para uma interpolação
    """

    error = abs(f_function(x_value) - f_approx(x_value))

    print(f"Erro exato de {error}")



def max_error(polynomial_order, step, x0, xn, f_np1_derivative):
    """
    Cálculo do erro máximo para uma interpolação polinomial,
    dadas a ordem do polinômio, o passo entre cada um dos valores
    utilizadas para a interpolação e a derivada de ordem n + 1
    """

    num_of_points = (xn - x0) / step

    max_f_np1_deriv = abs(f_np1_derivative(x0))

    for i in range(1, num_of_points + 1):
        f_np1_deriv_value = abs(f_np1_derivative(x0 + i * step))

        if (f_np1_deriv_value > max_f_np1_deriv):
            max_f_np1_deriv = f_np1_deriv_value

    error = ((step**(polynomial_order + 1)) / (4 * (polynomial_order + 1))) * max_f_np1_deriv

    return error

#################################################
### Main Function Call
#################################################

if __name__ == "__main__":
    main()
