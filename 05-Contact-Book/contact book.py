import tkinter as tk
from tkinter import ttk, messagebox

contacts = []


# ================= FUNCTIONS =================

def clear_fields():
    name_var.set("")
    phone_var.set("")
    email_var.set("")
    address_var.set("")


def refresh_contacts(filtered=None):
    contact_tree.delete(*contact_tree.get_children())

    data = filtered if filtered is not None else contacts

    for index, contact in enumerate(data):
        contact_tree.insert(
            "",
            "end",
            iid=str(index),
            values=(contact["name"], contact["phone"])
        )

    total_label.config(text=f"Total Contacts: {len(contacts)}")


def add_contact():
    name = name_var.get().strip()
    phone = phone_var.get().strip()
    email = email_var.get().strip()
    address = address_var.get().strip()

    if not name or not phone:
        messagebox.showwarning(
            "Required",
            "Name and Phone are required!"
        )
        return

    contacts.append({
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    })

    clear_fields()
    refresh_contacts()


def update_contact():
    selected = contact_tree.selection()

    if not selected:
        messagebox.showwarning(
            "Warning",
            "Select a contact first!"
        )
        return

    item = contact_tree.item(selected[0])
    old_name = item["values"][0]

    for contact in contacts:
        if contact["name"] == old_name:

            contact["name"] = name_var.get()
            contact["phone"] = phone_var.get()
            contact["email"] = email_var.get()
            contact["address"] = address_var.get()

            break

    refresh_contacts()
    clear_fields()


def delete_contact():
    selected = contact_tree.selection()

    if not selected:
        messagebox.showwarning(
            "Warning",
            "Select a contact first!"
        )
        return

    item = contact_tree.item(selected[0])
    name = item["values"][0]

    for contact in contacts:
        if contact["name"] == name:
            contacts.remove(contact)
            break

    refresh_contacts()

    details_label.config(
        text="Select a contact to view details"
    )


def search_contact():
    keyword = search_var.get().lower().strip()

    if not keyword:
        refresh_contacts()
        return

    results = []

    for contact in contacts:
        if (
            keyword in contact["name"].lower()
            or keyword in contact["phone"]
        ):
            results.append(contact)

    refresh_contacts(results)


def show_contact(event):
    selected = contact_tree.selection()

    if not selected:
        return

    item = contact_tree.item(selected[0])
    selected_name = item["values"][0]

    for contact in contacts:
        if contact["name"] == selected_name:

            details_label.config(
                text=
                f"👤 Name\n{contact['name']}\n\n"
                f"📞 Phone\n{contact['phone']}\n\n"
                f"✉ Email\n{contact['email']}\n\n"
                f"🏠 Address\n{contact['address']}"
            )

            name_var.set(contact["name"])
            phone_var.set(contact["phone"])
            email_var.set(contact["email"])
            address_var.set(contact["address"])

            break


# ================= WINDOW =================

root = tk.Tk()
root.title("📖 Contact Book")
root.geometry("1000x600")
root.configure(bg="#0f172a")
root.resizable(False, False)

# ================= HEADER =================

header = tk.Frame(
    root,
    bg="#1e293b",
    height=50
)
header.pack(fill="x")

title = tk.Label(
    header,
    text="📖 Contact Book",
    bg="#1e293b",
    fg="white",
    font=("Segoe UI", 18, "bold")
)
title.pack(pady=10)

# ================= SIDEBAR =================

sidebar = tk.Frame(
    root,
    bg="#111827",
    width=220
)
sidebar.pack(
    side="left",
    fill="y"
)

tk.Label(
    sidebar,
    text="Contact Manager",
    bg="#111827",
    fg="#38bdf8",
    font=("Segoe UI", 13, "bold")
).pack(pady=12)

name_var = tk.StringVar()
phone_var = tk.StringVar()
email_var = tk.StringVar()
address_var = tk.StringVar()
search_var = tk.StringVar()

