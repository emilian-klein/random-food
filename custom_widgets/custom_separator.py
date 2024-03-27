import tkinter as tk


class CustomSeparator(tk.Frame):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.config(bg="#FFFFFF", height=1, bd=0)
