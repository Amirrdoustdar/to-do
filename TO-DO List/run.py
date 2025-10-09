import sys
import os

# Add the main path to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from core.infrastructure.persistence.in_memory_repository import InMemoryTaskRepository
from core.usecases.task_usecase import TaskUseCase, CreateTaskRequest

def main():
    print("🚀 Starting To-Do Application...")
    
    # Create repository and usecase
    repo = InMemoryTaskRepository()
    usecase = TaskUseCase(repo)
    
    # Create some sample tasks
    tasks_to_create = [
        ("Buy groceries", "Milk, bread, eggs"),
        ("Programming practice", "Implement clean architecture"),
        ("Read book", "Chapter 3 and 4")
    ]
    
    for title, description in tasks_to_create:
        request = CreateTaskRequest(title, description)
        task = usecase.create_task(request)
        print(f"✅ Created: {task.title}")
    
    # Display all tasks
    print("\n📋 All Tasks:")
    print("-" * 40)
    tasks = usecase.get_all_tasks()
    for task in tasks:
        status = "✅" if task.completed else "⭕"
        print(f"{task.id}. {status} {task.title}")
        print(f"   📝 {task.description}")
        print()
    
    print("🎉 Application is working correctly!")

if __name__ == "__main__":
    main()