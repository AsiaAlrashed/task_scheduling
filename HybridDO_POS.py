import numpy as np
import math


class HybridDragonflyPSO:
    def __init__(self, epoch, pop_size):
        self.epoch = epoch
        self.pop_size = pop_size

    def solve(self, problem):
        num_dragonflies = self.pop_size
        num_dimensions = len(problem.tasks)

        lower_bound = np.min([var.lb for var in problem.bounds])
        upper_bound = np.max([var.ub for var in problem.bounds])

        # Initialize positions and velocities (Behaviors on which the Dragonfly algorithm is built)
        self.positions = np.random.uniform(
            lower_bound, upper_bound, (num_dragonflies, num_dimensions)
        )
        self.velocities = np.zeros((num_dragonflies, num_dimensions))
        self.personal_best = self.positions.copy()
        self.global_best = self.positions[0]
        self.fitness = np.full(num_dragonflies, float("inf"))

        def objective_function(solution):
            return problem.obj_func(solution)

        # Optimization loop
        for iteration in range(self.epoch):
            # For the first half of the iterations, Apply Dragonfly Algorithm
            if iteration < self.epoch // 2:
                self.dragonfly_algorithm(
                    iteration,
                    objective_function,
                    lower_bound,
                    upper_bound,
                    num_dimensions,
                )
            else:
                # For the second half of the iterations, Apply Particle Swarm Optimization Algorithm
                self.particle_swarm_optimization(
                    iteration,
                    objective_function,
                    lower_bound,
                    upper_bound,
                    num_dimensions,
                )

            self.update_fitness(objective_function)

        return type(
            "Result",
            (object,),
            {
                "solution": self.global_best,
                "target": type(
                    "Target",
                    (object,),
                    {"fitness": objective_function(self.global_best)},
                ),
            },
        )()

    def update_fitness(self, objective_function):
        for i in range(self.pop_size):
            current_fitness = objective_function(self.positions[i])
            if current_fitness < self.fitness[i]:
                self.fitness[i] = current_fitness
                self.personal_best[i] = self.positions[i]

        best_idx = np.argmin(self.fitness)
        if self.fitness[best_idx] < objective_function(self.global_best):
            self.global_best = self.positions[best_idx]

    def dragonfly_algorithm(
        self, iteration, objective_function, lower_bound, upper_bound, num_dimensions
    ):
        # A weighting factor (w) dampens velocities over time
        w = 0.4
        my_c = max(0, 0.1 - iteration * ((0.1 - 0) / (self.epoch / 2)))
        s, a, c, f, e = [2 * np.random.random() * my_c for _ in range(5)]

        for i in range(self.pop_size):
            neighbors = []
            for j in range(self.pop_size):
                distance = np.linalg.norm(self.positions[i] - self.positions[j])
                if 0 < distance <= 5:  # Assuming a neighborhood radius of 5
                    neighbors.append(j)

            if neighbors:
                separation = np.mean(
                    [self.positions[i] - self.positions[j] for j in neighbors], axis=0
                )
                alignment = np.mean([self.velocities[j] for j in neighbors], axis=0)
                cohesion = (
                    np.mean([self.positions[j] for j in neighbors], axis=0)
                    - self.positions[i]
                )
                food = self.global_best - self.positions[i]
                enemy = self.positions[np.argmax(self.fitness)] + self.positions[i]

                self.velocities[i] = (
                    s * separation
                    + a * alignment
                    + c * cohesion
                    + f * food
                    + e * enemy
                    + w * self.velocities[i]
                )
            else:
                self.velocities[i] = w * self.velocities[i] + np.random.uniform(
                    -1, 1, num_dimensions
                )

            self.positions[i] += self.velocities[i]
            self.positions[i] = self.handle_bounds(
                self.positions[i], lower_bound, upper_bound
            )

    def particle_swarm_optimization(
        self, iteration, objective_function, lower_bound, upper_bound, num_dimensions
    ):
        w = self.dynamic_inertia_weight(iteration, self.epoch)
        c1 = c2 = 2.05

        for i in range(self.pop_size):
            r1, r2 = np.random.random(2)
            self.velocities[i] = (
                w * self.velocities[i]
                + c1 * r1 * (self.personal_best[i] - self.positions[i])
                + c2 * r2 * (self.global_best - self.positions[i])
            )

            self.positions[i] += self.velocities[i]
            self.positions[i] = self.handle_bounds(
                self.positions[i], lower_bound, upper_bound
            )

    @staticmethod
    # Dynamically adjusts the inertia weight over iterations, starting high and gradually decreasing.
    def dynamic_inertia_weight(iteration, max_iter, w_min=0.4, w_max=0.9):
        return w_max - ((w_max - w_min) * (iteration / max_iter))

    @staticmethod
    # Ensures particles do not exceed the bounds of the search space
    def handle_bounds(position, lower_bound, upper_bound):
        position = np.clip(position, lower_bound, upper_bound)
        return position

    @staticmethod
    # Generates a step size for a random walk using the Levy distribution.
    def levy_flight(step_size, dimension):
        beta = 1.5
        sigma_u = (
            math.gamma(1 + beta)
            * math.sin(math.pi * beta / 2)
            / (math.gamma((1 + beta) / 2) * beta * 2 ** ((beta - 1) / 2))
        ) ** (1 / beta)
        u = np.random.normal(0, sigma_u, dimension)
        v = np.random.normal(0, 1, dimension)
        step = u / abs(v) ** (1 / beta)
        return step_size * step
