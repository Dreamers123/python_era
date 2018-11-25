from tkinter import ttk
import tkinter as tk
win = tk.Tk() # 2 Create instance
win.title("Python GUI")
ttk.Label(win, text="Enter a name:").grid(column=0, row=0) # 1
ttk.Label(win, text="Choose a number:").grid(column=1, row=0) # 1
def clickMe(): # 5
 action.configure(text='Hello ' + name.get() + ' ' + numberChosen.get())
 #action.configure(text='Hello ' + name.get() ,state='disabled')
 action.grid(column=3, row=1)
number = tk.StringVar() # 2
numberChosen = ttk.Combobox(win, width=12, textvariable=number,state='readonly') #3
numberChosen['values'] = (1, 2, 4, 42, 100) # 4
numberChosen.grid(column=1, row=1) # 5
numberChosen.current(0)
name = tk.StringVar() # 6
nameEntered = ttk.Entry(win, width=12, textvariable=name) # 7
nameEntered.grid(column=0, row=1) # 8
action = ttk.Button(win, text="Click Me!", command=clickMe) # 7
action.grid(column=2, row=1)

chVarDis = tk.IntVar()
check1 = tk.Checkbutton(win, text="Disabled", variable=chVarDis, state='disabled')
check1.select()
check1.grid(column=0, row=4, sticky=tk.W)
chVarUn = tk.IntVar()
check2 = tk.Checkbutton(win, text="UnChecked", variable=chVarUn)
check2.deselect()
check2.grid(column=1, row=4, sticky=tk.W)

chVarEn = tk.IntVar()
check3 = tk.Checkbutton(win, text="Enabled", variable=chVarEn)
check3.deselect()
check3.grid(column=2, row=4, sticky=tk.W)


win.mainloop()