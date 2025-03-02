from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
import csv

#creating main window
root = Tk()
root.title('TIMETABLE')
root.configure(bg='cyan')

w = 900 # width for the Tk root
h = 400 # height for the Tk root
ws = root.winfo_screenwidth() #width of the screen
hs = root.winfo_screenheight() #height of the screen
x = (ws/2) - (w/2) #calculate x and y coordinates for the Tk root window
y = (hs/2) - (h/2) # these calculations in order to set window in centre of screen
# set the dimensions of the screen and where it is placed
root.geometry('%dx%d+%d+%d' % (w, h, x, y))

#creating an entry and text box
entry1 = Entry(root,width = 35)
entry1.place(x = 140, y=20)
text1 = Text(root,height=8,width=58,borderwidth=8)
text1.place(x = 400, y = 230)

# read_csv method reads and writes csv file
def read_all_csv():
    if entry1.get() == '':
        messagebox.showwarning('Error message box',
                               'Please fill the file path!', parent=root)
        entry1.focus_force()

    entry = entry1.get()           # removes the parenthesis of copied file
    new_string = entry.strip('"') # remove parentheses
    with open(new_string) as file: # reads csv file from computer
        csv_reader = csv.reader(file)
        with open('sampledata2.csv', 'w') as new_file: #creates new file within python folder
            csv_writer = csv.writer(new_file, delimiter='\t')
            for row in csv_reader:
                csv_writer.writerow(row)
    with open("sampledata2.csv", "r") as f: # writes csv file within GUI textbox
        data = f.read()
        text2.insert(END, data)


# delete() method deletes all text that is within the main text box
def delete():
   text1.delete("1.0","end")

# display_all method reads our csv file and than check all necessary conditions
def display_all():
    delete()
    with open('sampledata2.csv') as csv_file:
        csv_reader = csv.reader(csv_file,delimiter = '\t')
        rows = list(csv_reader)
    if entry2.get() == '' and combobox1.get() == '':
        messagebox.showwarning('Error message box',
                             'Please fill the Department and Year fields!', parent=root )
        entry1.focus_force()
    elif entry2.get() == '':
        messagebox.showwarning('Error message box',
                             'Please fill the Department path field!', parent=root)
        entry1.focus_force()
    elif combobox1.get() == '':
        messagebox.showwarning('Error message box',
                             'Please fill Year field!', parent=root)
        entry1.focus_force()

    # these elif conditions checks program and semester and displays within box appropriate additional info.
    # its a bit long code, it could be more simplified but for personal reasons a left it this way.
    elif (entry2.get() == 'CHI' or entry2.get() == 'chi' or entry2.get() == 'Chi' )and combobox1.get() == '1':
        text1.insert(END,rows[0])
    elif (entry2.get() == 'CS' or entry2.get() == 'cs' or entry2.get() == 'Cs') and combobox1.get() == '1':
        text1.insert(END,f'{rows[2]}\n{rows[4]}')
    elif (entry2.get() == 'CS' or entry2.get() == 'cs' or entry2.get() == 'Cs') and combobox1.get() == '2':
        text1.insert(END,f'{rows[6]}\n{rows[8]}\n{rows[10]}\n{rows[12]}\n{rows[14]}')
    elif (entry2.get() == 'ECE' or entry2.get() == 'ece' or entry2.get() == 'Ece') and combobox1.get() == '3':
        text1.insert(END,f'{rows[16]}\n{rows[18]}\n{rows[20]}\n{rows[22]}\n{rows[24]}\n{rows[26]}\n{rows[28]}\n{rows[30]}\n{rows[32]}\n{rows[34]}\n{rows[36]}\n{rows[38]}')
    elif (entry2.get() == 'ECON' or entry2.get() == 'econ' or entry2.get() == 'Econ') and combobox1.get() == '1':
        text1.insert(END,f'{rows[40]}')
    elif (entry2.get() == 'EE' or entry2.get() == 'ee' or entry2.get() == 'Ee') and combobox1.get() == '1':
        text1.insert(END,f'{rows[42]}')
    elif (entry2.get() == 'EE' or entry2.get() == 'ee' or entry2.get() == 'Ee') and combobox1.get() == '2':
        text1.insert(END,f'{rows[44]}\n{rows[46]}\n{rows[48]}\n{rows[50]}\n{rows[52]}')
    elif (entry2.get() == 'EECS' or entry2.get() == 'eecs' or entry2.get() == 'Eecs') and combobox1.get() == '1':
        text1.insert(END,f'{rows[54]}\n{rows[56]}\n{rows[58]}\n{rows[60]}')
    elif (entry2.get() == 'EECS' or entry2.get() == 'eecs' or entry2.get() == 'Eecs') and combobox1.get() == '2':
        text1.insert(END,f'{rows[62]}\n{rows[64]}\n{rows[66]}\n{rows[68]}\n{rows[70]}\n{rows[72]}\n{rows[74]}\n{rows[76]}')
    elif (entry2.get() == 'ENGR' or entry2.get() == 'engr' or entry2.get() == 'Engr') and combobox1.get() == '1':
        text1.insert(END,f'{rows[78]}\n{rows[80]}\n{rows[82]}\n{rows[84]}\n{rows[86]}\n{rows[88]}\n{rows[90]}\n{rows[92]}\n{rows[94]}\n{rows[96]}')
    elif (entry2.get() == 'ENGR' or entry2.get() == 'engr' or entry2.get() == 'Engr') and combobox1.get() == '2':
        text1.insert(END,f'{rows[96]}\n{rows[98]}')
    elif (entry2.get() == 'FRE' or entry2.get() == 'fre' or entry2.get() == 'Fre') and combobox1.get() == '1':
        text1.insert(END,f'{rows[100]}\n{rows[102]}\n{rows[104]}')
    elif (entry2.get() == 'GER' or entry2.get() == 'ger' or entry2.get() == 'Ger') and combobox1.get() == '1':
        text1.insert(END,f'{rows[106]}\n{rows[108]}\n{rows[110]}\n{rows[112]}')
    elif (entry2.get() == 'IE' or entry2.get() == 'ie' or entry2.get() == 'Ie') and combobox1.get() == '1':
        text1.insert(END,f'{rows[114]}')
    elif (entry2.get() == 'IE' or entry2.get() == 'ie' or entry2.get() == 'Ie') and combobox1.get() == '2':
        text1.insert(END,f'{rows[116]}\n{rows[118]}\n{rows[120]}\n{rows[122]}\n{rows[124]}\n{rows[126]}\n{rows[128]}\n{rows[130]}')
    elif (entry2.get() == 'ISE' or entry2.get() == 'ise' or entry2.get() == 'Ise') and combobox1.get() == '3':
        text1.insert(END,f'{rows[132]}\n{rows[134]}\n{rows[136]}\n{rows[138]}\n{rows[140]}\n{rows[142]}\n{rows[144]}\n{rows[146]}')
    elif (entry2.get() == 'LIFE' or entry2.get() == 'life' or entry2.get() == 'Life') and combobox1.get() == '1':
        text1.insert(END,f'{rows[148]}\n{rows[150]}')
    elif (entry2.get() == 'MATH' or entry2.get() == 'math' or entry2.get() == 'Math') and combobox1.get() == '1':
        text1.insert(END,f'{rows[152]}\n{rows[154]}\n{rows[156]}\n{rows[158]}')
    elif (entry2.get() == 'MGT' or entry2.get() == 'mgt' or entry2.get() == 'Mgt') and combobox1.get() == '1':
        text1.insert(END,f'{rows[160]}\n{rows[162]}\n{rows[164]}\n{rows[166]}\n{rows[168]}')
    elif (entry2.get() == 'MGT' or entry2.get() == 'mgt' or entry2.get() == 'Mgt') and combobox1.get() == '2':
        text1.insert(END,f'{rows[170]}\n{rows[172]}\n{rows[174]}\n{rows[176]}\n{rows[178]}\n{rows[180]}\n{rows[182]}')
    elif (entry2.get() == 'UNI' or entry2.get() == 'uni' or entry2.get() == 'Uni') and combobox1.get() == '1':
        text1.insert(END,f'{rows[184]}\n{rows[186]}\n{rows[188]}\n{rows[190]}\n{rows[192]}\n{rows[194]}\n{rows[196]}')


