from tkinter import *
from PIL import Image, ImageTk

root=Tk()
root.geometry("600x600")
label1=Label(root, text="NAME")
label2=Label(root,text="PASSWORD")

label1.grid(row=0, column=0)
label2.grid(row=1, column=0)
    
uservalue=StringVar()
passvalue=StringVar()
username=Entry(root,textvariable=uservalue)
password=Entry(root,textvariable=passvalue)
username.grid(row=0,column=1)
password.grid(row=1,column=1)

def get_value():
    name=username.get()
    pwd=password.get()
    print("username= ", name,"\npassword= ", pwd)

sumbit_button=Button(root, text="SUBMIT", command=get_value)
sumbit_button.grid()
root.mainloop()