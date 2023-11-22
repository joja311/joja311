task_list = []
def to_do():
    class task:
        def __init__(self, name, type, time):
            self.name = name
            self.type = type
            self.time = time
        def __str__(self):
            return str(self.name+',starts at '+self.time+', type : '+self.type+' task ')





    class periodic_task(task):
        def __init__(self, name, type, time, period):
            super().__init__(name, type, time)
            self.period = period
        def __str__(self):
            return str(self.period + ' minutes of '+self.name+',starts at '+self.time+', type : '+self.type+' task ')




    task_num = int(input('how many tasks you wish to create: '))
    i = 1

    while i <= task_num :
        task_name = input('enter task'+str(i) +' name: ')
        task_type = input('enter task'+str(i) +' type: ')
        task_time = input('enter task'+str(i) +' start time: ')
        task_period_ask = input('do you want to add a period for task'+str(i) +'? (1 for yes and 0 for no)')
        if task_period_ask.strip() == '1':
            task_period = input('for how much minutes? :')
            task_add = periodic_task(task_name, task_type, task_time, task_period)
            task_list.append(task_add)
        else:
            task_add = task(task_name, task_type, task_time)
            task_list.append(task_add)

        i += 1
task_number = [x for x in range(1, len(task_list)+1)]
def menu():
    print('\n\nMENU :')

    for tsk in task_list :
            print('task'+str(task_list.index(tsk)+1)+': ', end='')
            print(tsk)

    print('OPTIONS :')
    print('1-add tasks')
    print('2-complete task')
    choice = int(input('enter choice number (1 or 2) : '))

    if choice == 1:
        to_do()
        menu()
    elif choice ==2:
        task_n = int(input('enter task number to remove (e.g: 1 for task1) : '))
        try:
            task_list.pop(task_n-1)
        except IndexError:
            print('! invalid choice number check the menu !')
        menu()
menu()