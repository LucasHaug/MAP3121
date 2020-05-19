#!/usr/bin/env python3

import numpy as np
from math import sin, cos

import plotter

def f_function(t, x, N, letter):
    if letter == "a":
        result = 10 * cos(10 * t) * (x**2) * ((1 - x)**2) - (1 + sin(10 * t)) * (12 * (x**2) - 12 * x + 2)
    elif letter == "b":
        pass
    elif letter == "c":
        r = 10000 * (1 - 2 * (t**2))

        h = 1 / N
        p = 0.25

        if (p - h / 2) <= x and x <= (p + h / 2):
            gh = N
        else:
            gh = 0

        result = r * gh
    else:
        result = 0
   
    return result

def u_solution(t, x, letter):
    if letter == "a":
        result = (1 + sin(10 * t)) * (x**2) * ((1 - x)**2)
    elif letter == "b":
        pass
    elif letter == "c":
        result = 0
    else:
        result = 0
   
    return result

def initial_condition(x, letter): 
    if letter == "a":
        result = (x**2) * ((1 - x)**2)
    elif letter == "b":
        pass
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
        cond_zero = 0
        cond_one = 0
    elif letter == "c":
        cond_zero = 0
        cond_one = 0
    else:
        cond_zero = 0
        cond_one = 0

    return cond_zero, cond_one

def run(letter, N, M, λ, Δx, Δt, images_dir):
    # Create and initializes x array 
    x_array = np.zeros(N + 1)

    for i in range(0, N + 1):
        # Uses N due to precision
        x_array[i] = i / N

    # Create and initializes time array 
    time_array = np.zeros(M + 1)

    for k in range(0, M + 1):
        time_array[k] = k * Δt

    # Create U matrix
    U = np.zeros((M + 1, N + 1))  

    # Initial conditions calculation
    for i in range(0, N + 1):
        U[0][i] = initial_condition(x_array[i], letter)
   
    # Boundary conditions calculation
    for k in range(0, M + 1):
        U[k][0], U[k][N] = boundary_conditions(time_array[i], letter)

    # Inside points calculation
    for k in range(0, M):
        for i in range(1, N):
            U[k + 1][i] = U[k][i] + Δt * (((U[k][i - 1] - 2 * U[k][i] + U[k][i + 1]) / (Δx**2)) + f_function(time_array[k], x_array[i], N, letter))

    # Plotting u(t, x)
    plotter.u_2d_graph(U, x_array, time_array, 11, f"1{letter.capitalize()}_APPROX_{N}_{round(λ * 100)}", True, False, images_dir)

    plotter.u_3d_graph(U, x_array, time_array, N, f"1{letter.capitalize()}_APPROX_{N}_{round(λ * 100)}", True, False, images_dir)

    # Plotting the u solution
    u_sol = np.zeros((M + 1, N + 1))  

    for k in range(0, M + 1):
        for i in range(0, N + 1):
            u_sol[k][i] = u_solution(time_array[k], x_array[i], letter)

    plotter.u_2d_graph(u_sol, x_array, time_array, 11, f"1{letter.capitalize()}_SOL_{N}_{round(λ * 100)}", True, False, images_dir)

    plotter.u_3d_graph(u_sol, x_array, time_array, N, f"1{letter.capitalize()}_SOL_{N}_{round(λ * 100)}", True, False, images_dir)

    # Truncation error calculation
    max_truncation_error = 0

    for k in range(0, M):
        for i in range(1, N):
            first_term = (u_solution(time_array[k + 1], x_array[i], letter) - u_solution(time_array[k], x_array[i], letter)) / Δt
            second_term = (u_solution(time_array[k], x_array[i - 1], letter) - 2 * u_solution(time_array[k], x_array[i], letter) + u_solution(time_array[k], x_array[i + 1], letter)) / (Δx**2)

            current_truncation_error = abs(first_term - second_term - f_function(time_array[k], x_array[i], N, letter))

            if current_truncation_error > max_truncation_error:
                max_truncation_error = current_truncation_error

    print(f"O erro máximo de truncamento é {max_truncation_error}")

    # Approximation error calculation for T = 1
    max_approx_error = 0

    for i in range(0, N):
        current_approx_error = abs(u_solution(time_array[M], x_array[i], letter) - U[M][i])

        if current_approx_error > max_approx_error:
            max_approx_error = current_approx_error

    print(f"O erro máximo de aproximação é {max_approx_error}")
