#! /usr/bin/env python

import tkinter as tk
import icon, metaflac
import os

class MainWindow(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.init()

    def init(self):
        self.labels_initialised = False

        self.parent.title('FLAC Librarian 0.1')
        self.pack(fill = tk.BOTH, expand = 1)

        self.frame = tk.Frame(self)
        self.frame.pack(fill = tk.BOTH, expand = 1)

        self.button = tk.Button(self.frame, text = "Read data", command = self.show_data)
        self.button.grid(row = 0)

        self.track_label  = tk.Label(self.frame, text = 'Track number:')
        self.title_label  = tk.Label(self.frame, text = 'Title:')
        self.artist_label = tk.Label(self.frame, text = 'Artist:')
        self.album_label  = tk.Label(self.frame, text = 'Album:')

        self.track_label.grid(row = 0, column = 1, sticky = 'w')
        self.title_label.grid(row = 1, column = 1, sticky = 'w')
        self.artist_label.grid(row = 2, column = 1, sticky = 'w')
        self.album_label.grid(row = 3, column = 1, sticky = 'w')

    def show_data(self):
        if self.labels_initialised:
            return

        artist = metaflac.get_attribute('artist', 'test.flac')
        title = metaflac.get_attribute('title', 'test.flac')
        album = metaflac.get_attribute('album', 'test.flac')
        tracknumber = metaflac.get_attribute('tracknumber', 'test.flac')

        self.track_value  = tk.Label(self.frame, text = tracknumber)
        self.title_value  = tk.Label(self.frame, text = title)
        self.artist_value = tk.Label(self.frame, text = artist)
        self.album_value  = tk.Label(self.frame, text = album)

        self.track_value.grid(row = 0, column = 2, sticky = 'w')
        self.title_value.grid(row = 1, column = 2, sticky = 'w')
        self.artist_value.grid(row = 2, column = 2, sticky = 'w')
        self.album_value.grid(row = 3, column = 2, sticky = 'w')

        self.labels_initialised = True

if __name__ == '__main__':
    root = tk.Tk()
    root.geometry('1280x720+200+200')

    app = MainWindow(root)

    icon.create_icon()
    root.iconbitmap('flac-librarian.ico')
    icon.delete_icon()

    root.mainloop()
