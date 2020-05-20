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
    task_letter = input("Qual letra deseja executar a, b ou c? ")

    task_result_dir = f"{results_dir}/{task_number}/{task_letter}"

    try:
        os.mkdir(task_result_dir)
    except OSError:
        pass

    if task_number == "1":
        task_one.run(task_letter.lower(), task_result_dir)
    else:
        task_two.run(task_letter.lower(), task_result_dir)

    print("Execução finalizada!")

if __name__ == "__main__":
    main()
