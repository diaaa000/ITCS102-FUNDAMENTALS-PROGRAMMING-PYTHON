import tkinter as tktr

window = tktr.Tk()
window.title("Registration and Log In System")
window.geometry("300x200")
window.resizable(True,True)
window.config(bg = "plum")

def Registor():
    new = tktr.Toplevel(window)
    new.title("Register")
    new.geometry("200x200")
    new.resizable(True,True)
    new.config(bg = "green")

    leybel = tktr.Label(new, text = "Register", font = ("Arial", 11))
    leybel.grid(column = 0, row = 0, columnspan = 3, padx = 5, pady = 5)

    libel = tktr.Label(new, text = "Username:", font = ("Arial", 12), bg = "green")
    libel.grid(column = 0, row = 1)

    enturi = tktr.Entry(new)
    enturi.grid(column = 1, row = 1, columnspan = 2)

    leybl = tktr.Label(new, text = "Password:", font = ("Arial", 12), bg = "green")
    leybl.grid(column = 0, row = 2, padx = 5, pady = 5)

    entri = tktr.Entry(new, show = "*")
    entri.grid(column = 1, row = 2, columnspan = 2)

    cbt = tktr.Checkbutton(new, text = "See Password")
    cbt.grid(column = 0, row = 3, columnspan = 3, padx = 5, pady = 5)

    but = tktr.Button(new, text = "Register")
    but.grid(column = 0, row = 4, columnspan = 4)


def Login():
    ntw = tktr.Toplevel(window)
    ntw.title("Log In")
    ntw.geometry("200x200")
    ntw.resizable(True,True)
    ntw.config(bg = "red")

    leybel = tktr.Label(ntw, text = "Login", font = ("Arial", 11))
    leybel.grid(column = 0, row = 0, columnspan = 3, padx = 5, pady = 5)

    libel = tktr.Label(ntw, text = "Username:", font = ("Arial", 12), bg = "red")
    libel.grid(column = 0, row = 1)

    enturi = tktr.Entry(ntw)
    enturi.grid(column = 1, row = 1, columnspan = 2)

    leybl = tktr.Label(ntw, text = "Password:", font = ("Arial", 12), bg = "red")
    leybl.grid(column = 0, row = 2, padx = 5, pady = 5)

    entri = tktr.Entry(ntw, show = "*")
    entri.grid(column = 1, row = 2, columnspan = 2)

    cbt = tktr.Checkbutton(ntw, text = "See Password")
    cbt.grid(column = 0, row = 3, columnspan = 3, padx = 5, pady = 5)

    but = tktr.Button(ntw, text = "Login")
    but.grid(column = 0, row = 4, columnspan = 4)

lbl = tktr.Label(window, text = "Welcome!", font = ("Arial", 15, "bold"))
lbl.grid(column = 1, row = 0, columnspan = 3, padx = 5, pady = 5)

btn = tktr.Button(window, text = "Register", font = ("Arial", 15), bg = "blue", command = Registor)
btn.grid(column = 2, row = 1, columnspan = 3, padx = 5, pady = 5)

butn = tktr.Button(window, text = "Log In", font = ("Arial", 15), bg = "green", command = Login)
butn.grid(column = 0 , row = 2, columnspan = 4)

window.mainloop() 



