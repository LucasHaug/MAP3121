#!/usr/bin/env python3

import matplotlib.pyplot as plt

#################################################
### Functions Definitions
#################################################

def two_graphs(y1_array, y2_array, x_array, image_name, show_image, save_image, where_to_save):
    """
    Plota os valores duas funções y1 e y2 em função dos valores de x.

    As imagens geradas podem ser mostradas e/ou salvas em um determinado
    diretório.
    """

    # Configuration
    fig = plt.figure(image_name)

    plt.title('Distribuição de temperatura no instante T em função da posição')
    plt.xlabel('x')
    plt.ylabel('U(x)')
    plt.grid(True)


    # Plotting
    plt.plot(x_array, y1_array, label = "Solução")
    plt.plot(x_array, y2_array, label = "Aproximação", linestyle='--')

    plt.legend()

    if save_image == True:
        fig.savefig(f"{where_to_save}/{image_name}.png")

    if show_image == True:
        plt.show()
