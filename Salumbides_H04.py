import tkinter as tktr

window = tktr.Tk

window.title("Profile Builder")

window.geometry("500x500")

frim = tktr.Frame(window, bg = "lightpink")
frim.grid(row = 0, column = 1)

libel = tktr.Label(frim, text = "Profile Builder", font = ("Times New Roman", 15, "Bold"), bg = "lightpink")
libel.grid(row = 0, column = 1, columnspan = 3)

frm = tktr.Frame(window, bg = "lightgreen")
frm.grid(row = 1, column = 1, rowspan = 3)
 
fnim_entry = tktr.Entry(frm)
fnim_entry.grid(row = 0, column = 0, columnspan = 2)

lbl = tktr.Label(frm, text = "First Name", font = ("Arial", 12, "Itallic"))
lbl.grid(row = 1, column = 1, columnspan = 2)

mnim_entry = tktr.Entry(frm)
mnim_entry.grid(row = 0, column = 2, columnspan = 2)

libl = tktr.Label(frm, text = "Middle Name", font = ("Arial", 12, "Itallic"))
libl.grid()

lnim_entry = tktr.Entry(frm)
lnim_entry.grid()

leybel = tktr.Label(frm, text = "Last Name", font = ("Arial", 12, "Itallic"))
leybel.grid()

bort_entry = tktr.Entry(frm)
bort_entry.grid()

window.mainloop()


