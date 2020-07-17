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

    result = (np.exp(x))

    return result



def f_derivative(x, derivative_order):
    """
    Derivada n da função f.

    Necesária somente para os cálculos dos erros.
    """

    if (derivative_order == 1):
        result = 0
    elif (derivative_order == 2):
        result = np.exp(x)
    elif (derivative_order == 3):
        result = 0
    elif (derivative_order == 4):
        result = 0
    elif (derivative_order == 5):
        result = 0
    else:
        result = 0

    return result


#################################################
### Main Function
#################################################


def main():
    integral_max = 1
    integral_min = 0
    step = 0.25
    # num_of_points = int((integral_max - integral_min) / step)
    num_of_points = 10

    gaussian_quadrature(num_of_points, integral_max, integral_min)

    trapezoidal_rule(num_of_points, integral_max, integral_min)
    trapezoidal_rule_error(num_of_points, integral_max, integral_min)


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



def trapezoidal_rule(num_of_points, integral_max, integral_min):
    """
    Regra das trapézios
    """

    step = (integral_max - integral_min) / num_of_points

    result = f_function(integral_min)

    for i in range(1, num_of_points):
        result += (2 * f_function(integral_min + i * step))

    result += f_function(integral_max)

    result *= (step / 2)

    print(result)



def trapezoidal_rule_error(num_of_points, integral_max, integral_min):
    """
    Cálculo do erro para a regra das trapézios
    """

    step = (integral_max - integral_min) / num_of_points

    max_f_second_deriv = abs(f_derivative(integral_min, 2))

    for i in range(1, num_of_points + 1):
        f_second_deriv_value = abs(f_derivative(integral_min + i * step, 2))

        if (f_second_deriv_value > max_f_second_deriv):
            max_f_second_deriv = f_second_deriv_value

    error = num_of_points * ((step**3) / 12) * max_f_second_deriv

    print(f"Erro = {error}")


#################################################
### Main Function Call
#################################################

if __name__ == "__main__":
    main()
