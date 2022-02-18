import math
from tkinter import *
from tkinter import messagebox


# Create window object
app = Tk()

# Set geometry
app.resizable(False, False)
# app.geometry('400x200')
app.title('Credit Card Validator')

# Label
label = Label(app, text='', font=('bold', 16), pady=20)
label.grid(row=2, column=0)
label_value = ''

# Number entry
def removePlaceholder(*args):
    number_entry.delete(0, 'end')
number_entry_value = StringVar()
number_entry = Entry(app, textvariable=number_entry_value, width=40)
number_entry.insert(0,'Enter card number...')
number_entry.bind("<Button-1>", removePlaceholder)
number_entry.grid(row=0, column=0)


def checkType():

    cardNumber = number_entry_value.get()
   
    if(cardNumber.isdigit()):
        cardNumber = int(cardNumber)
        numOfDigits = math.log10(cardNumber) + 1
        if(numOfDigits >= 13 and numOfDigits <= 16):
            validate()
        else:
            messagebox.showerror('Invalid card number', 'Valid card number must contain between 13 and 16 digits')

    else: 
        messagebox.showerror('Wrong input', 'Card number must contain digits only')


def validate():
    label.config(text='validating card...')
   

 
#Buttons
btn_validate = Button(app, text='Validate', width=20, command=checkType)
btn_validate.grid(row=1, column=0)

# Start program
app.mainloop()