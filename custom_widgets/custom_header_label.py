import tkinter as tk


class CustomHeaderLabel(tk.Label):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.config(font=("Bahnschrift", "14", "bold"), bg="#696969", fg="#FFFFFF", anchor="w", justify="left", padx=10)
