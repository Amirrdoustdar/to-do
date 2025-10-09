import unittest
from core.infrastructure.persistence.in_memory_repository import InMemoryTaskRepository
from core.usecases.task_usecase import TaskUseCase, CreateTaskRequest, UpdateTaskRequest

class TestTaskUseCase(unittest.TestCase):
    def setUp(self):
        self.repository = InMemoryTaskRepository()
        self.usecase = TaskUseCase(self.repository)

    def test_create_task(self):
        request = CreateTaskRequest("Test Task", "Test Description")
        task = self.usecase.create_task(request)
        
        self.assertEqual(task.title, "Test Task")
        self.assertEqual(task.description, "Test Description")
        self.assertFalse(task.completed)
        self.assertIsNotNone(task.id)

    def test_get_task(self):
        request = CreateTaskRequest("Test Task", "Test Description")
        created_task = self.usecase.create_task(request)
        
        retrieved_task = self.usecase.get_task(created_task.id)
        self.assertEqual(created_task.id, retrieved_task.id)

    def test_complete_task(self):
        request = CreateTaskRequest("Test Task", "Test Description")
        task = self.usecase.create_task(request)
        
        completed_task = self.usecase.complete_task(task.id)
        self.assertTrue(completed_task.completed)

if __name__ == '__main__':
    unittest.main()