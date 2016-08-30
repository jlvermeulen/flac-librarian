#! /usr/bin/env python

import tkinter as tk
from tkinter import messagebox

import icon, metaflac

import os.path, glob

class MainWindow(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.init()

    def init(self):
        self.tags = ['tracknumber', 'title', 'artist', 'album']
        self.tag_data = {}
        for tag in self.tags:
            self.tag_data[tag] = []

        self.parent.title('FLAC Librarian 0.1')
        self.pack(fill = tk.BOTH, expand = 1)

        self.frame = tk.Frame(self)
        self.frame.pack(fill = tk.BOTH, expand = 1)

        self.button = tk.Button(self.frame, text = "Read data", command = self.fill_table)
        self.button.grid(row = 0, column = 0, sticky = 'w')

        self.path_entry = tk.Entry(self.frame, width = 100)
        self.path_entry.grid(row = 0, column = 1, sticky = 'w', columnspan = 10, padx = 10)

        self.track_label  = tk.Label(self.frame, text = 'Track number:')
        self.title_label  = tk.Label(self.frame, text = 'Title:')
        self.artist_label = tk.Label(self.frame, text = 'Artist:')
        self.album_label  = tk.Label(self.frame, text = 'Album:')

        self.track_label.grid(row = 1, column = 0, sticky = 'w', padx = 10)
        self.title_label.grid(row = 1, column = 1, sticky = 'w', padx = 10)
        self.artist_label.grid(row = 1, column = 2, sticky = 'w', padx = 10)
        self.album_label.grid(row = 1, column = 3, sticky = 'w', padx = 10)

    def fill_table(self):
        path = self.path_entry.get()
        if not os.path.isdir(path):
            tk.messagebox.showerror('Invalid path', 'Please give a path to an existing directory!')
            return

        self.gather_data(path)
        self.show_data()

    def gather_data(self, path):
        for file in glob.glob(os.path.join(path, '*.flac')):
            for tag in self.tags:
                value = metaflac.get_attribute(tag, file)
                self.tag_data[tag].append(value)

    def show_data(self):
        i = 0
        for tag in self.tags:
            j = 2
            for value in self.tag_data[tag]:
                label = tk.Label(self.frame, text = value)
                label.grid(row = j, column = i, sticky = 'w', padx = 10)
                j = j + 1
            i = i + 1

def main():
    root = tk.Tk()
    root.geometry('1280x720+200+200')

    app = MainWindow(root)

    icon.create_icon()
    root.iconbitmap('flac-librarian.ico')
    icon.delete_icon()

    root.mainloop()

if __name__ == '__main__':
    main()
