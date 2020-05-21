#!/usr/bin/env python3

import numpy as np

import problems as pb
import plotter

def matrix_decomposition(a_matrix_diag, a_matrix_subdiag):
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
    # L * y = b, D * z = y, L' * x = z

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

    # Third system solution -> L' * x = z
    x_array = np.zeros(array_size, dtype=float)

    x_array[-1] = z_array[-1]

    for i in reversed(range(0, array_size - 1)):
        x_array[i] = z_array[i] - l_matrix_array[i + 1] * x_array[i + 1]

    return x_array

def run(letter, task_result_dir):
    # Input parameters
    N = int(input("Insira o valor de N: "))
    M = N

    Δx = 1 / float(N)
    Δt = Δx

    λ = Δt / (Δx**2)

    print(f"N: {N}, λ: {λ}, Δx: {Δx} e Δt: {Δt}")

    # A Matrix creation
    a_matrix_diag = np.full(N - 1, 1 + 2 * λ, dtype=float)
    a_matrix_subdiag = np.full(N - 1, -λ, dtype=float)

    # B array creation
    b_array = np.zeros(N - 1, dtype=float)

    # Create and initializes scale array
    scale_array = np.zeros(N + 1, dtype=float)

    for i in range(0, N + 1):
        # Uses N due to precision
        scale_array[i] = i / N

    # Create U matrix
    U = np.zeros((M + 1, N + 1))

    # Initial conditions calculation
    for i in range(0, N + 1):
        U[0][i] = pb.initial_condition(scale_array[i], letter)

    # Boundary conditions calculation
    for k in range(0, M + 1):
        U[k][0], U[k][N] = pb.boundary_conditions(scale_array[k], letter)

    # Inside points calculation
    for k in range(0, M):
        # b array calculation
        for i in range(1, N):
            b_array[i - 1] = U[k][i] + Δt * pb.heat_source(scale_array[k + 1], scale_array[i], N, letter)

        g1, g2 = pb.boundary_conditions(scale_array[k + 1], letter)

        b_array[0] += λ * g1
        b_array[-1] += λ * g2

        solution = solve_system(a_matrix_diag, a_matrix_subdiag, b_array)

        for i in range(1, N):
            U[k + 1][i] = solution[i - 1]

    # Plotting u(t, x)
    plotter.u_2d_graph(U, scale_array, scale_array, 11, f"2{letter.capitalize()}_{N}_APPROX", True, False, task_result_dir)

    plotter.u_3d_graph(U, scale_array, scale_array, N, f"2{letter.capitalize()}_{N}_APPROX", True, False, task_result_dir)
