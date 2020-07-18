#!/usr/bin/env python3

import numpy as np
import sympy as sym

#################################################
### Main Function
#################################################

"""
Para uma EDO em função de x (e suas derivadas) e t.

f(t, x, y) = x' = y

Substituir x' por y e isolar y', fazendo:

g(t, x, y) = y'

"""

def main():
    # Important => f(t, x, y) = x'
    f_function = lambda t, x, y: y

    # Important => g(t, x, y) = y'
    g_function = lambda t, x, y: -t * y - x

   # Method order
    order = 2

    # Parameters
    step = 1
    y0 = 0
    x0 = 1
    t0 = 0
    tf = 1

    if (order == 1):
        euler_method(y0, x0, t0, tf, step, f_function, g_function)
    elif (order == 2):
        modified_euler_method(y0, x0, t0, tf, step, f_function, g_function)
    elif (order == 3):
        runge_kutta_third_order(y0, x0, t0, tf, step, f_function, g_function)
    elif (order == 4):
        runge_kutta_fourth_order(y0, x0, t0, tf, step, f_function, g_function)
    else:
        print("Calma lá também né")


#################################################
### Methods functions
#################################################

def euler_method(y0, x0, t0, tf, step, f_function, g_function):
    """
    Método de Euler, método de primeira ordem
    """

    tn = t0
    wn = [x0, y0]

    print(f"tn = {tn} => wn = {wn}")

    num_of_ts = int((tf - t0) / step)

    for _ in range(num_of_ts):
        k1 = [f_function(tn, wn[0], wn[1]), g_function(tn, wn[0], wn[1])]

        print(f"k1 = {k1}")

        wnp1 = wn + step * np.array(k1)

        wn = np.copy(wnp1)
        tn += step

        print(f"tn = {tn} => wn = {wn}")

    print(f"x({tn}) = {wn[0]}")


def modified_euler_method(y0, x0, t0, tf, step, f_function, g_function):
    """
    Método de Euler modificado, método de segunda ordem
    """

    tn = t0
    wn = [x0, y0]

    print(f"tn = {tn} => wn = {wn}")

    num_of_ts = int((tf - t0) / step)

    for _ in range(num_of_ts):
        k1 = [f_function(tn, wn[0], wn[1]), g_function(tn, wn[0], wn[1])]

        k2 = [f_function(tn + step, wn[0] + step * k1[0], wn[1] + step * k1[1]),
              g_function(tn + step, wn[0] + step * k1[0], wn[1] + step * k1[1])]

        print(f"k1 = {k1} & k2 = {k2}")

        wnp1 = wn + (step / 2) * (np.array(k1) + np.array(k2))

        wn = np.copy(wnp1)
        tn += step

        print(f"tn = {tn} => wn = {wn}")

    print(f"x({tn}) = {wn[0]}")



def runge_kutta_third_order(y0, x0, t0, tf, step, f_function, g_function):
    """
    Runge-Kutta de terceira ordem
    """

    tn = t0
    wn = [x0, y0]

    print(f"tn = {tn} => wn = {wn}")

    num_of_ts = int((tf - t0) / step)

    for _ in range(num_of_ts):
        k1 = step * np.array([f_function(tn, wn[0], wn[1]), g_function(tn, wn[0], wn[1])])

        k2 = step * np.array([f_function(tn + step / 2, wn[0] + k1[0] / 2, wn[1] + k1[1] / 2),
                              g_function(tn + step / 2, wn[0] + k1[0] / 2, wn[1] + k1[1] / 2)])

        k3 = step * np.array([f_function(tn + 3 * step / 4, wn[0] + 3 * k2[0] / 4, wn[1] + 3 * k2[1] / 4),
                              g_function(tn + 3 * step / 4, wn[0] + 3 * k2[0] / 4, wn[1] + 3 * k2[1] / 4)])

        wnp1 = wn + 2 * np.array(k1) / 9 + np.array(k2) / 3 + 4 * np.array(k3) / 9

        wn = np.copy(wnp1)
        tn += step

        print(f"tn = {tn} => wn = {wn}")

    print(f"x({tn}) = {wn[0]}")



def runge_kutta_fourth_order(y0, x0, t0, tf, step, f_function, g_function):
    """
    Runge-Kutta de quarta ordem
    """

    tn = t0
    wn = [x0, y0]

    print(f"tn = {tn} => wn = {wn}")

    num_of_ts = int((tf - t0) / step)

    for _ in range(num_of_ts):
        k1 = step * np.array([f_function(tn, wn[0], wn[1]), g_function(tn, wn[0], wn[1])])

        k2 = step * np.array([f_function(tn + step / 2, wn[0] + k1[0] / 2, wn[1] + k1[1] / 2),
                              g_function(tn + step / 2, wn[0] + k1[0] / 2, wn[1] + k1[1] / 2)])

        k3 = step * np.array([f_function(tn + step / 2, wn[0] + k2[0] / 2, wn[1] + k2[1] / 2),
                              g_function(tn + step / 2, wn[0] + k2[0] / 2, wn[1] + k2[1] / 2)])

        k4 = step * np.array([f_function(tn + step, wn[0] + k3[0], wn[1] + k3[1]),
                              g_function(tn + step, wn[0] + k3[0], wn[1] + k3[1])])

        print(f"k1 = {k1}, k2 = {k2}, k3 = {k3}, k4 = {k4}")

        wnp1 = wn + (np.array(k1) + 2 * np.array(k2) + 2 * np.array(k3) + np.array(k4)) / 6

        wn = np.copy(wnp1)
        tn += step

        print(f"tn = {tn} => wn = {wn}")

    print(f"x({tn}) = {wn[0]}")


#################################################
### Main Function Call
#################################################

if __name__ == "__main__":
    main()
