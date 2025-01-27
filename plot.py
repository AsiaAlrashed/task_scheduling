import matplotlib.pyplot as plt
import csv
import pandas as pd
import numpy as np

# from execute_algorithms import execute_algorithm
df = pd.read_csv("result.csv")

fitness_list = []
algorithms = [
    "DO",
    "ABC",
    "ACOR",
    "AGTO",
    "ALO",
    "AO",
    "ARO",
    "BA",
    "BES",
    "BFO",
    "BSA",
    "BeesA",
    "COA",
    "CSA",
    "CSO",
    "CoatiOA",
    "EHO",
    "ESOA",
    "FA",
    "FFA",
    "FFO",
    "FOX",
    "GJO",
    "GOA",
    "GTO",
    "GWO",
    "HBA",
    "HGS",
    "HHO",
    "JA",
    "MFO",
    "MGO",
    "MPA",
    "MRFO",
    "MSA",
    "NGO",
    "NMRA",
    "OOA",
    "PFA",
    "POA",
    "PSO",
    "SCSO",
    "SFO",
    "SHO",
    "SLO",
    "SRSR",
    "SSA",
    "SSO",
    "SSpiderA",
    "SSpiderO",
    "STO",
    "SeaHO",
    "ServalOA",
    "TDO",
    "TSO",
    "WOA",
    "WaOA",
    "ZOA",
]

file_path = "result.csv"  # استبدل هذا بالمسار الفعلي لملف CSV
data = pd.read_csv(file_path)


def visual(alpha, beta, lam, num_vms):
    filtered_data = data[(data["Alpha"] == alpha) & (data["num_VMs"] == num_vms)]

    plt.figure(figsize=(10, 6))
    # رسم كل خوارزمية بلون مختلف
    algorithms = {"DO": "red", "PSO": "blue", "HybridDragonflyPSO": "purple"}

    for algorithm, color in algorithms.items():
        subset = filtered_data[filtered_data["Algorithm"] == algorithm]
        plt.plot(
            subset["Num_Tasks"],
            subset["Fitness"],
            label=algorithm,
            color=color,
            marker="o",
        )

    # إضافة تفاصيل للرسم
    plt.xlabel("Number of Tasks")
    plt.ylabel("Fitness Value")
    plt.title(
        f"Fitness vs Number of Tasks (alpha={alpha}, beta ={beta}, lam ={lam}, num_VMs={num_vms})",
        fontsize=10,
    )
    plt.legend()
    plt.grid(True)

    # عرض الرسم
    plt.show()


def plot(num_tasks, alpha, beta, lam, num_vms):

    filtered_data = data[
        (data["Num_Tasks"] == num_tasks)
        & (data["num_VMs"] == num_vms)
        & (data["Alpha"] == alpha)
        & (data["Beta"] == beta)
    ]

    # استخراج أسماء الخوارزميات وقيم Fitness النهائية
    algorithms = filtered_data["Algorithm"].tolist()
    fitness_list = filtered_data["Fitness"].tolist()

    # إنشاء الرسم
    plt.figure(figsize=(20, 12))
    plt.bar(algorithms, fitness_list, color="blue", alpha=0.2)

    # إضافة العناوين والتسميات
    plt.title(
        f"Final Fitness Comparison of Algorithms (Num_Tasks ={num_tasks}, num_vms={num_vms}, alpha ={alpha}, beta ={beta}, lam={lam})",
        fontsize=8,
    )
    plt.ylabel("Fitness Value", fontsize=8)
    plt.xlabel("Algorithms", fontsize=8)
    plt.xticks(fontsize=7, rotation=60)

    # إضافة القيم على الأعمدة
    for i, value in enumerate(fitness_list):
        plt.text(i, value, f"{value:.2f}", ha="center", fontsize=8, color="black")

    # عرض الرسم
    plt.tight_layout()
    plt.show()


