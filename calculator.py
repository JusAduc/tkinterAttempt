from tkinter import *

root = Tk()
root.title("Simeple Calculator")

#region Ex Code
# inputBox = Entry(root, bg="black", fg="white")
# inputBox.grid(row=0, column=1)
# inputBox.insert(0, "Enter your name.")

# def myButton_Click():
#     myLabel = Label(root, text=inputBox.get())
#     myLabel.grid(row=1, column=1)

# myButton = Button(root, text="Click Me", command=myButton_Click)

# myButton.grid(row=0, column=0)
#endregion

num1=0.0
num2=0.0
ans=0.0

answer = Entry(root, text="nothing", width = 55, bg="white")
answer.grid(row=0, column=0, columnspan=5)

def buttonClick(number):
    # answer.delete(0, END)
    # answer.insert(0, "number")
    i=0
    i = i + 1
    iStr = str(i)
    print("Hello WOrld!" + iStr)

#region Creating the Buttons
button1 = Button(root, text="1", width = 12, bg="#D3D3D3", command=buttonClick(1))
button2 = Button(root, text="2", width = 12, bg="#D3D3D3", command=buttonClick(2))
button3 = Button(root, text="3", width = 12, bg="#D3D3D3", command=buttonClick(3))
button4 = Button(root, text="4", width = 12, bg="#D3D3D3", command=buttonClick(4))
button5 = Button(root, text="5", width = 12, bg="#D3D3D3", command=buttonClick(5))
button6 = Button(root, text="6", width = 12, bg="#D3D3D3", command=buttonClick(6))
button7 = Button(root, text="7", width = 12, bg="#D3D3D3", command=buttonClick(7))
button8 = Button(root, text="8", width = 12, bg="#D3D3D3", command=buttonClick(8))
button9 = Button(root, text="9", width = 12, bg="#D3D3D3", command=buttonClick(9))
button0 = Button(root, text="0", width=12, bg="#D3D3D3", command=buttonClick(0))
buttonDot = Button(root, text=".", width=12, bg="#D3D3D3", command=buttonClick(0))
buttonClear = Button(root, text="Clear", width=55, bg="#D3D3D3", command=buttonClick(0))
buttonMul = Button(root, text="x", width=12, bg="#D3D3D3", command=buttonClick(0))
buttonDiv = Button(root, text="%", width=12, bg="#D3D3D3", command=buttonClick(0))
buttonAdd = Button(root, text="+", width=12, bg="#D3D3D3", command=buttonClick(0))
buttonSub = Button(root, text="-", width=12, bg="#D3D3D3", command=buttonClick(0))
buttonEqu = Button(root, text="=", width=12, bg="#D3D3D3", command=buttonClick(0))

#endregion

#region Showing the Buttons
button1.grid(row=3, column=1)
button2.grid(row=3, column=2)
button3.grid(row=3, column=3)
button4.grid(row=2, column=1)
button5.grid(row=2, column=2)
button6.grid(row=2, column=3)
button7.grid(row=1, column=1)
button8.grid(row=1, column=2)
button9.grid(row=1, column=3)
button0.grid(row=4, column=1)
buttonDot.grid(row=4, column=2)
buttonClear.grid(row=5, column=0, columnspan=5)
buttonMul.grid(row=3, column=4)
buttonDiv.grid(row=4, column=4)
buttonAdd.grid(row=1, column=4)
buttonSub.grid(row=2, column=4)
buttonEqu.grid(row=4, column=3)

#endregion

root.mainloop()