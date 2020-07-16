from tkinter import *
import time

root = Tk()
root.geometry('800x600')


def tick():
    watch.after(200, tick)
    watch['text'] = time.strftime('%H:%M:%S')


watch = Label(root, font='Arial 70')
watch.pack()
tick()

root.mainloop()
