from tkinter import *


class args:
    def __init__(self, compress, input):
        self.compress = compress
        self.input = input


def start_window(main_command):
    window = Tk()
    window.title("Архиватор")
    window.geometry('500x200')
    lbl = Label()
    entry = Entry(window, width=10)
    global compress
    compress = True

    def start_main_command():
        g = entry.get()
        global compress
        main_command(args(compress, g))

    def add_entry():
        entry.grid(column=3, row=0)

    def archive_window():
        lbl.configure(text="Введите путь до файла")
        add_entry()
        btn = Button(window, text="Заархивировать",
                     command=start_main_command)
        btn.grid(row=1, column=3)

    def unzip_window():
        lbl.configure(text="Введите путь до файла")
        add_entry()
        global compress
        compress = False
        btn = Button(window, text="Разархивировать",
                     command=start_main_command)
        btn.grid(row=1, column=3)

    lbl = Label(window, text="Что вам нужно?", font=("Arial Bold", 20))
    lbl.grid(row=0)
    btn_archive = Button(window, text="Архиватор", command=archive_window)
    btn_archive.grid(row=1)
    btn_unzip = Button(window, text="Разархиватор", command=unzip_window)
    btn_unzip.grid(row=2)
    window.mainloop()
