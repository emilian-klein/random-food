import tkinter as tk


class CustomButton(tk.Button):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.config(font=("Bahnschrift", "11", "bold"), bg="#75a832", fg="#FFFFFF", cursor="hand2")
