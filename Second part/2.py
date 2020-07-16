from tkinter import *
from tkinter import ttk

root = Tk()
root.geometry('600x400+500+300')


def clicked():
    print('Clicked')


btn = Button(root, text="Button\n2Line2line2", activebackground='#171',
             activeforeground="#099", font=("Arial", 20),
             justify=LEFT)
btn.pack()
btn.configure(width=10, height=5)
btn['font'] = 'Arial 12'

btn2 = ttk.Button(root, text='Button', command=clicked)
btn2.pack()


root.mainloop()  # mainloop (cycle)
