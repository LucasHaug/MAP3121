#!/usr/bin/env python3

import numpy as np

import problems as pb
import plotter

#################################################
### Public Variables
#################################################

ENABLE_ERRORS_CALCULATION = True
ENABLE_SOLUTION_PLOTTING = False

ENABLE_GRAPHS_VIEW = False
SAVE_GRAPHS_IMAGE = True

#################################################
### Functions Definitions
#################################################

def matrix_decomposition(a_matrix_diag, a_matrix_subdiag):
    """
    Decompõe uma matrix A tridiagonal simétrica em três matrizes
    L, D e Lt, retonando apenas dois vetores que representam as
    matrizes L e D.
    """

    array_size = len(a_matrix_diag)

    l_matrix_array = np.zeros(array_size, dtype=float)
    d_matrix_array = np.zeros(array_size, dtype=float)

    l_matrix_array[0] = 0
    d_matrix_array[0] = a_matrix_diag[0]

    for i in range(1, array_size):
        l_matrix_array[i] = a_matrix_subdiag[i] / d_matrix_array[i - 1]

        d_matrix_array[i] = a_matrix_diag[i] - d_matrix_array[i - 1] * ((l_matrix_array[i])**2)

    return l_matrix_array, d_matrix_array



def solve_system(a_matrix_diag, a_matrix_subdiag, b_array):
    """
    Soluciona um sistema Ax = b, onde A é uma matrix tridiagonal
    simétrica.

    Para a resolução do sistema, é feita a decomposição de A para L*D*Lt.

    É feita a divisão do problema em três sistemas menores:
    L * y = b
    D * z = y
    Lt * x = z
    """

    array_size = len(a_matrix_diag)

    l_matrix_array, d_matrix_array = matrix_decomposition(a_matrix_diag, a_matrix_subdiag)

    # First system solution -> L * y = b
    y_array = np.zeros(array_size, dtype=float)

    y_array[0] = b_array[0]

    for i in range(1, array_size):
        y_array[i] = b_array[i] - l_matrix_array[i] * y_array[i - 1]

    # Second system solution -> D * z = y
    z_array = np.zeros(array_size, dtype=float)

    for i in range(0, array_size):
        z_array[i] = y_array[i] / d_matrix_array[i]

    # Third system solution -> Lt * x = z
    x_array = np.zeros(array_size, dtype=float)

    x_array[-1] = z_array[-1]

    for i in reversed(range(0, array_size - 1)):
        x_array[i] = z_array[i] - l_matrix_array[i + 1] * x_array[i + 1]

    return x_array



