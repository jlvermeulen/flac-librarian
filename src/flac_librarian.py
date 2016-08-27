#! /usr/bin/env python3

import gui, metaflac

if __name__ == '__main__':
    gui.create_window()

    artist = metaflac.get_attribute('artist', 'test.flac')
    print(artist)
    title = metaflac.get_attribute('title', 'test.flac')
    print(title)
    album = metaflac.get_attribute('album', 'test.flac')
    print(album)
    tracknumber = metaflac.get_attribute('tracknumber', 'test.flac')
    print(tracknumber)
