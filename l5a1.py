import tkinter as tk
from tkinter import messagebox

# Function to create the Toplevel window
def open_toplevel():
    top_window = tk.Toplevel(window)
    top_window.title("Toplevel Window")
    top_window.geometry("300x200")
    
    # Adding a label to the Toplevel window
    tk.Label(top_window, text="This is a Toplevel window").pack(pady=10)
    
    # Adding a close button to the Toplevel window
    close_button = tk.Button(top_window, text="Close", command=top_window.destroy)
    close_button.pack(pady=10)

# Creating the main window
window = tk.Tk()
window.title("Main Window")
window.geometry("400x300")

# Button to open the Toplevel window
open_button = tk.Button(window, text="Open Toplevel Window", command=open_toplevel)
open_button.pack(pady=20)

# Running the main loop
window.mainloop()
