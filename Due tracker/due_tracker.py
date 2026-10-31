import os
import json
from datetime import datetime, timedelta
import colorama
from colorama import Fore, init

init(autoreset=True)

if not os.path.exists('due_data.json'):
    due_data = {"tasks": []}
else:
    with open('due_data.json', mode='r') as file:
        due_data = json.load(file)

def save_data():
    with open('due_data.json', mode='w') as file:
        json.dump(due_data, file, indent=4)

def get_valid_date(prompt):
    while True:
        date_text = input(prompt)
        try:
            datetime.strptime(date_text, '%d-%m-%Y')
            return date_text
        except ValueError:
            print("Please enter a real date in dd-mm-yyyy format.")

today_date = datetime.today().date()
idx = 1
for task in due_data.get('tasks', []):
    task_Date = task['due_date']
    task_date = datetime.strptime(task_Date, '%d-%m-%Y').date()
    print(f"{idx} Task: {task['task_name']}")  
    print(f"    Due: {task_Date}")
    days_left = (task_date - today_date).days
    print(f"    Days Remaining: {days_left} days left")
    if days_left < 0:
        print(Fore.RED + "    Status: OVERDUE")
    elif days_left == 0:
        print(Fore.BLUE + "   Status: Today's the day!")
    elif days_left < 15:
        print(Fore.YELLOW + "    Status: Be ready!")
    else:
        print(Fore.GREEN + "    Status: Enough time, relax!")
    idx += 1

print("do you want to add any changes to the list?")
print("1. set status to 'done' on a task")
print("2. update date of a task")
print("3. update task name")
print("4. remove a task")
print("5. add new task")
print("6. exit")

while True:
    try:
        user_input = int(input("Please answer by typing the option: "))
    except ValueError:
        print("Please enter a valid option. retrying...")
        continue
        
    if user_input == 6:
        print("bye!!")
        break
        
    if user_input in [1, 2, 3, 4]:
        try:
            task_num = int(input("Enter task number to edit: "))
            selected_task = due_data['tasks'][task_num-1]
        except (ValueError, IndexError):
            print("Please enter a valid task number. retrying...")
            continue

    if user_input == 1:
        current_due = datetime.strptime(selected_task['due_date'], '%d-%m-%Y').date()
        period = selected_task.get('period_days')
        if period is None:
            print("This task doesn't have a repetition period set.")
            continue
        next_due = current_due + timedelta(days=period)
        selected_task['due_date'] = next_due.strftime('%d-%m-%Y')
        save_data()
        print(f"Done! {selected_task['task_name']} has been moved to next due date {selected_task['due_date']}")
        print("bye!!")
        break
        
    elif user_input == 2:
        new_date = get_valid_date("enter the new date to change (dd-mm-yyyy): ")
        selected_task['due_date'] = new_date
        save_data()
        print(f"Done! date changed to: {selected_task['due_date']}")
        print("bye!!")
        break
        
    elif user_input == 3:
        new_name = input("enter a new name for the existing task: ")
        selected_task['task_name'] = new_name
        save_data()
        print(f"Done! task name has been changed to: {selected_task['task_name']}")
        print("bye!!")
        break
        
    elif user_input == 4:
        due_data['tasks'].remove(selected_task)
        save_data()
        print(f"done! {selected_task['task_name']} has been removed from the tasks list")
        print("bye!!")
        break
        
    elif user_input == 5:
        new_name = input("enter a new name for the new task: ")
        new_date = get_valid_date("enter the new date (dd-mm-yyyy): ")
        try:
            new_period = int(input("enter the repetition date: "))
        except ValueError:
            print("Not in valid format, defaulting to 0.")
            new_period = 0

        new_task = {
            "task_name": new_name,
            "due_date": new_date,
            "period_days": new_period
        }
        due_data['tasks'].append(new_task)
        save_data()
        print(f"Done! {new_name} has been added.")
        print("bye!!")
        break
