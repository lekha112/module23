import tkinter as tk
from tkinter import messagebox

# Function to convert inches to cm
def convert_to_cm():
    try:
        inches = float(entry.get())
        cm = inches * 2.54
        result_label.config(text=f"{inches} inches is equal to {cm:.2f} cm")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid number.")

# Creating the main window
window = tk.Tk()
window.title("Inches to Centimeters Converter")

# Creating the input field for inches
tk.Label(window, text="Enter inches:").pack(pady=10)
entry = tk.Entry(window)
entry.pack(pady=5)

# Button to trigger conversion
convert_button = tk.Button(window, text="Convert", command=convert_to_cm)
convert_button.pack(pady=10)

# Label to display the result
result_label = tk.Label(window, text="")
result_label.pack(pady=10)

# Running the main loop
window.mainloop()
