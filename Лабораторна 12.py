from tkinter import*
from tkinter import messagebox

root = Tk()
root.title('Анкета')

photo = None

def show():
    global photo
    try:
        photo = PhotoImage(file="11.gif")
        label6.config(image=photo)
    except TclError:
        messagebox.showerror("Помилка", "Файл '11.gif' не знайдено!")

def inf():
    s = edit4.get()
    if s == "111М":
        messagebox.showinfo('Про спеціальність', edit4.get() + '''\nСпеціальність 111 Математика\nОсвітня програма Ком'ютерна математика''')
    elif s == "COM":
        messagebox.showinfo('Про спеціальність', edit4.get() + '''\nСпеціальність 014 Середня освіта\nОсвітня програма Середня освіта. Математика, інформатика''')
    else:
        messagebox.showinfo('Про спеціальність', edit4.get() + '\nТакої спеціальності на факультеті немає')

# Параметри для віджетів
label_font = ('Arial', 12)
entry_width = 30
button_width = 20

# Розташування віджетів за допомогою grid()
label1 = Label(root, text='Прізвище', font=label_font, bg='lightgray')
label1.grid(row=0, column=0, padx=5, pady=5, sticky='w')

edit1 = Entry(root, width=entry_width)
edit1.grid(row=0, column=1, padx=5, pady=5, sticky='ew')

label2 = Label(root, text="Ім'я", font=label_font, bg='lightgray')
label2.grid(row=1, column=0, padx=5, pady=5, sticky='w')

edit2 = Entry(root, width=entry_width)
edit2.grid(row=1, column=1, padx=5, pady=5, sticky='ew')

label3 = Label(root, text='По батькові', font=label_font, bg='lightgray')
label3.grid(row=2, column=0, padx=5, pady=5, sticky='w')

edit3 = Entry(root, width=entry_width)
edit3.grid(row=2, column=1, padx=5, pady=5, sticky='ew')

checkbutton1 = Checkbutton(root, text='ч')
checkbutton1.grid(row=3, column=0, padx=5, pady=5, sticky='w')

checkbutton2 = Checkbutton(root, text='ж')
checkbutton2.grid(row=3, column=1, padx=5, pady=5, sticky='w')

label4 = Label(root, text='Виберіть курс:', font=label_font, bg='lightgray')
label4.grid(row=4, column=0, padx=5, pady=5, sticky='w')

result1 = IntVar()
result1.set(1)
Radiobutton1 = Radiobutton(root, text=1, variable=result1, value=1)
Radiobutton1.grid(row=5, column=0, padx=5, pady=2, sticky='w')
Radiobutton2 = Radiobutton(root, text=2, variable=result1, value=2)
Radiobutton2.grid(row=6, column=0, padx=5, pady=2, sticky='w')
Radiobutton3 = Radiobutton(root, text=3, variable=result1, value=3)
Radiobutton3.grid(row=7, column=0, padx=5, pady=2, sticky='w')
Radiobutton4 = Radiobutton(root, text=4, variable=result1, value=4)
Radiobutton4.grid(row=8, column=0, padx=5, pady=2, sticky='w')

label5 = Label(root, text='Спеціальність', font=label_font, bg='lightgray')
label5.grid(row=9, column=0, padx=5, pady=5, sticky='w')

edit4 = Entry(root, width=entry_width)
edit4.grid(row=9, column=1, padx=5, pady=5, sticky='ew')

button1 = Button(root, text='Про спеціальність', width=button_width, command=inf)
button1.grid(row=10, column=0, columnspan=2, padx=5, pady=10)

label6 = Label(root)
label6.grid(row=11, column=0, columnspan=2, padx=5, pady=5)

button2 = Button(root, text="Фото", width=button_width, command=show)
button2.grid(row=12, column=0, columnspan=2, padx=5, pady=10)

root.mainloop()