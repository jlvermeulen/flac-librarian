#! /usr/bin/env python

import tkinter as tk
import icon, metaflac

_app = None

class MainWindow(tk.Frame):
    frame = None
    labels_initialised = False

    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.init()

    def init(self):
        self.parent.title('FLAC Librarian 0.1')
        self.pack(fill = tk.BOTH, expand = 1)

        self.frame = tk.Frame(self)
        self.frame.pack(fill = tk.BOTH, expand = 1)

        button = tk.Button(self.frame, text = "Read data", command = self.show_data).grid(row = 0)

        track_label  = tk.Label(self.frame, text = 'Track number:').grid(row = 0, column = 1, sticky = 'w')
        title_label  = tk.Label(self.frame, text = 'Title:').grid(row = 1, column = 1, sticky = 'w')
        artist_label = tk.Label(self.frame, text = 'Artist:').grid(row = 2, column = 1, sticky = 'w')
        album_label  = tk.Label(self.frame, text = 'Album:').grid(row = 3, column = 1, sticky = 'w')

    def show_data(self):
        if self.labels_initialised:
            return

        artist = metaflac.get_attribute('artist', 'test.flac')
        title = metaflac.get_attribute('title', 'test.flac')
        album = metaflac.get_attribute('album', 'test.flac')
        tracknumber = metaflac.get_attribute('tracknumber', 'test.flac')

        track_label  = tk.Label(self.frame, text = tracknumber).grid(row = 0, column = 2, sticky = 'w')
        title_label  = tk.Label(self.frame, text = title).grid(row = 1, column = 2, sticky = 'w')
        artist_label = tk.Label(self.frame, text = artist).grid(row = 2, column = 2, sticky = 'w')
        album_label  = tk.Label(self.frame, text = album).grid(row = 3, column = 2, sticky = 'w')

        self.labels_initialised = True

if __name__ == '__main__':
    root = tk.Tk()
    root.geometry('1280x720+200+200')

    global _app
    _app = MainWindow(root)

    icon.create_icon()
    root.iconbitmap('flac-librarian.ico')
    icon.delete_icon()

    root.mainloop()
