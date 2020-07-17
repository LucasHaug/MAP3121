#!/usr/bin/env python3

import numpy as np

#################################################
### Change for each problem
#################################################

def f_function(x, y):
    """
    f(x, y) = y'
    """

    result = y - x

    return result


#################################################
### Main Function
#################################################


def main():
    order = 1

    h = 0.2
    x0 = 0
    xf = 1
    y0 = 2

    if (order == 1):
        euler_method(y0, x0, xf, h)
    elif (order == 2):
        modified_euler_method(y0, x0, xf, h)
    elif (order == 3):
        runge_kutta_third_order(y0, x0, xf, h)
    elif (order == 4):
        runge_kutta_fourth_order(y0, x0, xf, h)
    else:
        print("Calma lá também né")


#################################################
### Methods functions
#################################################

def euler_method(y0, x0, xf, h):
    """
    Método de Euler, método de primeira ordem
    """

    xn = x0
    yn = y0

    print(f"y({xn}) = {yn}")

    num_of_xs = int((xf - x0) / h)

    for _ in range(num_of_xs):
        k1 = f_function(xn, yn)

        print(f"k1 = {k1}")

        ynp1 = yn + h * k1

        yn = ynp1
        xn += h

        print(f"y({xn}) = {yn}")


def modified_euler_method(y0, x0, xf, h):
    """
    Método de Euler modificado, método de segunda ordem
    """

    xn = x0
    yn = y0

    print(f"y({xn}) = {yn}")

    num_of_xs = int((xf - x0) / h)

    for _ in range(num_of_xs):
        k1 = f_function(xn, yn)

        k2 = f_function(xn + h, yn + h * k1)

        print(f"k1 = {k1} & k2 = {k2}")


        ynp1 = yn + h * (k1 + k2) / 2

        yn = ynp1
        xn += h

        print(f"y({xn}) = {yn}")



def runge_kutta_third_order(y0, x0, xf, h):
    """
    Runge-Kutta de terceira ordem
    """

    xn = x0
    yn = y0

    print(f"y({xn}) = {yn}")

    num_of_xs = int((xf - x0) / h)

    for _ in range(num_of_xs):
        k1 = h * f_function(xn, yn)
        k2 = h * f_function(xn + h / 2, yn + k1 / 2)
        k3 = h * f_function(xn + 3 * h / 4, yn + 3 * k2 / 4)

        ynp1 = yn + 2 * k1 / 9 + k2 / 3 + 4 * k3 / 9

        yn = ynp1
        xn += h

        print(f"y({xn}) = {yn}")



def runge_kutta_fourth_order(y0, x0, xf, h):
    """
    Runge-Kutta de quarta ordem
    """

    xn = x0
    yn = y0

    print(f"y({xn}) = {yn}")

    num_of_xs = int((xf - x0) / h)

    for _ in range(num_of_xs):
        k1 = h * f_function(xn, yn)
        k2 = h * f_function(xn + h / 2, yn + k1 / 2)
        k3 = h * f_function(xn + h / 2, yn + k2 / 2)
        k4 = h * f_function(xn + h, yn + k3)

        print(f"k1 = {k1}, k2 = {k2}, k3 = {k3}, k4 = {k4}")

        ynp1 = yn + (k1 + 2 * k2 + 2 * k3 + k4) / 6

        yn = ynp1
        xn += h

        print(f"y({xn}) = {yn}")


#################################################
### Main Function Call
#################################################

if __name__ == "__main__":
    main()
