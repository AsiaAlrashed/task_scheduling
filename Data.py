import numpy as np


# Task and VM definitions
class Task:
    def __init__(self, task_id, workload):
        self.id = task_id
        self.workload = workload


class VM:
    def __init__(self, vm_id, capacity):
        self.id = vm_id
        self.capacity = capacity


def get_data_random():

    tasks = [Task(i, np.random.randint(10, 100)) for i in range(12)]
    vms = [VM(i, np.random.randint(50, 150)) for i in range(4)]
    return tasks, vms


def get_user_input():
    num_tasks = int(input("Enter the number of tasks: "))
    num_vms = int(input("Enter the number of VMs: "))
    alpha = 0
    beta = 0
    lam = 0
    tasks = []
    random = 1
    random = int(
        input(
            "Do you want enter value of tasks and vms or random (if random enter 0 else 1): "
        )
    )

    if random == 1:
        for i in range(num_tasks):
            workload = float(input(f"Enter workload for Task {i}: "))
            task = Task(i, workload)
            tasks.append(task)

        vms = []
        for i in range(num_vms):
            capacity = float(input(f"Enter capacity for VM {i}: "))
            vm = VM(i, capacity)
            vms.append(vm)
    else:
        tasks = [Task(i, np.random.randint(1, 30)) for i in range(num_tasks)]
        vms = [VM(i, np.random.randint(100, 200)) for i in range(num_vms)]

    alpha = float(input(f"Enter Alpha , Weight of makespan : "))
    beta = float(input(f"Enter Beta , Weight of load balancing : "))
    lam = float(input(f"Enter Lam , Weight of utilization: "))
    return num_tasks, num_vms, tasks, vms, alpha, beta, lam
