import sqlite3

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    status TEXT NOT NULL
)
""")

def add_task():
    title = input("Enter task: ")
    cursor.execute("INSERT INTO tasks (title, status) VALUES (?, ?)", (title, "Pending"))
    conn.commit()
    print("Task added successfully!\n")

def view_tasks():
    cursor.execute("SELECT * FROM tasks")
    tasks = cursor.fetchall()
    for task in tasks:
        print(task)
    print()

def delete_task():
    task_id = int(input("Enter task ID to delete: "))
    cursor.execute("DELETE FROM tasks WHERE id=?", (task_id,))
    conn.commit()
    print("Task deleted!\n")

def mark_complete():
    task_id = int(input("Enter task ID to mark complete: "))
    cursor.execute("UPDATE tasks SET status='Completed' WHERE id=?", (task_id,))
    conn.commit()
    print("Task marked as completed!\n")

while True:
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Mark Task as Completed")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        delete_task()
    elif choice == "4":
        mark_complete()
    elif choice == "5":
        print("Exiting...")
        break
    else:
        print("Invalid choice\n")