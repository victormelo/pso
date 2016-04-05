import numpy as np
import random


class Particle:

    def __str__(self):
        return '[%d] Position: %s - speed: %s - fitness: %f - pbest pos: %s - pbest: %f' % (self.index,
                                                                        self.position,
                                                                        self.speed,
                                                                        self.get_fitness(),
                                                                        self.pbest,
                                                                        self.get_pbest_fitness())

    def __init__(self, index, position, speed, fitness_function):
        self.position = position
        self.speed = speed
        self.index = index
        self.pbest = np.zeros(self.position.shape)
        self.pbest.fill(np.inf)

        self.lbest = np.zeros(self.position.shape)
        self.lbest.fill(np.inf)

        self.fitness_function = fitness_function

    def update_position(self):
        self.position = self.position + self.speed

    def update_speed(self, c1, c2, w=1):
        r1 = random.random()
        r2 = random.random()

        self.speed = w * (self.speed + \
            c1 * r1 * (self.pbest - self.position) + \
            c2 * r2 * (self.lbest - self.position))

    def update_pbest(self):
        fp = self.get_fitness()

        if(fp < self.get_pbest_fitness()):
            self.pbest = self.position

    def update_lbest(self, lbest_particle):
        if(lbest_particle.get_pbest_fitness() < self.get_lbest_fitness()):
            self.lbest = lbest_particle.position

    def get_fitness(self):
        return self.fitness_function(self.position)

    def get_pbest_fitness(self):
        return self.fitness_function(self.pbest)

    def get_lbest_fitness(self):
        return self.fitness_function(self.lbest)
