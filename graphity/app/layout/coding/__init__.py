import tkinter as tk

from .text import Text

class Coding(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.master = master
        
        self.text = Text(self)
        self.text.pack(fill=tk.BOTH, expand=True)
