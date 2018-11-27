from tkinter import ttk
import tkinter as tk
from tkinter import scrolledtext
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
# Radiobutton Globals # 1
COLOR1 = "Blue" # 2
COLOR2 = "Gold" # 3
COLOR3 = "Red" # 4
# Radiobutton Callback # 5
def radCall(): # 6
 radSel=radVar.get()
 if radSel == 1: win.configure(background=COLOR1)
 elif radSel == 2: win.configure(background=COLOR2)
 elif radSel == 3: win.configure(background=COLOR3)
# create three Radiobuttons # 7
radVar = tk.IntVar() # 8
rad1 = tk.Radiobutton(win, text=COLOR1, variable=radVar, value=1,
command=radCall) # 9
rad1.grid(column=0, row=5, sticky=tk.W) # 10
rad2 = tk.Radiobutton(win, text=COLOR2, variable=radVar, value=2, command=radCall) # 11
rad2.grid(column=1, row=5, sticky=tk.W) # 12
rad3 = tk.Radiobutton(win, text=COLOR3, variable=radVar, value=3, command=radCall) # 13
rad3.grid(column=2, row=5, sticky=tk.W) # 14
scrolW = 30 # 4
scrolH = 3
scr = scrolledtext.ScrolledText(win, width=scrolW, height=scrolH,
wrap=tk.WORD) # 6
scr.grid(column=0, columnspan=3) # 7
win.mainloop()