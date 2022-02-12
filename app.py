from cgi import test
from tkinter import *

# Create window object
app = Tk()

# Label
test_text = StringVar()
test_label = Label(app, text='Name', font=('bold', 14), pady=20)
test_label.grid(row=0, column=0, sticky=W)

test_entry = Entry(app, textvariable=test_text)
test_entry.grid(row=0, column=1)

app.title('Test')
app.geometry('700x350')

# Start program
app.mainloop()