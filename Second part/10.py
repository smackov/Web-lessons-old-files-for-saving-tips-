from tkinter import *

root = Tk()
root.geometry('600x400')

#
# class Buttons:
#
#     def __init__(self, master, name, row, column):
#         self.master = master
#         self.name = name
#         self.row = row
#         self.column = column
#         self.b = Button(master, text=name, padx=10, pady=5)
#         self.b.grid(row=row, column=column)
#
#
# f = Frame(root)
# f.pack()
#
# number = 9
# row = 0
# column = -1
# while number >= 0:
#     if column == 2:
#         row += 1
#         column = -1
#     column += 1
#     Buttons(f, number, row, column)
#     number -= 1

# btn7 = Button(f, text='7', padx=10, pady=5).grid(row=0, column=0)
# btn8 = Button(f, text='8', padx=10, pady=5).grid(row=0, column=1)
# btn9 = Button(f, text='9', padx=10, pady=5).grid(row=0, column=2)
#
# btn4 = Button(f, text='4', padx=10, pady=5).grid(row=1, column=0)
# btn5 = Button(f, text='5', padx=10, pady=5).grid(row=1, column=1)
# btn6 = Button(f, text='6', padx=10, pady=5).grid(row=1, column=2)
#
# btn1 = Button(f, text='1', padx=10, pady=5).grid(row=2, column=0)
# btn2 = Button(f, text='2', padx=10, pady=5).grid(row=2, column=1)
# btn3 = Button(f, text='3', padx=10, pady=5).grid(row=2, column=2)
#
# btn0 = Button(f, text='0', padx=10, pady=5).grid(row=3, column=0, columnspan=3)


l_user = Label(root, text="Login:").grid(row=0, column=0, padx=10, pady=10, sticky=E)
e_user = Entry(root).grid(row=0, column=1, padx=10, sticky=W+E)

l_pass = Label(root, text="Password:").grid(row=1, column=0, padx=10, pady=10)
e_pass = Entry(root, show='*').grid(row=1, column=1, padx=10, sticky=W+E)

btn_login = Button(root, text='Sign in').grid(row=2, column=0, pady=10)
btn_reg = Button(root, text='Registration').grid(row=2, column=1)
btn_forgot = Button(root, text='Forgot password?').grid(row=2, column=2)



root.mainloop()
