#!/usr/bin/env python3

import numpy as np

import plotter

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

def run(letter, N, M, λ, Δx, Δt, results_dir):
    # Resuls file
    results_file_name = f"{results_dir}/1{letter.capitalize()}_{N}_{round(λ * 100)}_ERRORS.txt"

    results_file = open(results_file_name, 'w')

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
        U[k][0], U[k][N] = boundary_conditions(time_array[k], letter)

    # Inside points calculation
    for k in range(0, M):
        for i in range(1, N):
            U[k + 1][i] = U[k][i] + Δt * (((U[k][i - 1] - 2 * U[k][i] + U[k][i + 1]) / (Δx**2)) + heat_source(time_array[k], x_array[i], N, letter))

    # Plotting u(t, x)
    plotter.u_2d_graph(U, x_array, time_array, 11, f"1{letter.capitalize()}_{N}_{round(λ * 100)}_APPROX", False, True, results_dir)

    plotter.u_3d_graph(U, x_array, time_array, N, f"1{letter.capitalize()}_{N}_{round(λ * 100)}_APPROX", False, True, results_dir)

    # Plotting the u solution
    u_sol = np.zeros((M + 1, N + 1))  

    for k in range(0, M + 1):
        for i in range(0, N + 1):
            u_sol[k][i] = u_solution(time_array[k], x_array[i], letter)

    plotter.u_2d_graph(u_sol, x_array, time_array, 11, f"1{letter.capitalize()}_{N}_{round(λ * 100)}_SOL", False, True, results_dir)

    plotter.u_3d_graph(u_sol, x_array, time_array, N, f"1{letter.capitalize()}_{N}_{round(λ * 100)}_SOL", False, True, results_dir)

    # Truncation error calculation
    max_truncation_error = 0

    for k in range(0, M):
        for i in range(1, N):
            first_term = (u_solution(time_array[k + 1], x_array[i], letter) - u_solution(time_array[k], x_array[i], letter)) / Δt
            second_term = (u_solution(time_array[k], x_array[i - 1], letter) - 2 * u_solution(time_array[k], x_array[i], letter) + u_solution(time_array[k], x_array[i + 1], letter)) / (Δx**2)

            current_truncation_error = abs(first_term - second_term - heat_source(time_array[k], x_array[i], N, letter))

            if current_truncation_error > max_truncation_error:
                max_truncation_error = current_truncation_error

    max_truncation_error_result = f"O erro máximo de truncamento é {max_truncation_error}"
    print(max_truncation_error_result)
    results_file.write(max_truncation_error_result + "\n")

    # Approximation error calculation for T = 1
    max_approx_error = 0

    for i in range(0, N):
        current_approx_error = abs(u_solution(time_array[M], x_array[i], letter) - U[M][i])

        if current_approx_error > max_approx_error:
            max_approx_error = current_approx_error

    max_approx_error_result = f"O erro máximo de aproximação é {max_approx_error}"
    print(max_approx_error_result)
    results_file.write(max_approx_error_result)

    # End task
    results_file.close()
