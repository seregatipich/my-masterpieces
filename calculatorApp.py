from tkinter import *
from decimal import *

root = Tk()
root.title('Calculator')

buttons = (('7', '8', '9', '/', '4'),
           ('4', '5', '6', '*', '4'),
           ('1', '2', '3', '-', '4'),
           ('0', '.', '=', '+', '4'))

dialedNumber = ''

list = []


def calculate():
    global list
    global label
    result = 0
    b = Decimal(list.pop())
    operation = list.pop()
    a = Decimal(list.pop())

    if operation == '+':
        result = a + b
    if operation == '-':
        result = a - b
    if operation == '*':
        result = a * b
    elif operation == '/':
        result = a / b
    label.configure(text=str(result))


def click(text):
    global dialedNumber
    global list
    if text == 'CE':
        list.clear()
        dialedNumber = ''
        label.configure(text='0')
    elif '0' <= text <= '9':
        dialedNumber += text
        label.configure(text=dialedNumber)
    elif text == '.':
        if dialedNumber.find('.') == -1:
            dialedNumber += text
            label.configure(text=dialedNumber)
    else:
        if len(list) >= 2:
            list.append(label['text'])
            calculate()
            list.clear()
            list.append(label['text'])
            dialedNumber = ''
            if text != '=':
                list.append(text)
        else:
            if text != '=':
                list.append(label['text'])
                list.append(text)
                dialedNumber = ''
                label.configure(text='0')


label = Label(root, text='0', width=30)
label.grid(row=0, column=0, columnspan=4, sticky='nsew')

button = Button(root, text='CE', command=lambda text='CE': click(text))
button.grid(row=1, column=3, sticky='nsew')
for row in range(4):
    for col in range(4):
        button = Button(root, text=buttons[row][col], command=lambda row=row, col=col: click(buttons[row][col]))
        button.grid(row=row + 2, column=col, sticky="nsew")

root.grid_rowconfigure(6, weight=1)
root.grid_columnconfigure(4, weight=1)

root.mainloop()
