import tkinter as tk
from tkinter import messagebox

# Function to calculate the total bill
def calculate_total():
    try:
        # Get the quantities entered
        burger_qty = int(burger_entry.get())
        pizza_qty = int(pizza_entry.get())
        fries_qty = int(fries_entry.get())
        drinks_qty = int(drinks_entry.get())

        # Calculate total for each item
        burger_total = burger_qty * 5.99
        pizza_total = pizza_qty * 8.99
        fries_total = fries_qty * 2.99
        drinks_total = drinks_qty * 1.99

        # Calculate overall total
        total_cost = burger_total + pizza_total + fries_total + drinks_total
        
        # Display the total cost
        total_label.config(text=f"Total: ${total_cost:.2f}")
    
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers for quantities.")

# Function to reset all input fields and total
def reset_order():
    burger_entry.delete(0, tk.END)
    pizza_entry.delete(0, tk.END)
    fries_entry.delete(0, tk.END)
    drinks_entry.delete(0, tk.END)
    total_label.config(text="Total: $0.00")

# Creating the main window
window = tk.Tk()
window.title("Restaurant Management System")
window.geometry("400x400")

# Creating labels and entry fields for the menu items
tk.Label(window, text="Menu", font=('Arial', 16)).pack(pady=10)

tk.Label(window, text="Burger ($5.99)").pack()
burger_entry = tk.Entry(window)
burger_entry.pack(pady=5)

tk.Label(window, text="Pizza ($8.99)").pack()
pizza_entry = tk.Entry(window)
pizza_entry.pack(pady=5)

tk.Label(window, text="Fries ($2.99)").pack()
fries_entry = tk.Entry(window)
fries_entry.pack(pady=5)

tk.Label(window, text="Drinks ($1.99)").pack()
drinks_entry = tk.Entry(window)
drinks_entry.pack(pady=5)

# Button to calculate total bill
calculate_button = tk.Button(window, text="Calculate Total", command=calculate_total)
calculate_button.pack(pady=10)

# Button to reset the form
reset_button = tk.Button(window, text="Reset", command=reset_order)
reset_button.pack(pady=10)

# Label to display the total cost
total_label = tk.Label(window, text="Total: $0.00", font=('Arial', 14))
total_label.pack(pady=20)

# Running the main loop
window.mainloop()
