import sys
from typing import List
from ...usecases.task_usecase import TaskUseCase, CreateTaskRequest, UpdateTaskRequest

class CLIHandler:
    def __init__(self, task_usecase: TaskUseCase):
        self.task_usecase = task_usecase

    def print_usage(self):
        print("To-Do Application")
        print("Commands:")
        print("  create <title> <description>  - Create a new task")
        print("  list                          - List all tasks")
        print("  update <id> [--title=<title>] [--description=<desc>] [--completed=<true|false>]")
        print("  complete <id>                 - Mark task as completed")
        print("  delete <id>                   - Delete a task")
        print("  help                          - Show this help")
        print("  exit                          - Exit the application")

    def handle_create(self, args: List[str]):
        if len(args) < 2:
            print("Error: Title and description are required")
            return
        
        title = args[0]
        description = args[1]
        
        request = CreateTaskRequest(title, description)
        task = self.task_usecase.create_task(request)
        
        print(f"Task created successfully (ID: {task.id})")

    def handle_list(self, args: List[str]):
        tasks = self.task_usecase.get_all_tasks()
        
        if not tasks:
            print("No tasks found")
            return
        
        print("\nTasks:")
        print("-" * 80)
        for task in tasks:
            status = "✓" if task.completed else "○"
            print(f"{task.id:3d} [{status}] {task.title:<30} | {task.description:<30}")
            print(f"     Created: {task.created_at.strftime('%Y-%m-%d %H:%M')}")
            print(f"     Updated: {task.updated_at.strftime('%Y-%m-%d %H:%M')}")
            print()

    def handle_update(self, args: List[str]):
        if not args:
            print("Error: Task ID is required")
            return
        
        try:
            task_id = int(args[0])
        except ValueError:
            print("Error: Task ID must be a number")
            return
        
        title = None
        description = None
        completed = None
        
        for arg in args[1:]:
            if arg.startswith("--title="):
                title = arg.split("=", 1)[1]
            elif arg.startswith("--description="):
                description = arg.split("=", 1)[1]
            elif arg.startswith("--completed="):
                completed_str = arg.split("=", 1)[1].lower()
                completed = completed_str in ['true', '1', 'yes']
        
        request = UpdateTaskRequest(task_id, title, description, completed)
        task = self.task_usecase.update_task(request)
        
        if task:
            print(f"Task {task_id} updated successfully")
        else:
            print(f"Error: Task with ID {task_id} not found")

    def handle_complete(self, args: List[str]):
        if not args:
            print("Error: Task ID is required")
            return
        
        try:
            task_id = int(args[0])
        except ValueError:
            print("Error: Task ID must be a number")
            return
        
        task = self.task_usecase.complete_task(task_id)
        if task:
            print(f"Task '{task.title}' marked as completed")
        else:
            print(f"Error: Task with ID {task_id} not found")

    def handle_delete(self, args: List[str]):
        if not args:
            print("Error: Task ID is required")
            return
        
        try:
            task_id = int(args[0])
        except ValueError:
            print("Error: Task ID must be a number")
            return
        
        if self.task_usecase.delete_task(task_id):
            print(f"Task {task_id} deleted successfully")
        else:
            print(f"Error: Task with ID {task_id} not found")

    def run(self):
        print("Welcome to To-Do Application!")
        self.print_usage()
        
        while True:
            try:
                user_input = input("\n> ").strip()
                if not user_input:
                    continue
                
                parts = user_input.split()
                command = parts[0].lower()
                args = parts[1:]
                
                if command == 'exit':
                    print("Goodbye!")
                    break
                elif command == 'help':
                    self.print_usage()
                elif command == 'create':
                    self.handle_create(args)
                elif command == 'list':
                    self.handle_list(args)
                elif command == 'update':
                    self.handle_update(args)
                elif command == 'complete':
                    self.handle_complete(args)
                elif command == 'delete':
                    self.handle_delete(args)
                else:
                    print(f"Unknown command: {command}")
                    self.print_usage()
                    
            except KeyboardInterrupt:
                print("\nGoodbye!")
                break
            except Exception as e:
                print(f"Error: {e}")