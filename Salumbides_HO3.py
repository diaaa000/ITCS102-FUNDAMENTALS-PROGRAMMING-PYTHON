import tkinter as tktr

window = tktr.Tk()
window.title("Simple Calculator")
window.geometry("350x250")
window.resizable(True, True)
window.configure(bg = "lightpink",cursor="arrow")

def get_numbers():
    numbah1 = int(entry1.get())
    numbah2 = int(entry2.get())
    return numbah1, numbah2

def add():
    n1, n2 = get_numbers()
    label_result.config(text=f"The sum of {n1} + {n2} is {n1+n2}", bg = "pale violet red")

def subtract():
    n1, n2 = get_numbers()
    label_result.config(text=f"The difference of {n1} - {n2} is {n1-n2}", bg = "pale violet red")

def multiply():
    n1, n2 = get_numbers()
    label_result.config(text=f"The product of {n1} x {n2} is {n1*n2}", bg = "pale violet red")

def divide():
    n1, n2 = get_numbers()
    if n2 != 0:
        label_result.config(text=f"The quotient of {n1} ÷ {n2} is {n1/n2}", bg = "pale violet red")
    else:
        label_result.config(text="Cannot divide by zero", bg = "pale violet red")

label_result = tktr.Label(window, text="CALCULATOR", font=("Arial", 12), bg = "pale violet red")
label_result.grid(row=0, column=0, columnspan=2, pady=10)

tktr.Label(window, text="Enter 1st Number:", bg = "pale violet red").grid(row=1, column=0, padx=10, pady=5)
entry1 = tktr.Entry(window)
entry1.grid(row=1, column=1, padx=10)

tktr.Label(window, text="Enter 2nd Number:", bg = "pale violet red").grid(row=2, column=0, padx=10, pady=5)
entry2 = tktr.Entry(window)
entry2.grid(row=2, column=1, padx=10)

tktr.Button(window, text="Add", bg = "thistle",activebackground = "medium purple",width=10, command=add).grid(row=3, column=0, pady=5)
tktr.Button(window, text="Subtract", bg = "thistle",activebackground = "medium purple", width=10, command=subtract).grid(row=3, column=1, pady=5)
tktr.Button(window, text="Multiply",bg = "thistle",activebackground = "medium purple", width=10, command=multiply).grid(row=4, column=0, pady=5)
tktr.Button(window, text="Division",bg = "thistle",activebackground = "medium purple", width=10, command=divide).grid(row=4, column=1, pady=5)

window.mainloop()