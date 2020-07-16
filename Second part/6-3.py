from tkinter import *

root = Tk()
root.title("Радуга")
root.geometry('220x220')
root.resizable(False, False)


def get_color(text_color, hex_color):
    e_code_color.delete(0, END)
    e_code_color.insert(0, hex_color)
    l_name_color['text'] = text_color


colors = {
    "#ff0000": "Red",
    "#ff7d00": "Orange",
    "#ffff00": "Yellow",
    "#00ff00": "Green",
    "#007dff": "Blue",
    "#0000ff": "Dark Blue",
    "#7d00ff": "Violet",
}

l_name_color = Label(root, text="Color")
l_name_color.pack(fill=X)

e_code_color = Entry(root, justify=CENTER)
e_code_color.pack(fill=X)


for k, v in colors.items():
    Button(root, bg=k,
           command=lambda text=k, hex=v: get_color(text, hex)).pack(fill=X)

root.mainloop()
