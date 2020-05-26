import matplotlib.pyplot as plt
from itertools import combinations

def plot_cliques(cliques_lists, legend, title):
    """
    Plots list(s) of total energies.
    :param energy_lists: a list that contains a list of total energies
    :param legend: a list of curve labels
    :param title: plot title
    """
    # plot each list of total energies
    for cliques_list in cliques_lists:
        plt.plot(range(len(cliques_list)), cliques_list, marker = 'x')

    # set the x-axis and y-axis labels
    plt.xlabel('Value of t (100)')
    plt.ylabel('Cliques')

    # set the legend, title, clean up the plot layout and show it
    plt.legend(legend)
    plt.title(title)
    plt.tight_layout()
    plt.show()
    plt.clf()