def save_results_to_csv(
    filename, algorithms, fitness_values, alpha, beta, lam, num_tasks
):
    """
    Save results to a CSV file.

    Parameters:
        filename (str): The name of the CSV file to save results.
        algorithms (list): List of algorithm names.
        fitness_values (list): List of corresponding fitness values for the algorithms.
        alpha (float): The alpha parameter value.
        beta (float): The beta parameter value.
        num_tasks (int): The number of tasks.
    """
    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        # Write the header
        writer.writerow(["Algorithm", "Fitness", "Alpha", "Beta", "Lam", "Num_Tasks"])

        # Write the data rows
        for algo, fitness in zip(algorithms, fitness_values):
            writer.writerow([algo, fitness, alpha, beta, num_tasks])


def plot_fintess(alpha, beta, lam, num_vms):
    filtered_data = data[(data["Alpha"] == alpha) & (data["num_VMs"] == num_vms)]

    plt.figure(figsize=(12, 8))
    algorithms = {"DO": "red", "PSO": "blue", "HybridDragonflyPSO": "purple"}

    # تحديد موقع الأعمدة بناءً على عدد المهام
    num_tasks = sorted(filtered_data["Num_Tasks"].unique())
    x = np.arange(len(num_tasks))  # مواقع الأعمدة
    bar_width = 0.25  # عرض الأعمدة

    # رسم الأعمدة
    for i, (algorithm, color) in enumerate(algorithms.items()):
        subset = filtered_data[filtered_data["Algorithm"] == algorithm]
        fitness_values = [
            subset[subset["Num_Tasks"] == task]["Fitness"].mean() for task in num_tasks
        ]
        plt.bar(
            x + i * bar_width,
            fitness_values,
            width=bar_width,
            label=algorithm,
            color=color,
        )

    # إضافة تفاصيل الرسم
    plt.xlabel("Number of Tasks")
    plt.ylabel("Fitness Value")
    plt.title(
        f"Fitness vs Number of Tasks (alpha={alpha}, beta={beta}, lam={lam}, num_VMs={num_vms})",
        fontsize=10,
    )
    plt.xticks(x + bar_width, num_tasks)  # تعديل أماكن النصوص على المحور السيني
    plt.legend()
    plt.grid(axis="y", linestyle="--", alpha=0.7)

    # عرض الرسم
    plt.show()


def plot_matrics(alpha, beta, lam, num_vms, target):
    filtered_data = data[(data["Alpha"] == alpha) & (data["num_VMs"] == num_vms)]

    plt.figure(figsize=(12, 8))
    algorithms = {"DO": "red", "PSO": "blue", "HybridDragonflyPSO": "purple"}

    # تحديد موقع الأعمدة بناءً على عدد المهام
    num_tasks = sorted(filtered_data["Num_Tasks"].unique())
    x = np.arange(len(num_tasks))  # مواقع الأعمدة
    bar_width = 0.25  # عرض الأعمدة

    # رسم الأعمدة
    for i, (algorithm, color) in enumerate(algorithms.items()):
        subset = filtered_data[filtered_data["Algorithm"] == algorithm]
        MakeSpan_values = [
            subset[subset["Num_Tasks"] == task][target].mean() for task in num_tasks
        ]
        plt.bar(
            x + i * bar_width,
            MakeSpan_values,
            width=bar_width,
            label=algorithm,
            color=color,
        )

    # إضافة تفاصيل الرسم
    plt.xlabel("Number of Tasks")
    plt.ylabel(target)
    plt.title(
        f"{target} vs Number of Tasks num_VMs={num_vms}",
        fontsize=10,
    )
    plt.xticks(x + bar_width, num_tasks)  # تعديل أماكن النصوص على المحور السيني
    plt.legend()
    plt.grid(axis="y", linestyle="--", alpha=0.7)

    # عرض الرسم
    plt.show()


# visual(1.0, 0, 0, 16)
# visual(1.0, 0, 0, 32)
# visual(0.5, 0.4, 0.1, 16)
plot_fintess(0.5, 0.4, 0.1, 4)
# plot_matrics(0.5, 0.4, 0.1, 4, "MakeSpan")
# plot_matrics(0.5, 0.4, 0.1, 4, "load_balance")
# plot_matrics(0.5, 0.4, 0.1, 4, "utilization")
