from tkinter import *

addresBook = Tk()
addresBook.title('Адресная книга')
addresBook.geometry('400x500')

def inputcontact():
    inputTitle.place(x=40, y=100)
    inputNumber.place(x=80, y=200)
    cancel.place(x=134, y=350)
    addcontact.place(x=200, y=350)
    add.pack_forget()


def cancelAdd():
    add.pack()

inputTitle = Text(width=40, height=2)
inputNumber = Text(width=30, height=1)
add = Button(addresBook, text='Добавить контакт', width=15, height=2, command=inputcontact)
add.place(x=145, y=0)
add.pack()
cancel = Button(addresBook, text='отмена', width=8, height=2, command=cancelAdd)
addcontact = Button(addresBook, text='добавить', width=8, height=2)
addresBook.mainloop()