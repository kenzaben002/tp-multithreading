from manager import QueueClient


class Minion(QueueClient):
    def work(self):
        while True:
            task = self.task_queue.get()
            if task is None:
                break
            result = task.work()
            self.result_queue.put(result)
