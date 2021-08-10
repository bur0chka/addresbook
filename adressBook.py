from tkinter import *

addresBook = Tk()
addresBook.title('Адресная книга')
addresBook.geometry('800x600')

def inputcontact():
    contactTitle.pack_forget()
    inputTitle.place(x=460, y=100)
    inputNumber.place(x=520, y=200)
    inputTitle.delete(1.0, END)
    inputNumber.delete(1.0, END)
    textinputTitle.place(x=370, y=70)
    textinputNumber.place(x=375, y=170)
    cancel.place(x=500, y=350)
    addcontact.place(x=566, y=350)
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


#def deletecontact():



def savecontact():
    def delete():
        contactTitle.destroy()
        contactNumber.destroy()
        deleteb.destroy()
        changeb.destroy()

    def change():
        changetk = Tk()
        changetk.title("Изменить")
        changetk.geometry("400x500")
        editTitle = Text(width=40, height=2, master=changetk)
        editNumber = Text(width=30, height=1, master=changetk)
        editTitle.place(x=39, y=100)
        editNumber.place(x=79, y=200)
        editcontact = Button(changetk, text='Изменить контакт', width=15, height=2)
        editcontact.place(x=150, y=300)

    global score
    global heightTitle
    global heightNumber
    global heightDeleteEdit
    score += 1
    saveTitle = inputTitle.get('1.0', 'end-1c')
    saveNumber = inputNumber.get('1.0', 'end-1c')
    #titles.append(saveTitle)
    #numbers.append(saveNumber)
    #for i in titles:
    contactTitle = Label(text=saveTitle, font='25')
    heightTitle += 15
    changeb = Button(text="Изменить", command=change)
    deleteb = Button(text="Удалить", command=delete)
    print(heightTitle)
    contactTitle.grid(row=score, column=0)
    changeb.grid(row=score, column=2)
    deleteb.grid(row=score, column=3)
    #for i in numbers:
    contactNumber = Label(text=saveNumber, font='25')
    contactNumber.grid(row=score, column=1)
    heightNumber += 15
    print(heightNumber)
    heightDeleteEdit += 25






score  = 1 # счетчик контактов
heightNumber = 45
heightTitle = 55
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
cancel = Button(addresBook, text='отмена', width=8, height=2, command=cancelAdd)
addcontact = Button(addresBook, text='добавить', width=8, height=2, command=savecontact)
addresBook.mainloop()