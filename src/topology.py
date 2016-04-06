import numpy as np

def global_best(population):
    all_fitness = []

    for particle in population:
        all_fitness.append(particle.get_pbest_fitness())

    return population[np.argmin(all_fitness)]
