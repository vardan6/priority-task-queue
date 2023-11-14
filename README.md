## Task description:
* Requires a task queue with priorities and resource limits.
* Each task has a priority and the required amount of resources to process it.
* Publishers create tasks with specified resource limits, and put them in a task queue.
* Consumer receives the highest priority task that satisfies available resources.
* The queue is expected to contain thousands of tasks.
* Write a unit test to demonstrate the operation of the queue.

## Solution
The TaskQueue class is implemented under: `src/task_queue.py`
The test demonstration is done in the: `tests/task_queue.py`

Testsed few approaches to reside/add/get queue list:
 1. `src/task_queue.py` Using Python builtin list: `add_task()` is sorting on add, `get_task()` uses del to delete returning item.
 2. `src/task_queue_s.py` Using Python builtin list: `add_task()` is sorting after `list.append()`.
 3. `src/task_queue_ll.py` Using LinkedList from structlinks installed by `pip3 install structlinks`

The performance is about the same withing for all three cases

In the test demonstration tasks list of `NUM_TASKS` lenght is generated with random values defined in `tests/config.py`

