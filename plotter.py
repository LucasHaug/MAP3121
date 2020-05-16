#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np

def u_2d_graph(u_matrix, x_array, time_array, number_of_times_to_plot, image_name):
    # Configuration
    plt.figure(f"{image_name}_2D")

    plt.title('Distribuição de temperatura em função do tempo')
    plt.xlabel('x')
    plt.ylabel('U(x)')
    plt.grid(True)

    times_to_plot = np.linspace(time_array[0], time_array[-1], number_of_times_to_plot)

    for i in range(0, number_of_times_to_plot):
        times_to_plot[i] = round(times_to_plot[i], 1)

    # Plotting
    for k in range(0, number_of_times_to_plot):
        plt.plot(x_array, u_matrix[np.searchsorted(time_array, times_to_plot[k], side = 'right') - 1], label = f"t = {times_to_plot[k]}")

    plt.legend()
    plt.show()

def u_3d_graph(u_matrix, x_array, time_array, number_of_points, image_name):
    # Configuration
    plt.figure(f"{image_name}_3D")

    graph = plt.axes(projection = '3d')
    graph.set_title('Distribuição 3D da temperatura em função do tempo')
    graph.set_xlabel('t')
    graph.set_ylabel('x')
    graph.set_zlabel('U(t,x)')

    times_to_plot = np.linspace(time_array[0], time_array[-1], number_of_points)
    positions_to_plot = np.linspace(x_array[0], x_array[-1], number_of_points)

    for k in range(0, number_of_points):
        times_to_plot[k] = round(times_to_plot[k], 3)

    for i in range(0, number_of_points):
        positions_to_plot[i] = round(positions_to_plot[i], 3)

    u_to_plot = np.zeros((number_of_points, number_of_points))

    # Plotting
    for k in range(0, number_of_points):
        for i in range(0, number_of_points):
            u_to_plot[k][i] = u_matrix[np.searchsorted(time_array, times_to_plot[k], side = 'right') - 1][np.searchsorted(x_array, positions_to_plot[i], side = 'right') - 1]

    times_to_plot, positions_to_plot = np.meshgrid(times_to_plot, positions_to_plot)

    graph.plot_surface(positions_to_plot, times_to_plot, u_to_plot, rstride = 1, cstride = 1, cmap = 'rainbow', edgecolor = 'none')

    plt.show()