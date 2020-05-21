#!/usr/bin/env python3

import os

import plotter

import task_one
import task_two

def main():
    # Configuration
    results_dir = "./results"

    try:
        os.mkdir(results_dir)
    except OSError:
        pass

    # Task selection
    task_number = input("Qual tarefa deseja executar 1 ou 2? ")
    task_letter = input("Qual problema deseja executar:\n"
                        "a -> f(t, x) = 10*cos*(10t)*(x^2)*(1 − x)^2 − (1 + sin(10t))*(12x^2 − 12x + 2)\n"
                        "b -> f(t, x) = 5(e^(t - x))*((5(t^2)*cos(5tx)) - (sin(5tx)*(2t + x)))\n"
                        "c -> f pontual localizada em p = 0.25\n")

    task_letter = task_letter.lower()

    task_result_dir = f"{results_dir}/{task_number}/{task_letter}"

    try:
        os.mkdir(task_result_dir)
    except OSError:
        pass

    if task_number == "1":
        task_one.run(task_letter, task_result_dir)
    else:
        task_two.run(task_letter, task_result_dir)

    print("Execução finalizada!")

if __name__ == "__main__":
    main()
