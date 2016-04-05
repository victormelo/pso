from particle import Particle
import numpy as np

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
            position = np.random.uniform(-5.12, 5.12, self.num_dimensions)
            speed = np.random.random_sample(self.num_dimensions)
            particle = Particle(i, position, speed, self.fitness_function)
            self.population.append(particle)

    def run_pso(self):

        self.init_population()

        for iteration in range(self.iterations):

            for particle in self.population:
                particle.update_pbest()

            for particle in self.population:
                particle.update_lbest(self.local_best_function(self.population))
                particle.update_speed(self.c1, self.c2)
                particle.update_position()

            best = self.best_fitness()

    def best_fitness(self):
        return global_best(self.population)
