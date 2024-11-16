from tkinter import *
from tkinter import messagebox
import os

# Function to save the note
def save_note():
    title = title_entry.get()
    content = text_area.get("1.0", END).strip()
    if not title or not content:
        messagebox.showwarning("Warning", "Both Title and Content are required!")
        return
    with open(f"{title}.txt", "w") as file:
        file.write(content)
    messagebox.showinfo("Success", "Note saved successfully!")

# GUI Setup
root = Tk()
root.title("Virtual Notebook")

Label(root, text="Note Title:").pack(pady=5)
title_entry = Entry(root, width=40)
title_entry.pack(pady=5)

Label(root, text="Content:").pack(pady=5)
text_area = Text(root, width=50, height=20)
text_area.pack(pady=10)

Button(root, text="Save Note", command=save_note).pack(pady=10)

root.mainloop()
