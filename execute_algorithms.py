from mealpy import (
    DO,
    ABC,
    ACOR,
    AGTO,
    ALO,
    AO,
    ARO,
    AVOA,
    BA,
    BES,
    BFO,
    BSA,
    BeesA,
    COA,
    CSA,
    CSO,
    CoatiOA,
    DMOA,
    EHO,
    ESOA,
    FA,
    FFA,
    FFO,
    FOA,
    FOX,
    GJO,
    GOA,
    GTO,
    GWO,
    HBA,
    HGS,
    HHO,
    JA,
    MFO,
    MGO,
    MPA,
    MRFO,
    MSA,
    NGO,
    NMRA,
    OOA,
    PFA,
    POA,
    PSO,
    SCSO,
    SFO,
    SHO,
    SLO,
    SRSR,
    SSA,
    SSO,
    SSpiderA,
    SSpiderO,
    STO,
    SeaHO,
    ServalOA,
    TDO,
    TSO,
    WOA,
    WaOA,
    ZOA,
)

from ALgorithm import Alogorithm
from Data import get_user_input
from HybridDO_POS import HybridDragonflyPSO
import pandas as pd


# from plot import df
import logging


df = pd.read_csv("result.csv")
algorithms = [
    {"name": "DO", "model": DO.OriginalDO(epoch=100, pop_size=50)},
    {"name": "ABC", "model": ABC.OriginalABC(epoch=100, pop_size=50, n_limits=50)},
    {
        "name": "ACOR",
        "model": ACOR.OriginalACOR(
            epoch=100, pop_size=50, sample_count=25, intent_factor=0.5, zeta=1.0
        ),
    },
    {
        "name": "AGTO",
        "model": AGTO.OriginalAGTO(epoch=100, pop_size=50, p1=0.03, p2=0.8, beta=3.0),
    },
    {"name": "ALO", "model": ALO.OriginalALO(epoch=100, pop_size=50)},
    {"name": "AO", "model": AO.OriginalAO(epoch=100, pop_size=50)},
    {"name": "ARO", "model": ARO.OriginalARO(epoch=100, pop_size=50)},
    {
        "name": "BA",
        "model": BA.OriginalBA(
            epoch=100,
            pop_size=50,
            loudness=0.8,
            pulse_rate=0.95,
            pf_min=0.1,
            pf_max=10.0,
        ),
    },
    {
        "name": "BES",
        "model": BES.OriginalBES(
            epoch=100, pop_size=50, a_factor=10, R_factor=1.5, alpha=2.0, c1=2.0, c2=2.0
        ),
    },
    {
        "name": "BFO",
        "model": BFO.OriginalBFO(
            epoch=100,
            pop_size=50,
            Ci=0.01,
            Ped=0.25,
            Nc=5,
            Ns=4,
            d_attract=0.1,
            w_attract=0.2,
            h_repels=0.1,
            w_repels=10,
        ),
    },
    {
        "name": "BSA",
        "model": BSA.OriginalBSA(
            epoch=100,
            pop_size=50,
            ff=10,
            pff=0.8,
            c1=1.5,
            c2=1.5,
            a1=1.0,
            a2=1.0,
            fc=0.5,
        ),
    },
    {
        "name": "BeesA",
        "model": BeesA.CleverBookBeesA(
            epoch=100,
            pop_size=50,
            n_elites=16,
            n_others=4,
            patch_size=5.0,
            patch_reduction=0.985,
            n_sites=3,
            n_elite_sites=1,
        ),
    },
    {"name": "COA", "model": COA.OriginalCOA(epoch=50, pop_size=20, n_coyotes=5)},
    {"name": "CSA", "model": CSA.OriginalCSA(epoch=50, pop_size=20, p_a=0.3)},
    {
        "name": "CSO",
        "model": CSO.OriginalCSO(
            epoch=100,
            pop_size=50,
            mixture_ratio=0.15,
            smp=5,
            spc=False,
            cdc=0.8,
            srd=0.15,
            c1=0.4,
            w_min=0.4,
            w_max=0.9,
        ),
    },
    {"name": "CoatiOA", "model": CoatiOA.OriginalCoatiOA(epoch=100, pop_size=50)},
    {
        "name": "EHO",
        "model": EHO.OriginalEHO(
            epoch=100, pop_size=50, alpha=0.5, beta=0.5, n_clans=4
        ),
    },
    {"name": "ESOA", "model": ESOA.OriginalESOA(epoch=100, pop_size=50)},
    {
        "name": "FA",
        "model": FA.OriginalFA(
            epoch=100,
            pop_size=50,
            max_sparks=50,
            p_a=0.04,
            p_b=0.8,
            max_ea=40,
            m_sparks=50,
        ),
    },
    {
        "name": "FAA",
        "model": FFA.OriginalFFA(
            epoch=100,
            pop_size=50,
            gamma=0.001,
            beta_base=2,
            alpha=0.2,
            alpha_damp=0.99,
            delta=0.05,
            exponent=2,
        ),
    },
    {"name": "FFO", "model": FFO.OriginalFFO(epoch=100, pop_size=50)},
    {"name": "FOX", "model": FOX.OriginalFOX(epoch=100, pop_size=50, c1=0.18, c2=0.82)},
    {"name": "GJO", "model": GJO.OriginalGJO(epoch=100, pop_size=50)},
    {
        "name": "GOA",
        "model": GOA.OriginalGOA(epoch=100, pop_size=50, c_min=0.00004, c_max=1.0),
    },
    {"name": "GTO", "model": GTO.OriginalGTO(epoch=100, pop_size=50, A=0.4, H=2.0)},
    {"name": "GWO", "model": GWO.OriginalGWO(epoch=100, pop_size=50)},
    {"name": "HBA", "model": HBA.OriginalHBA(epoch=100, pop_size=50)},
    {
        "name": "HGS",
        "model": HGS.OriginalHGS(epoch=100, pop_size=50, PUP=0.08, LH=10000),
    },
    {"name": "HHO", "model": HHO.OriginalHHO(epoch=100, pop_size=50)},
    {"name": "JA", "model": JA.DevJA(epoch=100, pop_size=50)},
    {"name": "MFO", "model": MFO.OriginalMFO(epoch=100, pop_size=50)},
    {"name": "MGO", "model": MGO.OriginalMGO(epoch=100, pop_size=50)},
    {"name": "MPA", "model": MPA.OriginalMPA(epoch=100, pop_size=50)},
    {
        "name": "MRFO",
        "model": MRFO.OriginalMRFO(epoch=100, pop_size=50, somersault_range=2.0),
    },
    {
        "name": "MSA",
        "model": MSA.OriginalMSA(
            epoch=100, pop_size=50, n_best=5, partition=0.5, max_step_size=1.0
        ),
    },
    {"name": "MGO", "model": NGO.OriginalNGO(epoch=100, pop_size=50)},
    {"name": "NMRA", "model": NMRA.OriginalNMRA(epoch=100, pop_size=50, pb=0.75)},
    {"name": "OOA", "model": OOA.OriginalOOA(epoch=100, pop_size=50)},
    {"name": "PFA", "model": PFA.OriginalPFA(epoch=100, pop_size=50)},
    {"name": "POA", "model": POA.OriginalPOA(epoch=100, pop_size=50)},
    {
        "name": "PSO",
        "model": PSO.OriginalPSO(epoch=100, pop_size=50, c1=2.5, c2=2.5, w=0.4),
    },
    {"name": "SCSO", "model": SCSO.OriginalSCSO(epoch=100, pop_size=50)},
    {
        "name": "SFO",
        "model": SFO.OriginalSFO(
            epoch=100, pop_size=50, pp=0.1, AP=4.0, epsilon=0.0001
        ),
    },
    {
        "name": "SHO",
        "model": SHO.OriginalSHO(epoch=100, pop_size=50, h_factor=5.0, n_trials=10),
    },
    {"name": "SLO", "model": SLO.OriginalSLO(epoch=100, pop_size=50)},
    {"name": "SRSR", "model": SRSR.OriginalSRSR(epoch=100, pop_size=50)},
    {
        "name": "SSA",
        "model": SSA.DevSSA(epoch=100, pop_size=50, ST=0.8, PD=0.2, SD=0.1),
    },
    {"name": "SSO", "model": SSO.OriginalSSO(epoch=100, pop_size=50)},
    {
        "name": "SSpiderA",
        "model": SSpiderA.OriginalSSpiderA(
            epoch=100, pop_size=50, r_a=1.0, p_c=0.7, p_m=0.1
        ),
    },
    {
        "name": "SSpiderO",
        "model": SSpiderO.OriginalSSpiderO(
            epoch=100, pop_size=50, fp_min=0.65, fp_max=0.9
        ),
    },
    {
        "name": "SSpiderO",
        "model": SSpiderO.OriginalSSpiderO(
            epoch=100, pop_size=50, fp_min=0.65, fp_max=0.9
        ),
    },
    {"name": "STO", "model": STO.OriginalSTO(epoch=100, pop_size=50)},
    {"name": "SeaHO", "model": SeaHO.OriginalSeaHO(epoch=100, pop_size=50)},
    {"name": "ServalOA", "model": ServalOA.OriginalServalOA(epoch=100, pop_size=50)},
    {"name": "TDO", "model": TDO.OriginalTDO(epoch=100, pop_size=50)},
    {"name": "TSO", "model": TSO.OriginalTSO(epoch=100, pop_size=50)},
    {"name": "WOA", "model": WOA.OriginalWOA(epoch=100, pop_size=50)},
    {"name": "WaOA", "model": WaOA.OriginalWaOA(epoch=100, pop_size=50)},
    {"name": "ZOA", "model": ZOA.OriginalZOA(epoch=100, pop_size=50)},
    {
        "name": "HybridDragonflyPSO",
        "model": HybridDragonflyPSO(epoch=100, pop_size=50),
    },
]

