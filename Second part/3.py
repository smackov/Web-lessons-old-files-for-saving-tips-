from tkinter import *
import time

root = Tk()  # object
root.title('Counter')
root.iconbitmap('python.ico')  # ico image
root.geometry('600x400+500+300')  # window's size and place


def check_time():
    btn_time['text'] = time.strftime('%H:%M:%S')

clicks = 0
def counter():
    global clicks
    clicks += 1
    root.title(f'Counter: {clicks}')

btn_time = Button(root, text="Check time", command=check_time)
btn_time.pack()

btn_cnt = Button(root, text="Counter", command=counter)
btn_cnt.pack()

root.mainloop()  # mainloop (cycle)