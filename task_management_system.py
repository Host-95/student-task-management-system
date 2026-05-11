
import json
import os
from datetime import datetime


class Task:
    def __init__(self, task_id, title, category, deadline, status):
        self.task_id = task_id
        self.title = title
        self.category = category
        self.deadline = deadline
        self.status = status

    def to_dict(self):
        return {
            "Task ID": self.task_id,
            "Title": self.title,
            "Category": self.category,
            "Deadline": self.deadline,
            "Status": self.status
        }


class TaskManagementSystem:
    def __init__(self):
        self.file_name = "tasks.json"
        self.tasks = []
        self.load_tasks()

    def load_tasks(self):
        if os.path.exists(self.file_name):
            with open(self.file_name, "r") as file:
                try:
                    data = json.load(file)
                    for item in data:
                        task = Task(
                            item["Task ID"],
                            item["Title"],
                            item["Category"],
                            item["Deadline"],
                            item["Status"]
                        )
                        self.tasks.append(task)
                except json.JSONDecodeError:
                    self.tasks = []

    def save_tasks(self):
        with open(self.file_name, "w") as file:
            json.dump([task.to_dict() for task in self.tasks], file, indent=4)

    def add_task(self):
        print("\nAdd New Task")

        task_id = input("Enter Task ID: ")
        title = input("Enter Task Title: ")
        category = input("Enter Task Category: ")
        deadline = input("Enter Deadline (DD-MM-YYYY): ")
        status = "Pending"

        try:
            datetime.strptime(deadline, "%d-%m-%Y")
        except ValueError:
            print("Invalid date format.")
            return

        task = Task(task_id, title, category, deadline, status)
        self.tasks.append(task)
        self.save_tasks()

        print("Task added successfully.")

    def view_tasks(self):
        print("\nAll Tasks")

        if not self.tasks:
            print("No tasks available.")
            return

        for task in self.tasks:
            print("----------------------------")
            print(f"Task ID   : {task.task_id}")
            print(f"Title     : {task.title}")
            print(f"Category  : {task.category}")
            print(f"Deadline  : {task.deadline}")
            print(f"Status    : {task.status}")

    def update_task(self):
        print("\nUpdate Task")

        task_id = input("Enter Task ID to update: ")

        for task in self.tasks:
            if task.task_id == task_id:
                print("1. Update Title")
                print("2. Update Category")
                print("3. Update Deadline")
                print("4. Update Status")

                choice = input("Choose an option: ")

                if choice == "1":
                    task.title = input("Enter new title: ")

                elif choice == "2":
                    task.category = input("Enter new category: ")

                elif choice == "3":
                    task.deadline = input("Enter new deadline (DD-MM-YYYY): ")

                elif choice == "4":
                    task.status = input("Enter status (Pending/Completed): ")

                else:
                    print("Invalid option.")
                    return

                self.save_tasks()
                print("Task updated successfully.")
                return

        print("Task not found.")

    def delete_task(self):
        print("\nDelete Task")

        task_id = input("Enter Task ID to delete: ")

        for task in self.tasks:
            if task.task_id == task_id:
                self.tasks.remove(task)
                self.save_tasks()
                print("Task deleted successfully.")
                return

        print("Task not found.")

    def search_task(self):
        print("\nSearch Task")

        keyword = input("Enter task title keyword: ").lower()

        found = False

        for task in self.tasks:
            if keyword in task.title.lower():
                found = True
                print("----------------------------")
                print(f"Task ID   : {task.task_id}")
                print(f"Title     : {task.title}")
                print(f"Category  : {task.category}")
                print(f"Deadline  : {task.deadline}")
                print(f"Status    : {task.status}")

        if not found:
            print("No matching task found.")

    def display_menu(self):
        while True:
            print("\n==============================")
            print(" Student Task Management System")
            print("==============================")
            print("1. Add Task")
            print("2. View Tasks")
            print("3. Update Task")
            print("4. Delete Task")
            print("5. Search Task")
            print("6. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                self.add_task()

            elif choice == "2":
                self.view_tasks()

            elif choice == "3":
                self.update_task()

            elif choice == "4":
                self.delete_task()

            elif choice == "5":
                self.search_task()

            elif choice == "6":
                print("Exiting program...")
                break

            else:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    system = TaskManagementSystem()
    system.display_menu()