#! /usr/bin/env python

import tkinter as tk
import icon

class MainWindow(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.init()

    def init(self):
        self.parent.title('FLAC Librarian 0.1')
        self.pack(fill = tk.BOTH, expand = 1)


def create_window():
    root = tk.Tk()
    root.geometry('1280x720+200+200')
    app = MainWindow(root)

    icon.create_icon()
    root.iconbitmap('flac-librarian.ico')
    icon.delete_icon()

    root.mainloop()
