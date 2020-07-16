from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import os
from datetime import datetime
from tkinter import ttk


def choose_dir():
    dir_path = filedialog.askdirectory()
    e_path.delete(0, END)
    e_path.insert(0, dir_path)


def f_start():
    cur_path = e_path.get()
    if cur_path:
        for folder, subfolders, files in os.walk(cur_path):
            for file in files:
                path = os.path.join(folder, file)
                mtime = os.path.getmtime(path)
                date = datetime.fromtimestamp(mtime)
                date = date.strftime('%Y-%m-%d')
                date_folder = os.path.join(cur_path, date)
                if not os.path.exists(date_folder):
                    os.mkdir(date_folder)
                os.rename(path, os.path.join(date_folder, file))
        messagebox.showinfo('Success', 'Sort has been successfuly complited')
        e_path.delete(0, END)
    else:
        messagebox.showwarning('Warning', 'Choose directory with photos')


root = Tk()
root.title('Photosort')
root.geometry('500x150')

s = ttk.Style()
s.configure('my.TButton', font=('Helvetica', 15))

frame = Frame(root, bg='#56ADFF', bd=5)
frame.pack(pady=10, padx=10, fill=X)

e_path = ttk.Entry(frame)
e_path.pack(side=LEFT, ipady=2, expand=1, fill=X)

btn_dialog = ttk.Button(frame, text='Choose directory', command=choose_dir)
btn_dialog.pack(side=LEFT, padx=10)

btn_start = ttk.Button(root, text='Start', style='my.TButton', command=f_start)
btn_start.pack(fill=X, padx=10)



root.mainloop()
