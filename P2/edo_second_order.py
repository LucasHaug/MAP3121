#!/usr/bin/env python3

import numpy as np

#################################################
### Change for each problem
#################################################

"""
Para uma EDO em função de x (e suas derivadas) e t.

f(t, x, y) = x' = y

Substituir x' por y e isolar y', fazendo:

g(t, x, y) = y'

"""

def f_function(t, x, y):
    """
    f(t, x, y) = x'
    """

    result = y

    return result

def g_function(t, x, y):
    """
    g(t, x, y) = y'
    """

    result = -t * y - x

    return result


#################################################
### Main Function
#################################################


def main():
    order = 4

    h = 0.5
    y0 = 0
    x0 = 1
    t0 = 0
    tf = 1

    if (order == 1):
        first_order(y0, x0, t0, tf, h)
    elif (order == 2):
        second_order(y0, x0, t0, tf, h)
    elif (order == 3):
        third_order(y0, x0, t0, tf, h)
    elif (order == 4):
        fouth_order(y0, x0, t0, tf, h)
    else:
        print("Calma lá também né")


#################################################
### Methods functions
#################################################

def first_order(y0, x0, t0, tf, h):
    """
    Método de Euler, método de primeira ordem
    """

    tn = t0
    wn = [x0, y0]

    print(f"tn = {tn} => wn = {wn}")

    num_of_ts = int((tf - t0) / h)

    for _ in range(num_of_ts):
        k1 = [f_function(tn, wn[0], wn[1]), g_function(tn, wn[0], wn[1])]

        print(f"k1 = {k1}")

        wnp1 = wn + h * np.array(k1)

        wn = np.copy(wnp1)
        tn += h

        print(f"tn = {tn} => wn = {wn}")

    print(f"x({tn}) = {wn[0]}")


def second_order(y0, x0, t0, tf, h):
    """
    Método de Euler modificado, método de primeira ordem
    """

    tn = t0
    wn = [x0, y0]

    print(f"tn = {tn} => wn = {wn}")

    num_of_ts = int((tf - t0) / h)

    for _ in range(num_of_ts):
        k1 = [f_function(tn, wn[0], wn[1]), g_function(tn, wn[0], wn[1])]

        k2 = [f_function(tn + h, wn[0] + h * k1[0], wn[1] + h * k1[1]), g_function(tn + h, wn[0] + h * k1[0], wn[1] + h * k1[1])]

        print(f"k1 = {k1} & k2 = {k2}")

        wnp1 = wn + (h / 2) * (np.array(k1) + np.array(k2))

        wn = np.copy(wnp1)
        tn += h

        print(f"tn = {tn} => wn = {wn}")

    print(f"x({tn}) = {wn[0]}")



def third_order(y0, x0, t0, tf, h):
    """
    Runge-Kutta de terceira ordem
    """

    tn = t0
    wn = [x0, y0]

    print(f"tn = {tn} => wn = {wn}")

    num_of_ts = int((tf - t0) / h)

    for _ in range(num_of_ts):
        k1 = h * np.array([f_function(tn, wn[0], wn[1]), g_function(tn, wn[0], wn[1])])

        k2 = h * np.array([f_function(tn + h / 2, wn[0] + k1[0] / 2, wn[1] + k1[1] / 2),
                           g_function(tn + h / 2, wn[0] + k1[0] / 2, wn[1] + k1[1] / 2)])

        k3 = h * np.array([f_function(tn + 3 * h / 4, wn[0] + 3 * k2[0] / 4, wn[1] + 3 * k2[1] / 4),
                           g_function(tn + 3 * h / 4, wn[0] + 3 * k2[0] / 4, wn[1] + 3 * k2[1] / 4)])

        wnp1 = wn + 2 * np.array(k1) / 9 + np.array(k2) / 3 + 4 * np.array(k3) / 9

        wn = np.copy(wnp1)
        tn += h

        print(f"tn = {tn} => wn = {wn}")

    print(f"x({tn}) = {wn[0]}")



def fouth_order(y0, x0, t0, tf, h):
    """
    Runge-Kutta de quarta ordem
    """

    tn = t0
    wn = [x0, y0]

    print(f"tn = {tn} => wn = {wn}")

    num_of_ts = int((tf - t0) / h)

    for _ in range(num_of_ts):
        k1 = h * np.array([f_function(tn, wn[0], wn[1]), g_function(tn, wn[0], wn[1])])

        k2 = h * np.array([f_function(tn + h / 2, wn[0] + k1[0] / 2, wn[1] + k1[1] / 2),
                           g_function(tn + h / 2, wn[0] + k1[0] / 2, wn[1] + k1[1] / 2)])

        k3 = h * np.array([f_function(tn + h / 2, wn[0] + k2[0] / 2, wn[1] + k2[1] / 2),
                           g_function(tn + h / 2, wn[0] + k2[0] / 2, wn[1] + k2[1] / 2)])

        k4 = h * np.array([f_function(tn + h, wn[0] + k3[0], wn[1] + k3[1]),
                           g_function(tn + h, wn[0] + k3[0], wn[1] + k3[1])])

        print(f"k1 = {k1}, k2 = {k2}, k3 = {k3}, k4 = {k4}")

        wnp1 = wn + (np.array(k1) + 2 * np.array(k2) + 2 * np.array(k3) + np.array(k4)) / 6

        wn = np.copy(wnp1)
        tn += h

        print(f"tn = {tn} => wn = {wn}")

    print(f"x({tn}) = {wn[0]}")


#################################################
### Main Function Call
#################################################

if __name__ == "__main__":
    main()
