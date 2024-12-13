import tkinter as tk
from math import sin, cos, tan, log, sqrt, radians

def btn_click(item):
    global expression
    expression += str(item)
    input_text.set(expression)

def btn_clear():
    global expression
    expression = ""
    input_text.set("")

def btn_equal():
    global expression
    try:
        result = str(eval(expression))
        input_text.set(result)
        expression = result
    except Exception as e:
        input_text.set("Error")
        expression = ""

def scientific_function(func):
    global expression
    try:
        value = eval(expression)  # Evaluate the current expression
        if func == "sin":
            result = sin(radians(value))
        elif func == "cos":
            result = cos(radians(value))
        elif func == "tan":
            result = tan(radians(value))
        elif func == "log":
            result = log(value)
        elif func == "sqrt":
            result = sqrt(value)
        input_text.set(str(result))
        expression = str(result)
    except Exception as e:
        input_text.set("Error")
        expression = ""

expression = ""

window = tk.Tk()
window.title("Scientific Calculator")
window.geometry("400x400")  # Initial size
window.resizable(True, True)

input_text = tk.StringVar()

input_frame = tk.Frame(window, bg="#eee")
input_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
input_frame.pack_propagate(False)

input_field = tk.Entry(input_frame, font=("arial", 24, "bold"), textvariable=input_text, bg="#eee", bd=0, justify=tk.RIGHT)
input_field.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

# Button frame
btns_frame = tk.Frame(window, bg="grey")
btns_frame.pack(fill=tk.BOTH, expand=True)

btns_frame.grid_rowconfigure(tuple(range(7)), weight=1)
btns_frame.grid_columnconfigure(tuple(range(4)), weight=1)

# Button layout
buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
]

for (text, row, col) in buttons:
    if text == "=":
        btn = tk.Button(btns_frame, text=text,fg="black", bg="#eee", cursor="hand2", command=btn_equal)
    else:
        btn = tk.Button(btns_frame, text=text, fg="black", bg="#fff", cursor="hand2", command=lambda t=text: btn_click(t))
    btn.grid(row=row, column=col, sticky="nsew", padx=1, pady=1)

# Scientific function buttons
scientific_buttons = [
    ("sin", 5, 0), ("cos", 5, 1), ("tan", 5, 2), ("sqrt", 5, 3),
    ("log", 6, 0), ("C", 6, 3)
]

for (text, row, col) in scientific_buttons:
    if text == "C":
        btn = tk.Button(btns_frame, text=text, fg="black", bg="#f00", cursor="hand2", command=btn_clear)
    else:
        btn = tk.Button(btns_frame, text=text, fg="black", bg="#ccc", cursor="hand2", command=lambda t=text: scientific_function(t))
    btn.grid(row=row, column=col, sticky="nsew", padx=1, pady=1)

# Run the application
window.mainloop()
