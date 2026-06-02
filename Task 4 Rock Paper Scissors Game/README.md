<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=00d4ff&height=220&section=header&text=🎮%20Rock%20Paper%20Scissors&fontSize=60&fontColor=ffffff&animation=fadeIn&fontAlignY=40&desc=Interactive%20GUI%20Game%20%7C%20Python%20Tkinter&descAlignY=65" width="100%"/>

<br/>

![Python](https://img.shields.io/badge/Python-3.12-blue?style=for-the-badge&logo=python&logoColor=white)
![Tkinter](https://img.shields.io/badge/Tkinter-GUI-green?style=for-the-badge)
![Game](https://img.shields.io/badge/Type-Game-orange?style=for-the-badge)
![CodSoft](https://img.shields.io/badge/CodSoft-Task%204-purple?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Completed-success?style=for-the-badge)


<br/>

> **Rock Paper Scissors Ultimate** is an interactive desktop game built with Python and Tkinter. Play against the computer, track your score, and challenge yourself to beat the AI opponent with a modern, sleek user interface and real-time statistics.

<br/>

[✨ Features](#-features) • [🚀 How to Play](#-how-to-play) • [🏗️ Architecture](#️-architecture) • [🛠️ Tech-Stack](#️-tech-stack) • [📋 Installation](#-installation) • [👨‍💻 Author](#-author)

</div>

---

# ✨ Features

<table>
<tr>
<td width="50%">

### 🎮 Gameplay

* Play against Computer AI
* Three Choice Options (Rock, Paper, Scissors)
* Instant Game Results
* Smart Win Logic
* Tie Detection

</td>

<td width="50%">

### 📊 Score Tracking

* Real-time Score Updates
* Win Rate Calculation
* Total Games Counter
* Player Score Display
* Computer Score Display

</td>
</tr>

<tr>
<td width="50%">

### 🎨 User Interface

* Modern Dark Theme
* Responsive Design
* Color-coded Messages
* Interactive Buttons
* Hover Effects

</td>

<td width="50%">

### 📋 Game History

* Round-by-Round Log
* Detailed Results
* Choice Tracking
* Scrollable History Box
* Clear Game Summary

</td>
</tr>
</table>

---

# 🚀 How to Play

1. **Start the Game** - Run the Python script to launch the GUI
2. **Make Your Choice** - Click on Rock, Paper, or Scissors button
3. **See Results** - View your choice vs. Computer's choice
4. **Track Progress** - Monitor your score and win rate
5. **Keep Playing** - Play as many rounds as you want!

### Game Rules:
- ✂️ **Scissors** beats Paper
- 📄 **Paper** beats Rock
- 🪨 **Rock** beats Scissors

---

# 🏗️ Architecture

```
Rock-Paper-Scissors Game
├── Window Setup
│   ├── Tkinter Root Window
│   ├── Theme Configuration
│   └── Color Scheme
├── Custom Components
│   ├── HoverButton Class
│   ├── Interactive UI Elements
│   └── Dynamic Styling
├── Game Logic
│   ├── Play Function
│   ├── Score Calculation
│   └── Result Determination
└── UI Elements
    ├── Score Display
    ├── History Box
    ├── Game Buttons
    └── Result Labels
```

---

# 🛠️ Tech-Stack

| Technology | Purpose |
|-----------|---------|
| **Python** | Core Language |
| **Tkinter** | GUI Framework |
| **Random Module** | Computer AI Decisions |
| **MessageBox** | User Notifications |

---

# 📋 Installation

### Prerequisites
- Python 3.7 or higher
- Tkinter (usually comes with Python)

### Steps

1. **Clone or Download** the project
   ```bash
   git clone <repository-url>
   cd "Task 4 Rock Paper Scissors Game"
   ```

2. **Install Dependencies** (if needed)
   ```bash
   pip install tkinter
   ```

3. **Run the Game**
   ```bash
   python "Rock-Paper-Scissors game.py"
   ```

---

# 🎯 Game Statistics

The game automatically tracks:
- **Your Score** - Number of rounds you won
- **Computer Score** - Number of rounds computer won
- **Total Games** - Total rounds played
- **Win Rate** - Your winning percentage

---

# 🎨 User Interface Highlights

- **Dark Theme** - Eye-friendly dark background (#0f1419)
- **Cyan Accents** - Primary color (#00d4ff)
- **Color-Coded Results**:
  - 🎉 Green (#10b981) - Victory
  - 😢 Red (#ef4444) - Loss
  - 🤝 Amber (#f59e0b) - Tie
- **Hover Effects** - Interactive button feedback
- **Responsive Layout** - 900x750px fixed window

---

# 🚀 Features in Detail

## Interactive Buttons
- Rock, Paper, Scissors buttons with hover effects
- Reset button to start fresh
- Lightening color effect on hover

## Real-time Updates
- Live score display
- Win rate calculation
- Round counter

## Game History
- Scrollable text box showing all previous rounds
- Detailed information for each game
- Tracks choices and results

## Visual Feedback
- Color-coded win/loss/tie messages
- Player and computer choice display
- Emoji indicators for better UX

---

# 💡 Future Enhancements

- [ ] Difficulty Levels (Easy, Medium, Hard)
- [ ] Sound Effects
- [ ] Save Game Statistics to File
- [ ] Multiplayer Mode
- [ ] Leaderboard
- [ ] Theme Customization

---

# 📝 Code Highlights

### Custom HoverButton Class
```python
class HoverButton(tk.Button):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.default_bg = self['bg']
        self.bind("<Enter>", self._on_enter)
        self.bind("<Leave>", self._on_leave)
```

### Game Logic
```python
if (user_choice == "Rock" and computer_choice == "Scissors") or \
   (user_choice == "Paper" and computer_choice == "Rock") or \
   (user_choice == "Scissors" and computer_choice == "Paper"):
    user_score += 1
```

---

# 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest features
- Submit pull requests
- Improve documentation

---



---

# 👨‍💻 Author

**CodSoft Intern** 
<div align="center">

### Joe Flaming

**CodSoft Python Programming Internship**
Task 4: Rock Paper Scissors Game  
*Making learning fun, one game at a time!*
[![GitHub](https://img.shields.io/badge/GitHub-joeflaming777--lgtm-181717?style=for-the-badge\&logo=github)](https://github.com/joeflaming777-lgtm)

</div>


---

<div align="center">

 **CodSoft Internship Program**

[⬆ Back to Top](#rock-paper-scissors-ultimate)

</div>
