from tkinter import *

win = Tk()
win.title('My First Py Layout')
win.geometry("640x480")

top = Frame(win, height=200, background='yellow')
top.pack(side=TOP, expand=False, fill=BOTH)
left = Frame(win, height=500, width=200, background="red")
left.pack(side=LEFT, expand=False, fill=BOTH)
right = Frame(win, height=500, width=200, background="green")
right.pack(side=RIGHT, expand=False, fill=BOTH)
btn = Frame(win, height=200, background="blue")
grd = Frame(btn, background="white")
Button(grd, text="SCP-001").grid(row=1, column=1)
Button(grd, text="SCP-002").grid(row=3, column=1)
Button(grd, text="SCP-003").grid(row=4, column=1)
Button(grd, text="SCP-004").grid(row=5, column=1)
Button(grd, text="SCP-005").grid(row=6, column=1)
Button(grd, text="SCP-006").grid(row=7, column=1)
Button(grd, text="SCP-007").grid(row=8, column=1)
Button(grd, text="SCP-008").grid(row=9, column=1)
Button(grd, text="SCP-009").grid(row=1, column=1)
grd.pack
btn.pack(side=BOTTOM, expand=False, fill=BOTH)
Label(win, text="Jestem wolnym elektronem", background='pink').place(x=13, y=13, height="64")
mainloop()