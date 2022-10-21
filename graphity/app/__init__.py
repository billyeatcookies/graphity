import tkinter as tk

class App:
    def __init__(self, *args, **kwargs):
        self.root = tk.Tk()

    def launch(self):
        print("launch successful")
        self.root.mainloop()