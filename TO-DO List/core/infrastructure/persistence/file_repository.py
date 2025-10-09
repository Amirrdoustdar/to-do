import json
from typing import List, Optional
from datetime import datetime
from ...entities.task import Task
from ...entities.repository import TaskRepository

class FileTaskRepository(TaskRepository):
    def __init__(self, filename: str = "tasks.json"):
        self.filename = filename

    def _load_tasks(self) -> List[dict]:
        try:
            with open(self.filename, 'r') as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def _save_tasks(self, tasks_data: List[dict]):
        with open(self.filename, 'w') as f:
            json.dump(tasks_data, f, indent=2)

    def _to_dict(self, task: Task) -> dict:
        return task.to_dict()

    def _from_dict(self, task_dict: dict) -> Task:
        return Task(
            id=task_dict['id'],
            title=task_dict['title'],
            description=task_dict['description'],
            completed=task_dict['completed'],
            created_at=datetime.fromisoformat(task_dict['created_at']),
            updated_at=datetime.fromisoformat(task_dict['updated_at'])
        )

    def save(self, task: Task) -> Task:
        tasks_data = self._load_tasks()
        
        if task.id is None:
            # New task
            if tasks_data:
                new_id = max(t['id'] for t in tasks_data) + 1
            else:
                new_id = 1
            task.id = new_id
            tasks_data.append(self._to_dict(task))
        else:
            # Update existing task
            for i, t in enumerate(tasks_data):
                if t['id'] == task.id:
                    tasks_data[i] = self._to_dict(task)
                    break
        
        self._save_tasks(tasks_data)
        return task

    def find_by_id(self, task_id: int) -> Optional[Task]:
        tasks_data = self._load_tasks()
        for task_dict in tasks_data:
            if task_dict['id'] == task_id:
                return self._from_dict(task_dict)
        return None

    def find_all(self) -> List[Task]:
        tasks_data = self._load_tasks()
        return [self._from_dict(task_dict) for task_dict in tasks_data]

    def delete(self, task_id: int) -> bool:
        tasks_data = self._load_tasks()
        initial_length = len(tasks_data)
        tasks_data = [t for t in tasks_data if t['id'] != task_id]
        
        if len(tasks_data) < initial_length:
            self._save_tasks(tasks_data)
            return True
        return False