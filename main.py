# This is the start of our code. 
from tkinter import *
from tkinter.ttk import *
window=Tk()

sizeOfBoardLbl=Label(window, text="Size of Board:", foreground='red', font=("Helvetica", 16))
txtfld=Entry(window, text="")
txtfld.place(x=80, y=150)
window.title('Nine Men\'s Morris')
window.geometry("300x200+10+10")
window.mainloop()

print("hello world")


