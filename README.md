## Task description:
* Requires a task queue with priorities and resource limits.
* Each task has a priority and the required amount of resources to process it.
* Publishers create tasks with specified resource limits, and put them in a task queue.
* Consumer receives the highest priority task that satisfies available resources.
* The queue is expected to contain thousands of tasks.
* Write a unit test to demonstrate the operation of the queue.

## Solution
The TaskQueue class is implemented under: [src/task_queue.py](./src/task_queue.py)</br>
The test demonstration is done in the: [tests/task_queue.py](./tests/task_queue.py)</br>


Tested a few approaches to reside/add/get queue list:
 1. [src/task_queue.py](./src/task_queue.py) Using Python builtin list: `add_task()` is sorting on add, `get_task()` uses del to delete returning item.</br>
 2. [src/task_queue_s.py](./src/task_queue_s.py) Using Python builtin list: `add_task()` is sorting after `list.append()`.</br>
 3. [src/task_queue_ll.py](./src/task_queu_lle.py) Using `LinkedList` from `structlinks` installed by `pip3 install structlinks`.</br>

Interestingly the performance is about the same for all three cases.

The last bullet of the task can be considered as not complete because I haven't used the unit tests package for it, but I find the current testing approach better to demonstrate the functionality.

In the test demonstration, the tasks list of `NUM_TASKS` length is generated with random values defined in [tests/config.py](./tests/config.py).

<span style="color:rgb(200, 200, 200)">
Initially, I implemented this task based on `PriorityQueue`(from 'queue') Python library but then decided to do it in place.
</span>
