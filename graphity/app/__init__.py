import tkinter as tk

from .layout import Root

class App:
    def __init__(self, *args, **kwargs):
        self.root = Root()

    def launch(self):
        print("launch successful")
        self.root.mainloop()