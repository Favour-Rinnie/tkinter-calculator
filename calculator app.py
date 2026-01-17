import tkinter as tk
from tkinter import messagebox

# Function to update expression
def press(num):
    global expression
    expression = expression + str(num)
    equation.set(expression)

# Function to evaluate final expression
def equalpress():
    try:
        global expression
        total = str(eval(expression))
        equation.set(total)
        expression = total
    except ZeroDivisionError:
        messagebox.showerror("Error", "Oops! Division by zero not allowed.")
        expression = ""
        equation.set("")
    except:
        messagebox.showerror("Error", "Invalid Input!")
        expression = ""
        equation.set("")

# Function to clear the screen
def clear():
    global expression
    expression = ""
    equation.set("")

# Main code
if __name__ == "__main__":
    gui = tk.Tk()
    gui.configure(background="#a8a8ee")
    gui.title("Calc-u-later")
    gui.geometry("350x450")

    expression = ""
    equation = tk.StringVar()

    # Input field
    expression_field = tk.Entry(gui, textvariable=equation, font=('Arial', 20, 'bold'), bg="#2c2c3e", fg="white", bd=10, insertwidth=2, width=15, borderwidth=5)
    expression_field.grid(row=0, column=0, columnspan=4, ipadx=10, ipady=15, pady=10)

    # Button styles
    button_style = {'padx': 20, 'pady': 20, 'bd': 5, 'bg': "#DBB1C6", 'fg': "white", 'font': ('Arial', 14, 'bold')}
    op_style = {'padx': 20, 'pady': 20, 'bd': 5, 'bg': "#8eb39d", 'fg': "white", 'font': ('Arial', 14, 'bold')}

    # Buttons
    buttons = [
        ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
        ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
        ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
        ('0', 4, 0), ('.', 4, 1), ('C', 4, 2), ('+', 4, 3),
        ('=', 5, 0)
    ]

    for (text, row, col) in buttons:
        if text == "=":
            btn = tk.Button(gui, text=text, command=equalpress, **op_style)
            btn.grid(row=row, column=col, columnspan=4, sticky="nsew", pady=10, padx=10)
        elif text == "C":
            btn = tk.Button(gui, text=text, command=clear, **op_style)
            btn.grid(row=row, column=col, padx=10, pady=10, sticky="nsew")
        elif text in ['+', '-', '*', '/']:
            btn = tk.Button(gui, text=text, command=lambda t=text: press(t), **op_style)
            btn.grid(row=row, column=col, padx=10, pady=10, sticky="nsew")
        else:
            btn = tk.Button(gui, text=text, command=lambda t=text: press(t), **button_style)
            btn.grid(row=row, column=col, padx=10, pady=10, sticky="nsew")

    gui.mainloop()
