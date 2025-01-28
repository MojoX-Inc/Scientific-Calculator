import tkinter as tk
from tkinter import messagebox, simpledialog
import math
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad


def click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = eval(screen.get())
            screen.delete(0, tk.END)
            screen.insert(tk.END, str(result))
            history_list.insert(tk.END, f"{screen.get()} = {result}")
        except Exception as e:
            messagebox.showerror("Error", "Invalid expression!")
    elif text == "C":
        screen.delete(0, tk.END)
    elif text == "Matrix":
        matrix_operations()
    elif text == "Plot":
        plot_function()
    elif text == "Solve":
        solve_equation()
    elif text == "Derivative":
        derivative()
    elif text == "Integral":
        integral()
    elif text == "Complex":
        complex_operations()
    elif text in ["sin", "cos", "tan", "log", "ln", "x²", "1/x", "√", "!"]:
        try:
            value = float(screen.get())
            screen.delete(0, tk.END)
            if text == "sin":
                screen.insert(tk.END, str(math.sin(math.radians(value))))
            elif text == "cos":
                screen.insert(tk.END, str(math.cos(math.radians(value))))
            elif text == "tan":
                screen.insert(tk.END, str(math.tan(math.radians(value))))
            elif text == "log":
                screen.insert(tk.END, str(math.log10(value)))
            elif text == "ln":
                screen.insert(tk.END, str(math.log(value)))
            elif text == "x²":
                screen.insert(tk.END, str(value**2))
            elif text == "1/x":
                screen.insert(tk.END, str(1 / value))
            elif text == "√":
                screen.insert(tk.END, str(math.sqrt(value)))
            elif text == "!":
                screen.insert(tk.END, str(math.factorial(int(value))))
        except:
            messagebox.showerror("Error", "Invalid input!")
    else:
        screen.insert(tk.END, text)


def matrix_operations():
    try:
        matrix1 = simpledialog.askstring("Matrix 1", "Enter the first matrix (comma-separated rows, space-separated columns):")
        matrix2 = simpledialog.askstring("Matrix 2", "Enter the second matrix (if applicable):")
        operation = simpledialog.askstring("Operation", "Enter operation (add, multiply):").lower()

        matrix1 = np.array([list(map(float, row.split())) for row in matrix1.split(",")])
        if matrix2:
            matrix2 = np.array([list(map(float, row.split())) for row in matrix2.split(",")])
        else:
            matrix2 = None

        if operation == "add" and matrix2 is not None:
            result = matrix1 + matrix2
        elif operation == "multiply" and matrix2 is not None:
            result = np.dot(matrix1, matrix2)
        else:
            raise ValueError("Invalid operation or missing second matrix!")
        messagebox.showinfo("Result", f"Result:\n{result}")
    except Exception as e:
        messagebox.showerror("Error", f"Matrix operation failed: {e}")


def plot_function():
    try:
        function = simpledialog.askstring("Function", "Enter the function to plot (in terms of x):")
        x_min = simpledialog.askfloat("Range", "Enter the minimum value of x:")
        x_max = simpledialog.askfloat("Range", "Enter the maximum value of x:")

        x = np.linspace(x_min, x_max, 500)
        y = [eval(function) for x in x]

        plt.plot(x, y)
        plt.title(f"Plot of {function}")
        plt.xlabel("x")
        plt.ylabel("y")
        plt.grid(True)
        plt.show()
    except Exception as e:
        messagebox.showerror("Error", f"Plotting failed: {e}")


def solve_equation():
    try:
        equation = simpledialog.askstring("Equation", "Enter the equation (in terms of x):")
        solution = sp.solve(equation, sp.Symbol('x'))
        messagebox.showinfo("Solution", f"Solutions:\n{solution}")
    except Exception as e:
        messagebox.showerror("Error", f"Equation solving failed: {e}")


def derivative():
    try:
        function = simpledialog.askstring("Function", "Enter the function (in terms of x):")
        x = sp.Symbol('x')
        derivative_result = sp.diff(function, x)
        messagebox.showinfo("Derivative", f"Derivative:\n{derivative_result}")
    except Exception as e:
        messagebox.showerror("Error", f"Derivative calculation failed: {e}")


def integral():
    try:
        function = simpledialog.askstring("Function", "Enter the function (in terms of x):")
        x = sp.Symbol('x')
        integral_result = sp.integrate(function, x)
        messagebox.showinfo("Integral", f"Integral:\n{integral_result}")
    except Exception as e:
        messagebox.showerror("Error", f"Integral calculation failed: {e}")


def complex_operations():
    try:
        real = simpledialog.askfloat("Complex", "Enter the real part:")
        imag = simpledialog.askfloat("Complex", "Enter the imaginary part:")
        operation = simpledialog.askstring("Operation", "Enter operation (magnitude, conjugate):").lower()

        z = complex(real, imag)
        if operation == "magnitude":
            result = abs(z)
        elif operation == "conjugate":
            result = z.conjugate()
        else:
            raise ValueError("Invalid operation!")
        messagebox.showinfo("Result", f"Result:\n{result}")
    except Exception as e:
        messagebox.showerror("Error", f"Complex operation failed: {e}")


root = tk.Tk()
root.title("Advanced Scientific Calculator")
root.geometry("700x800")
root.configure(bg="#2c3e50")

screen = tk.Entry(root, font="Arial 20", bd=8, relief=tk.FLAT, justify="right", bg="#ecf0f1", fg="#2c3e50")
screen.grid(row=0, column=0, columnspan=5, pady=10, padx=10)

buttons = [
    "7", "8", "9", "/", "C",
    "4", "5", "6", "*", "√",
    "1", "2", "3", "-", "x²",
    "0", ".", "=", "+", "1/x",
    "sin", "cos", "tan", "log", "ln",
    "Matrix", "Plot", "Solve", "Derivative", "Integral",
    "Complex", "!", "pi", "e", "()"
]

row_val = 1
col_val = 0
for button in buttons:
    btn = tk.Button(
        root,
        text=button,
        font=("Arial", 14),
        width=8,
        height=2,
        bg="#34495e",
        fg="#ecf0f1",
        activebackground="#1abc9c",
        activeforeground="white",
        bd=5,
        relief=tk.RAISED,
    )
    btn.grid(row=row_val, column=col_val, padx=5, pady=5)
    btn.bind("<Button-1>", click)
    col_val += 1
    if col_val > 4:
        col_val = 0
        row_val += 1

history_label = tk.Label(root, text="History", font=("Arial", 12), bg="#2c3e50", fg="#ecf0f1", anchor="w")
history_label.grid(row=row_val, column=0, columnspan=5, pady=10, padx=5, sticky="w")

history_list = tk.Listbox(root, height=8, font=("Arial", 12), bd=5, relief=tk.FLAT, bg="#34495e", fg="#ecf0f1")
history_list.grid(row=row_val + 1, column=0, columnspan=5, padx=10, pady=5)

root.mainloop()
