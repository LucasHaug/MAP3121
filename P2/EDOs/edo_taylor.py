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
    # Important => f(x, y) = y'
    f_function = lambda x, y: y - x**2 + 1

   # Method order
    order = 4

    # Parameters
    step = 0.2
    x0 = 0
    xf = 2
    y0 = 0.5

    solve(y0, x0, xf, step, order, f_function)


#################################################
### Methods functions
#################################################

def solve(y0, x0, xf, step, order, f_function):
    """
    Método de Euler, método de primeira ordem
    """

    xn = x0
    yn = y0

    print(f"y({xn}) = {yn}")

    num_of_xs = int((xf - x0) / step)

    for _ in range(num_of_xs):
        t_function = f_function(xn, yn)

        for i in range(1, order):
            t_function += f_derivative(xn, yn, i) * (step**i) / (np.math.factorial(i + 1))

        ynp1 = yn + step * t_function

        yn = ynp1
        xn += step

        print(f"y({xn}) = {yn}")


#################################################
### Main Function Call
#################################################

if __name__ == "__main__":
    main()
