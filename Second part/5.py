from tkinter import *

root = Tk()  # object
root.iconbitmap('python.ico')  # ico image
root.geometry('600x400+500+300')  # window's size and place


def add_str():
    e.insert(END, 'Hello!')


def del_str():
    e.delete(0, END)


def get_str():
    l_text['text'] = e.get()


l = Label(root, text="Entery:")
l.pack()

e = Entry(root, show="*")
e.insert(0, 'Hello')
e.insert(END, ' world')
e.pack()

btn_add = Button(root, text='Add', command=add_str).pack()
btn_del = Button(root, text='Delete', command=del_str).pack()
btn_get = Button(root, text='Get', command=get_str).pack()

l_text = Label(root, text="Entery:", bg='#101', fg='white')
l_text.pack(fill=X)

root.mainloop()  # mainloop (cycle)