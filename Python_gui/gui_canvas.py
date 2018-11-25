from tkinter import *
root = Tk()
canvas = Canvas(root, width=200, height=100)
canvas.pack()
blackLine = canvas.create_line(0, 0, 200, 50)
redLine = canvas.create_line(0, 100, 200, 50, fill="red")
greenBox = canvas.create_rectangle(10, 40, 130, 60, fill="green")
##canvas.delete(redLine)
##canvas.delete(ALL)

##photo = PhotoImage(file="banana.png")
##label = Label(root, image=photo)
##label.pack()

root.mainloop()