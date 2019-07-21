from tkinter import *
import os
from tkinter.messagebox import *
from tkinter.filedialog import *


class Notepad:
    win = Tk()
    __textarea = Text(win)
    __menubar = Menu(win)
    __filemenu = Menu(__menubar, tearoff=0)
    __edit_menu = Menu(__menubar, tearoff=0)
    __help_menu = Menu(__menubar, tearoff=0)
    file = None
    __scroll = Scrollbar(__textarea)

    def __init__(self):
        self.win.title("Untitled - NotePad")
        self.win.geometry("480x640")
        self.win.grid_columnconfigure(0, weight=1)
        self.win.grid_rowconfigure(0, weight=1)
        self.__textarea.grid(sticky=N + E + S + W)
        self.__filemenu.add_command(label="New", command=self.__new)
        self.__filemenu.add_command(label="Open", command=self.__open)
        self.__filemenu.add_command(label="Save", command=self.__save)
        self.__menubar.add_cascade(label="File", menu=self.__filemenu)
        self.__filemenu.add_separator()
        self.__filemenu.add_command(label="Exit", command=self.__quit)
        self.__edit_menu.add_command(label="Cut", command=self.__cut)
        self.__edit_menu.add_command(label="Copy", command=self.__copy)
        self.__edit_menu.add_command(label="Paste", command=self.__paste)
        self.__menubar.add_cascade(label="Edit", menu=self.__edit_menu)
        self.__help_menu.add_cascade(label="About", command=self.__about)
        self.__menubar.add_cascade(label="Help", menu=self.__help_menu)
        self.win.config(menu=self.__menubar)
        self.__scroll.pack(side="right", fill=Y)
        self.__scroll.config(command=self.__textarea.yview)
        self.__textarea.config(yscrollcommand=self.__scroll.set)

    def __quit(self):
        self.win.destroy()

    @staticmethod
    def __about():
        showinfo("Notepad", "Anish Varshney")

    def __cut(self):
        self.__textarea.event_generate('<<Cut>>')

    def __copy(self):
        self.__textarea.event_generate('<<Copy>>')

    def __paste(self):
        self.__textarea.event_generate('<<Paste>>')

    def __new(self):
        self.win.title("Untitled - Notepad")
        self.file = None
        self.__textarea.delete(1.0, END)

    def __open(self):
        self.file = askopenfilename(defaultextension=".txt",
                                    filetype=[("All Files", "*.*"), ("Text Documents", "*.txt*")])
        if self.file is None:
            self.file = None
        else:
            self.win.title(os.path.basename(self.file) + " -NotePad")
            self.__textarea.delete(1.0, END)
            with open(self.file, "r") as File:
                self.__textarea.insert(1.0, File.read())

    def __save(self):
        if self.file is None:
            self.file = asksaveasfilename(initialfile="Untitled", defaultextension=".txt",
                                          filetype=[("All Files", "*.*"),
                                                    ("Text Documents",
                                                     "*.txt*"
                                                     )])
            if self.file is "":
                self.file = None
            else:
                with open(self.file, "w") as new:
                    new.write(self.__textarea.get(1.0, END))
                    self.win.title(os.path.basename(self.file) + " - NotePad")

        else:
            with open(self.file, "w") as file:
                file.write(self.__textarea.get(1.0, END))

    def run(self):
        self.win.mainloop()


notepad = Notepad()
notepad.run()
