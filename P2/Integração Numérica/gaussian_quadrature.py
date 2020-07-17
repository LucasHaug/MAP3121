#!/usr/bin/env python3

import numpy as np
from scipy.special import roots_legendre

#################################################
### Change for each problem
#################################################

def f_function(t, integral_min, integral_max):
    """
    Função f a ser integrada
    """

    x = t * (integral_max - integral_min) / 2 + (integral_max + integral_min) / 2

    # f em função de x
    result = (np.exp(x))

    return result


#################################################
### Main Function
#################################################


def main():
    num_of_points = 2
    integral_max = 10
    integral_min = 5

    solve(num_of_points, integral_max, integral_min)


#################################################
### Methods functions
#################################################

def solve(num_of_points, integral_max, integral_min):
    """
    Quadratura Gaussiana
    """

    x_array, w_array = roots_legendre(num_of_points)
    print(roots_legendre(num_of_points))

    result = 0

    for i in range(len(x_array)):
        result += w_array[i] * f_function(x_array[i], integral_min, integral_max)

    result *= ((integral_max - integral_min) / 2)

    print(result)

#################################################
### Main Function Call
#################################################

if __name__ == "__main__":
    main()
