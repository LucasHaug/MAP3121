#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np
from math import sin, cos

import plotter

def f_function(t, x):
    result = 10 * cos(10 * t) * (x**2) * ((1 - x)**2) - (1 + sin(10 * t)) * (12 * (x**2) - 12 * x + 2)
    return result

def initial_condition(x):
    result = (x**2) * ((1 - x)**2)
    return result

def main():
    # Input parameters
    N = int(input("Insira o valor de N: "))
    λ = float(input("Insira o valor de λ: "))

    # Total amount of time in seconds
    total_time_s = 1

    Δx = 1 / float(N)
    Δt = λ * (Δx**2)

    M = int(round(total_time_s / Δt))

    print(f"N: {N}, M: {M}, λ: {λ}, Δx: {Δx} e Δt: {Δt}")

    # Create and initializes x array 
    x_array = np.zeros(N + 1)

    for i in range(0, N + 1):
        # Uses N due to precision
        x_array[i] = i / N

    # Create and initializes t array 
    t_array = np.zeros(M + 1)

    for k in range(0, M + 1):
        t_array[k] = k * Δt

    # Boundary Conditions are zero
    # Initial conditions calculation
    U = np.zeros((M + 1, N + 1))  

    for i in range(0, N + 1):
        U[0][i] = initial_condition(x_array[i])

    # Inside points calculation
    for k in range(0, M):
        for i in range(1, N):
            U[k + 1][i] = U[k][i] + Δt * (((U[k][i - 1] - 2 * U[k][i] + U[k][i + 1]) / (Δx**2)) + f_function(t_array[k], x_array[i]))

    plotter.u_2d_graph(U, x_array, t_array, 11, f"{N}_{round(λ * 100)}")

    plotter.u_3d_graph(U, x_array, t_array, N, f"{N}_{round(λ * 100)}")

if __name__ == "__main__":
    main()