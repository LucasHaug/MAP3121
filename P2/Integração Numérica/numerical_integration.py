#!/usr/bin/env python3

import numpy as np
from scipy.special import roots_legendre
import sympy as sym

#################################################
### Main Function
#################################################


def main():
    # Method to be used
    method = "RM"

    # Function to be integrated
    f_function = lambda x: np.sin(x)

    # For errors calculation
    f_second_derivative = lambda x: np.exp(x)
    f_fourth_derivative = lambda x: np.exp(x)

    # Parameters
    integral_max = np.pi
    integral_min = 0
    step = 0.1
    num_of_points = int((integral_max - integral_min) / step)
    # num_of_points = 10
    array_of_num_of_points = [1, 2, 4, 8, 16]

    if (method == "GQ"):
        result = gaussian_quadrature(num_of_points, integral_max, integral_min, f_function)
        error = "'Não sei'"
    elif (method == "TR"):
        result = trapezoidal_rule(num_of_points, integral_max, integral_min, f_function)
        error = trapezoidal_rule_error(num_of_points, integral_max, integral_min, f_second_derivative)
    elif (method == "SR"):
        result = simpson_rule(num_of_points, integral_max, integral_min, f_function)
        error = simpson_rule_error(num_of_points, integral_max, integral_min, f_fourth_derivative)
    elif (method == "RM"):
        result = rombergs_method(array_of_num_of_points, integral_max, integral_min, f_function)
        error = "'Não sei'"
    else:
        print("Tente novamente")

    print(f"Pelo método {method}, resultado de {result}, com erro de {error}")


#################################################
### Methods functions
#################################################

def gaussian_quadrature(num_of_points, integral_max, integral_min, f_function):
    """
    Quadratura Gaussiana
    """

    x_array, w_array = roots_legendre(num_of_points) # pylint: disable=unbalanced-tuple-unpacking

    result = 0

    for i in range(len(x_array)):
        t = x_array[i] * (integral_max - integral_min) / 2 + (integral_max + integral_min) / 2

        result += w_array[i] * f_function(t)

    result *= ((integral_max - integral_min) / 2)

    return result



def trapezoidal_rule(num_of_points, integral_max, integral_min, f_function):
    """
    Regra das trapézios
    """

    step = (integral_max - integral_min) / num_of_points

    result = f_function(integral_min)

    for i in range(1, num_of_points):
        result += (2 * f_function(integral_min + i * step))

    result += f_function(integral_max)

    result *= (step / 2)

    return result



def trapezoidal_rule_error(num_of_points, integral_max, integral_min, f_second_derivative):
    """
    Cálculo do erro máximo para a regra das trapézios
    """

    step = (integral_max - integral_min) / num_of_points

    max_f_second_deriv = abs(f_second_derivative(integral_min))

    for i in range(1, num_of_points + 1):
        f_second_deriv_value = abs(f_second_derivative(integral_min + i * step))

        if (f_second_deriv_value > max_f_second_deriv):
            max_f_second_deriv = f_second_deriv_value

    error = num_of_points * ((step**3) / 12) * max_f_second_deriv

    return error



def simpson_rule(num_of_points, integral_max, integral_min, f_function):
    """
    Regra de Simpson
    """

    if ((num_of_points + 1) % 2 ==0):
        num_of_points -= 1

    step = (integral_max - integral_min) / num_of_points

    result = f_function(integral_min)

    for i in range(1, num_of_points):
        if (i % 2 == 1):
            result += (4 * f_function(integral_min + i * step))
        else:
            result += (2 * f_function(integral_min + i * step))

    result += f_function(integral_max)

    result *= (step / 3)

    return result



def simpson_rule_error(num_of_points, integral_max, integral_min, f_fourth_derivative):
    """
    Cálculo do erro máximo para a regra de simpson
    """

    step = (integral_max - integral_min) / num_of_points

    max_f_fourth_deriv = abs(f_fourth_derivative(integral_min))

    for i in range(1, num_of_points + 1):
        f_second_deriv_value = abs(f_fourth_derivative(integral_min + i * step))

        if (f_second_deriv_value > max_f_fourth_deriv):
            max_f_fourth_deriv = f_second_deriv_value

    error = (num_of_points / 2) * ((step**5) / 90) * max_f_fourth_deriv

    return error



def rombergs_method(array_of_num_of_points, integral_max, integral_min, f_function):
    """
    Método de Romberg
    """

    num_of_ns = 3

    array = [1/4, 7/24, 509/1680]

    r_matrix = np.zeros((num_of_ns, num_of_ns), dtype=float)

    for k in range(0, num_of_ns):
        r_matrix[k][0] = array[k]
        print(f"R[{k}][{0}] = {sym.nsimplify(r_matrix[k][0])}")

    for j in range(1, num_of_ns):
        for k in range(j, num_of_ns):
            r_matrix[k][j] = r_matrix[k][j - 1] + (1 / ((4**(j)) - 1)) * (r_matrix[k][j - 1] - r_matrix[k - 1][j - 1])
            print(f"R[{k}][{j}] = {sym.nsimplify(r_matrix[k][j])}")

    return r_matrix[num_of_ns - 1][num_of_ns - 1]



#################################################
### Main Function Call
#################################################

if __name__ == "__main__":
    main()
