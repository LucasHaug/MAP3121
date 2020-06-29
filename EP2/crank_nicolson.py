#!/usr/bin/env python3

import numpy as np

#################################################
### Functions Definitions
#################################################

def punctual_heat_source(source_position, t, x, N):
    """
    Calcula o valor de uma fonte de calor pontual, em um
    determinado instante, em uma determinada posição.
    """

    r = 10 * (1 + np.cos(5 * t))

    h = 1 / N
    p = source_position

    if (p - h / 2) <= x <= (p + h / 2):
        gh = N
    else:
        gh = 0

    result = r * gh

    return result



def initial_condition(x):
    """
    Retorna as condições iniciais do problema em
    uma determinada posição.
    """

    return 0



def boundary_conditions(t):
    """
    Retorna as condições de contorno do problema, em um determinado
    instante.

    Se retorna primeiro a condição de contorno em x = 0, depois
    em x = 1.
    """

    cond_zero = 0
    cond_one = 0

    return cond_zero, cond_one



def create_u(times_array, positions_array):
    """
    Cria uma matrix U, dado um vetor com a discretização do tempo
    e um vetor com a descretização do espaço.

    A matriz é inicializada com as condições de contorno e condições
    iniciais, dependendo do problema que se está analizando.
    """

    num_of_times = len(times_array)
    num_of_position = len(positions_array)

    # Create U matrix
    U = np.zeros((num_of_times, num_of_position))

    # Initial conditions calculation
    for i in range(0, num_of_position):
        U[0][i] = initial_condition(positions_array[i])

    # Boundary conditions calculation
    for k in range(0, num_of_times):
        U[k][0], U[k][-1] = boundary_conditions(times_array[k])

    return U



def matrix_decomposition(a_matrix_diag, a_matrix_subdiag):
    """
    Decompõe uma matrix A tridiagonal simétrica em três matrizes
    L, D e Lt, retornando apenas dois vetores que representam as
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



def solve_linear_system(a_matrix_diag, a_matrix_subdiag, b_array):
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



def solve_heat_equation(source_position, N):
    """
    Soluciona o problema da equação de calor a partir do método de
    Crank-Nicolson, retornando um vetor da solução no instante final.
    """

    M = N

    Δx = 1 / float(N)
    Δt = Δx

    λ = Δt / (Δx**2)

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
    U = create_u(scale_array, scale_array)

    # Inside points calculation
    for k in range(0, M):
        # b array calculation
        for i in range(1, N):
            b_array[i - 1] = (U[k][i] + (λ / 2) * (U[k][i - 1] - 2 * U[k][i] + U[k][i + 1])
                            + (Δt / 2) * (punctual_heat_source(source_position, scale_array[k], scale_array[i], N)
                            + punctual_heat_source(source_position, scale_array[k + 1], scale_array[i], N)))

        g1, g2 = boundary_conditions(scale_array[k + 1])

        b_array[0] += (λ / 2) * g1
        b_array[-1] += (λ / 2) * g2

        solution = solve_linear_system(a_matrix_diag, a_matrix_subdiag, b_array)

        for i in range(1, N):
            U[k + 1][i] = solution[i - 1]

    return U[-1], scale_array



def generate_uk(heat_sources_positions_array, N):
    """
    Gera os vetores uk(T, xi), i = 0, ..., N
    """

    nf = len(heat_sources_positions_array)

    uk_matrix = np.zeros((nf, N + 1))

    for k in range(0, nf):
        uk_matrix[k], scale_array = solve_heat_equation(heat_sources_positions_array[k], N)

    return uk_matrix, scale_array
