from lib2to3.pgen2.pgen import DFAState
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
label.grid(row=3, column=0)
# label_value = ''

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
        numOfDigits = int(math.log10(cardNumber) + 1)
        if(numOfDigits >= 13 and numOfDigits <= 16):
            validate(cardNumber, int(numOfDigits))
        else:
            label.config(text='')
            messagebox.showerror('Invalid card number', 'Valid card number must contain between 13 and 16 digits')

    else: 
        label.config(text='')
        messagebox.showerror('Wrong input', 'Card number must contain digits only')
        


def doChecksum(cardNumber):
    cardNumberIterable = [int(n) for n in str(cardNumber)]
    products = []
    sumEven = 0
    sumOdd = 0

    for index, num in enumerate(reversed(cardNumberIterable)):
     
        if (index % 2 == 1 and index != 0):
            products.append(num * 2)
        else:
            sumOdd += num
    for n in products:
        if(n > 9):
            toSingleDigits = [int(m) for m in str(n)]
            sumEven += toSingleDigits[0]
            sumEven += toSingleDigits[1]
        else:
            sumEven += n
   
    return ((sumEven + sumOdd) % 10 == 0)


def validate(cardNumber, numOfDigits):
    cardType = ''

    if (numOfDigits == 13 and int(cardNumber / 1000000000000 == 4)):
        cardType = 'Visa'
        

    if (numOfDigits == 15 and (int(cardNumber / 10000000000000) == 34 or int(cardNumber / 10000000000000) == 37)):
        cardType = 'American Express'
    if (numOfDigits == 16):
        typeNumber = int(cardNumber / 100000000000000)
        masterCard = [51, 52, 53, 54, 55]

        for num in masterCard:
            if(num == typeNumber):
                cardType = 'MasterCard'
                
        
        if (cardType == '' and int(cardNumber / 1000000000000000) == 4):
            cardType = 'Visa'

    if(doChecksum(cardNumber) and cardType != ''):
        label.config(text=cardType)
   

 
#Buttons
btn_validate = Button(app, text='Validate', width=20, command=checkType)
btn_validate.grid(row=2, column=0)

# Start program
app.mainloop()