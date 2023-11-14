import sys, os

sys.path.append(os.path.abspath(os.path.dirname(os.path.dirname(__file__))))

from src.task_queue import *


NUM_TASKS = 20000
NUM_TASKS = 10000
MIN_PRIORITY = 1
MAX_PRIORITY = 10
MIN_RAM = 4  # in GB
MAX_RAM = 16  # in GB
MIN_CPU_CORES = 1
MAX_CPU_CORES = 16
MIN_GPU_COUNT = 0
MAX_GPU_COUNT = 8

available_resources = Resources(
        MIN_RAM + 0.7*(MAX_RAM-MIN_RAM),
        int(MIN_CPU_CORES + 0.7*(MAX_CPU_CORES-MIN_CPU_CORES)),
        int(MIN_GPU_COUNT + 0.7*(MAX_GPU_COUNT-MIN_GPU_COUNT))
    )
