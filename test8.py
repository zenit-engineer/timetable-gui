import csv
from tkinter import *
root = Tk()
root.geometry('900x400')


def save():
    textbox = text1.get("1.0",END)
    with open('timetable.csv', 'w', encoding='utf-8') as f:
        writer = csv.writer(f, delimiter='.')
        writer.writerow(textbox)

button4 = Button(root, text = 'Save',command = save)
button4.place(x = 250, y = 140)
text1 = Text(root,height=4,width=30,bg='white',borderwidth=10)
text1.place(x = 10, y = 5)


root.mainloop()

