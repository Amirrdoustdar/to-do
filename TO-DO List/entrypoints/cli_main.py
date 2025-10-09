import sys
from core.infrastructure.persistence.in_memory_repository import InMemoryTaskRepository
from core.infrastructure.persistence.file_repository import FileTaskRepository
from core.usecases.task_usecase import TaskUseCase
from core.interfaces.cli.cli_handler import CLIHandler

def main():
    # Choose repository type
    if len(sys.argv) > 1 and sys.argv[1] == "--file":
        repository = FileTaskRepository()
        print("Using file-based storage")
    else:
        repository = InMemoryTaskRepository()
        print("Using in-memory storage")
    
    # Dependency injection
    task_usecase = TaskUseCase(repository)
    cli_handler = CLIHandler(task_usecase)
    
    # Run CLI
    cli_handler.run()

if __name__ == "__main__":
    main()