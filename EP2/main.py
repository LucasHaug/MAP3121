#!/usr/bin/env python3

import os

import plotter
import tests
import mmq

#################################################
### Public Variables
#################################################

ENABLE_GRAPHS_VIEW = False
SAVE_GRAPHS_IMAGE = True

#################################################
### Main Function
#################################################

def main():
    # Configuration
    results_dir = "./results"

    try:
        os.mkdir(results_dir)
    except OSError:
        pass

    # Test selection
    test_letter = input("Qual teste deseja executar a, b, c ou d? ")

    while test_letter not in ("a", "b", "c", "d"):
        print("Tetse não encontrado, escolha entre a, b, c ou d")
        test_letter = input("Qual teste deseja executar a, b, c ou d? ")

    test_letter = test_letter.lower()

    # Get test data
    ut_array, uk_matrix, x_array, N = tests.get_data(test_letter)

    # Create results file
    results_file_name = f"{results_dir}/{test_letter.upper()}_{N}_ERRORS.txt"
    results_file = open(results_file_name, 'w')

    # Generate and solve normal system
    a_matrix, b_array = mmq.generate_linear_system(ut_array, uk_matrix)

    coeficients_array = mmq.solve_linear_system(a_matrix, b_array)

    print(f"Coeficientes ak:\n {coeficients_array}")

    # Calculate squared error and save it
    squared_error = mmq.squared_error_calculation(ut_array, uk_matrix, coeficients_array)

    squared_error_result = f"Erro quadrático: {squared_error}"

    print(squared_error_result)

    results_file.write(squared_error_result)

    # Plota o gráfico
    ut_approx = mmq.f_approximation(uk_matrix, coeficients_array)

    plotter.two_graphs(ut_array, ut_approx, x_array, f"{test_letter.upper()}_{N}_GRAPH", ENABLE_GRAPHS_VIEW, SAVE_GRAPHS_IMAGE, results_dir)

    # Finaliza a execução
    results_file.close()

    print("Execução finalizada!")


if __name__ == "__main__":
    main()
