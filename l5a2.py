import tkinter as tk
from tkinter import messagebox

# Function to calculate denominations
def calculate_denominations():
    try:
        amount = float(entry.get())
        if amount <= 0:
            messagebox.showerror("Input Error", "Please enter a positive amount.")
            return
        
        # Denominations: bills and coins
        denominations = {
            "100 Dollar Bill": 100,
            "50 Dollar Bill": 50,
            "20 Dollar Bill": 20,
            "10 Dollar Bill": 10,
            "5 Dollar Bill": 5,
            "1 Dollar Bill": 1,
            "Quarter (25¢)": 0.25,
            "Dime (10¢)": 0.10,
            "Nickel (5¢)": 0.05,
            "Penny (1¢)": 0.01
        }

        result = ""
        for name, value in denominations.items():
            count = int(amount // value)
            if count > 0:
                result += f"{count} x {name}\n"
            amount = round(amount % value, 2)

        # Display result
        result_label.config(text=result)
        
    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid number.")

# Creating the main window
window = tk.Tk()
window.title("Denomination Calculator")
window.geometry("400x400")

# Input field for the amount
tk.Label(window, text="Enter amount:").pack(pady=10)
entry = tk.Entry(window)
entry.pack(pady=5)

# Button to trigger denomination calculation
calculate_button = tk.Button(window, text="Calculate Denominations", command=calculate_denominations)
calculate_button.pack(pady=10)

# Label to display the calculated denominations
result_label = tk.Label(window, text="", justify="left")
result_label.pack(pady=10)

# Running the main loop
window.mainloop()
