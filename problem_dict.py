import numpy as np

from mealpy.utils.problem import Problem
from mealpy.utils.space import IntegerVar

# Fitness is a criterion for optimizing a DO algorithm, and is based on optimizing a specific goal.
# goal -> Reduces makespan while improving load balance.

# Fitness function inside the problem class


class Problem(Problem):
    def __init__(self, tasks, vms, Alpha, Beta, lam):
        self.tasks = tasks
        self.vms = vms
        self.Alpha = Alpha
        self.Beta = Beta
        self.lam = lam
        lower_bound = [0] * len(self.tasks)
        upper_bound = [len(self.vms) - 1] * len(self.tasks)
        bounds = [IntegerVar(lb, ub) for lb, ub in zip(lower_bound, upper_bound)]
        print("bounds : ", bounds)
        super().__init__(bounds, minmax="min")

    def obj_func(self, solution):

        vm_loads = np.zeros(len(self.vms))
        solution = np.clip(solution.astype(int), 0, len(self.vms) - 1)

        for task_idx, vm_idx in enumerate(solution.astype(int)):
            vm_loads[vm_idx] += self.tasks[task_idx].workload

        makespan = max(vm_loads)  # Max time for any VM
        load_balance = np.std(vm_loads)  # Standard deviation of load across all VMs
        # The lower the standard deviation, the more evenly distributed the tasks.

        # Utilization: Ratio of total usage to total capacity
        total_usage = np.sum(vm_loads)
        total_capacity = 0
        for index in range(len(self.vms)):
            total_capacity += self.vms[index].capacity
        utilization = total_usage / total_capacity

        return (
            (self.Alpha * makespan)
            + (self.Beta * load_balance)
            + (self.lam * 1 / utilization)
        )
