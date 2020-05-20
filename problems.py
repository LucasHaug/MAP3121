#!/usr/bin/env python3

import numpy as np

def heat_source(t, x, N, letter):
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
    # Conditions at (t, 0) and (t, 1)

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
