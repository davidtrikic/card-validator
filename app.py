# from cgi import test
from tkinter import *
# from turtle import width


def validate():
    print(number_entry_value.get())
    label.config(text=label_value)

def removePlaceholder(*args):
    number_entry.delete(0, 'end')

# Create window object
app = Tk()

# Set geometry
app.resizable(False, False)
# app.geometry('400x200')
app.title('Credit Card Validator')


# Number entry
number_entry_value = StringVar()
number_entry = Entry(app, textvariable=number_entry_value, width=40)
number_entry.insert(0,'Enter card number...')
number_entry.bind("<Button-1>", removePlaceholder)
number_entry.grid(row=0, column=0)
 
#Buttons
btn_validate = Button(app, text='Validate', width=20, command=validate)
btn_validate.grid(row=1, column=0)

# Label
label = Label(app, text='', font=('bold', 16), pady=20)
label.grid(row=2, column=0)
label_value = 'asdfasd'


# Start program
app.mainloop()