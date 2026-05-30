from tkinter import *
from tkinter import messagebox
import math

# ================= WINDOW =================

root = Tk()
root.title("Smart Calculator 🤖")

# PERFECT SIZE FOR LAPTOP
root.geometry("1000x900")

# MODERN BACKGROUND COLOR
root.config(bg="#1e1e2f")

root.resizable(False, False)

# ================= VARIABLES =================

expression = ""
input_text = StringVar()
history = []

# ================= FUNCTIONS =================

def button_click(item):
    global expression

    if expression == "0":
        expression = str(item)
    else:
        expression = expression + str(item)

    input_text.set(expression)

def clear():
    global expression
    expression = ""
    input_text.set("0")

def equal():
    global expression

    try:
        result = str(eval(expression))

        history.append(expression + " = " + result)

        input_text.set(result)

        expression = result

    except:
        messagebox.showerror("Error", "Invalid Input")
        expression = ""
        input_text.set("0")

def square_root():
    global expression

    try:
        result = str(math.sqrt(float(expression)))

        history.append("√" + expression + " = " + result)

        input_text.set(result)

        expression = result

    except:
        messagebox.showerror("Error", "Invalid Input")

def percentage():
    global expression

    try:
        result = str(float(expression) / 100)

        history.append(expression + "% = " + result)

        input_text.set(result)

        expression = result

    except:
        messagebox.showerror("Error", "Invalid Input")

def show_history():

    history_window = Toplevel(root)
    history_window.title("Calculation History")
    history_window.geometry("400x400")
    history_window.config(bg="#2d2f4a")

    text = Text(
        history_window,
        font=("Arial", 16),
        bg="#2d2f4a",
        fg="white"
    )

    text.pack(fill=BOTH, expand=True)

    if history:
        for item in history:
            text.insert(END, item + "\n")
    else:
        text.insert(END, "No History Available")

# ================= DISPLAY =================

display_frame = Frame(root, bg="#1e1e2f")
display_frame.pack(pady=20)

display = Entry(
    display_frame,
    textvariable=input_text,
    font=("Arial", 36, "bold"),
    width=28,
    bd=10,
    relief=RIDGE,
    justify=RIGHT,
    bg="#2d2f4a",
    fg="white",
    insertbackground="white"
)

display.pack(ipady=15)

input_text.set("0")

# ================= MAIN FRAME =================

main_frame = Frame(root, bg="#1e1e2f")
main_frame.pack(pady=10)

# ================= LEFT BUTTON FRAME =================

button_frame = Frame(main_frame, bg="#1e1e2f")
button_frame.grid(row=0, column=0, padx=20)

# ================= RIGHT SIDE FRAME =================

side_frame = Frame(main_frame, bg="#1e1e2f")
side_frame.grid(row=0, column=1, padx=20)

# ================= BUTTON STYLE =================

btn_font = ("Arial", 24, "bold")

# ================= CALCULATOR BUTTONS =================

buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['0', '.', '=', '+']
]

for row in range(4):
    for col in range(4):

        value = buttons[row][col]

        btn = Button(
            button_frame,
            text=value,
            font=btn_font,
            width=3,
            height=1,
            bd=5,
            relief=RAISED,
            bg="#3b3f63",
            fg="white",
            activebackground="#5c63a5",
            activeforeground="white",
            command=lambda x=value: equal() if x == "=" else button_click(x)
        )

        btn.grid(row=row, column=col, padx=10, pady=10, ipadx=25, ipady=25)

# ================= SIDE FEATURE BUTTONS =================

side_font = ("Arial", 20, "bold")

Button(
    side_frame,
    text="CLEAR",
    font=side_font,
    width=12,
    height=2,
    bg="#ff4b5c",
    fg="white",
    bd=5,
    activebackground="#ff6b81",
    command=clear
).pack(pady=12)

Button(
    side_frame,
    text="√ ROOT",
    font=side_font,
    width=12,
    height=2,
    bg="#00b894",
    fg="white",
    bd=5,
    activebackground="#00d2a0",
    command=square_root
).pack(pady=12)

Button(
    side_frame,
    text="% PERCENT",
    font=side_font,
    width=12,
    height=2,
    bg="#0984e3",
    fg="white",
    bd=5,
    activebackground="#3498ff",
    command=percentage
).pack(pady=12)

Button(
    side_frame,
    text="HISTORY",
    font=side_font,
    width=12,
    height=2,
    bg="#6c5ce7",
    fg="white",
    bd=5,
    activebackground="#8c7ae6",
    command=show_history
).pack(pady=12)

# ================= KEYBOARD SUPPORT =================

def key_press(event):
    global expression

    key = event.char

    # Numbers and operators
    if key in "0123456789+-*/.":
        button_click(key)

    # Enter key
    elif event.keysym == "Return":
        equal()

    # Backspace key
    elif event.keysym == "BackSpace":

        expression = expression[:-1]

        if expression == "":
            expression = "0"

        input_text.set(expression)

    # Escape key
    elif event.keysym == "Escape":
        clear()

# KEYBOARD BIND
root.bind("<Key>", key_press)

# ================= FOOTER =================

footer = Label(
    root,
    text="Smart Calculator | Python Project",
    font=("Arial", 16, "bold"),
    bg="#1e1e2f",
    fg="#dfe6e9"
)

footer.pack(pady=15)

# ================= RUN APPLICATION =================

root.mainloop()