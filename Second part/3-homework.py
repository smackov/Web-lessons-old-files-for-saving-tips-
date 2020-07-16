from tkinter import *

root = Tk()
root.title('Start!')
root.geometry("400x500+500+500")

a = 10
b = 5


def sum():
    print(a + b)


def division():
    print(a / b)


def multiple():
    print(a * b)


btn_sum = Button(root, text='Sum', command=sum)
btn_div = Button(root, text='Sum', command=division)
btn_mult = Button(root, text='Sum', command=multiple)

btn_sum.pack()
btn_div.pack()
btn_mult.pack()

root.mainloop()
