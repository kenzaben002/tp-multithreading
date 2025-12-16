import numpy as np
import json
import time


class Task:
    def __init__(self, identifier=0, size=None):
        self.identifier = identifier
        self.size = size or np.random.randint(300, 3_000)
        self.a = np.random.rand(self.size, self.size)
        self.b = np.random.rand(self.size)
        self.x = np.zeros((self.size))
        self.time = 0

    def work(self):
        start = time.perf_counter()
        self.x = np.linalg.solve(self.a, self.b)
        self.time = time.perf_counter() - start

    def to_json(self) -> str:
        data = self.__dict__.copy()
        # Convertir les arrays en listes pour JSON
        data["a"] = self.a.tolist()
        data["b"] = self.b.tolist()
        data["x"] = self.x.tolist()
        return json.dumps(data)

    @staticmethod
    def from_json(text: str) -> "Task":
        data = json.loads(text)
        task = Task(identifier=data.get("identifier", 0), size=data.get("size", None))
        task.a = np.array(data["a"])
        task.b = np.array(data["b"])
        task.x = np.array(data["x"])
        task.time = data.get("time", 0)
        return task

    def __eq__(self, other: "Task") -> bool:
        if not isinstance(other, Task):
            return False
        # Comparer les arrays avec np.array_equal
        return (
            self.identifier == other.identifier
            and self.size == other.size
            and np.array_equal(self.a, other.a)
            and np.array_equal(self.b, other.b)
            and np.array_equal(self.x, other.x)
            and self.time == other.time
        )
