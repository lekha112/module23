import tkinter as tk
from tkinter import messagebox
import random
import string

# Function to generate a random password
def generate_password():
    try:
        length = int(length_entry.get())
        if length < 4:
            messagebox.showerror("Input Error", "Password length should be at least 4.")
            return
        
        # Characters to use for password generation
        characters = string.ascii_letters + string.digits + string.punctuation
        
        # Generate random password
        password = ''.join(random.choice(characters) for _ in range(length))
        
        # Display generated password
        password_label.config(text=f"Generated Password: {password}")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid number.")

# Creating the main window
window = tk.Tk()
window.title("Random Password Generator")

# Length entry
tk.Label(window, text="Enter password length:").pack(pady=10)
length_entry = tk.Entry(window)
length_entry.pack(pady=5)

# Button to trigger password generation
generate_button = tk.Button(window, text="Generate Password", command=generate_password)
generate_button.pack(pady=10)

# Label to display the generated password
password_label = tk.Label(window, text="")
password_label.pack(pady=10)

# Running the main loop
window.mainloop()
