import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import scrolledtext

# Function to open a file
def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if file_path:
        with open(file_path, 'r') as file:
            text_area.delete(1.0, tk.END)  # Clear current content
            text_area.insert(tk.INSERT, file.read())
        window.title(f"Text Editor - {file_path}")

# Function to save the current file
def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", 
                                             filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if file_path:
        with open(file_path, 'w') as file:
            file.write(text_area.get(1.0, tk.END))
        window.title(f"Text Editor - {file_path}")

# Function to save as a new file
def save_as():
    save_file()

# Function to exit the application
def exit_editor():
    if messagebox.askokcancel("Quit", "Do you want to exit the editor?"):
        window.quit()

# Creating the main window
window = tk.Tk()
window.title("My Text Editor")
window.geometry("600x400")

# Creating a text area with scrollbars
text_area = scrolledtext.ScrolledText(window, wrap=tk.WORD, undo=True)
text_area.pack(expand=True, fill='both')

# Creating a menu bar
menu_bar = tk.Menu(window)

# File menu
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_command(label="Save As", command=save_as)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=exit_editor)
menu_bar.add_cascade(label="File", menu=file_menu)

# Edit menu for cut, copy, paste functionality
edit_menu = tk.Menu(menu_bar, tearoff=0)
edit_menu.add_command(label="Cut", command=lambda: text_area.event_generate("<<Cut>>"))
edit_menu.add_command(label="Copy", command=lambda: text_area.event_generate("<<Copy>>"))
edit_menu.add_command(label="Paste", command=lambda: text_area.event_generate("<<Paste>>"))
menu_bar.add_cascade(label="Edit", menu=edit_menu)

# Adding the menu bar to the window
window.config(menu=menu_bar)

# Running the main loop
window.mainloop()
