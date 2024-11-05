import tkinter as tk
from tkinter import messagebox

# Function to handle form submission
def submit_form():
    name = name_entry.get()
    street = street_entry.get()
    city = city_entry.get()
    state = state_entry.get()
    zip_code = zip_entry.get()
    
    if not (name and street and city and state and zip_code):
        messagebox.showerror("Input Error", "All fields are required.")
    else:
        # Display entered information
        messagebox.showinfo("Submitted Information",
                            f"Name: {name}\n"
                            f"Street: {street}\n"
                            f"City: {city}\n"
                            f"State: {state}\n"
                            f"Zip Code: {zip_code}")

# Creating the main window
window = tk.Tk()
window.title("Address Entry Form")

# Name entry
tk.Label(window, text="Full Name:").grid(row=0, column=0, padx=10, pady=5, sticky="e")
name_entry = tk.Entry(window)
name_entry.grid(row=0, column=1, padx=10, pady=5)

# Street Address entry
tk.Label(window, text="Street Address:").grid(row=1, column=0, padx=10, pady=5, sticky="e")
street_entry = tk.Entry(window)
street_entry.grid(row=1, column=1, padx=10, pady=5)

# City entry
tk.Label(window, text="City:").grid(row=2, column=0, padx=10, pady=5, sticky="e")
city_entry = tk.Entry(window)
city_entry.grid(row=2, column=1, padx=10, pady=5)

# State entry
tk.Label(window, text="State:").grid(row=3, column=0, padx=10, pady=5, sticky="e")
state_entry = tk.Entry(window)
state_entry.grid(row=3, column=1, padx=10, pady=5)

# Zip code entry
tk.Label(window, text="Zip Code:").grid(row=4, column=0, padx=10, pady=5, sticky="e")
zip_entry = tk.Entry(window)
zip_entry.grid(row=4, column=1, padx=10, pady=5)

# Submit button
submit_button = tk.Button(window, text="Submit", command=submit_form)
submit_button.grid(row=5, columnspan=2, pady=20)

# Running the main loop
window.mainloop()
