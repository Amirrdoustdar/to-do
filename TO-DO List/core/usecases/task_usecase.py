from typing import List, Optional
from ..entities.task import Task
from ..entities.repository import TaskRepository

class CreateTaskRequest:
    def __init__(self, title: str, description: str):
        self.title = title
        self.description = description

class UpdateTaskRequest:
    def __init__(self, task_id: int, title: Optional[str] = None, 
                 description: Optional[str] = None, completed: Optional[bool] = None):
        self.task_id = task_id
        self.title = title
        self.description = description
        self.completed = completed

class TaskUseCase:
    def __init__(self, task_repository: TaskRepository):
        self.task_repository = task_repository

    def create_task(self, request: CreateTaskRequest) -> Task:
        task = Task(
            id=None,
            title=request.title,
            description=request.description,
            completed=False,
            created_at=None,
            updated_at=None
        )
        return self.task_repository.save(task)

    def get_task(self, task_id: int) -> Optional[Task]:
        return self.task_repository.find_by_id(task_id)

    def get_all_tasks(self) -> List[Task]:
        return self.task_repository.find_all()

    def update_task(self, request: UpdateTaskRequest) -> Optional[Task]:
        task = self.task_repository.find_by_id(request.task_id)
        if not task:
            return None

        if request.title:
            task.title = request.title
        if request.description:
            task.description = request.description
        if request.completed is not None:
            task.completed = request.completed
        
        task.update(request.title, request.description)

        return self.task_repository.save(task)

    def delete_task(self, task_id: int) -> bool:
        return self.task_repository.delete(task_id)

    def complete_task(self, task_id: int) -> Optional[Task]:
        task = self.task_repository.find_by_id(task_id)
        if not task:
            return None
        
        task.mark_completed()
        return self.task_repository.save(task)