#!/usr/bin/env python

from tkinter import Tk, Button


class SimpleApp(object):

    def __init__(self):
        self.root = Tk()
        self.build()

    def greet(self):
        print('Hello world from Tkinter!')

    def build(self):
        self.root.title = 'Hello World from Tkinter'

        button = Button(
            self.root,
            text='Greet!',
            command=self.greet
        )
        button.pack()

    def run(self):
        self.root.mainloop()


if __name__ == '__main__':

    app = SimpleApp()
    app.run()
