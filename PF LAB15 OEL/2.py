import pyodbc
import tkinter as tk
from tkinter import messagebox

# Establishing a connection to the database
con = pyodbc.connect(r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=E:\\hello.accdb;')
cur = con.cursor()

# Fetching data from the database for display
def fetch_data():
    cur.execute("SELECT * FROM Table1")
    data = cur.fetchall()
    for record in data:
        print(record)

fetch_data()  # Fetch initial data

def insert_record():
    try:
        # Example insert query to add a new record to Table1
        cur.execute("INSERT INTO Table1 (Column1, Column2) VALUES (?, ?)", (value1.get(), value2.get()))
        con.commit()
        messagebox.showinfo("Success", "Record inserted successfully.")
        fetch_data()  # Refresh data after insert
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

def delete_record():
    try:
        # Ensure the column names and table name are correct and exist in your database
        cur.execute("DELETE FROM Table1 WHERE Column1 = ?", (value1.get(),))
        con.commit()
        messagebox.showinfo("Success", "Record deleted successfully.")
        fetch_data()  # Refresh data after delete
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Creating the GUI application
root = tk.Tk()
root.title("Database Operations")

# Labels and Entry widgets
tk.Label(root, text="Value 1 (for Column1)").grid(row=0)
tk.Label(root, text="Value 2 (for Column2)").grid(row=1)

value1 = tk.Entry(root)
value2 = tk.Entry(root)

value1.grid(row=0, column=1)
value2.grid(row=1, column=1)

# Buttons for Insert and Delete
insert_button = tk.Button(root, text="Insert", command=insert_record)
insert_button.grid(row=2, column=0)

delete_button = tk.Button(root, text="Delete", command=delete_record)
delete_button.grid(row=2, column=1)

# Cleanup function to close the connection when exiting
def on_close():
    con.close()
    root.destroy()

root.protocol("WM_DELETE_WINDOW", on_close)

# Start the Tkinter event loop
root.mainloop()
