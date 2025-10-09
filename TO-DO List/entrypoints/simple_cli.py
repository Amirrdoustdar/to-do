import sys
from core.infrastructure.persistence.file_repository import FileTaskRepository
from core.usecases.task_usecase import TaskUseCase, CreateTaskRequest, UpdateTaskRequest

def main():
    if len(sys.argv) < 2:
        print("Usage:")
        print("  python simple_cli.py create <title> <description>")
        print("  python simple_cli.py list")
        print("  python simple_cli.py update <id> [--title=<title>] [--description=<desc>]")
        print("  python simple_cli.py complete <id>")
        print("  python simple_cli.py delete <id>")
        return

    repository = FileTaskRepository("tasks.json")
    task_usecase = TaskUseCase(repository)
    
    command = sys.argv[1]
    
    try:
        if command == "create":
            if len(sys.argv) < 4:
                print("Error: Title and description are required")
                return
            title = sys.argv[2]
            description = sys.argv[3]
            request = CreateTaskRequest(title, description)
            task = task_usecase.create_task(request)
            print(f"Task created with ID: {task.id}")
            
        elif command == "list":
            tasks = task_usecase.get_all_tasks()
            for task in tasks:
                status = "✓" if task.completed else "○"
                print(f"{task.id}. [{status}] {task.title} - {task.description}")
                
        elif command == "update":
            if len(sys.argv) < 3:
                print("Error: Task ID is required")
                return
            task_id = int(sys.argv[2])
            title = None
            description = None
            for arg in sys.argv[3:]:
                if arg.startswith("--title="):
                    title = arg.split("=", 1)[1]
                elif arg.startswith("--description="):
                    description = arg.split("=", 1)[1]
            request = UpdateTaskRequest(task_id, title, description)
            task = task_usecase.update_task(request)
            if task:
                print(f"Task {task_id} updated")
            else:
                print(f"Task {task_id} not found")
                
        elif command == "complete":
            if len(sys.argv) < 3:
                print("Error: Task ID is required")
                return
            task_id = int(sys.argv[2])
            task = task_usecase.complete_task(task_id)
            if task:
                print(f"Task {task_id} completed")
            else:
                print(f"Task {task_id} not found")
                
        elif command == "delete":
            if len(sys.argv) < 3:
                print("Error: Task ID is required")
                return
            task_id = int(sys.argv[2])
            if task_usecase.delete_task(task_id):
                print(f"Task {task_id} deleted")
            else:
                print(f"Task {task_id} not found")
                
        else:
            print(f"Unknown command: {command}")
            
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()