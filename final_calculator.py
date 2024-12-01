import tkinter as tk

# Function to handle button clicks
def button_click(value):
    if value == "C":
        entry.delete(0, tk.END)  # Clear the entry field
    elif value == "=":
        try:
            expression = entry.get()
            result = eval(expression)  # Evaluate the mathematical expression
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    else:
        entry.insert(tk.END, value)  # Insert the clicked value into the entry field

# Main application window
root = tk.Tk()
root.title("Colorful Calculator")
root.geometry("400x600")
root.resizable(False, False)
root.configure(bg="white")  # white background for the calculator

# Title Label
title_label = tk.Label(root, text="CALCULATOR", font=("Arial", 20, "bold"), bg="white", fg="#000080")
title_label.grid(row=0, column=0, columnspan=4, pady=10)

# Entry field for user input
entry = tk.Entry(root, font=("Arial", 24), borderwidth=2,bg="#dadada", relief="solid", justify="right")
entry.grid(row=1, column=0, columnspan=4, ipadx=8, ipady=15, padx=10, pady=10)

# Button configuration
buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "C", "0", "=", "+"
]

# Colors for the buttons
button_colors = {
    "C": "#ff0000", "=": "#cc4d0d", "/": "#e66727", "*": "#ff8040", 
    "-": "#ff9a5a", "+": "#ffb373"
}
default_color = "#ffff00"

# Create buttons and place them in the grid
row_value = 2
col_value = 0
for button in buttons:
    btn = tk.Button(
        root, text=button, font=("Arial", 18), bg=button_colors.get(button, default_color), 
        fg="black", width=5, height=2, command=lambda b=button: button_click(b)
    )
    btn.grid(row=row_value, column=col_value, padx=5, pady=5)
    col_value += 1
    if col_value > 3:
        col_value = 0
        row_value += 1

# Author name at the bottom
author_label = tk.Label(root, text="Thanks for visit...", font=("Arial", 12, "italic","bold"), bg="white", fg="#000080")
author_label.grid(row=6, column=0, columnspan=4, pady=10)

# Run the application
root.mainloop()