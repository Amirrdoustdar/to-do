# TO-DO List Application

A clean architecture implementation of a command-line TODO list application in Python. This project demonstrates separation of concerns, dependency injection, and multiple storage options.

## Features

- ✅ Create, read, update, and delete tasks
- ✅ Mark tasks as completed
- ✅ Multiple storage options (in-memory or file-based)
- ✅ Clean Architecture principles
- ✅ Interactive and simple CLI modes
- ✅ Unit tests included

## Project Structure

```
TO-DO List/
├── core/
│   ├── entities/          # Domain entities
│   │   ├── task.py        # Task entity
│   │   └── repository.py  # Repository interface
│   ├── usecases/          # Business logic
│   │   └── task_usecase.py
│   ├── interfaces/        # Interface adapters
│   │   └── cli/
│   │       └── cli_handler.py
│   └── infrastructure/    # External implementations
│       └── persistence/
│           ├── in_memory_repository.py
│           └── file_repository.py
├── entrypoints/           # Application entry points
│   ├── cli_main.py        # Interactive CLI
│   └── simple_cli.py      # Command-line arguments
├── tests/                 # Unit tests
│   └── test_task_usecase.py
└── run.py                 # Demo script
```

## Architecture

This application follows Clean Architecture principles:

- **Entities**: Core business objects (Task)
- **Use Cases**: Application business rules (TaskUseCase)
- **Interface Adapters**: CLI handlers and presenters
- **Infrastructure**: External implementations (repositories)

## Installation

1. Clone the repository
2. Ensure you have Python 3.7+ installed
3. No external dependencies required (uses only standard library)

## Usage

### Interactive CLI Mode

Run the interactive shell:

```bash
# In-memory storage (default)
python entrypoints/cli_main.py

# File-based storage
python entrypoints/cli_main.py --file
```

Available commands in interactive mode:
- `create <title> <description>` - Create a new task
- `list` - List all tasks
- `update <id> [--title=<title>] [--description=<desc>] [--completed=<true|false>]` - Update a task
- `complete <id>` - Mark task as completed
- `delete <id>` - Delete a task
- `help` - Show help
- `exit` - Exit the application

### Simple CLI Mode

Execute single commands:

```bash
# Create a task
python entrypoints/simple_cli.py create "Buy groceries" "Milk, bread, eggs"

# List all tasks
python entrypoints/simple_cli.py list

# Update a task
python entrypoints/simple_cli.py update 1 --title="Buy groceries updated"

# Complete a task
python entrypoints/simple_cli.py complete 1

# Delete a task
python entrypoints/simple_cli.py delete 1
```

### Demo Script

Run the demo to see the application in action:

```bash
python run.py
```

## Running Tests

Execute the test suite:

```bash
python -m unittest tests/test_task_usecase.py
```

Or run all tests:

```bash
python -m unittest discover tests
```

## Storage Options

### In-Memory Storage
- Tasks are stored in memory and lost when the application closes
- Fast and suitable for testing
- Default option for `cli_main.py`

### File-Based Storage
- Tasks are persisted to `tasks.json`
- Data survives application restarts
- Used by `simple_cli.py` and optional in `cli_main.py`

## Examples

### Interactive Session

```bash
$ python entrypoints/cli_main.py
Using in-memory storage
Welcome to To-Do Application!

> create "Learn Python" "Study clean architecture"
Task created successfully (ID: 1)

> list
Tasks:
  1 [○] Learn Python            | Study clean architecture
     Created: 2025-10-19 14:30
     Updated: 2025-10-19 14:30

> complete 1
Task 'Learn Python' marked as completed

> exit
Goodbye!
```

### Command-Line Usage

```bash
$ python entrypoints/simple_cli.py create "Meeting" "Team standup at 10am"
Task created with ID: 1

$ python entrypoints/simple_cli.py list
1. [○] Meeting - Team standup at 10am

$ python entrypoints/simple_cli.py complete 1
Task 1 completed

$ python entrypoints/simple_cli.py list
1. [✓] Meeting - Team standup at 10am
```

## Design Patterns

- **Repository Pattern**: Abstract data access
- **Dependency Injection**: Loose coupling between components
- **Use Case Pattern**: Encapsulate business logic
- **Abstract Base Classes**: Define interfaces

## Future Enhancements

- Database support (SQLite, PostgreSQL)
- Task priorities and due dates
- Task categories/tags
- Search and filter functionality
- REST API interface
- Web interface

## License

This project is open source and available for educational purposes.

## Contributing

Feel free to fork this project and submit pull requests for improvements.
