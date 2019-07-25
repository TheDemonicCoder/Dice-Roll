import tkinter
import random

m = tkinter.Tk()

m.title("Roll Dice")
m.geometry("250x250")

click = tkinter.Label(m, text="Click to roll dice", font = ('Comic Sans MS', 12))
click.pack()

def disp():
    l2.config(text=random.randint(1, 6))

b = tkinter.Button(m, text="Click", font = ('Comic Sans MS', 12), pady = 2, command = disp)
b.pack()

l1 = tkinter.Label(m,pady = 2, width = 3, wraplength = 1)
l1.pack()
l2 = tkinter.Label(m, text="0", pady = 10, bg = "blue", width = 7, font = ('Comic Sans MS', 18))
l2.pack()

m.mainloop()