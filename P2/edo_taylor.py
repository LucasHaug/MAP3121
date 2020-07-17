#!/usr/bin/env python3

import numpy as np

#################################################
### Change for each problem
#################################################

def f_function(x, y):
    """
    f(x, y) = y´
    """

    result = y - x**2 + 1
    
    return result

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
    order = 4

    h = 0.2
    x0 = 0
    xf = 2
    y0 = 0.5
    
    solve(y0, x0, xf, h, order)


#################################################
### Methods functions
#################################################

def solve(y0, x0, xf, h, order):
    """
    Método de Euler, método de primeira ordem
    """

    xn = x0
    yn = y0

    print(f"y({xn}) = {yn}")

    num_of_xs = int((xf - x0) / h)

    for _ in range(num_of_xs):
        t_function = f_function(xn, yn)

        for i in range(1, order):
            t_function += f_derivative(xn, yn, i) * (h**i) / (np.math.factorial(i + 1))
        
        ynp1 = yn + h * t_function
        
        yn = ynp1
        xn += h 

        print(f"y({xn}) = {yn}")


#################################################
### Main Function Call
#################################################

if __name__ == "__main__":
    main()
