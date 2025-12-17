from multiprocessing.managers import BaseManager
from queue import Queue


class QueueManager(BaseManager):
    pass


task_queue = Queue()
result_queue = Queue()

QueueManager.register("get_task_queue", callable=lambda: task_queue)
QueueManager.register("get_result_queue", callable=lambda: result_queue)


class QueueClient:
    def __init__(self, address=("localhost", 8000), authkey=b"abc"):
        self.manager = QueueManager(address=address, authkey=authkey)
        self.manager.connect()

        self.task_queue = self.manager.get_task_queue()
        self.result_queue = self.manager.get_result_queue()
