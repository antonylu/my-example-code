"""
tkinter is Python's default tk GUI library interface
works with Linux, Windows and Mac

The example code shows a window with two Listboxs

"""
from tkinter import *  

# empty windows example
# top = Tk()

# Code to add widgets will go here...
# top.mainloop()


root = Tk()

li     = ['C','python','php','html','SQL','java']
movie  = ['CSS','jQuery','Bootstrap']
listb  = Listbox(root)
listb2 = Listbox(root)
for item in li:
    listb.insert(0,item)

for item in movie:
    listb2.insert(0,item)

listb.pack() # pack to root
listb2.pack()
root.mainloop()