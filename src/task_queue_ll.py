from dataclasses import dataclass

# import structlinks 
from structlinks import LinkedList
  
@dataclass
class Resources:
    ram: int
    cpu_cores: int
    gpu_count: int

@dataclass
class Task:
    id: int
    priority: int
    resources: Resources
    content: str
    result: str = ""

# pip install structlinks

class TaskQueue:
    def __init__(self):
        self.queue = LinkedList.LinkedList()

    def add_task(self, task: Task):
        for i, queue_task in enumerate(self.queue):
            if task.priority < queue_task.priority:
                self.queue.insert(i, task)
                return
        self.queue.append(task)

    def get_task(self, available_resources: Resources) -> Task:
        for i, task in enumerate(self.queue):
            # print("TT",task)
            if self.can_process(task.resources, available_resources):
                self.queue.pop(i)
                return task
        return None
    
    def can_process(self, task_resources: Resources, available_resources: Resources) -> bool:
        return (
            available_resources.ram >= task_resources.ram
            and available_resources.cpu_cores >= task_resources.cpu_cores
            and available_resources.gpu_count >= task_resources.gpu_count
        )
        
    def size(self):
        return len(self.queue)
    
    def empty(self):
        if len(self.queue) <= 0:
            return True 
        return False
            
