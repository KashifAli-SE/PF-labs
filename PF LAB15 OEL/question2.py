import tkinter as tk

root = tk.Tk()
root.title("Simple GUI Application")
root.geometry("400x300")  

label = tk.Label(root, text="greetings application!", font=("Arial", 14))
label.pack(pady=10)

entry_label = tk.Label(root, text="Enter your name:")
entry_label.pack()
entry = tk.Entry(root, width=30)
entry.pack(pady=5)

def greet():
    name = entry.get()
    if name:
        output_label.config(text=f"Hello, {name}!")
    else:
        output_label.config(text="Please enter your name.")

button = tk.Button(root, text="Greet Me", command=greet)
button.pack(pady=10)

output_label = tk.Label(root, text="", font=("Arial", 12), fg="green")
output_label.pack(pady=10)

root.mainloop()
