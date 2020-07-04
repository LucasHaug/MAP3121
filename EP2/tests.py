#!/usr/bin/env python3

import numpy as np
from random import random

import crank_nicolson

#################################################
### Functions Definitions
#################################################

def get_data(test_letter):
    if test_letter == "a":
        ut_array, uk_matrix, x_array, N = test_a()
    elif test_letter == "b":
        ut_array, uk_matrix, x_array, N = test_b()
    elif test_letter == "c":
        ut_array, uk_matrix, x_array, N = test_c()
    else:
        ut_array, uk_matrix, x_array, N = test_d()

    return ut_array, uk_matrix, x_array, N



def test_a():
    N = 128

    # Create heat sources positions array
    heat_sources_positions_array = [0.35]

    # Calculate uk matrix
    uk_matrix, scale_array = crank_nicolson.generate_uk(heat_sources_positions_array, N)

    uk_matrix = np.delete(uk_matrix, [0, N], axis=1)

    # Calculate ut array
    ut_array = np.array(uk_matrix[0]) * 7

    # Delete extremes from scale array
    scale_array = np.delete(scale_array, [0, N])

    return ut_array, uk_matrix, scale_array, N



def test_b():
    N = 128

    # Create heat sources positions array
    heat_sources_positions_array = [0.15, 0.3, 0.7, 0.8]

    # Calculate uk matrix
    uk_matrix, scale_array = crank_nicolson.generate_uk(heat_sources_positions_array, N)

    uk_matrix = np.delete(uk_matrix, [0, N], axis=1)

    # Calculate ut array
    ut_array = (np.array(uk_matrix[0]) * 2.3 + np.array(uk_matrix[1]) * 3.7 +
                np.array(uk_matrix[2]) * 0.3 + np.array(uk_matrix[3]) * 4.2)

    # Delete extremes from scale array
    scale_array = np.delete(scale_array, [0, N])

    return ut_array, uk_matrix, scale_array, N



def test_c():
    # Configuration
    N = int(input("Insira o valor de N: "))

    mesh_size = 2048

    mesh_relation = int(mesh_size / N)

    test_file_name = "teste.txt"

    test_file = open(test_file_name, "r")
    file_lines = test_file.readlines()

    test_file.close()
    
    # Create heat sources positions array
    heat_sources_positions_array = [float(item) for item in (file_lines.pop(0).split())]

    print(file_lines[1])

    # Calculate uk matrix
    uk_matrix, scale_array = crank_nicolson.generate_uk(heat_sources_positions_array, N)

    uk_matrix = np.delete(uk_matrix, [0, N], axis=1)

    # Create ut array
    ut_array = np.zeros(N - 1, dtype=float)

    for i in range(0, N - 1):
        ut_array[i] = file_lines[(i + 1) * mesh_relation]

    # Delete extremes from scale array
    scale_array = np.delete(scale_array, [0, N])

    return ut_array, uk_matrix, scale_array, N



def test_d():
    ut_array, uk_matrix, scale_array, N = test_c()

    ε = 0.01

    for i in range(0, N - 1):
        random_num = (random() - 0.5) * 2

        ut_array[i] *= (1 + random_num * ε)

    return ut_array, uk_matrix, scale_array, N
