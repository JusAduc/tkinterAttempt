from tkinter import *

root = Tk()
root.title("Simple Calculator")
global i
i = 0

answer = Entry(root, text="nothing", width = 55, bg="white")
answer.grid(row=0, column=0, columnspan=5)

#region Button Click Functions
def buttonClick(number):
    answer.insert("end", number)

def buttonClickEqu():
    num2Str = answer.get()
    global num2
    global ans
    global num1
    num2 = float(num2Str)
    print(num2)
    answer.delete(0, END)
    if equation =="add":
        ans = num1 + num2
        answer.insert("end", ans)
    elif equation == "sub":
        ans = num1 - num2
        answer.insert("end", ans)
    elif equation == "div":
        ans = num1 / num2
        answer.insert("end", ans)
    elif equation == "mul":
        ans = num1 * num2
        answer.insert("end", ans)
    num1 = ans

    print(f"Number 1: {num1}")
    print(f"Number 2: {num2}")
    print(f"Answer: {ans}")

def numberStringToInt():
    num1Str = answer.get()
    global num1
    global i
    i = i + 1
    print(i)
    if i>=2:
        buttonClickEqu()
    num1 = float(num1Str)
    answer.delete(0, END)

def buttonClickAdd():
    numberStringToInt()
    global equation
    equation = "add"

def buttonClickSub():
    numberStringToInt()
    global equation
    equation = "sub"

def buttonClickMul():
    numberStringToInt()
    global equation
    equation = "mul"

def buttonClickDiv():
    numberStringToInt()
    global equation
    equation = "div"

def buttonClickClear():
    global num1
    global num2
    global ans
    num1=0.0
    num2=0.0
    ans=0.0
    answer.delete(0, END)

def buttonClickDot():
    answer.insert("end", ".")

#endregion

#region Creating the Buttons
button1 = Button(root, text="1", width = 12, bg="#D3D3D3", command= lambda : buttonClick(1))
button2 = Button(root, text="2", width = 12, bg="#D3D3D3", command= lambda : buttonClick(2))
button3 = Button(root, text="3", width = 12, bg="#D3D3D3", command= lambda : buttonClick(3))
button4 = Button(root, text="4", width = 12, bg="#D3D3D3", command= lambda : buttonClick(4))
button5 = Button(root, text="5", width = 12, bg="#D3D3D3", command= lambda : buttonClick(5))
button6 = Button(root, text="6", width = 12, bg="#D3D3D3", command= lambda : buttonClick(6))
button7 = Button(root, text="7", width = 12, bg="#D3D3D3", command= lambda : buttonClick(7))
button8 = Button(root, text="8", width = 12, bg="#D3D3D3", command= lambda : buttonClick(8))
button9 = Button(root, text="9", width = 12, bg="#D3D3D3", command= lambda : buttonClick(9))
button0 = Button(root, text="0", width=12, bg="#D3D3D3", command= lambda : buttonClick(0))
buttonDot = Button(root, text=".", width=12, bg="#D3D3D3", command=buttonClickDot)
buttonClear = Button(root, text="Clear", width=55, bg="#D3D3D3", command=buttonClickClear)
buttonMul = Button(root, text="x", width=12, bg="#D3D3D3", command=buttonClickMul)
buttonDiv = Button(root, text="%", width=12, bg="#D3D3D3", command=buttonClickDiv)
buttonAdd = Button(root, text="+", width=12, bg="#D3D3D3", command=buttonClickAdd)
buttonSub = Button(root, text="-", width=12, bg="#D3D3D3", command=buttonClickSub)
buttonEqu = Button(root, text="=", width=12, bg="#D3D3D3", command=buttonClickEqu)

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
