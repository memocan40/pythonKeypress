from tkinter import *

def pressPlay():
   print("Pressed")

master = Tk()
Label(master, text="Key to Press").grid(row=0)
Label(master, text="Key been Pressed").grid(row=1)

e1 = Entry(master)
e2 = Label(master,text="Test")

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

Button(master, text='Quit', command=master.quit).grid(row=3, column=0, sticky=W, pady=4)
Button(master, text='Show', command=pressPlay).grid(row=3, column=1, sticky=W, pady=4)

mainloop()