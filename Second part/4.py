from tkinter import *

root = Tk()  # object
root.iconbitmap('python.ico')  # ico image
root.geometry('600x400+500+300')  # window's size and place

# l = Label(root, text="Text in 1 line\n1 line\n2 line\n3 line\n",
#           bg="#171", fg='#fff', font=("Comic Sans", 12),
#           justify=LEFT, anchor=W, width=50, height=20)
# l.pack()

img = PhotoImage(file='pt.png')
l_logo = Label(root, image=img)
l_logo.pack()

root.mainloop()  # mainloop (cycle)