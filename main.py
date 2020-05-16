#!/usr/bin/env python3

import os

import plotter
import task_one

def main():
    # Configuration
    images_dir = "./images"

    try:
        os.mkdir(images_dir)
    except OSError:
        pass

    # Input parameters
    task_number = input("Qual tarefa deseja executar 1 ou 2? ")
    task_letter = input("Qual letra deseja executar a, b ou c? ")

    N = int(input("Insira o valor de N: "))
    λ = float(input("Insira o valor de λ: "))

    # Total amount of time in seconds
    total_time_s = 1

    Δx = 1 / float(N)
    Δt = λ * (Δx**2)

    M = int(round(total_time_s / Δt))

    print(f"N: {N}, M: {M}, λ: {λ}, Δx: {Δx} e Δt: {Δt}")
    
    if task_number == "1":
        task_one.run(task_letter.lower(), N, M, λ, Δx, Δt, images_dir)
    else: 
        pass

    print("Execução finalizada!")

if __name__ == "__main__":
    main()