# 📖 Contact Book

A **Contact Book** desktop application built with Python and Tkinter. This project was developed as **Task 5** of the CodSoft Python Programming Internship.

---

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Screenshots](#screenshots)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [How to Run](#how-to-run)
- [How to Use](#how-to-use)
- [Core Functions](#core-functions)
- [Author](#author)

---

## 🗂 Overview

The **Contact Book** is a fully functional GUI application that allows users to store, manage, and search contacts. Each contact can hold a **name**, **phone number**, **email address**, and **physical address**. The application provides a clean, dark-themed interface with a sidebar for data entry, a searchable contact list, and a details card panel.

---

## ✨ Features

| Feature | Description |
|---|---|
| ➕ **Add Contact** | Save a new contact with name, phone, email, and address |
| ✏️ **Update Contact** | Edit an existing contact's details |
| 🗑️ **Delete Contact** | Remove a selected contact from the list |
| 🔍 **Search Contact** | Filter contacts in real-time by name or phone number |
| 📇 **View Details** | Click any contact to see its full info in a detail card |
| 🔢 **Total Count** | Live counter at the bottom showing total number of contacts |
| 🖥️ **Dark UI Theme** | Modern dark-themed interface using Tkinter with custom colors |

---

## 🖥️ Tech Stack

- **Language:** Python 3.x
- **GUI Library:** `tkinter` (built-in)
- **Widget Set:** `tkinter.ttk` (Treeview, Scrollbar, Style)
- **Dialogs:** `tkinter.messagebox`
- **Storage:** In-memory list (runtime only)

> No external libraries required — runs on any system with Python 3 installed.

---

## 📁 Project Structure

```
Task 5 Contact Book/
│
├── contact book.py     # Main application file
└── README.md           # Project documentation
```

---

## ▶️ How to Run

### Prerequisites

- Python 3.x installed on your system
- Tkinter is included with Python by default

### Steps

1. **Clone or download** this repository.

2. Navigate to the `Task 5 Contact Book` folder:
   ```bash
   cd "Task 5 Contact Book"
   ```

3. Run the application:
   ```bash
   python "contact book.py"
   ```

The application window will open immediately — no installation needed.

---

## 🕹️ How to Use

### ➕ Adding a Contact
1. Fill in the **Name** and **Phone** fields in the left sidebar (required).
2. Optionally fill in **Email** and **Address**.
3. Click **➕ Add Contact**.

### ✏️ Updating a Contact
1. Click on a contact in the list to select it (fields auto-fill).
2. Modify the desired fields in the sidebar.
3. Click **✏ Update Contact** to save changes.

### 🗑️ Deleting a Contact
1. Click on a contact in the list to select it.
2. Click **🗑 Delete Contact** — the contact is removed immediately.

### 🔍 Searching Contacts
1. Type a **name** or **phone number** in the search bar at the top.
2. Click **🔍 Search** — the list filters in real-time.
3. Clear the search field and click Search again to reset the full list.

### 📇 Viewing Contact Details
- Simply **click** any row in the contact list.
- The right-side **Contact Details** card displays the full information for that contact.

---

## 🔧 Core Functions

| Function | Purpose |
|---|---|
| `add_contact()` | Validates inputs and appends a new contact dictionary to the list |
| `update_contact()` | Finds the selected contact by name and updates its fields |
| `delete_contact()` | Removes the selected contact from the in-memory list |
| `search_contact()` | Filters contacts by name or phone and refreshes the Treeview |
| `show_contact(event)` | Populates the detail card and sidebar fields on row selection |
| `refresh_contacts()` | Clears and reloads the Treeview with current contact data |
| `clear_fields()` | Resets all sidebar input fields to empty |

---


## 👤 Author

**Joe Flaming**
CodSoft Python Programming Internship — Task 5

---

## 📌 Notes

- Contacts are stored **in memory only** — data is lost when the application closes.
- **Name** and **Phone** are required fields; all others are optional.
- The search function matches against both **name** and **phone number**.
