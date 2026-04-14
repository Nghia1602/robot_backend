from threading import Lock
from collections import deque

class TaskService:
    _lock = Lock()
    _tasks = deque()
    
    @classmethod
    def add_task(cls, task: dict):
        with cls._lock:
            cls._tasks.append(task)
    @classmethod
    def get_tasks(cls):
        with cls._lock:
            if cls._tasks:
                return cls._tasks.popleft()
            return None
        