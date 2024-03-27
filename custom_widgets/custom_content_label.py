import tkinter as tk


class CustomContentLabel(tk.Label):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.config(font=("Bahnschrift", "11", "normal"), bg="#696969", fg="#FFFFFF", anchor="w", justify="left", padx=10)
