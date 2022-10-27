import time
from tkinter import *
import threading

def checkloop(param):
    if param == "Stop":
        print(2)
a = 'Stop'
def pressPlay():
   global e2,e1,a
   e2.config(text=e1.get()) 
   if a == "Stop":
    a='Start'
   else:
    a='Stop' 
def pressStop():
    global e2,e1
    e1.delete("0", "end")

thread = threading.Thread(target=checkloop(a))
#make test_loop terminate when the user exits the window
thread.daemon = True 
thread.start()
root = Tk()
root.title("PressButton")
Label(root, text="Key to Press").grid(row=0)
Label(root, text="Key been Pressed").grid(row=1)

e1 = Entry(root)
e2 = Label(root,text="Test")

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

Button(root, text='Stop', command=pressStop).grid(row=3, column=0, sticky=W, pady=4)
Button(root, text='Start', command=pressPlay).grid(row=3, column=1, sticky=W, pady=4)
root.mainloop()