from tkinter import *

addresBook = Tk()
addresBook.title('Адресная книга')
addresBook.geometry('400x500')

def inputcontact():
    contactTitle.pack()
    contactTitle.pack_forget()
    inputTitle.place(x=40, y=100)
    inputNumber.place(x=80, y=200)
    textinputTitle.place(x=125, y=70)
    textinputNumber.place(x=130, y=170)
    cancel.place(x=134, y=350)
    addcontact.place(x=200, y=350)
    add.pack_forget()


def cancelAdd():
    add.pack()
    cancel.pack()
    cancel.pack_forget()
    addcontact.pack()
    addcontact.pack_forget()
    inputNumber.pack()
    inputNumber.pack_forget()
    inputTitle.pack()
    inputTitle.pack_forget()
    textinputTitle.pack()
    textinputTitle.pack_forget()
    textinputNumber.pack()
    textinputNumber.pack_forget()


def savecontact():
    global heightTitle
    global heightNumber
    saveTitle = inputTitle.get('1.0', 'end-1c')
    saveNumber = inputNumber.get('1.0', 'end-1c')
    add.pack()
    cancel.pack()
    cancel.pack_forget()
    addcontact.pack()
    addcontact.pack_forget()
    inputNumber.pack()
    inputNumber.pack_forget()
    inputTitle.pack()
    inputTitle.pack_forget()
    textinputTitle.pack()
    textinputTitle.pack_forget()
    textinputNumber.pack()
    textinputNumber.pack_forget()
    contactTitle = Label(text=saveTitle, font='25')
    heightTitle += 43
    contactTitle.place(x=30, y=heightTitle)
    contactNumber = Label(text=saveNumber, font='25')
    heightNumber += 44
    contactNumber.place(x=30, y=heightNumber)


heightNumber = 25
heightTitle = 50
textinputTitle = Label(text='Введите название:', font='25')
textinputNumber = Label(text='Введите номер:', font='25')
inputTitle = Text(width=40, height=2)
inputNumber = Text(width=30, height=1)
save = inputTitle.get('1.0', 'end-1c')
contactTitle = Label(text=save, font='25')
add = Button(addresBook, text='Добавить контакт', width=15, height=2, command=inputcontact)
add.pack()
cancel = Button(addresBook, text='отмена', width=8, height=2, command=cancelAdd)
addcontact = Button(addresBook, text='добавить', width=8, height=2, command=savecontact)
addresBook.mainloop()