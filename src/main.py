from pso import PSO
from fitness_functions import Spheres
from topology import global_best

def main():
    particles = 30
    dimensions = 30
    iterations = 10000
    c1 = 2.05
    c2 = 2.05

    pso = PSO(particles,
        dimensions,
        iterations,
        c1,
        c2,
        Sphere(),
        global_best).run_pso()


if __name__ == '__main__':
    main()
