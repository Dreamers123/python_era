from tkinter import *
root = Tk()
def printName(event):
    print("Chello my name is Abeer")
button_1 = Button(root, text="Print Message")
button_1.bind("<Button-1>",printName)
button_1.pack()
root.mainloop()