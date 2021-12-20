from tkinter import *


class args:
    def __init__(self, compress, input, output):
        self.compress = compress
        self.input = input
        self.output = output


def start_window(main_command):
    window = Tk()
    window.title("Архиватор")
    window.geometry('500x200')
    btn = Button()
    lbl = Label()
    entry = Entry(window, width=10)

    def add_entry():
        entry.grid(column=3, row=0)

    def archive_window():
        lbl.configure(text="Введите путь до файла")
        add_entry()
        btn.configure(text="Заархивировать", command=main_command(args(True, entry.get(), entry.get())))

    def unzip_window():
        lbl.configure(text="Введите путь до файла")
        add_entry()
        btn.configure(text="Разархивировать", command=main_command(args(False, entry.get(), entry.get())))

    lbl = Label(window, text="Что вам нужно?", font=("Arial Bold", 20))
    lbl.grid(row=0)
    btn_archive = Button(window, text="Архиватор", command=archive_window)
    btn_archive.grid(row=1)
    btn_unzip = Button(window, text="Разархиватор", command=unzip_window)
    btn_unzip.grid(row=2)
    window.mainloop()
