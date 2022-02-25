from cProfile import label
from tkinter import *

root = Tk()
def myButton_Click():
    myLabel = Label(root, text="Test")
    myLabel.grid(row=1, column=1)

myButton = Button(root, text="Click Me", command=myButton_Click)

myButton.grid(row=0, column=0)

root.mainloop()