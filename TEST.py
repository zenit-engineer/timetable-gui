import csv
from tkinter import *
root = Tk()
root.geometry('900x400')
top = Toplevel(root,bg='orange')

top.title('Error message box')
x_position = 330
y_position = 486
top.geometry(f"340x140+{x_position}+{y_position}")
l1 = Label(top, text="Please fullfill the area", bg="green", fg="white", height=50, width=50)
l1.place(x = 335, y = 490)

def save():
    textbox = text1.get("1.0",END)
    with open('timetable.csv', 'w', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(textbox)

button4 = Button(root, text = 'Save',command = save)
button4.place(x = 250, y = 140)
text1 = Text(root,height=4,width=30,bg='white',borderwidth=10)
text1.place(x = 10, y = 5)
entry1 = Entry(root,width = 35,)
entry1.place(x = 140, y=100)


root.mainloop()

