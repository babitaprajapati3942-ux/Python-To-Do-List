import tkinter as tk
from tkinter import messagebox


# Main window
window = tk.Tk()
window.title("To-Do List")
window.geometry("600x600")
window.resizable(False, False)


# Heading
heading = tk.Label(
    window,
    text="MY TO-DO LIST",
    font=("Arial", 26, "bold")
)
heading.pack(pady=20)


# Task input
task_entry = tk.Entry(
    window,
    font=("Arial", 16),
    width=35
)
task_entry.pack(pady=10)


# Task list
task_list = tk.Listbox(
    window,
    font=("Arial", 16),
    width=40,
    height=12
)
task_list.pack(pady=15)


# Starting/sample tasks
task_list.insert(tk.END, "Study Python")
task_list.insert(tk.END, "Complete College Assignment")
task_list.insert(tk.END, "Prepare Project PPT")
task_list.insert(tk.END, "Practice Coding")
task_list.insert(tk.END, "Revise Data Structures")


# Add task
def add_task():
    task = task_entry.get()

    if task != "":
        task_list.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning(
            "Warning",
            "Please enter a task."
        )


# Mark task as completed
def complete_task():
    selected = task_list.curselection()

    if selected:
        task = task_list.get(selected[0])

        if not task.startswith("✓"):
            task_list.delete(selected[0])
            task_list.insert(
                selected[0],
                "✓ " + task
            )
    else:
        messagebox.showwarning(
            "Warning",
            "Please select a task."
        )


# Delete task
def delete_task():
    selected = task_list.curselection()

    if selected:
        task_list.delete(selected[0])
    else:
        messagebox.showwarning(
            "Warning",
            "Please select a task."
        )


# Clear all tasks
def clear_all():
    task_list.delete(0, tk.END)


# Button frame
button_frame = tk.Frame(window)
button_frame.pack(pady=10)


# Add button
tk.Button(
    button_frame,
    text="ADD TASK",
    font=("Arial", 13),
    width=13,
    command=add_task
).grid(row=0, column=0, padx=5)


# Complete button
tk.Button(
    button_frame,
    text="COMPLETE",
    font=("Arial", 13),
    width=13,
    command=complete_task
).grid(row=0, column=1, padx=5)


# Delete button
tk.Button(
    button_frame,
    text="DELETE",
    font=("Arial", 13),
    width=13,
    command=delete_task
).grid(row=0, column=2, padx=5)


# Clear All button
tk.Button(
    button_frame,
    text="CLEAR ALL",
    font=("Arial", 13),
    width=13,
    command=clear_all
).grid(row=0, column=3, padx=5)


# Exit button
tk.Button(
    window,
    text="EXIT",
    font=("Arial", 14),
    width=20,
    command=window.destroy
).pack(pady=15)


# Start application
window.mainloop()