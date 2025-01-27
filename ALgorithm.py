from problem_dict import Problem
from task_scheduling import task_scheduling_simulation
from plot import fitness_list
import numpy as np


class Alogorithm:
    def __init__(self, model, name_Algorithm):
        self.model = model
        self.name_Algorithm = name_Algorithm
        self.fitness = 0

    def execute(self, tasks, vms, Alpha, Beta, lam, file_name):
        problem = Problem(tasks, vms, Alpha, Beta, lam)
        g_best = self.model.solve(problem)
        self.fitness = g_best.target.fitness

        vm_loads = np.zeros(len(vms))
        best_solution = np.clip(g_best.solution.astype(int), 0, len(vms) - 1)
        for task_idx, vm_idx in enumerate(best_solution):
            vm_loads[vm_idx] += problem.tasks[task_idx].workload

        self.makespan = max(vm_loads)
        self.load_balance = np.std(vm_loads)
        # Utilization: Ratio of total usage to total capacity
        total_usage = np.sum(vm_loads)
        total_capacity = 0
        for index in range(len(vms)):
            total_capacity += vms[index].capacity
        self.utilization = total_usage / total_capacity
        print(
            f"Solution: {g_best.solution.astype(int)},Fitness: {g_best.target.fitness},Makespan: {self.makespan}, Load_balance: {self.load_balance}, utilization: {self.utilization}"
        )
        fitness_list.append(g_best.target.fitness)
        with open(file_name, "a") as file:
            file.write(f"Algorithm: {self.name_Algorithm}\n")
            file.write(f"Solution: {g_best.solution.astype(int).tolist()}\n")
            file.write(f"Fitness: {g_best.target.fitness:.6f}\n")

        task_scheduling_simulation(tasks, vms, g_best.solution, output_file=file_name)
