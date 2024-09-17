tdl = []

def view_tasks():
    if not tdl:
        print("Your to-do list is empty.")
    else:
        for index, task in enumerate(tdl, start=1):
            if task["done"]:
                mark = "Done"
            else:
                mark = "Not Done"
            print(f"{index}. {task['title']} - [{mark}]")

def add_task():
    title = input("Enter the new task: ")
    tdl.append({"title": title, "done": False})
    print("Task added to your to-do list.")

def update_task():
    task_num = int(input("Enter the task number to update: "))
    if 1 <= task_num <= len(tdl):
        new_title = input("Enter the new title for the task: ")
        tdl[task_num - 1]["title"] = new_title
        print("Task updated.")
    else:
        print("Invalid task number.")
def delete_task():
    task_num = int(input("Enter the task number to delete: "))
    if 1 <= task_num <= len(tdl):
        removed_task = tdl.pop(task_num - 1)
        print("Task deleted.")
    else:
        print("Invalid task number.")
def mark_task():
    task_num = int(input("Enter the task number to mark as done: "))
    if 1 <= task_num <= len(tdl):
        tdl[task_num - 1]["done"] = True
        print("Task marked as done.")
    else:
        print("Invalid task number.")

def main():
    while True:
        print("\nTo-Do List Menu:")
        print("1. View tasks")
        print("2. Add task")
        print("3. Update task")
        print("4. Delete task")
        print("5. Mark task as done")
        choice = input("Choose an option: ")

        if choice == '1':
            view_tasks()
        elif choice == '2':
            add_task()
        elif choice == '3':
            update_task()
        elif choice == '4':
            delete_task()
        elif choice == '5':
            mark_task()
        else:
            print("Invalid option. Please choose again.")

# if num == "main":
    # main()