from pso import PSO
from fitness_functions import sphere
from topology import global_best

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
