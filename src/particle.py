import numpy as np
import random

class Particle:

    personal_best = np.array()

    def __init__(self, position, speed):
        self.position = position
        self.speed = speed


    def update_position(self):
        self.position = self.position + self.speed

    def update_speed(self, local_best, c1, c2):
        self.speed = self.speed + \
            c1 * random.random() * (self.personal_best - self.position) + \
            c2 * random.random() * (local_best - self.position)

    def get_fitness(self, fitness_function):
        return fitness_function(position)
