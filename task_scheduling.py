import numpy as np
import simpy
import contextlib

def execute_task(env, task, vm):
    print(f"Task {task.id} assigned to VM {vm.id} at time {env.now}")
    yield env.timeout(task.workload / vm.capacity)
    print(f"Task {task.id} completed on VM {vm.id} at time {env.now}")

# SimPy Simulation
def task_scheduling_simulation(tasks, vms, allocation, output_file="output.txt"):
    with open(output_file, "a") as f:
        with contextlib.redirect_stdout(f):
            env = simpy.Environment()
            allocation = np.floor(allocation).astype(int)
            for task_index, vm_index in enumerate(allocation):
                env.process(execute_task(env, tasks[task_index], vms[vm_index]))
            f.write("\n")
            env.run()
            f.write("-" * 50 + "\n")  # خط فاصل بين النتائج