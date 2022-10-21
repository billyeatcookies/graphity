import tkinter as tk

from .canvas import Canvas

class Graphing(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.master = master 

        self.canvas = Canvas(self)
        self.pack(fill=tk.BOTH, expand=True)
