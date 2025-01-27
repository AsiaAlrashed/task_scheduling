from execute_algorithms import algorithms, run_algorithm
from plot import visual, plot
import pandas as pd

# from plot import plot
from concurrent.futures import ThreadPoolExecutor

if __name__ == "__main__":

    HybridDOPSO_algorithm = [
        algo for algo in algorithms if algo["name"] == "HybridDragonflyPSO"
    ]
    selected_algorithms = [
        algo
        for algo in algorithms
        if algo["name"] in {"HybridDragonflyPSO", "DO", "PSO"}
    ]

    with ThreadPoolExecutor() as executor:
        # if you eant executeall algorith , replace selected_algorithms with algorithms
        executor.map(run_algorithm, selected_algorithms)
