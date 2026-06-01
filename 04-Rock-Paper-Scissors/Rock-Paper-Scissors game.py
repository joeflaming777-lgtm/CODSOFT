import tkinter as tk
from tkinter import messagebox
import random

# ---------------- WINDOW SETUP ---------------- #

root = tk.Tk()
root.title("🎮 Rock Paper Scissors Ultimate")
root.geometry("900x750")
root.configure(bg="#0f1419")
root.resizable(False, False)

# Configure styles
root.option_add("*Font", ("Segoe UI", 10))

# Colors
PRIMARY_COLOR = "#00d4ff"
SECONDARY_COLOR = "#1e293b"
ACCENT_BG = "#1a2332"
SUCCESS_COLOR = "#10b981"
DANGER_COLOR = "#ef4444"
WARNING_COLOR = "#f59e0b"

# Custom button hover effects
class HoverButton(tk.Button):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.default_bg = self['bg']
        self.hover_bg = self._lighten_color(self.default_bg)
        self.bind("<Enter>", self._on_enter)
        self.bind("<Leave>", self._on_leave)
    
    def _lighten_color(self, color):
        if color.startswith("#"):
            hex_color = color.lstrip("#")
            rgb = tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
            lighter_rgb = tuple(min(c + 40, 255) for c in rgb)
            return "#{:02x}{:02x}{:02x}".format(*lighter_rgb)
        return color
    
    def _on_enter(self, event):
        self.config(bg=self.hover_bg, relief=tk.SUNKEN, bd=3)
    
    def _on_leave(self, event):
        self.config(bg=self.default_bg, relief=tk.RAISED, bd=1)

# ---------------- VARIABLES ---------------- #

choices = ["Rock", "Paper", "Scissors"]

user_score = 0
computer_score = 0
total_games = 0

# ---------------- GAME FUNCTION ---------------- #

def play(user_choice):
    global user_score, computer_score, total_games

    computer_choice = random.choice(choices)
    total_games += 1

    user_choice_label.config(text=f"👤 You: {user_choice}", fg=PRIMARY_COLOR)
    computer_choice_label.config(text=f"🤖 Computer: {computer_choice}", fg=PRIMARY_COLOR)

    if user_choice == computer_choice:
        result = "🤝 It's a Tie!"
        result_label.config(text=result, fg=WARNING_COLOR, font=("Segoe UI", 24, "bold"))

    elif (
        (user_choice == "Rock" and computer_choice == "Scissors")
        or (user_choice == "Paper" and computer_choice == "Rock")
        or (user_choice == "Scissors" and computer_choice == "Paper")
    ):
        user_score += 1
        result = "🎉 You Win!"
        result_label.config(text=result, fg=SUCCESS_COLOR, font=("Segoe UI", 24, "bold"))

    else:
        computer_score += 1
        result = "😢 Computer Wins!"
        result_label.config(text=result, fg=DANGER_COLOR, font=("Segoe UI", 24, "bold"))

    # Calculate win percentage
    win_percentage = (user_score / total_games * 100) if total_games > 0 else 0
    
    score_label.config(
        text=f"🏆 Your Score: {user_score}  |  🤖 Computer Score: {computer_score}  |  Total: {total_games}"
    )
    
    percentage_label.config(
        text=f"📊 Win Rate: {win_percentage:.1f}%"
    )

    # Enable, insert, and disable history box
    history_box.config(state=tk.NORMAL)
    history_box.insert(
        tk.END,
        f"Round {total_games}: You [{user_choice}] vs Computer [{computer_choice}] ➜ {result}\n"
    )

    history_box.see(tk.END)
    history_box.config(state=tk.DISABLED)

# Keyboard bindings
def on_key_press(event):
    if event.char.lower() == 'r':
        play("Rock")
    elif event.char.lower() == 'p':
        play("Paper")
    elif event.char.lower() == 's':
        play("Scissors")

root.bind('<r>', on_key_press)
root.bind('<p>', on_key_press)
root.bind('<s>', on_key_press)

# ---------------- RESET GAME FUNCTION ---------------- #

def reset_game():
    global user_score, computer_score, total_games

    if total_games > 0:
        result = messagebox.askyesno("Confirm Reset", "Are you sure you want to reset the game?")
        if not result:
            return

    user_score = 0
    computer_score = 0
    total_games = 0

    score_label.config(
        text=f"🏆 Your Score: 0  |  🤖 Computer Score: 0  |  Total: 0"
    )
    
    percentage_label.config(text="📊 Win Rate: 0.0%")

    user_choice_label.config(text="👤 You: -", fg="white")
    computer_choice_label.config(text="🤖 Computer: -", fg="white")

    result_label.config(text="Choose Your Move!", fg=PRIMARY_COLOR, font=("Segoe UI", 24, "bold"))

    # Clear history
    history_box.config(state=tk.NORMAL)
    history_box.delete(1.0, tk.END)
    history_box.config(state=tk.DISABLED)

# ============ TOP FRAME - HEADER ============ #

top_frame = tk.Frame(root, bg=ACCENT_BG, height=80)
top_frame.pack(fill=tk.X, padx=0, pady=0)

