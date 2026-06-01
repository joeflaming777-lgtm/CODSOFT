import tkinter as tk
from tkinter import ttk, messagebox
import json
import os
from datetime import datetime

# ==========================================
# FILE SETUP
# ==========================================

FILE_NAME = "tasks.json"

# ==========================================
# LOAD TASKS
# ==========================================

def load_tasks():
    if not os.path.exists(FILE_NAME):
        return []

    with open(FILE_NAME, "r") as file:
        try:
            return json.load(file)
        except:
            return []

# ==========================================
# SAVE TASKS
# ==========================================

def save_tasks():
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)

# ==========================================
# ENERGY CALCULATION
# ==========================================

def calculate_energy():
    total = 0

    for task in tasks:
        if not task["completed"]:

            if task["energy"] == "Low":
                total += 1

            elif task["energy"] == "Medium":
                total += 2

            elif task["energy"] == "High":
                total += 3

    return total

# ==========================================
# XP SYSTEM
# ==========================================

def calculate_xp():
    xp = 0

    for task in tasks:
        if task["completed"]:

            if task["energy"] == "Low":
                xp += 5

            elif task["energy"] == "Medium":
                xp += 10

            elif task["energy"] == "High":
                xp += 20

    return xp

# ==========================================
# REFRESH TASK TABLE
# ==========================================

def refresh_tasks():

    for row in tree.get_children():
        tree.delete(row)

    for index, task in enumerate(tasks):

        status = "✅ Completed" if task["completed"] else "⌛ Pending"

        tree.insert(
            "",
            "end",
            values=(
                index + 1,
                task["name"],
                task["energy"],
                task["due_date"],
                status
            )
        )

    update_dashboard()

# ==========================================
# UPDATE DASHBOARD
# ==========================================

def update_dashboard():

    total = len(tasks)

    completed = len([t for t in tasks if t["completed"]])

    pending = total - completed

    xp = calculate_xp()

    energy = calculate_energy()

    dashboard_text.set(
        f"""
Total Tasks: {total}

Completed: {completed}

Pending: {pending}

XP Earned: {xp}

Mental Energy Load: {energy}
"""
    )

    # Warning system
    high_tasks = [
        t for t in tasks
        if t["energy"] == "High" and not t["completed"]
    ]

    if len(high_tasks) >= 3:
        warning_label.config(
            text="⚠️ Cognitive Load Critical!",
            fg="red"
        )
    else:
        warning_label.config(
            text="System Balanced ✅",
            fg="green"
        )

# ==========================================
# ADD TASK
# ==========================================

def add_task():

    name = task_entry.get()

    energy = energy_combo.get()

    due_date = due_entry.get()

    if name == "":
        messagebox.showerror("Error", "Task Name Required")
        return

    task = {
        "name": name,
        "energy": energy,
        "due_date": due_date,
        "completed": False
    }

    tasks.append(task)

    save_tasks()

    refresh_tasks()

    task_entry.delete(0, tk.END)

# ==========================================
# COMPLETE TASK
# ==========================================

def complete_task():

    selected = tree.selection()

    if not selected:
        messagebox.showerror("Error", "Select a task")
        return

    item = tree.item(selected)

    task_id = int(item["values"][0]) - 1

    tasks[task_id]["completed"] = True

    tasks[task_id]["completed_time"] = str(datetime.now())

    save_tasks()

    refresh_tasks()

# ==========================================
# DELETE TASK
# ==========================================

def delete_task():

    selected = tree.selection()

    if not selected:
        messagebox.showerror("Error", "Select a task")
        return

    item = tree.item(selected)

    task_id = int(item["values"][0]) - 1

    tasks.pop(task_id)

    save_tasks()

    refresh_tasks()

# ==========================================
# MAIN WINDOW
# ==========================================

root = tk.Tk()

root.title("🤖 To Do List")
root.geometry("900x600")
root.config(bg="#1e1e1e")

tasks = load_tasks()

# ==========================================
# TITLE
# ==========================================

title = tk.Label(
    root,
    text="🤖 To Do List",
    font=("Arial", 24, "bold"),
    bg="#1e1e1e",
    fg="cyan"
)

title.pack(pady=10)

# ==========================================
# DASHBOARD
# ==========================================

dashboard_text = tk.StringVar()

dashboard_label = tk.Label(
    root,
    textvariable=dashboard_text,
    font=("Arial", 12),
    bg="#2d2d2d",
    fg="white",
    width=40,
    height=8
)

dashboard_label.pack(pady=10)

warning_label = tk.Label(
    root,
    text="",
    font=("Arial", 14, "bold"),
    bg="#1e1e1e"
)

warning_label.pack()

# ==========================================
# INPUT FRAME
# ==========================================

input_frame = tk.Frame(root, bg="#1e1e1e")

input_frame.pack(pady=10)

# Task Name
task_entry = tk.Entry(
    input_frame,
    width=25,
    font=("Arial", 12)
)

task_entry.grid(row=0, column=0, padx=10)

# Energy Level
energy_combo = ttk.Combobox(
    input_frame,
    values=["Low", "Medium", "High"],
    width=15
)

energy_combo.current(1)

energy_combo.grid(row=0, column=1, padx=10)

# Due Date
due_entry = tk.Entry(
    input_frame,
    width=15,
    font=("Arial", 12)
)

due_entry.insert(0, str(datetime.now().date()))

due_entry.grid(row=0, column=2, padx=10)

# ==========================================
# BUTTONS
# ==========================================

button_frame = tk.Frame(root, bg="#1e1e1e")

button_frame.pack(pady=10)

add_btn = tk.Button(
    button_frame,
    text="Add Task",
    command=add_task,
    bg="green",
    fg="white",
    width=15
)

add_btn.grid(row=0, column=0, padx=10)

complete_btn = tk.Button(
    button_frame,
    text="Complete Task",
    command=complete_task,
    bg="blue",
    fg="white",
    width=15
)

complete_btn.grid(row=0, column=1, padx=10)

delete_btn = tk.Button(
    button_frame,
    text="Delete Task",
    command=delete_task,
    bg="red",
    fg="white",
    width=15
)

delete_btn.grid(row=0, column=2, padx=10)

# ==========================================
# TASK TABLE
# ==========================================

columns = ("ID", "Task", "Priority", "Due Date", "Status")

tree = ttk.Treeview(
    root,
    columns=columns,
    show="headings",
    height=15
)

for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=150)

tree.pack(pady=20)

# ==========================================
# INITIAL LOAD
# ==========================================

refresh_tasks()

# ==========================================
# RUN APP
# ==========================================

root.mainloop() 