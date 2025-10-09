from abc import ABC, abstractmethod
from typing import List, Optional
from .task import Task

class TaskRepository(ABC):
    @abstractmethod
    def save(self, task: Task) -> Task:
        pass

    @abstractmethod
    def find_by_id(self, task_id: int) -> Optional[Task]:
        pass

    @abstractmethod
    def find_all(self) -> List[Task]:
        pass

    @abstractmethod
    def delete(self, task_id: int) -> bool:
        pass