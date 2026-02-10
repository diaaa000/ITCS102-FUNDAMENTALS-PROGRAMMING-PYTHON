import tkinter as tktr

window = tktr.Tk()

window.title("mi propayl")

window.geometry("600x600")

window.resizable(False,True)

window.configure(bg="light blue",cursor="arrow")

label = tktr.Label(window,text="My Student Profile",font = ("Sitka Text","20","bold"),fg = "Black",bg = "cyan",anchor = "center")

label.pack(padx=10,pady=30)

label = tktr.Label(window,text="Name: Princess Diane B. Salumbides",font = ("MS Serif","15","bold"),fg = "Black",bg = "light blue")

label.pack(padx=10,anchor = "w")

label = tktr.Label(window,text="Age: 19",font = ("MS Serif","15","bold"),fg = "Black",bg = "light blue")

label.pack(padx=10,anchor = "w")

label = tktr.Label(window,text="Course and Section: BSIT 1A",font = ("MS Serif","15","bold"),fg = "Black",bg = "light blue")

label.pack(padx=10,anchor = "w")

label = tktr.Label(window,text="Birthday: December 24, 2006",font = ("MS Serif","15","bold"),fg = "Black",bg = "light blue")

label.pack(padx=10,anchor = "w")

label = tktr.Label(window,text="Personal Motto or Quote: Be the change you wish to see.",font = ("MS Serif","15","bold"),fg = "Black",bg = "light blue")

label.pack(padx=10,anchor = "w")

window.mainloop()