from particle import Particle
import numpy as np
from topology import global_best

class PSO:

    def __init__(self, num_particles, num_dimensions, iterations, c1, c2, fitness_function, local_best_function):
        self.num_particles = num_particles
        self.num_dimensions = num_dimensions
        self.iterations = iterations
        self.c1 = c1
        self.c2 = c2
        self.fitness_function = fitness_function
        self.local_best_function = local_best_function

    def init_population(self):
        self.population = []

        for i in range(self.num_particles):
            position = np.random.uniform(self.fitness_function.lower, self.fitness_function.higher, self.num_dimensions)
            speed = np.random.random_sample(self.num_dimensions)
            particle = Particle(i, position, speed, self.fitness_function)
            self.population.append(particle)

    def run_pso(self):

        self.init_population()
        self.best_particles = []

        for iteration in range(self.iterations):

            for particle in self.population:
                particle.update_pbest()

            for particle in self.population:
                particle.update_lbest(self.local_best_function(self.population))
                particle.update_speed(self.c1, self.c2, w=0.8)
                particle.update_position()

            best = self.best_fitness()
            self.best_particles.append(best)
            print best.get_pbest_fitness()

    def best_fitness(self):
        return global_best(self.population)
