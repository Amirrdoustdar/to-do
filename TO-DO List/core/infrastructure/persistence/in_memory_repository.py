from typing import List, Optional
from core.entities.task import Task
from core.entities.repository import TaskRepository

class InMemoryTaskRepository(TaskRepository):
    def __init__(self):
        self._tasks = {}
        self._next_id = 1

    def save(self, task: Task) -> Task:
        if task.id is None:
            task.id = self._next_id
            self._next_id += 1
        self._tasks[task.id] = task
        return task

    def find_by_id(self, task_id: int) -> Optional[Task]:
        return self._tasks.get(task_id)

    def find_all(self) -> List[Task]:
        return list(self._tasks.values())

    def delete(self, task_id: int) -> bool:
        if task_id in self._tasks:
            del self._tasks[task_id]
            return True
        return False