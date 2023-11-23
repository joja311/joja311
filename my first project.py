import datetime

task_list = []

class Task:
    """
    Represents a general task.
    """
    def __init__(self, name, type, time):
        """
        Initializes a Task instance.

        Parameters:
        - name (str): The name of the task.
        - type (str): The type of the task.
        - time (str): The start time of the task.
        """
        self.name = name
        self.type = type
        self.time = time
        self.completed = False

    def __str__(self):
        """
        Returns a string representation of the task.
        """
        status = "Completed" if self.completed else "Pending"
        return f"{self.name}, starts at {self.time}, type: {self.type} task ({status})"

class PeriodicTask(Task):
    """
    Represents a periodic task.
    """
    def __init__(self, name, type, time, period):
        """
        Initializes a PeriodicTask instance.

        Parameters:
        - name (str): The name of the task.
        - type (str): The type of the task.
        - time (str): The start time of the task.
        - period (int): The period of the task in minutes.
        """
        super().__init__(name, type, time)
        self.period = period

    def __str__(self):
        """
        Returns a string representation of the periodic task.
        """
        status = "Completed" if self.completed else "Pending"
        return f"{self.period} minutes of {self.name}, starts at {self.time}, type: {self.type} task ({status})"

def to_do():
    """
    Takes user input to create tasks and adds them to the task list.
    """
    try:
        task_num = int(input('How many tasks do you wish to create: '))
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return

    for i in range(1, task_num + 1):
        task_name = input(f'Enter task {i} name: ')
        task_type = input(f'Enter task {i} type: ')
        task_time = input(f'Enter task {i} start time: ')

        try:
            task_period_ask = input(f'Do you want to add a period for task {i}? (1 for yes and 0 for no) ')
            if task_period_ask.strip() == '1':
                task_period = int(input('For how many minutes? '))
                task_add = PeriodicTask(task_name, task_type, task_time, task_period)
            else:
                task_add = Task(task_name, task_type, task_time)
            task_list.append(task_add)
        except ValueError:
            print("Invalid input. Please enter a valid number for the period.")
            return

def complete_task():
    """
    Marks a task as completed based on user input.
    """
    print("Incomplete Tasks:")
    for i, task in enumerate(task_list, start=1):
        if not task.completed:
            print(f"{i}. {task}")

    try:
        task_n = int(input("Enter the task number to mark as completed: "))
        if 1 <= task_n <= len(task_list):
            task_list[task_n - 1].completed = True
            print(f"Task {task_n} marked as completed.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

def view_completed_tasks():
    """
    Displays a list of completed tasks.
    """
    completed_tasks = [task for task in task_list if task.completed]
    if not completed_tasks:
        print('No completed tasks.')
    else:
        print('\nCompleted Tasks:')
        for i, task in enumerate(completed_tasks, start=1):
            print(f'{i}. {task}')

def menu():
    """
    Displays the main menu and handles user choices.
    """
    while True:
        print('\n\nMENU:')
        for i, tsk in enumerate(task_list, start=1):
            print(f'{i}. {tsk}')

        print('OPTIONS:')
        print('1. Add tasks')
        print('2. Complete task')
        print('3. View completed tasks')
        print('4. Exit')

        try:
            choice = int(input('Enter choice number (1, 2, 3, or 4): '))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue

        if choice == 1:
            to_do()
        elif choice == 2:
            complete_task()
        elif choice == 3:
            view_completed_tasks()
        elif choice == 4:
            exit()
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    menu()

