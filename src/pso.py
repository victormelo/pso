from fitness_functions import sphere, equation
from particle import Particle
from topology import global_best
import numpy as np
import logging

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
        logging.basicConfig(level=logging.INFO)
        logger = logging.getLogger(__name__)

        self.init_population()

        for iteration in range(self.iterations):

            for particle in self.population:
                particle.update_pbest()

            for particle in self.population:
                particle.update_lbest(self.local_best_function(self.population))
                particle.update_speed(self.c1, self.c2)
                particle.update_position()

            best = self.best_fitness()
            logger.info((iteration, best.pbest, best.get_pbest_fitness()))
            raw_input("Press Enter to continue to next iteration...")

    def best_fitness(self):
        return global_best(self.population)


def main():
    particles = 30
    dimensions = 2
    iterations = 10000
    c1 = 2.05
    c2 = 2.05

    PSO(particles,
        dimensions,
        iterations,
        c1,
        c2,
        sphere,
        global_best).run_pso()

if __name__ == '__main__':
    main()