# clear_all() clears all text within the textbox
def clear_all():
    text1.delete("1.0", "end")

# save() saves text from text box within a new csv file
def save():
    textbox = text1.get("1.0",'end-1c')
    with open('timetable.csv', 'w', encoding='utf-8') as f:
        writer = csv.writer(f)
        for row in textbox:
            writer.writerow(textbox)

# this method shows error in case of a blank field
def something():
    if entry1.get() == '':
        messagebox.showwarning('Error message box',
                             'Please fill the blank field', parent=root)
        entry1.focus_force()

# creation of buttons, labels and text boxes
button1 = Button(root, text = 'Enter the file path:',command=read_all_csv)
button1.place(x = 5, y = 20)
label1 = Label(root, text = 'Year:')
label1.place(x=80,y=70)
label2 = Label(root,text = 'Department:')
label2.place(x=286,y=70)
entry2 = Entry(root,width = 55)
entry2.place(x = 380, y=70)
button2 = Button(root, text = 'Display', command = display_all)
button2.place(x = 50, y = 140)
button3 = Button(root, text = 'Clear',command=clear_all)
button3.place(x = 150, y = 140)
button4 = Button(root, text = 'Save',command = save)
button4.place(x = 250, y = 140)
label3 = Label(root,text = 'Courses Available:')
label3.place(x =5, y = 200)
label4 = Label(root,text = 'Courses:')
label4.place(x =400, y = 200)
#canvas = Canvas(root,bg='orange',height=145,width=350)
#canvas.place(x=5,y=230)
text2 = Text(root,height=8,width=45,borderwidth=8,bg='yellow')
text2.place(x = 10, y = 230)

#creating first combobox in order to select year of studies
n = StringVar()
combobox1 = Combobox(root,width=2,textvariable=n)
combobox1['values'] = ('1','2','3','4')
combobox1.place(x=140, y=70)

root.mainloop()