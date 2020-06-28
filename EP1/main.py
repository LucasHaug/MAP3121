#!/usr/bin/env python3

import os

import plotter

import task_one
import task_two

#################################################
### Main Function
#################################################

def main():
    # Configuration
    results_dir = "./results"

    try:
        os.mkdir(results_dir)
    except OSError:
        print("Erro ao criar o diretório de resultados")

    # Task selection
    task_number = input("Qual tarefa deseja executar 1 ou 2? ")
    task_letter = input("\na -> f(t, x) = 10*cos*(10t)*(x^2)*(1 − x)^2 − (1 + sin(10t))*(12x^2 − 12x + 2)\n"
                        "b -> f(t, x) = 5(e^(t - x))*((5(t^2)*cos(5tx)) - (sin(5tx)*(2t + x)))\n"
                        "c -> f pontual localizada em p = 0.25\n"
                        "\nQual desses problemas deseja executar? ")

    task_letter = task_letter.lower()

    task_result_dir = f"{results_dir}/{task_number}/{task_letter}"

    try:
        os.makedirs(task_result_dir)
    except OSError:
        print("Erro ao criar os diretórios da tarefa")

    # Task running
    if task_number == "1":
        task_one.run(task_letter, task_result_dir)
    else:
        task_two.run(task_letter, task_result_dir)

    print("Execução finalizada!")


if __name__ == "__main__":
    main()
