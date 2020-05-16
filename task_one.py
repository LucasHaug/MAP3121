#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np
import os
from math import sin, cos

import plotter

def f_function(t, x):
    result = 10 * cos(10 * t) * (x**2) * ((1 - x)**2) - (1 + sin(10 * t)) * (12 * (x**2) - 12 * x + 2)
    return result

def initial_condition(x):
    result = (x**2) * ((1 - x)**2)
    return result

def boundary_conditions(t):
    # Conditions at (t, 0) and (t, 1)
    return 0, 0

def run(letter, N, M, λ, Δx, Δt, images_dir):
    # Create and initializes x array 
    x_array = np.zeros(N + 1)

    for i in range(0, N + 1):
        # Uses N due to precision
        x_array[i] = i / N

    # Create and initializes t array 
    time_array = np.zeros(M + 1)

    for k in range(0, M + 1):
        time_array[k] = k * Δt

    # Create U matrix
    U = np.zeros((M + 1, N + 1))  

    # Initial conditions calculation
    for i in range(0, N + 1):
        U[0][i] = initial_condition(x_array[i])
   
    # Boundary conditions calculation
    for k in range(0, M + 1):
        U[k][0], U[k][N] = boundary_conditions(time_array[i])

    # Inside points calculation
    for k in range(0, M):
        for i in range(1, N):
            U[k + 1][i] = U[k][i] + Δt * (((U[k][i - 1] - 2 * U[k][i] + U[k][i + 1]) / (Δx**2)) + f_function(time_array[k], x_array[i]))

    plotter.u_2d_graph(U, x_array, time_array, 11, f"1{letter.capitalize()}_{N}_{round(λ * 100)}", True, False, images_dir)

    plotter.u_3d_graph(U, x_array, time_array, N, f"1{letter.capitalize()}_{N}_{round(λ * 100)}", True, False, images_dir)
