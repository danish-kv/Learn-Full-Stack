import time
from collections import deque

class TaskSheduler:
    def __init__(self) -> None:
        self.task_queue = deque()
    
    def add_task(self, task_id, execution_time):
        self.task_queue.append((task_id, execution_time))

    def process_tasks(self):
        while self.task_queue:
            task_id, execution_time = self.task_queue.popleft()
            print(f"{task_id} started, excuting for {execution_time} seconds")
            time.sleep(execution_time)
            print(f'{task_id} is completed')

s = TaskSheduler()
s.add_task("Task 1", 4)
s.add_task("Task 2", 78)
s.add_task("Task 3", 2)
s.add_task("Task 4", 7)

s.process_tasks()