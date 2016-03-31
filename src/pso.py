import numpy as np
import random
from fitness_functions import esfera

class Particle:

    personal_best = np.array()

    def __init__(self, position, speed, c1, c2):
        self.position = position
        self.speed = speed
        self.c1 = c1
        self.c2 = c2

    def update_position(self):
        self.position = self.position + self.speed

    def update_speed(self, local_best):
        self.speed = self.speed + \
            self.c1 * random.random() * (self.personal_best - self.position) + \
            self.c2 * random.random() * (local_best - self.position)

    def get_fitness(self, fitness_function):
        return fitness_function(position)


class PSO:

