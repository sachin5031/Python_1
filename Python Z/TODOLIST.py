N = int(input())  # Number of operations

tasks = {}  # Dictionary to store tasks with task_number as key
counter = 1  # Task numbering

i = 0
while i < N:
    command = input().split()
    if command[0] == '1':  # Add a new task
        tasks[counter] = {'description': ' '.join(command[1:]), 'completed': False}
        counter += 1
    elif command[0] == '2':  # Mark a task as completed
        task_number = int(command[1])
        if task_number in tasks:
            tasks[task_number]['completed'] = True
    elif command[0] == '3':  # Remove a task
        task_number = int(command[1])
        if task_number in tasks:
            del tasks[task_number]
    elif command[0] == '4':  # View the current to-do list
        print("To-Do List:")
        if tasks:
            for key in sorted(tasks.keys()):
                status = '✓' if tasks[key]['completed'] else '✗'
                print(f"{key}. {tasks[key]['description']} [{status}]")
        else:
            print("No tasks remaining.")
    elif command[0] == '5':  # Make a copy of the to-do list
        tasks_copy = tasks.copy()
    i += 1
