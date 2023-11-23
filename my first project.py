import datetime

task_list = []

class Task:
    def __init__(self, name, type, time):
        self.name = name
        self.type = type
        self.time = time
        self.completed = False

    def __str__(self):
        status = "Completed" if self.completed else "Pending"
        return f"{self.name}, starts at {self.time}, type: {self.type} task ({status})"

class PeriodicTask(Task):
    def __init__(self, name, type, time, period):
        super().__init__(name, type, time)
        self.period = period

    def __str__(self):
        status = "Completed" if self.completed else "Pending"
        return f"{self.period} minutes of {self.name}, starts at {self.time}, type: {self.type} task ({status})"

def to_do():
    task_num = int(input('How many tasks do you wish to create: '))
    for i in range(1, task_num + 1):
        task_name = input(f'Enter task {i} name: ')
        task_type = input(f'Enter task {i} type: ')
        task_time = input(f'Enter task {i} start time: ')
        task_period_ask = input(f'Do you want to add a period for task {i}? (1 for yes and 0 for no) ')
        if task_period_ask.strip() == '1':
            task_period = input('For how many minutes? ')
            task_add = PeriodicTask(task_name, task_type, task_time, task_period)
        else:
            task_add = Task(task_name, task_type, task_time)
        task_list.append(task_add)

def complete_task():
    print("Incomplete Tasks:")
    for i, task in enumerate(task_list, start=1):
        if not task.completed:
            print(f"{i}. {task}")

    task_n = int(input("Enter the task number to mark as completed: "))
    try:
        task_list[task_n - 1].completed = True
        print(f"Task {task_n} marked as completed.")
    except IndexError:
        print("Invalid task number.")

def menu():
    print('\n\nMENU:')
    for i, tsk in enumerate(task_list, start=1):
        print(f'{i}. {tsk}')

    print('OPTIONS:')
    print('1. Add tasks')
    print('2. Complete task')
    print('3. View completed tasks')
    print('4. Exit')

    choice = int(input('Enter choice number (1, 2, 3, or 4): '))

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

    menu()

def view_completed_tasks():
    completed_tasks = [task for task in task_list if task.completed]
    if not completed_tasks:
        print('No completed tasks.')
    else:
        print('\nCompleted Tasks:')
        for i, task in enumerate(completed_tasks, start=1):
            print(f'{i}. {task}')

if __name__ == "__main__":
    menu()
