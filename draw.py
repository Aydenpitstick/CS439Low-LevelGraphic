from tkinter import *

root = Tk()

C = Canvas(root, bg="blue", height=250, width=300)

eye1 = C.create_oval(50, 40, 110, 140, fill="black")

eye2 = C.create_oval(200, 40, 260, 140, fill="black")

mouth = C.create_arc(80, 100, 230, 240, start=0, extent= -180, fill="red")
C.pack()
mainloop()