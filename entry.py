from tkinter import *

root = Tk()

inputBox = Entry(root, bg="black", fg="white")
inputBox.grid(row=0, column=1)
inputBox.insert(0, "Enter your name.")

def myButton_Click():
    myLabel = Label(root, text=inputBox.get())
    myLabel.grid(row=1, column=1)

myButton = Button(root, text="Click Me", command=myButton_Click)

myButton.grid(row=0, column=0)

root.mainloop()