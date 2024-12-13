# rows = 5  # Number of rows for the pyramid

# # Pyramid
# for i in range(1, rows + 1):
#     print(' ' * (rows - i) + '*' * (2 * i - 1))

# # Reverse Pyramid
# for i in range(rows - 1, 0, -1):
#     print(' ' * (rows - i) + '*' * (2 * i - 1))


from tkinter import *
import random

# Function to generate a random color
def color():
    return f'#{random.randint(0, 0xFFFFFF):06x}'

# Create the main Tkinter window
root = Tk()

row = 6  # Number of rows for the pyramid

# Generate the pyramid of buttons
for i in range(row):
    for j in range(i + 1):
        but = Button(width=10, height=3, bg=color())
        but.grid(row=i, column=j)

# Start the Tkinter main loop
root.mainloop()
