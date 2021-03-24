from tkinter import *

root = Tk()

c = Canvas(root, width = 600, height = 600, bg = '#27E6EC')
c.pack()

# Код для ввода даты
entry1 = Entry(root)
c.create_window(200, 140, window=entry1, height = 20, width = 30)

label2 = Label(root, text='Введите год:')
label2.config(font=('helvetica', 10))
c.create_window(140, 140, window=label2)

root.mainloop()