fields = [
    ("Name", name_var),
    ("Phone", phone_var),
    ("Email", email_var),
    ("Address", address_var)
]

for text, variable in fields:

    tk.Label(
        sidebar,
        text=text,
        bg="#111827",
        fg="white",
        font=("Segoe UI", 9)
    ).pack(anchor="w", padx=15)

    tk.Entry(
        sidebar,
        textvariable=variable,
        width=24,
        font=("Segoe UI", 10)
    ).pack(pady=3, padx=5)

# Buttons

tk.Button(
    sidebar,
    text="➕ Add Contact",
    bg="#10b981",
    fg="white",
    width=20,
    font=("Segoe UI", 9),
    command=add_contact
).pack(pady=5)

tk.Button(
    sidebar,
    text="✏ Update Contact",
    bg="#f59e0b",
    fg="white",
    width=20,
    font=("Segoe UI", 9),
    command=update_contact
).pack(pady=5)

tk.Button(
    sidebar,
    text="🗑 Delete Contact",
    bg="#ef4444",
    fg="white",
    width=20,
    font=("Segoe UI", 9),
    command=delete_contact
).pack(pady=5)

# ================= MAIN AREA =================

main = tk.Frame(
    root,
    bg="#0f172a"
)
main.pack(
    side="left",
    fill="both",
    expand=True
)

# Search Bar

search_frame = tk.Frame(
    main,
    bg="#0f172a"
)
search_frame.pack(
    fill="x",
    pady=10
)

tk.Entry(
    search_frame,
    textvariable=search_var,
    width=28,
    font=("Segoe UI", 10)
).pack(
    side="left",
    padx=15
)

tk.Button(
    search_frame,
    text="🔍 Search",
    bg="#3b82f6",
    fg="white",
    font=("Segoe UI", 9),
    command=search_contact
).pack(side="left")

# Table Area

table_frame = tk.Frame(
    main,
    bg="#0f172a"
)
table_frame.pack(
    side="left",
    padx=10
)

style = ttk.Style()
style.theme_use("clam")

style.configure(
    "Treeview",
    background="#1e293b",
    foreground="white",
    fieldbackground="#1e293b",
    rowheight=24
)

contact_tree = ttk.Treeview(
    table_frame,
    columns=("Name", "Phone"),
    show="headings",
    height=16
)

contact_tree.heading("Name", text="Name")
contact_tree.heading("Phone", text="Phone")

contact_tree.column("Name", width=220)
contact_tree.column("Phone", width=150)

contact_tree.pack(side="left")

scrollbar = ttk.Scrollbar(
    table_frame,
    orient="vertical",
    command=contact_tree.yview
)

contact_tree.configure(
    yscrollcommand=scrollbar.set
)

scrollbar.pack(
    side="right",
    fill="y"
)

contact_tree.bind(
    "<<TreeviewSelect>>",
    show_contact
)

# Details Card

card = tk.Frame(
    main,
    bg="#1e293b",
    width=380,
    height=500
)

card.pack(
    side="right",
    padx=15,
    pady=10
)

card.pack_propagate(False)

tk.Label(
    card,
    text="📇 Contact Details",
    bg="#1e293b",
    fg="#38bdf8",
    font=("Segoe UI", 14, "bold")
).pack(pady=12)

details_label = tk.Label(
    card,
    text="Select a contact to view details",
    bg="#1e293b",
    fg="white",
    justify="left",
    anchor="nw",
    font=("Segoe UI", 10),
    wraplength=340
)

details_label.pack(
    fill="both",
    expand=True,
    padx=15,
    pady=12
)

# Footer

total_label = tk.Label(
    root,
    text="Total Contacts: 0",
    bg="#1e293b",
    fg="white",
    font=("Segoe UI", 10, "bold")
)

total_label.pack(
    side="bottom",
    fill="x",
    pady=5
)

refresh_contacts()

root.mainloop()