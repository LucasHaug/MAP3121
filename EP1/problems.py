#!/usr/bin/env python3

import numpy as np

#################################################
### Functions Definitions
#################################################

def heat_source(t, x, N, letter):
    """
    Calcula o valor da fonte de calor de um determinado problema,
    em um determinado instante, em uma determinada posição.
    """

    if letter == "a":
        result = 10 * np.cos(10 * t) * (x**2) * ((1 - x)**2) - (1 + np.sin(10 * t)) * (12 * (x**2) - 12 * x + 2)
    elif letter == "b":
        result = 5 * np.exp(t - x) * ((5 * (t**2) * np.cos(5 * t * x)) - (np.sin(5 * t * x) * (2 * t + x)))
    elif letter == "c":
        r = 10000 * (1 - 2 * (t**2))

        h = 1 / N
        p = 0.25

        if (p - h / 2) <= x <= (p + h / 2):
            gh = N
        else:
            gh = 0

        result = r * gh
    else:
        result = 0

    return result



def u_solution(t, x, letter):
    """
    Calcula o valor da solução de um determinado problema,
    em um determinado instante, em uma determinada posição.
    """

    if letter == "a":
        result = (1 + np.sin(10 * t)) * (x**2) * ((1 - x)**2)
    elif letter == "b":
        result = np.exp(t - x) * np.cos(5 * t * x)
    elif letter == "c":
        result = 0
    else:
        result = 0

    return result



def initial_condition(x, letter):
    """
    Retorna as condições iniciais de u determinado problema em
    uma determinada posição.
    """

    if letter == "a":
        result = (x**2) * ((1 - x)**2)
    elif letter == "b":
        # result = u_solution(0, x, letter)
        result = np.exp(-x)
    elif letter == "c":
        result = 0
    else:
        result = 0

    return result



def boundary_conditions(t, letter):
    """
    Retorna as condições de contorno de um determinado problema,
    em um determinado instante.

    Se retorna primeiro a condição de contorno em x = 0, depois
    em x = 1.
    """

    if letter == "a":
        cond_zero = 0
        cond_one = 0
    elif letter == "b":
        # cond_zero = u_solution(t, 0, letter)
        cond_zero = np.exp(t)
        # cond_one = u_solution(t, 1, letter)
        cond_one = np.exp(t - 1) * np.cos(5 * t)
    elif letter == "c":
        cond_zero = 0
        cond_one = 0
    else:
        cond_zero = 0
        cond_one = 0

    return cond_zero, cond_one



def create_u(times_array, positions_array, letter):
    """
    Cria uma matrix U, dado um vetor com a discretização do tempo
    e um vetor com a descretização do espaço.

    A matriz é inicializada com as condições de contorno e condições
    iniciais, dependendo do problema que se está analizando.
    """

    num_of_times = len(times_array)
    num_of_position = len(positions_array)

    # Create U matrix
    U = np.zeros((num_of_times, num_of_position))

    # Initial conditions calculation
    for i in range(0, num_of_position):
        U[0][i] = initial_condition(positions_array[i], letter)

    # Boundary conditions calculation
    for k in range(0, num_of_times):
        U[k][0], U[k][-1] = boundary_conditions(times_array[k], letter)

    return U
