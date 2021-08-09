from tkinter import *

addresBook = Tk()
addresBook.title('Адресная книга')
addresBook.geometry('400x500')

def inputcontact():
    contactTitle.pack()
    contactTitle.pack_forget()
    inputTitle.place(x=40, y=100)
    inputNumber.place(x=80, y=200)
    inputTitle.delete(1.0, END)
    inputNumber.delete(1.0, END)
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


def deletecontact():
    for i in titles:
        titles.remove(i)
    for i in numbers:
        numbers.remove(i)


def savecontact():
    global heightTitle
    global heightNumber
    global heightDeleteEdit
    saveTitle = inputTitle.get('1.0', 'end-1c')
    saveNumber = inputNumber.get('1.0', 'end-1c')
    titles.append(saveTitle)
    numbers.append(saveNumber)
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
    for i in titles:
        contactTitle = Label(text=i, font='25')
        heightTitle += 55
        contactTitle.place(x=30, y=heightTitle)
    for i in numbers:
        contactNumber = Label(text=i, font='25')
        contactNumber.place(x=30, y=heightNumber)
        heightNumber += 85
        heightDeleteEdit += 25
        delete.place(x=325, y=heightDeleteEdit)
        edit.place(x=259, y=heightDeleteEdit)


heightNumber = 25
heightTitle = 40
heightDeleteEdit = 70
titles = []
numbers = []
textinputTitle = Label(text='Введите название:', font='25')
textinputNumber = Label(text='Введите номер:', font='25')
inputTitle = Text(width=40, height=2)
inputNumber = Text(width=30, height=1)
saveTitle = inputTitle.get('1.0', 'end-1c')
saveNumber = inputNumber.get('1.0', 'end-1c')
contactTitle = Label(text=saveTitle, font='25')
contactNumber = Label(text=saveNumber, font='25')
add = Button(addresBook, text='Добавить контакт', width=15, height=2, command=inputcontact)
add.pack()
delete = Button(addresBook, text='удалить', width=8, height=2, command=deletecontact)
cancel = Button(addresBook, text='отмена', width=8, height=2, command=cancelAdd)
addcontact = Button(addresBook, text='добавить', width=8, height=2, command=savecontact)
edit = Button(addresBook, text='именить', width=8, height=2)
addresBook.mainloop()