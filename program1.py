# Tkinter GUI Calculator
import tkinter as tk
from tkinter import messagebox

def add():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        result.set(num1 + num2)
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers")

def subtract():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        result.set(num1 - num2)
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers")

def multiply():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        result.set(num1 * num2)
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers")

def divide():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        if num2 != 0:
            result.set(num1 / num2)
        else:
            messagebox.showerror("Error", "Cannot divide by zero")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers")

# Create the main window
root = tk.Tk()
root.title("Calculator")

# Create entry widgets for numbers
entry1 = tk.Entry(root)
entry1.grid(row=0, column=1)
entry2 = tk.Entry(root)
entry2.grid(row=1, column=1)

# Create labels for entry widgets
label1 = tk.Label(root, text="Number 1:")
label1.grid(row=0, column=0)
label2 = tk.Label(root, text="Number 2:")
label2.grid(row=1, column=0)

# Create buttons for operations
button_add = tk.Button(root, text="Add", command=add)
button_add.grid(row=2, column=0)
button_subtract = tk.Button(root, text="Subtract", command=subtract)
button_subtract.grid(row=2, column=1)
button_multiply = tk.Button(root, text="Multiply", command=multiply)
button_multiply.grid(row=3, column=0)
button_divide = tk.Button(root, text="Divide", command=divide)
button_divide.grid(row=3, column=1)

# Create a label to display the result
result = tk.StringVar()
result_label = tk.Label(root, textvariable=result)
result_label.grid(row=4, column=0, columnspan=2)

# Start the main event loop
root.mainloop()