execute_algorithm = []

num_tasks, num_vms, tasks, vms, alpha, beta, lam = get_user_input()
file_name = "results_comparison.txt"

with open(file_name, "a") as file:

    file.write(f"Tasks(id, workload):\n")
    for index in range(len(tasks)):
        file.write(f"{tasks[index].id}: {tasks[index].workload}\t")

    file.write(f"\nVMs(id, capacity, current_load):\n")

    for index in range(len(vms)):
        file.write(f"{vms[index].id}: {vms[index].capacity} \t\t")

    file.write(f"\n Alpha = {alpha} , Beta = {beta} , Lam = {lam} \n")
    file.write("\n" + "-" * 50 + "\n")
    file.close()


def run_algorithm(algo):

    try:
        print(f"------------------{algo['name']}------------------")
        algorithm_instance = Alogorithm(algo["model"], algo["name"])
        algorithm_instance.execute(tasks, vms, alpha, beta, lam, file_name)
        print()
        new_row = pd.DataFrame(
            [
                {
                    "Algorithm": algorithm_instance.name_Algorithm,
                    "Fitness": algorithm_instance.fitness,
                    "Num_Tasks": num_tasks,
                    "num_VMs": num_vms,
                    "Alpha": alpha,
                    "Beta": beta,
                    "Lam": lam,
                    "MakeSpan ": algorithm_instance.makespan,
                    "load_balance": algorithm_instance.load_balance,
                    "utilization": algorithm_instance.utilization,
                }
            ]
        )
        new_row.to_csv("result.csv", mode="a", index=False, header=False)
    except Exception as e:
        logging.error(f"Error while running {algo['name']}: {e}")


# FOA,DMOA
