import tkinter as tk

from .graphing import Graphing 
from .coding import Coding 

class Root(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        
        self.graphing = Graphing(self)
        self.graphing.grid(row=0, column=0)

        self.coding = Coding(self)
        self.coding.grid(row=0, column=1)
