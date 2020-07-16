from tkinter import *

root = Tk()
root.title("Радуга")
root.geometry('220x220')
root.resizable(False, False)


colors = {
    "#ff0000": "Red",
    "#ff7d00": "Orange",
    "#ffff00": "Yellow",
    "#00ff00": "Green",
    "#007dff": "Blue",
    "#0000ff": "Dark Blue",
    "#7d00ff": "Violet",
}


class MyButtons:

    def __init__(self, master, text_color, hex_color):
        self.text_color = text_color
        self.hex_color = hex_color
        self.b = Button(root, bg=hex_color, command=self.get_color)
        self.b.pack(fill=X)


    def get_color(self):
        e_code_color.delete(0, END)
        e_code_color.insert(0, self.hex_color)
        l_name_color['text'] = self.text_color


l_name_color = Label(root, text="Color")
l_name_color.pack(fill=X)

e_code_color = Entry(root, justify=CENTER)
e_code_color.pack(fill=X)

for k, v in colors.items():
    MyButtons(root, v, k)

root.mainloop()