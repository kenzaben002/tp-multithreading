from manager import QueueClient
from task import Task


class Boss(QueueClient):
    def submit_tasks(self, n):
        for i in range(n):
            self.task_queue.put(Task(i, i, i * 2))

    def collect_results(self, n):
        for _ in range(n):
            print(self.result_queue.get())
