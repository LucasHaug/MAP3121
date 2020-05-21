#!/usr/bin/env python3

import numpy as np

import problems as pb
import plotter

#################################################
### Public Variables
#################################################

ENABLE_ERRORS_CALCULATION = True
ENABLE_SOLUTION_PLOTTING = False

#################################################
### Functions Definitions
#################################################

def run(letter, task_result_dir):
    """
    Soluciona o problema da equação de calor.
    """

    # Input parameters
    N = int(input("Insira o valor de N: "))
    λ = float(input("Insira o valor de λ: "))

    # Total amount of time in seconds
    total_time_s = 1

    Δx = 1 / float(N)
    Δt = λ * (Δx**2)

    M = int(round(total_time_s / Δt))

    print(f"N: {N}, M: {M}, λ: {λ}, Δx: {Δx} e Δt: {Δt}")

    # Resuls file
    results_file_name = f"{task_result_dir}/1{letter.capitalize()}_{N}_{round(λ * 100)}_ERRORS.txt"

    if letter != "c" and ENABLE_ERRORS_CALCULATION == True:
        results_file = open(results_file_name, 'w')

    # Create and initializes x array
    x_array = np.zeros(N + 1)

    for i in range(0, N + 1):
        x_array[i] = i / N

    # Create and initializes time array
    time_array = np.zeros(M + 1)

    for k in range(0, M + 1):
        time_array[k] = k * Δt

    # Create U matrix
    U = pb.create_u(time_array, x_array, letter)

    # Inside points calculation
    for k in range(0, M):
        for i in range(1, N):
            U[k + 1][i] = U[k][i] + Δt * (((U[k][i - 1] - 2 * U[k][i] + U[k][i + 1]) / (Δx**2))
                        + pb.heat_source(time_array[k], x_array[i], N, letter))

    # Plotting u(t, x)
    approx_image_name = f"1{letter.capitalize()}_{N}_{round(λ * 100)}_APPROX"

    plotter.u_2d_graph(U, x_array, time_array, 11, approx_image_name, True, False, task_result_dir)

    plotter.u_3d_graph(U, x_array, time_array, N, approx_image_name, True, False, task_result_dir)

    if letter != "c":
        if ENABLE_SOLUTION_PLOTTING == True:
            # Plotting the u solution
            u_sol = np.zeros((M + 1, N + 1))

            for k in range(0, M + 1):
                for i in range(0, N + 1):
                    u_sol[k][i] = pb.u_solution(time_array[k], x_array[i], letter)

            sol_image_name = f"1{letter.capitalize()}_{N}_{round(λ * 100)}_SOL"

            plotter.u_2d_graph(u_sol, x_array, time_array, 11, sol_image_name, True, False, task_result_dir)

            plotter.u_3d_graph(u_sol, x_array, time_array, N, sol_image_name, True, False, task_result_dir)

        if ENABLE_ERRORS_CALCULATION == True:
            # Truncation error calculation
            max_truncation_error = 0

            for k in range(0, M):
                for i in range(1, N):
                    first_term = (pb.u_solution(time_array[k + 1], x_array[i], letter)
                               - pb.u_solution(time_array[k], x_array[i], letter)) / Δt
                    second_term = (pb.u_solution(time_array[k], x_array[i - 1], letter)
                                - 2 * pb.u_solution(time_array[k], x_array[i], letter)
                                + pb.u_solution(time_array[k], x_array[i + 1], letter)) / (Δx**2)

                    current_truncation_error = abs(first_term - second_term - pb.heat_source(time_array[k], x_array[i], N, letter))

                    if current_truncation_error > max_truncation_error:
                        max_truncation_error = current_truncation_error

            max_truncation_error_result = f"O erro máximo de truncamento é {max_truncation_error}"
            print(max_truncation_error_result)
            results_file.write(max_truncation_error_result + "\n")

            # Approximation error calculation for T = 1
            max_approx_error = 0

            for i in range(0, N):
                current_approx_error = abs(pb.u_solution(time_array[M], x_array[i], letter) - U[M][i])

                if current_approx_error > max_approx_error:
                    max_approx_error = current_approx_error

            max_approx_error_result = f"O erro máximo de aproximação é {max_approx_error}"
            print(max_approx_error_result)
            results_file.write(max_approx_error_result)

        # End task
        results_file.close()
