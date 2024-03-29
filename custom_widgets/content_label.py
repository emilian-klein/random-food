import tkinter as tk


class ContentLabel(tk.Label):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.configure(font=("Bahnschrift", "11", "normal"), bg="#d1d1d1", anchor="w", justify="left", padx=10)
