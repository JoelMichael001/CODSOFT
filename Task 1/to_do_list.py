class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f'Task "{task}" added.')

    def remove_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
            print(f'Task "{task}" removed.')
        else:
            print(f'Task "{task}" not found.')

    def update_task(self, old_task, new_task):
        if old_task in self.tasks:
            index = self.tasks.index(old_task)
            self.tasks[index] = new_task
            print(f'Task "{old_task}" updated to "{new_task}".')
        else:
            print(f'Task "{old_task}" not found.')

    def display_tasks(self):
        if not self.tasks:
            print('No tasks.')
        else:
            print('Tasks:')
            for index, task in enumerate(self.tasks, start=1):
                print(f'{index}. {task}')

def main():
    todo_list = ToDoList()

    while True:
        print("\n===== To-Do List =====")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Update Task")
        print("4. Display Tasks")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            task = input("Enter task: ")
            todo_list.add_task(task)
        elif choice == '2':
            task = input("Enter task name which you want to remove: ")
            todo_list.remove_task(task)
        elif choice == '3':
            old_task = input("Enter task name which you want to update: ")
            new_task = input("Enter new task: ")
            todo_list.update_task(old_task, new_task)
        elif choice == '4':
            todo_list.display_tasks()
        elif choice == '5':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
