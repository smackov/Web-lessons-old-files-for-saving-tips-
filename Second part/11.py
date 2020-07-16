from tkinter import *

root = Tk()
root.geometry('600x400')

# l1 = Label(root, text='Hello world?', bg='#3498db', fg='#fff', font='16',
#            padx=20, pady=8)
# l1.place(x=10, y=100)
#
# l2 = Label(root, text='Hello world?', bg='#3498db', fg='#fff', font='16',
#            padx=20, pady=8)
# l2.place(relx=0.5, rely=0.5, anchor=CENTER)

# btn1 = Button(text='Button 1', bg='#3498db', fg='#fff', font='16',
#               padx=20, pady=8)
# btn1.place(x=0, y=0)
#
# btn1 = Button(text='Button 1', bg='#3498db', fg='#fff', font='16',
#               padx=20, pady=8)
# btn1.place(relx=0.5, rely=0.5, anchor=CENTER)
#
# btn1 = Button(text='Button 1', bg='#3498db', fg='#fff', font='16',
#               padx=20, pady=8)
# btn1.place(relx=1, rely=1, anchor='se')

l1 = Label(root, bg='black')
l1.place(relx=0.5, rely=0.5, anchor=CENTER, relheight=0.8, relwidth=0.8)


root.mainloop()
