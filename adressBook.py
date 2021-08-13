from tkinter import *


def inputcontact():
    """ Ввод названия и номера контакта"""
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
    """Отмена добавления контакта"""
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


def savecontact(): # Создание контакта
    def delete(): # Удаление контакта
        """Удаление номера, названия контакта и кнопок 'Удалить' и 'Изменить'"""
        contactTitle.destroy()
        contactNumber.destroy()
        deleteb.destroy()
        changeb.destroy()
        contacts.remove(saveTitle)
        contacts.remove(saveNumber)
        print(contacts)

    def change():  # Изменение контакта
        def changecontact():
            nonlocal contactNumber
            nonlocal contactTitle
            nonlocal saveTitle
            nonlocal saveNumber
            global score
            contacts.remove(saveTitle)
            contacts.remove(saveNumber)
            saveNumber = editTitle.get('1.0', 'end-1c')
            saveTitle = editNumber.get('1.0', 'end-1c')
            # contactTitle_edit = Label(text=saveTitle, font='25', master=addresBook)  # Добавление контакта
            # contactNumber_edit = Label(text=saveNumber, font='25', master=addresBook)
            if saveNumber != '' and saveTitle != '':
                contactTitle.destroy()
                contactNumber.destroy()
                contactTitle = Label(text=saveTitle, font='25')
                contactNumber = Label(text=saveNumber, font='25')
                print(contacts)
                score += 1
                contactNumber.grid(row=score, column=1)
                contactTitle.grid(row=score, column=0)
                changeb.grid(row=score, column=2)
                deleteb.grid(row=score, column=3)
                contacts.append(saveTitle)
                contacts.append(saveNumber)
                print(contacts)
                # contactNumber_edit.destroy()
                # contactTitle_edit.destroy()
                # contactTitle_edit = Label(text=saveTitle, font='25', master=addresBook)  # Добавление контакта
                # contactNumber_edit = Label(text=saveNumber, font='25', master=addresBook)
                # contactTitle_edit.grid(row=score, column=0)
                # contactNumber_edit.grid(row=score, column=1)
                changetk.destroy()

        # Создание окна для изменения контакта
        changetk = Tk()
        changetk.title("Изменить")
        changetk.geometry("400x500")
        # Создание текстовых полей для изменения контакта
        editTitle = Text(width=40, height=2, master=changetk)
        editNumber = Text(width=30, height=1, master=changetk)
        # Расположение текстовых полей
        editTitle.place(x=39, y=100)
        editNumber.place(x=79, y=200)

        # Кнопка 'Изменить контакт'
        editcontact = Button(changetk, text='Изменить контакт', width=15, height=2, command=changecontact)
        editcontact.place(x=150, y=300)
        # Кнопка 'Отмена'
        cancel_change = Button(changetk, text='Отмена', width=15, height=2, command=changetk.destroy)
        cancel_change.place(x=150, y=415)

    global score
    global heightTitle
    global heightNumber
    global heightDeleteEdit
    score += 1
    # Сохранение в переменые номер и название контакта
    saveTitle = inputTitle.get('1.0', 'end-1c')
    saveNumber = inputNumber.get('1.0', 'end-1c')

    if saveNumber != '' and saveTitle != '':
        contactTitle = Label(text=saveTitle, font='25')  # Добавление контакта
        # Создание кнопок 'Изменить', 'Удалить' и 'Изменить'
        changeb = Button(text="Изменить", command=change)
        deleteb = Button(text="Удалить", command=delete)
        contactNumber = Label(text=saveNumber, font='25')
        # Расположение номера и название и кнопок 'Удалить' и 'Изменить'
        contactTitle.grid(row=score, column=0)
        changeb.grid(row=score, column=2)
        deleteb.grid(row=score, column=3)
        contactNumber.grid(row=score, column=1)
        contacts.append(saveTitle)
        contacts.append(saveNumber)
        print(contacts)


def saveContacts():
    with open("contacts.txt", "w") as vc:
        vc.seek(0)
        for item in contacts:
            vc.write("%s\n" %item)
        print(contacts)
        addresBook.destroy()


def contactfromfile(namelabel, numberlabel):
    global score
    name = Label(text=namelabel, font="25")
    number = Label(text=numberlabel, font="25")
    name.grid(row=score, column=0)
    number.grid(row=score, column=1)
    # changeb = Button(text="Изменить",)
    # deleteb = Button(text="Удалить", )
    # changeb.grid(row=score, column=2)
    # deleteb.grid(row=score, column=3)
    score += 1


if __name__ == '__main__':


    addresBook = Tk()
    addresBook.title('Адресная книга')
    addresBook.geometry('800x600')

    score = 1  # счетчик контактов
    contacts = []
    with open("contacts.txt", "r") as vv:
        lsts = [line.strip() for line in vv]
        for savedcontacts in range(int(len(lsts)/2)):
            contactfromfile(lsts[2*savedcontacts], lsts[2*savedcontacts+1])

    textinputTitle = Label(text='Введите название:', font='25')
    textinputNumber = Label(text='Введите номер:', font='25')
    inputTitle = Text(width=40, height=2)
    inputNumber = Text(width=30, height=1)

    saveTitle = inputTitle.get('1.0', 'end-1c')
    saveNumber = inputNumber.get('1.0', 'end-1c')
    contactTitle = Label(text=saveTitle, font='25')
    contactNumber = Label(text=saveNumber, font='25')

    add = Button(addresBook, text='Добавить контакт', width=15, height=2, command=inputcontact)
    cancel = Button(addresBook, text='отмена', width=8, height=2, command=cancelAdd)
    addcontact = Button(addresBook, text='добавить', width=8, height=2, command=savecontact)
    save = Button(addresBook, text='Сохранить и выйти', width=15, height=2, command=saveContacts)
    save.place(x=285)
    add.place(x=400)
    for contact in contacts:
        print(contact)
    addresBook.mainloop()