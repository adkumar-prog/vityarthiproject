import datetime

class Task:
    def __init__(self, description, priority="medium"):
        self.description = description
        self.priority = priority
        self.created_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
        self.is_completed = False

    def mark_complete(self):
        self.is_completed = True

    def __str__(self):
        status = "Completed" if self.is_completed else "Pending"
        return f"[{status}] (Priority: {self.priority.capitalize()}) Created: {self.created_date} - {self.description}"

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, description, priority="medium"):
        new_task = Task(description, priority)
        self.tasks.append(new_task)
        print(f"Task added: '{description}'")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks found.")
            return

        pending = [t for t in self.tasks if not t.is_completed]
        completed = [t for t in self.tasks if t.is_completed]

        print("\n--- Pending Tasks ---")
        if not pending:
            print("None.")
        for i, task in enumerate(pending):
            print(f"{i + 1}. {task}")
        
        print("\n--- Completed Tasks ---")
        if not completed:
            print("None.")
        for task in completed:
            print(f"- {task}")
        print("---------------------\n")

    def complete_task(self, task_index):
        pending_tasks = [t for t in self.tasks if not t.is_completed]
        
        if 0 <= task_index < len(pending_tasks):
            pending_tasks[task_index].mark_complete()
            print(f"Task '{pending_tasks[task_index].description}' marked as complete.")
        else:
            print("Invalid task number.")


def main_menu():
    manager = TaskManager()
    while True:
        print("\nPython Task Manager")
        print("1. Add a new task")
        print("2. View all tasks")
        print("3. Mark a task as complete")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            desc = input("Enter task description: ")
            priority = input("Enter priority (low, medium, high - default is medium): ") or "medium"
            manager.add_task(desc, priority)
        elif choice == '2':
            manager.view_tasks()
        elif choice == '3':
            manager.view_tasks()
            if not [t for t in manager.tasks if not t.is_completed]:
                continue
            try:
                task_num = int(input("Enter the number of the task to complete (from pending list): ")) - 1
                manager.complete_task(task_num)
            except ValueError:
                print("Invalid input. Please enter a number.")
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()