title = tk.Label(
    top_frame,
    text="🎮 ROCK PAPER SCISSORS ULTIMATE 🎮",
    font=("Segoe UI", 28, "bold"),
    bg=ACCENT_BG,
    fg=PRIMARY_COLOR
)
title.pack(pady=15)

# ============ STATS FRAME ============ #

stats_frame = tk.Frame(root, bg="#0f1419")
stats_frame.pack(pady=15, fill=tk.X, padx=20)

score_label = tk.Label(
    stats_frame,
    text="🏆 Your Score: 0  |  🤖 Computer Score: 0  |  Total: 0",
    font=("Segoe UI", 12, "bold"),
    bg="#0f1419",
    fg=PRIMARY_COLOR
)
score_label.pack()

percentage_label = tk.Label(
    stats_frame,
    text="📊 Win Rate: 0.0%",
    font=("Segoe UI", 11),
    bg="#0f1419",
    fg="#fbbf24"
)
percentage_label.pack(pady=5)

# ============ BUTTONS FRAME ============ #

button_frame = tk.Frame(root, bg="#0f1419")
button_frame.pack(pady=20)

rock_btn = HoverButton(
    button_frame,
    text="🪨 ROCK",
    font=("Segoe UI", 14, "bold"),
    bg="#8b5cf6",
    fg="white",
    width=12,
    height=2,
    relief=tk.RAISED,
    bd=1,
    command=lambda: play("Rock")
)
rock_btn.grid(row=0, column=0, padx=15)

paper_btn = HoverButton(
    button_frame,
    text="📄 PAPER",
    font=("Segoe UI", 14, "bold"),
    bg="#3b82f6",
    fg="white",
    width=12,
    height=2,
    relief=tk.RAISED,
    bd=1,
    command=lambda: play("Paper")
)
paper_btn.grid(row=0, column=1, padx=15)

scissors_btn = HoverButton(
    button_frame,
    text="✂️ SCISSORS",
    font=("Segoe UI", 14, "bold"),
    bg="#ec4899",
    fg="white",
    width=12,
    height=2,
    relief=tk.RAISED,
    bd=1,
    command=lambda: play("Scissors")
)
scissors_btn.grid(row=0, column=2, padx=15)

# Add keyboard shortcuts text
shortcuts_label = tk.Label(
    button_frame,
    text="💡 Press: R=Rock | P=Paper | S=Scissors",
    font=("Segoe UI", 9),
    bg="#0f1419",
    fg="#6b7280"
)
shortcuts_label.grid(row=1, column=0, columnspan=3, pady=(10, 0))

# ============ DISPLAY FRAME ============ #

display_frame = tk.Frame(root, bg=ACCENT_BG)
display_frame.pack(pady=15, padx=20, fill=tk.BOTH)

user_choice_label = tk.Label(
    display_frame,
    text="👤 You: -",
    font=("Segoe UI", 16, "bold"),
    bg=ACCENT_BG,
    fg="white"
)
user_choice_label.pack(pady=8)

computer_choice_label = tk.Label(
    display_frame,
    text="🤖 Computer: -",
    font=("Segoe UI", 16, "bold"),
    bg=ACCENT_BG,
    fg="white"
)
computer_choice_label.pack(pady=8)

result_label = tk.Label(
    display_frame,
    text="Choose Your Move!",
    font=("Segoe UI", 24, "bold"),
    bg=ACCENT_BG,
    fg=PRIMARY_COLOR
)
result_label.pack(pady=15)

# ============ HISTORY FRAME ============ #

history_title = tk.Label(
    root,
    text="📜 Match History",
    font=("Segoe UI", 13, "bold"),
    bg="#0f1419",
    fg=PRIMARY_COLOR
)
history_title.pack()

history_box = tk.Text(
    root,
    height=8,
    width=90,
    bg="#1a2332",
    fg="#d1d5db",
    font=("Consolas", 9),
    state=tk.DISABLED
)
history_box.pack(pady=10, padx=20)

# ============ BUTTONS FRAME - ACTIONS ============ #

action_frame = tk.Frame(root, bg="#0f1419")
action_frame.pack(pady=15)

reset_btn = HoverButton(
    action_frame,
    text="🔄 Reset Game",
    font=("Segoe UI", 12, "bold"),
    bg=DANGER_COLOR,
    fg="white",
    width=20,
    relief=tk.RAISED,
    bd=1,
    command=reset_game
)
reset_btn.pack(side=tk.LEFT, padx=10)

exit_btn = HoverButton(
    action_frame,
    text="❌ Exit",
    font=("Segoe UI", 12, "bold"),
    bg="#6b7280",
    fg="white",
    width=20,
    relief=tk.RAISED,
    bd=1,
    command=root.quit
)
exit_btn.pack(side=tk.LEFT, padx=10)

# ============ FOOTER ============ #

footer = tk.Label(
    root,
    text="🚀 Have Fun Playing! Created with Python ❤️ | Keyboard: R, P, S",
    font=("Segoe UI", 9),
    bg="#0f1419",
    fg="#4b5563"
)
footer.pack(side="bottom", pady=8)

root.mainloop()