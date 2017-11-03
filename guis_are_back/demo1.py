#!/usr/bin/env python

from tkinter import Tk, Button


if __name__ == '__main__':

    root = Tk()
    root.title = 'Hello World from Tkinter!'

    button = Button(
        root, text='Greet!',
        command=lambda: print(
            'Hello world from Tkinter!'
        )
    )

    button.pack()
    root.mainloop()
