import unittest
import sys, os
import random

sys.path.append(os.path.abspath(os.path.dirname(os.path.dirname(__file__))))

from src.task_queue import *
from config import *


# NUM_TASKS = 20000
# NUM_TASKS = 1000
# MIN_PRIORITY = 1
# MAX_PRIORITY = 10
# MIN_RAM = 4  # in GB
# MAX_RAM = 16  # in GB
# MIN_CPU_CORES = 1
# MAX_CPU_CORES = 16
# MIN_GPU_COUNT = 0
# MAX_GPU_COUNT = 8

# available_resources = Resources(
#         MIN_RAM + 0.5*(MAX_RAM-MIN_RAM),
#         int(MIN_CPU_CORES + 0.5*(MAX_CPU_CORES-MIN_CPU_CORES)),
#         int(MIN_GPU_COUNT + 0.5*(MAX_GPU_COUNT-MIN_GPU_COUNT))
#     )

class TestTaskQueue():
    def __init__(self,numtasks=NUM_TASKS) -> None:
        self.num_tasks = numtasks
        self.tasks = []
        self.task_queue = TaskQueue()
        self.can_run_tasks = []

    def generate_tasks(self):
        for i in range(1, self.num_tasks + 1):
            id = i
            priority = random.randint(MIN_PRIORITY, MAX_PRIORITY)
            ram = random.randint(MIN_RAM, MAX_RAM)
            cpu_cores = random.randint(MIN_CPU_CORES, MAX_CPU_CORES)
            gpu_count = random.randint(MIN_GPU_COUNT, MAX_GPU_COUNT)
            resources = Resources(ram=ram, cpu_cores=cpu_cores, gpu_count=gpu_count, )
            task = Task(
                id = id,
                priority = priority,
                resources = resources,
                content = f"TaskInfo: id={i}, priority{priority}, ram={ram}, cpu_cores={cpu_cores}, gpu_count={gpu_count}",
                result = "Added"
            )
            self.tasks.append(task)
    
    def add_tasks(self):
        for task in self.tasks:
            self.task_queue.add_task(task)

    def get_tasks(self):
        task = None
        for i in range(self.task_queue.size()):
            task = self.task_queue.get_task(available_resources)
            if task is None:
                break
            self.can_run_tasks.append(task)
    
    def print_all_tasks(self):
        print(f"Tasks which can run on: {available_resources}")
        for task in self.can_run_tasks:
            print(task)
        print(f"\nTasks which can NOT run on: {available_resources}")
        for task in self.task_queue.queue:
            print(task)

    def print_sum(self):
        # print("Type:", type(self.task_queue))
        print("Number of tasks:", len(self.task_queue.queue))
            
    def print_task_queue(self):
        for task in self.task_queue.queue:
            print(task)
        # print("PP",self.task_queue.queue.pop())


if __name__ == "__main__":
    # unittest.main()
    p = TestTaskQueue()
    p.generate_tasks()
    p.add_tasks()
    # p.print_task_queue()
    # p.print_sum()
    p.get_tasks()
    # p.task_queue
    # p.print_all_tasks()
    pass
