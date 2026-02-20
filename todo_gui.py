import tkinter as tk
from tkinter import messagebox

# Window create
root = tk.Tk()
root.title("To-Do List GUI")
root.geometry("400x400")

# Sample Label
label = tk.Label(root, text="Welcome to To-Do List", font=("Arial", 16))
label.pack(pady=20)

# Quit button
quit_btn = tk.Button(root, text="Quit", command=root.destroy)
quit_btn.pack(pady=20)

# Entry for new task
task_entry = tk.Entry(root, width=30)
task_entry.pack(pady=10)

# Listbox to display tasks
tasks_listbox = tk.Listbox(root, width=50)
tasks_listbox.pack(pady=10)


# Function to add task
def add_task():
    task = task_entry.get()
    if task != "":
        tasks_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task!")

# Button to add task
add_btn = tk.Button(root, text="Add Task", command=add_task)
add_btn.pack(pady=5)


# Function to delete task
def delete_task():
    try:
        selected_task_index = tasks_listbox.curselection()[0]
        tasks_listbox.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete!")

# Button to delete task
delete_btn = tk.Button(root, text="Delete Task", command=delete_task)
delete_btn.pack(pady=5)


# Function to mark task as completed
def mark_complete():
    try:
        selected_task_index = tasks_listbox.curselection()[0]
        task_text = tasks_listbox.get(selected_task_index)
        if not task_text.endswith(" ✅"):
            tasks_listbox.delete(selected_task_index)
            tasks_listbox.insert(selected_task_index, task_text + " ✅")
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to mark complete!")

# Button to mark task as completed
complete_btn = tk.Button(root, text="Mark Complete", command=mark_complete)
complete_btn.pack(pady=5)


# Run window
root.mainloop()
