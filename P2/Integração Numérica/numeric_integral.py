#!/usr/bin/env python3

import numpy as np
from scipy.special import roots_legendre

#################################################
### Change for each problem
#################################################

def f_function(x):
    """
    Função f a ser integrada
    """

    result = (np.sin(x)) / x

    return result


#################################################
### Main Function
#################################################


def main():
    num_of_points = 3
    integral_max = 1
    integral_min = 0

    gaussian_quadrature(num_of_points, integral_max, integral_min)


#################################################
### Methods functions
#################################################

def gaussian_quadrature(num_of_points, integral_max, integral_min):
    """
    Quadratura Gaussiana
    """

    x_array, w_array = roots_legendre(num_of_points)
    print(roots_legendre(num_of_points))

    result = 0

    for i in range(len(x_array)):
        t = x_array[i] * (integral_max - integral_min) / 2 + (integral_max + integral_min) / 2

        result += w_array[i] * f_function(t)

    result *= ((integral_max - integral_min) / 2)

    print(result)

#################################################
### Main Function Call
#################################################

if __name__ == "__main__":
    main()
