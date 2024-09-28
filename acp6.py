import tkinter as tk
from tkinter import messagebox
import random

# Function to determine the winner
def play(user_choice):
    options = ['Rock', 'Paper', 'Scissors']
    computer_choice = random.choice(options)

    if user_choice == computer_choice:
        result = "It's a Draw!"
    elif (user_choice == 'Rock' and computer_choice == 'Scissors') or \
         (user_choice == 'Paper' and computer_choice == 'Rock') or \
         (user_choice == 'Scissors' and computer_choice == 'Paper'):
        result = "You Win!"
    else:
        result = "You Lose!"

    # Update the result label
    result_label.config(text=f"You chose {user_choice}, Computer chose {computer_choice}\n{result}")

# Creating the main window
window = tk.Tk()
window.title("Rock, Paper, Scissors")
window.geometry("400x400")

# Title label
tk.Label(window, text="Rock, Paper, Scissors", font=("Arial", 16)).pack(pady=20)

# Create buttons for Rock, Paper, Scissors
rock_button = tk.Button(window, text="Rock", width=15, command=lambda: play("Rock"))
rock_button.pack(pady=10)

paper_button = tk.Button(window, text="Paper", width=15, command=lambda: play("Paper"))
paper_button.pack(pady=10)

scissors_button = tk.Button(window, text="Scissors", width=15, command=lambda: play("Scissors"))
scissors_button.pack(pady=10)

# Label to display the result of the game
result_label = tk.Label(window, text="", font=("Arial", 14))
result_label.pack(pady=20)

# Running the main loop
window.mainloop()
