import tkinter as tk
from tkinter import messagebox
import random
import string

# Generate Password Function
def generate_password():
    try:
        length = int(length_entry.get())

        chars = ""

        if upper_var.get():
            chars += string.ascii_uppercase

        if lower_var.get():
            chars += string.ascii_lowercase

        if number_var.get():
            chars += string.digits

        if symbol_var.get():
            chars += string.punctuation

        if chars == "":
            messagebox.showwarning(
                "Selection Required",
                "Please select at least one character type."
            )
            return

        password = "".join(random.choice(chars) for _ in range(length))

        password_entry.delete(0, tk.END)
        password_entry.insert(0, password)

    except ValueError:
        messagebox.showerror(
            "Invalid Input",
            "Please enter a valid password length."
        )


# Copy Password Function
def copy_password():
    password = password_entry.get()

    if password:
        root.clipboard_clear()
        root.clipboard_append(password)
        messagebox.showinfo(
            "Copied",
            "Password copied to clipboard!"
        )


# Main Window
root = tk.Tk()
root.title("🔐 Password Generator")
root.geometry("500x450")
root.resizable(False, False)
root.configure(bg="#1e1e2f")

# Heading
title = tk.Label(
    root,
    text="🔐 Password Generator",
    font=("Arial", 20, "bold"),
    bg="#1e1e2f",
    fg="#00e5ff"
)
title.pack(pady=15)

# Length Input
length_label = tk.Label(
    root,
    text="Password Length",
    font=("Arial", 12),
    bg="#1e1e2f",
    fg="white"
)
length_label.pack()

length_entry = tk.Entry(
    root,
    font=("Arial", 14),
    justify="center"
)
length_entry.pack(pady=10)

# Checkboxes
upper_var = tk.BooleanVar(value=True)
lower_var = tk.BooleanVar(value=True)
number_var = tk.BooleanVar(value=True)
symbol_var = tk.BooleanVar(value=True)

tk.Checkbutton(
    root,
    text="Uppercase Letters (A-Z)",
    variable=upper_var,
    bg="#1e1e2f",
    fg="white",
    selectcolor="#333333"
).pack(anchor="w", padx=120)

tk.Checkbutton(
    root,
    text="Lowercase Letters (a-z)",
    variable=lower_var,
    bg="#1e1e2f",
    fg="white",
    selectcolor="#333333"
).pack(anchor="w", padx=120)

tk.Checkbutton(
    root,
    text="Numbers (0-9)",
    variable=number_var,
    bg="#1e1e2f",
    fg="white",
    selectcolor="#333333"
).pack(anchor="w", padx=120)

tk.Checkbutton(
    root,
    text="Special Characters (!@#$)",
    variable=symbol_var,
    bg="#1e1e2f",
    fg="white",
    selectcolor="#333333"
).pack(anchor="w", padx=120)

# Generate Button
generate_btn = tk.Button(
    root,
    text="Generate Password",
    font=("Arial", 12, "bold"),
    bg="#00c853",
    fg="white",
    width=20,
    command=generate_password
)
generate_btn.pack(pady=20)

# Password Output
password_entry = tk.Entry(
    root,
    font=("Arial", 14),
    justify="center",
    width=30
)
password_entry.pack(pady=10)

# Copy Button
copy_btn = tk.Button(
    root,
    text="Copy Password",
    font=("Arial", 12, "bold"),
    bg="#2962ff",
    fg="white",
    width=20,
    command=copy_password
)
copy_btn.pack(pady=10)

root.mainloop()