def run(letter, task_result_dir):
    """
    Soluciona o problema da equação de calor a partir de dois métodos implícitos,
    Euler implícito e Crank-Nicolson.
    """

    # Input parameters
    method = (input("Qual método executar: Euler implícito ou (e) ou Crank-Nicolson (c)? ")).lower()

    while method not in ("e", "c"):
        print("Método não encontrado, escolha entre 'e' e 'c'")
        method = (input("Qual método executar: Euler implícitou (e) ou Crank-Nicolson (c)? ")).lower()

    if method == "e":
        method_name = "EULER_IMP"
    else:
        method_name = "CN"

    N = int(input("Insira o valor de N: "))
    M = N

    Δx = 1 / float(N)
    Δt = Δx

    λ = Δt / (Δx**2)

    print(f"N: {N}, λ: {λ}, Δx: {Δx} e Δt: {Δt}")

    # Resuls file
    results_file_name = f"{task_result_dir}/2{letter.capitalize()}_{method_name}_{N}_ERRORS.txt"

    if letter != "c" and ENABLE_ERRORS_CALCULATION == True:
        results_file = open(results_file_name, 'w')

    # A Matrix creation
    if method == "e":
        diag_value = 1 + 2 * λ
        subdiag_value = -λ
    else:
        diag_value = 1 + λ
        subdiag_value = -λ / 2

    a_matrix_diag = np.full(N - 1, diag_value, dtype=float)
    a_matrix_subdiag = np.full(N - 1, subdiag_value, dtype=float)

    # B array creation
    b_array = np.zeros(N - 1, dtype=float)

    # Create and initializes scale array
    scale_array = np.zeros(N + 1, dtype=float)

    for i in range(0, N + 1):
        scale_array[i] = i / N

    # Create U matrix
    U = pb.create_u(scale_array, scale_array, letter)

    # Inside points calculation
    for k in range(0, M):
        # b array calculation
        for i in range(1, N):
            if method == "e":
                b_array[i - 1] = U[k][i] + Δt * pb.heat_source(scale_array[k + 1], scale_array[i], N, letter)
            else:
                b_array[i - 1] = (U[k][i] + (λ / 2) * (U[k][i - 1] - 2 * U[k][i] + U[k][i + 1])
                               + (Δt / 2) * (pb.heat_source(scale_array[k], scale_array[i], N, letter)
                               + pb.heat_source(scale_array[k + 1], scale_array[i], N, letter)))

        g1, g2 = pb.boundary_conditions(scale_array[k + 1], letter)

        if method == "e":
            b_array[0] += λ * g1
            b_array[-1] += λ * g2
        else:
            b_array[0] += (λ / 2) * g1
            b_array[-1] += (λ / 2) * g2

        solution = solve_system(a_matrix_diag, a_matrix_subdiag, b_array)

        for i in range(1, N):
            U[k + 1][i] = solution[i - 1]

    # Plotting u(t, x)
    approx_image_name = f"2{letter.capitalize()}_{method_name}_{N}_APPROX"

    plotter.u_2d_graph(U, scale_array, scale_array, 11, approx_image_name, ENABLE_GRAPHS_VIEW, SAVE_GRAPHS_IMAGE, task_result_dir)

    plotter.u_3d_graph(U, scale_array, scale_array, N, approx_image_name, ENABLE_GRAPHS_VIEW, SAVE_GRAPHS_IMAGE, task_result_dir)

    if letter != "c":
        if ENABLE_SOLUTION_PLOTTING == True:
            # Plotting the u solution
            u_sol = np.zeros((M + 1, N + 1))

            for k in range(0, M + 1):
                for i in range(0, N + 1):
                    u_sol[k][i] = pb.u_solution(scale_array[k], scale_array[i], letter)

            sol_image_name = f"2{letter.capitalize()}_{method_name}_{N}_SOL"

            plotter.u_2d_graph(u_sol, scale_array, scale_array, 11, sol_image_name, ENABLE_GRAPHS_VIEW, SAVE_GRAPHS_IMAGE, task_result_dir)

            plotter.u_3d_graph(u_sol, scale_array, scale_array, N, sol_image_name, ENABLE_GRAPHS_VIEW, SAVE_GRAPHS_IMAGE, task_result_dir)

        if ENABLE_ERRORS_CALCULATION == True:
            if method == "e":
                # Truncation error calculation
                max_truncation_error = 0

                for k in range(0, M):
                    for i in range(1, N):
                        first_term = (pb.u_solution(scale_array[k + 1], scale_array[i], letter)
                                   - pb.u_solution(scale_array[k], scale_array[i], letter)) / Δt
                        second_term = (pb.u_solution(scale_array[k + 1], scale_array[i - 1], letter)
                                    - 2 * pb.u_solution(scale_array[k + 1], scale_array[i], letter)
                                    + pb.u_solution(scale_array[k + 1], scale_array[i + 1], letter)) / (Δx**2)

                        current_truncation_error = abs(first_term - second_term - pb.heat_source(scale_array[k + 1], scale_array[i], N, letter))

                        if current_truncation_error > max_truncation_error:
                            max_truncation_error = current_truncation_error

                max_truncation_error_result = f"O erro máximo de truncamento é {max_truncation_error}"
                print(max_truncation_error_result)
                results_file.write(max_truncation_error_result + "\n")

            # Approximation error calculation for T = 1
            max_approx_error = 0

            for i in range(0, N):
                current_approx_error = abs(pb.u_solution(scale_array[M], scale_array[i], letter) - U[M][i])

                if current_approx_error > max_approx_error:
                    max_approx_error = current_approx_error

            max_approx_error_result = f"O erro máximo de aproximação é {max_approx_error}"
            print(max_approx_error_result)
            results_file.write(max_approx_error_result)

        # End task
        results_file.close()
